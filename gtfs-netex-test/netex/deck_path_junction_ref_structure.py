from dataclasses import dataclass

from .generic_path_junction_ref_structure import GenericPathJunctionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DeckPathJunctionRefStructure(GenericPathJunctionRefStructure):
    pass
