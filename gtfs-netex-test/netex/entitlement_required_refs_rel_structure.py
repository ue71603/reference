from dataclasses import dataclass, field
from typing import List
from .entitlement_required_ref import EntitlementRequiredRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class EntitlementRequiredRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "entitlementRequiredRefs_RelStructure"

    entitlement_required_ref: List[EntitlementRequiredRef] = field(
        default_factory=list,
        metadata={
            "name": "EntitlementRequiredRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
