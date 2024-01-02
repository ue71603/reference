from dataclasses import dataclass
from .reselling_version_structure import ResellingVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Reselling(ResellingVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
