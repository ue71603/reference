from dataclasses import dataclass
from .type_of_entity_version_structure import TypeOfEntityVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfResponsibilityRoleValueStructure(TypeOfEntityVersionStructure):
    class Meta:
        name = "TypeOfResponsibilityRole_ValueStructure"
