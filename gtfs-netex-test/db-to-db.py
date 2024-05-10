import sqlite3
from decimal import Decimal, ROUND_HALF_UP
from itertools import chain
from typing import List, Iterable, T

from pyproj import Transformer, CRS
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.handlers import LxmlEventHandler, lxml
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from netex import ServiceJourneyPattern, Direction, Codespace, MultilingualString, DirectionType, ServiceJourney, \
    AvailabilityCondition, TimeDemandType, ScheduledStopPoint, Pos, PointVersionStructure, RoutePoint, RouteLink, \
    StopPointInJourneyPattern, TimingPointInJourneyPattern, ScheduledStopPointRef, TimingLink, ServiceLink, \
    TimingLinkRefStructure, ServiceLinkRefStructure, RouteRef, Route, RouteLinkRef, RouteLinkRefStructure, \
    RouteRefStructure, ScheduledStopPointRefStructure, RoutePointRef, RoutePointRefStructure, PointProjection, \
    TimingPoint, TimingPointRefStructure, LineString, Link, LinkVersionStructure, PosList
from refs import getId, getRef
from servicecalendarepip import ServiceCalendarEPIPFrame
from timetabledpassingtimesprofile import TimetablePassingTimesProfile
from utils import project

# First monkey patching test
def get_route(self, con) -> Route:
    return get_single(con, Route, self.ref, self.version)

RouteRefStructure.get = get_route

def get_routelink(self, con) -> RouteLink:
    return get_single(con, RouteLink, self.ref, self.version)

RouteLinkRefStructure.get = get_routelink

def get_scheduledstoppoint(self, con) -> ScheduledStopPoint:
    return get_single(con, ScheduledStopPoint, self.ref, self.version)

ScheduledStopPointRefStructure.get = get_scheduledstoppoint

def get_timingpoint(self, con) -> TimingPoint | ScheduledStopPoint:
    if self.name_of_ref_class == 'TimingPoint':
        return get_single(con, TimingPoint, self.ref, self.version)
    elif  self.name_of_ref_class == 'ScheduledStopPoint':
        return get_single(con, ScheduledStopPoint, self.ref, self.version)
    else:
        timing_point = get_single(con, TimingPoint, self.ref, self.version)
        if timing_point is not None:
            return timing_point
        else:
            return get_single(con, ScheduledStopPoint, self.ref, self.version)

TimingPointRefStructure.get = get_timingpoint

def get_servicelink(self, con) -> ServiceLink:
    return get_single(con, ServiceLink, self.ref, self.version)

ServiceLinkRefStructure.get = get_servicelink

def get_timinglink(self, con) -> TimingLink:
    return get_single(con, TimingLink, self.ref, self.version)

TimingLinkRefStructure.get = get_timinglink


ns_map = {'': 'http://www.netex.org.uk/netex', 'gml': 'http://www.opengis.net/gml/3.2'}

context = XmlContext()
config = ParserConfig(fail_on_unknown_properties=False)
parser = XmlParser(context=context, config=config, handler=LxmlEventHandler)

serializer_config = SerializerConfig(ignore_default_attributes=True)
serializer_config.indent = None
serializer_config.xml_declaration = False
serializer_config.ignore_default_attributes = True
serializer = XmlSerializer(config=serializer_config)

transformers = {}

def write_objects(con, objs, empty=False, many=False):
    cur = con.cursor()
    clazz = objs[0].__class__
    objectname = getattr(clazz.Meta, 'name', clazz.__name__)
   

    if empty:
        sql_drop_table = f"DROP TABLE IF EXISTS {objectname}"
        cur.execute(sql_drop_table)

    sql_create_table = f"CREATE TABLE IF NOT EXISTS {objectname} (id varchar(64) NOT NULL, version varchar(64) NOT NULL, object text NOT NULL, PRIMARY KEY (id, version));"
    cur.execute(sql_create_table)

    if many:
        print(objectname, len(objs))
        cur.executemany(f'INSERT INTO {objectname} (id, version, object) VALUES (?, ?, ?);', [(obj.id, obj.version, serializer.render(obj, ns_map).replace('\n', '').encode('utf-8')) for obj in objs])
    else:
        for i in range(0, len(objs)):
            obj = objs[i]
            cur.execute(f'INSERT INTO {objectname} (id, version, object) VALUES (?, ?, ?);', (obj.id, obj.version, serializer.render(obj, ns_map).replace('\n', '').encode('utf-8')))
            print('\r', str(i), end = '')
        print('\r', end='')

