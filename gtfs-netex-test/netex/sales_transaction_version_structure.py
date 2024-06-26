from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from .customer_purchase_packages_rel_structure import CustomerPurchasePackagesRelStructure
from .fare_contract_entry_version_structure import FareContractEntryVersionStructure
from .multilingual_string import MultilingualString
from .organisational_unit_ref import OrganisationalUnitRef
from .payment_method_enumeration import PaymentMethodEnumeration
from .point_version_structure import PointVersionStructure
from .price_rule_step_results_rel_structure import PriceRuleStepResultsRelStructure
from .price_unit_ref import PriceUnitRef
from .private_code_structure import PrivateCodeStructure
from .retail_device_ref import RetailDeviceRef
from .travel_documents_rel_structure import TravelDocumentsRelStructure
from .travel_specifications_rel_structure import TravelSpecificationsRelStructure
from .type_of_payment_method_ref import TypeOfPaymentMethodRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SalesTransactionVersionStructure(FareContractEntryVersionStructure):
    class Meta:
        name = "SalesTransaction_VersionStructure"

    amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    currency: Optional[str] = field(
        default=None,
        metadata={
            "name": "Currency",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_length": 3,
            "max_length": 3,
            "pattern": r"[A-Z][A-Z][A-Z]",
        },
    )
    price_unit_ref: Optional[PriceUnitRef] = field(
        default=None,
        metadata={
            "name": "PriceUnitRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    units: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Units",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    rule_step_results: Optional[PriceRuleStepResultsRelStructure] = field(
        default=None,
        metadata={
            "name": "ruleStepResults",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    payment_method: Optional[PaymentMethodEnumeration] = field(
        default=None,
        metadata={
            "name": "PaymentMethod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_payment_method_ref: Optional[TypeOfPaymentMethodRef] = field(
        default=None,
        metadata={
            "name": "TypeOfPaymentMethodRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    card_number: Optional[PrivateCodeStructure] = field(
        default=None,
        metadata={
            "name": "CardNumber",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    travel_specifications: Optional[TravelSpecificationsRelStructure] = field(
        default=None,
        metadata={
            "name": "travelSpecifications",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    customer_purchase_packages: Optional[CustomerPurchasePackagesRelStructure] = field(
        default=None,
        metadata={
            "name": "customerPurchasePackages",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    travel_documents: Optional[TravelDocumentsRelStructure] = field(
        default=None,
        metadata={
            "name": "travelDocuments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    collection_point_ref: Optional[PointVersionStructure] = field(
        default=None,
        metadata={
            "name": "CollectionPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    collection_note: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "CollectionNote",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    organisational_unit_ref: Optional[OrganisationalUnitRef] = field(
        default=None,
        metadata={
            "name": "OrganisationalUnitRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    retail_device_ref: Optional[RetailDeviceRef] = field(
        default=None,
        metadata={
            "name": "RetailDeviceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
