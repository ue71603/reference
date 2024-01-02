from dataclasses import dataclass
from .rhythmical_journey_group_ref_structure import (
    RhythmicalJourneyGroupRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RhythmicalJourneyGroupRef(RhythmicalJourneyGroupRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
