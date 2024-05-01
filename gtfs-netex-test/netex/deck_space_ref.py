from dataclasses import dataclass

from .deck_space_ref_structure import DeckSpaceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DeckSpaceRef(DeckSpaceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