def infer_directions_from_sjps_and_apply(con, service_journey_patterns: Iterable[ServiceJourneyPattern], generator_defaults):
    used_direction_types = {sjp.direction_type for sjp in service_journey_patterns if sjp.direction_type is not None}
    directions = {}
    for used_direction_type in used_direction_types:
        direction: Direction = Direction(id=getId(Direction, generator_defaults['codespace'], used_direction_type.value),
                                         version=generator_defaults['version'],
                                         name=MultilingualString(value=str(used_direction_type.value)),
                                         direction_type=DirectionType(value=used_direction_type))
        directions[used_direction_type] = direction

    write_objects(con, list(directions.values()), True)

    for sjp in service_journey_patterns:
        sjp.direction_ref_or_direction_view = getRef(directions.get(sjp.direction_type, None))


def project_location2(transformer, location):
    if transformer.target_crs.to_epsg() == 4326:
        if location.pos is not None:
            latitude, longitude = transformer.transform(location.pos.value[0], location.pos.value[1])
            location.longitude = Decimal(longitude).quantize(Decimal('0.000001'), ROUND_HALF_UP)
            location.latitude = Decimal(latitude).quantize(Decimal('0.000001'), ROUND_HALF_UP)
            location.pos = None
    else:
        if location.latitude is not None and location.longitude is not None:
            x, y = transformer.transform(location.longitude, location.latitude)
            location.srs_name = transformer.name
            location.pos = Pos(value=[x, y])
            location.longitude = None
            location.latitude = None
        elif location.pos is not None:
            x, y = transformer.transform(location.pos.value[0], location.pos.value[1])
            location.srs_name = transformer.name
            location.pos = Pos(value=[x, y])

def project_location_4326(transformer, location):
    if location.pos is not None:
        latitude, longitude = transformer.transform(location.pos.value[0], location.pos.value[1])
        location.longitude = Decimal(longitude).quantize(Decimal('0.000001'), ROUND_HALF_UP)
        location.latitude = Decimal(latitude).quantize(Decimal('0.000001'), ROUND_HALF_UP)
        location.pos = None

def project_location(points: Iterable[PointVersionStructure], generator_defaults, crs_to):
    transformer = transformers.get(generator_defaults['DefaultLocationsystem'], Transformer.from_crs(generator_defaults['DefaultLocationsystem'], crs_to))
    transformers[generator_defaults['DefaultLocationsystem']] = transformer
    if crs_to == 'EPSG:4326':
        for point in points:
            if point.location.srs_name != crs_to:
                project_location_4326(transformer, point.location)
    else:
        for point in points:
            if point.location.srs_name != crs_to:
                project_location2(transformer, point.location)

def project_linestring2(transformer, linestring):
    srs_dimension = linestring.srs_dimension or 2
    xx = []
    yy = []
    zz = []
    if isinstance(linestring.pos_or_point_property_or_pos_list[0], PosList):
        xx = linestring.pos_or_point_property_or_pos_list[0].value[0::srs_dimension]
        yy = linestring.pos_or_point_property_or_pos_list[0].value[1::srs_dimension]
        if srs_dimension >= 2:
            zz = linestring.pos_or_point_property_or_pos_list[0].value[2::srs_dimension]
    elif isinstance(linestring.pos_or_point_property_or_pos_list[0], Pos):
        xx = [pos.value[0] for pos in linestring.pos_or_point_property_or_pos_list]
        yy = [pos.value[1] for pos in linestring.pos_or_point_property_or_pos_list]
        if srs_dimension >= 2:
            zz = [pos.value[2] for pos in linestring.pos_or_point_property_or_pos_list]

    if srs_dimension == 2:
        pxx, pyy = transformer.transform(xx, yy)
        linestring.pos_or_point_property_or_pos_list = [PosList(value=list(chain(*zip(pxx, pyy))))]
    elif srs_dimension == 3:
        pxx, pyy, pzz = transformer.transform(xx, yy, zz)
        linestring.pos_or_point_property_or_pos_list = [PosList(value=list(chain(*zip(pxx, pyy, pzz))))]

