from dataclasses import dataclass

from .point_in_journey_pattern_ref_structure import PointInJourneyPatternRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TimingPointInJourneyPatternRefStructure(PointInJourneyPatternRefStructure):
    pass
