from dataclasses import dataclass

from .stop_place_space_ref_structure import StopPlaceSpaceRefStructure

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass(kw_only=True)
class AccessSpaceRefStructure(StopPlaceSpaceRefStructure):
    pass