def project_linestring(links: Iterable[LinkVersionStructure], generator_defaults, crs_to):
    transformer = transformers.get(generator_defaults['DefaultLocationsystem'], Transformer.from_crs(generator_defaults['DefaultLocationsystem'], crs_to))
    transformers[generator_defaults['DefaultLocationsystem']] = transformer
    for link in links:
        if link.line_string.srs_name != crs_to:
            project_linestring2(transformer, link.line_string)
            if crs_to == 'EPSG:4326':
                link.line_string.pos_or_point_property_or_pos_list[0].value = [Decimal(value).quantize(Decimal('0.000001'), ROUND_HALF_UP) for value in link.line_string.pos_or_point_property_or_pos_list[0].value]

def load_local(con, clazz: T, limit=None) -> List[T]:
    type = getattr(clazz.Meta, 'name', clazz.__name__)

    cur = con.cursor()
    if limit is not None:
        cur.execute(f"SELECT object FROM {type} LIMIT {limit};")
    else:
        cur.execute(f"SELECT object FROM {type};")

    objs: List[T] = []
    for xml, in cur.fetchall():
        obj = parser.from_bytes(xml, clazz)
        objs.append(obj)

    return objs

def load_generator(con, clazz):
    type = getattr(clazz.Meta, 'name', clazz.__name__)

    cur = con.cursor()
    cur.execute(f"SELECT object FROM {type};")

    while True:
        xml = cur.fetchone()
        if xml is None:
            break
        yield parser.from_bytes(xml[0], clazz)

def get_single(con, clazz: T, id, version) -> T:
    type = getattr(clazz.Meta, 'name', clazz.__name__)
    cur = con.cursor()
    if version == 'any':
        cur.execute(f"SELECT object FROM {type} WHERE id = ? ORDER BY version DESC LIMIT 1;", (id,))
    else:
        cur.execute(f"SELECT object FROM {type} WHERE id = ? AND version = ? LIMIT 1;", (id, version,))

    row = cur.fetchone()
    if row is not None:
        obj = parser.from_bytes(row[0], clazz)
        return obj

def find_route_link(con, from_point: RoutePointRefStructure, to_point: RoutePointRefStructure, route_links: List[RouteLink], offset=0) -> (RouteLink, int):
    if from_point is None or to_point is None:
        return (None, offset)

    for i in range(offset, len(route_links)):
        route_link: RouteLink = route_links[i]
        if route_link.from_point_ref.ref == from_point.ref and route_link.to_point_ref.ref == to_point.ref:
            return (route_link, i)

    return (None, offset)

def point_to_route_point_ref(point):
    if point.projections:
        for projection in point.projections.projection_ref_or_projection:
            if isinstance(projection, PointProjection):
                projection: PointProjection
                if projection.project_to_point_ref is not None and projection.project_to_point_ref.name_of_ref_class == 'RoutePoint':
                    return project(projection.project_to_point_ref, RoutePointRef)

def append_timing_links_to_service_link(con, pis: StopPointInJourneyPattern, intermediate_timing_links: List[TimingLinkRefStructure], scheduled_stop_point_ref: ScheduledStopPointRef, route_links: List[RouteLink], new_service_links: List[ServiceLink], offset):
    service_link: ServiceLink = None
    if pis.onward_timing_link_ref:
        service_link = project(pis.onward_timing_link_ref.get(con), ServiceLink)
        new_service_links.append(service_link)
        pis.onward_service_link_ref = getRef(service_link)

        # First strategy: we must find a RouteLink that has the FromPoint + ToPoint
        from_ssp: ScheduledStopPoint = service_link.from_point_ref.get(con)
        from_ssp_pp = point_to_route_point_ref(from_ssp)
        to_ssp: ScheduledStopPoint = service_link.to_point_ref.get(con)
        to_ssp_pp = point_to_route_point_ref(to_ssp)

        route_link, offset = find_route_link(con, from_ssp_pp, to_ssp_pp, route_links, offset + 1)
        if route_link is not None:
            route_link: RouteLink
            service_link.line_string = route_link.line_string

        tl: TimingLink = None
        for tl_ref in intermediate_timing_links:
            tl = tl_ref.get(con)
            # update the previous pis's service link, so the timing links are appended
            # we only care about the line string, nothing else, resolve matching routelink

            from_point = tl.from_point_ref.get(con)
            from_point_pp = point_to_route_point_ref(from_point)
            to_point = tl.to_point_ref.get(con)
            to_point_pp = point_to_route_point_ref(to_point)

            route_link, offset = find_route_link(con, from_ssp_pp, to_ssp_pp, route_links, offset + 1)
            if route_link is not None:
                route_link: RouteLink
                # TODO: guard for dimensions
                if service_link.line_string[-2:] == route_link.line_string[0:2]:
                    service_link.line_string += route_link.line_string[2:]
                else:
                    print("End does not match start")

        if tl is not None and (
                tl.to_point_ref.name_of_ref_class == 'ScheduledStopPoint' or 'ScheduledStopPoint' in tl.to_point_ref.ref):
            service_link.to_point_ref = project(tl.to_point_ref, ScheduledStopPointRef)

    else:
        service_link = pis.onward_service_link_ref.get(con)
        # First strategy: we must find a RouteLink that has the FromPoint + ToPoint
        from_ssp: ScheduledStopPoint = service_link.from_point_ref.get(con)
        from_ssp_pp = point_to_route_point_ref(from_ssp)
        to_ssp: ScheduledStopPoint = service_link.to_point_ref.get(con)
        to_ssp_pp = point_to_route_point_ref(to_ssp)

        route_link, offset = find_route_link(con, from_ssp_pp, to_ssp_pp, route_links, offset + 1)
        if route_link is not None:
            route_link: RouteLink
            service_link.line_string = route_link.line_string

    if service_link.to_point_ref.ref != scheduled_stop_point_ref.ref:
        print("Expected end points don't match.")

    return offset


