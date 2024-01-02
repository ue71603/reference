from dataclasses import dataclass
from .railway_point_ref_structure import RailwayPointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RailwayPointRef(RailwayPointRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
