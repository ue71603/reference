from dataclasses import dataclass, field
from typing import List, Optional

from .extension_type import ExtensionType
from .external_referencing import ExternalReferencing
from .point_coordinates import PointCoordinates

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class Location:
    external_referencing: List[ExternalReferencing] = field(
        default_factory=list,
        metadata={
            "name": "externalReferencing",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    location_for_display: Optional[PointCoordinates] = field(
        default=None,
        metadata={
            "name": "locationForDisplay",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    location_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "locationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