def transform_timinglinks_to_servicelinks(con, service_journey_pattern: ServiceJourneyPattern):
    route_links: List[RouteLink] = None
    if isinstance(service_journey_pattern.route_ref_or_route_view, RouteRef):
        route: Route = service_journey_pattern.route_ref_or_route_view.get(con)
        route_links = [por.onward_route_link_ref.get(con) for por in route.points_in_sequence.point_on_route if por.onward_route_link_ref is not None]

    # Van de ScheduledStopPoints is er een projectie naar RoutePoint
    # De RouteLink van de Route die hier gebruikt wordt (in volgorde) zou dus een relatie moeten hebben
    # tussen de eerst bekende scheduled stop point en de laatst gevonden scheduled stop point (geprojecteerd naar RoutePoint, als Ref)

    previous_pis = None
    new_pis_sequence = []
    intermediate_timing_links = []
    service_links = []
    offset = -1

    for pis in service_journey_pattern.points_in_sequence.point_in_journey_pattern_or_stop_point_in_journey_pattern_or_timing_point_in_journey_pattern:
        if isinstance(pis, StopPointInJourneyPattern):
            pis: StopPointInJourneyPattern
            # Handle that the previous pis, with a timing_link, now becomes a service_link
            if previous_pis is not None:
                offset = append_timing_links_to_service_link(con, previous_pis, intermediate_timing_links, pis.scheduled_stop_point_ref, route_links, service_links, offset)

            intermediate_timing_links = []

            new_pis_sequence.append(pis)

            previous_pis = pis

        elif isinstance(pis, TimingPointInJourneyPattern):
            pis: TimingPointInJourneyPattern
            if isinstance(pis.timing_point_ref_or_scheduled_stop_point_ref_or_parking_point_ref_or_relief_point_ref, ScheduledStopPointRef):
                # If this is the case, we must rewrite the TimingPointInSequence as a StopPointInJourneyPattern, otherwise we cannot create a OnwardServiceLink
                new_pis: StopPointInJourneyPattern = project(pis, StopPointInJourneyPattern)
                new_pis.scheduled_stop_point_ref = pis.timing_point_ref_or_scheduled_stop_point_ref_or_parking_point_ref_or_relief_point_ref
                new_pis_sequence.append(new_pis)

                offset = append_timing_links_to_service_link(previous_pis.onward_service_link_ref, intermediate_timing_links, new_pis.scheduled_stop_point_ref, route_links, service_links, offset)
                intermediate_timing_links = []

                previous_pis = new_pis

                # We can directly map the onward_timing_link

            else:
                intermediate_timing_links.append(pis.onward_timing_link_ref)

        if len(intermediate_timing_links):
            # if we end up here, the last pis' refer to timingpoints
            pass

    service_journey_pattern.points_in_sequence.point_in_journey_pattern_or_stop_point_in_journey_pattern_or_timing_point_in_journey_pattern = new_pis_sequence

    return service_links



generator_defaults = {'codespace': Codespace(xmlns='OPENOV'), 'version': 1, 'DefaultLocationsystem': 'EPSG:28992'} # Invent something, that materialises the refs, so VersionFrameDefaultsStructure can be used

