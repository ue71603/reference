from dataclasses import dataclass
from .point_ref_structure import PointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PointRef(PointRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
