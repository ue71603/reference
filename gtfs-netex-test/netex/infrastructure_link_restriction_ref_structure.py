from dataclasses import dataclass

from .network_restriction_ref_structure import NetworkRestrictionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class InfrastructureLinkRestrictionRefStructure(NetworkRestrictionRefStructure):
    pass