with sqlite3.connect("/tmp/netex.sqlite") as con:
    # Voor alle PointsInJourneyPattern, als TimingLink een ServiceLink zou kunnen zijn, haal op basis van PointProjection de RouteLink op waar deze informatie
    # in zou kunnen zitten. Doe dit niet exclusief op basis van From/To maar neem de Route die in het ServiceJourneyPattern staat mee als referentie.
    # In het geval dat er sprake is van een TimingPointInJourneyPattern, haal dan de route op tot de eerst volgende ScheduledStopPoint en voeg de verschillende
    # RouteLinks samen, houdt er rekening mee dat bij het samen voegen het laatste punt op de lijn gelijk is aan het eerste, en daarmee overgeslagen zou
    # moeten worden.

    service_journey_patterns = load_local(con, ServiceJourneyPattern)
    tmp_service_links = []
    for service_journey_pattern in service_journey_patterns:
        # The problem that may appear is that there are multiple routes, for single timing_links, dependend on the ServiceJourneyPattern
        # so in the case where this may happen, the academic correct way would change the id, and incorporate the route as well. This would
        # bring Route unique ServiceLinks, not a bad idea, but edge case.
        tmp_service_links += transform_timinglinks_to_servicelinks(con, service_journey_pattern)

    sls = {}
    for sl in tmp_service_links:
        sls[sl.id] = sl

    service_links = list(sls.values())
    project_linestring(service_links, generator_defaults, 'EPSG:4326')
    with sqlite3.connect("/tmp/target.sqlite") as con2:
        write_objects(con2, service_links, True, True)
        service_links = None
        write_objects(con2, service_journey_patterns, True, True)

    # route_links: List[RouteLink] = load_local(con, RouteLink)
    # with sqlite3.connect("/tmp/target.sqlite") as con2:
    #     for route_link in route_links:
    #         route_link.line_string = None
    #         route_link.operational_context_ref = None
    #         route_link.responsibility_set_ref_attribute = None
            # TODO: Magic to ServiceLink

    #     write_objects(con2, route_links, True, True)
    #     route_links = None

    if False:
        route_points = load_local(con, RoutePoint)
        with sqlite3.connect("/tmp/target.sqlite") as con2:
            project_location(route_points, generator_defaults, 'EPSG:4326')
            write_objects(con2, route_points, True, True)
            route_points = None

        scheduled_stop_points = load_local(con, ScheduledStopPoint)
        with sqlite3.connect("/tmp/target.sqlite") as con2:
            project_location(scheduled_stop_points, generator_defaults, 'EPSG:4326')
            write_objects(con2, scheduled_stop_points, True, True)
            scheduled_stop_points = None

        service_journey_patterns = load_local(con, ServiceJourneyPattern)
        time_demand_types = load_local(con, TimeDemandType)
        service_journeys = load_local(con, ServiceJourney, 10)

        timetabledpassingtimesprofile = TimetablePassingTimesProfile(generator_defaults['codespace'], generator_defaults['version'], service_journeys, service_journey_patterns, time_demand_types)

        # TODO: Implement getTimetabledPassingTimes incrementally. As generator won't work, since it has to store the result (directly).
        timetabledpassingtimesprofile.getTimetabledPassingTimes(clean=True)
        time_demand_types = None

        availability_conditions = load_local(con, AvailabilityCondition)
        servicecalendarepip = ServiceCalendarEPIPFrame(generator_defaults['codespace'])

        with sqlite3.connect("/tmp/target.sqlite") as con2:
            service_calendar = servicecalendarepip.availabilityConditionsToServiceCalendar(service_journeys, availability_conditions)
            availability_conditions = None
            write_objects(con2, [service_calendar], True, False)
            service_calendar = None
            infer_directions_from_sjps_and_apply(con2, service_journey_patterns, generator_defaults)
            for sj in service_journeys:
                sj: ServiceJourney
                sj.validity_conditions_or_valid_between = None
                sj.key_list = None
                sj.private_code = None

            write_objects(con2, service_journeys, True, False)
            service_journeys = None

            service_links = transform_timinglinks_to_servicelinks(con, service_journey_patterns)
            project_linestring(service_links, generator_defaults, 'EPSG:4326')
            write_objects(con2, service_links, True, True)
            service_links = None

            write_objects(con2, service_journey_patterns, True, True)
            service_journey_patterns = None