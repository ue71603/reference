from dataclasses import dataclass, field
from typing import Optional

from .extension_type import ExtensionType
from .network_management import NetworkManagement
from .speed_management_type_enum import SpeedManagementTypeEnum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class SpeedManagement(NetworkManagement):
    speed_management_type: Optional[SpeedManagementTypeEnum] = field(
        default=None,
        metadata={
            "name": "speedManagementType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    temporary_speed_limit: Optional[float] = field(
        default=None,
        metadata={
            "name": "temporarySpeedLimit",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    speed_management_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "speedManagementExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
