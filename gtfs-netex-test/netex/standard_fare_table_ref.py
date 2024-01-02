from dataclasses import dataclass
from .standard_fare_table_ref_structure import StandardFareTableRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class StandardFareTableRef(StandardFareTableRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
