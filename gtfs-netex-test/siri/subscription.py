from dataclasses import dataclass, field
from typing import List, Optional

from xsdata.models.datatype import XmlDateTime

from .catalogue_reference import CatalogueReference
from .extension_type import ExtensionType
from .filter_reference import FilterReference
from .operating_mode_enum import OperatingModeEnum
from .subscription_state_enum import SubscriptionStateEnum
from .target import Target
from .update_method_enum import UpdateMethodEnum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class Subscription:
    delete_subscription: Optional[bool] = field(
        default=None,
        metadata={
            "name": "deleteSubscription",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    delivery_interval: Optional[float] = field(
        default=None,
        metadata={
            "name": "deliveryInterval",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    operating_mode: OperatingModeEnum = field(
        metadata={
            "name": "operatingMode",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    subscription_start_time: XmlDateTime = field(
        metadata={
            "name": "subscriptionStartTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    subscription_state: SubscriptionStateEnum = field(
        metadata={
            "name": "subscriptionState",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    subscription_stop_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "subscriptionStopTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    update_method: UpdateMethodEnum = field(
        metadata={
            "name": "updateMethod",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    target: List[Target] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "min_occurs": 1,
        },
    )
    filter_reference: Optional[FilterReference] = field(
        default=None,
        metadata={
            "name": "filterReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    catalogue_reference: Optional[CatalogueReference] = field(
        default=None,
        metadata={
            "name": "catalogueReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    subscription_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "subscriptionExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
