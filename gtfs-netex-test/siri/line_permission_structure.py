from dataclasses import dataclass, field
from typing import List

from .abstract_topic_permission_structure import AbstractTopicPermissionStructure
from .direction_ref_structure import DirectionRefStructure
from .line_ref_structure import LineRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class LinePermissionStructure(AbstractTopicPermissionStructure):
    line_ref: LineRefStructure = field(
        metadata={
            "name": "LineRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    direction_ref: List[DirectionRefStructure] = field(
        default_factory=list,
        metadata={
            "name": "DirectionRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
