from dataclasses import dataclass, field
from typing import Optional

from .construction_work_type_enum import ConstructionWorkTypeEnum
from .extension_type import ExtensionType
from .roadworks import Roadworks

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class ConstructionWorks(Roadworks):
    construction_work_type: Optional[ConstructionWorkTypeEnum] = field(
        default=None,
        metadata={
            "name": "constructionWorkType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    construction_works_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "constructionWorksExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
