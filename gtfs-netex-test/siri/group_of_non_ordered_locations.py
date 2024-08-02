from dataclasses import dataclass, field
from typing import List, Optional

from .extension_type import ExtensionType
from .group_of_locations import GroupOfLocations
from .location import Location

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class GroupOfNonOrderedLocations(GroupOfLocations):
    location_contained_in_group: List[Location] = field(
        default_factory=list,
        metadata={
            "name": "locationContainedInGroup",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "min_occurs": 1,
        },
    )
    group_of_non_ordered_locations_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "groupOfNonOrderedLocationsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
