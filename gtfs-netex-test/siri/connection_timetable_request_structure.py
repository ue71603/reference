from dataclasses import dataclass, field
from typing import List, Optional

from .abstract_functional_service_request_structure import AbstractFunctionalServiceRequestStructure
from .closed_timestamp_range_structure import ClosedTimestampRangeStructure
from .connection_link_ref_structure import ConnectionLinkRefStructure
from .direction_ref_structure import DirectionRefStructure
from .extensions_1 import Extensions1
from .include_translations import IncludeTranslations
from .line_ref_structure import LineRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ConnectionTimetableRequestStructure(AbstractFunctionalServiceRequestStructure):
    arrival_window: Optional[ClosedTimestampRangeStructure] = field(
        default=None,
        metadata={
            "name": "ArrivalWindow",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    connection_link_ref: ConnectionLinkRefStructure = field(
        metadata={
            "name": "ConnectionLinkRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    line_ref: Optional[LineRefStructure] = field(
        default=None,
        metadata={
            "name": "LineRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    direction_ref: Optional[DirectionRefStructure] = field(
        default=None,
        metadata={
            "name": "DirectionRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    language: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Language",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    include_translations: Optional[IncludeTranslations] = field(
        default=None,
        metadata={
            "name": "IncludeTranslations",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    extensions: Optional[Extensions1] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    version: str = field(
        default="2.1",
        metadata={
            "type": "Attribute",
        },
    )
