from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional, Union

from xsdata.models.datatype import XmlDate

from .capping_rule_price_ref import CappingRulePriceRef
from .controllable_element_price_ref import ControllableElementPriceRef
from .customer_purchase_package_price_ref import CustomerPurchasePackagePriceRef
from .discounting_rule import DiscountingRule
from .discounting_rule_ref import DiscountingRuleRef
from .distance_matrix_element_price_ref import DistanceMatrixElementPriceRef
from .entity_in_version_structure import VersionedChildStructure
from .fare_price_ref import FarePriceRef
from .fare_product_price_ref import FareProductPriceRef
from .fare_structure_element_price_ref import FareStructureElementPriceRef
from .fulfilment_method_price_ref import FulfilmentMethodPriceRef
from .geographical_interval_price_ref import GeographicalIntervalPriceRef
from .geographical_unit_price_ref import GeographicalUnitPriceRef
from .limiting_rule import LimitingRule
from .limiting_rule_in_context import LimitingRuleInContext
from .limiting_rule_ref import LimitingRuleRef
from .multilingual_string import MultilingualString
from .parking_price_ref import ParkingPriceRef
from .price_rule_step_results_rel_structure import PriceRuleStepResultsRelStructure
from .price_unit_ref import PriceUnitRef
from .pricing_rule import PricingRule
from .pricing_rule_ref import PricingRuleRef
from .pricing_service_ref import PricingServiceRef
from .private_code import PrivateCode
from .quality_structure_factor_price_ref import QualityStructureFactorPriceRef
from .rounding_ref import RoundingRef
from .sales_offer_package_price_ref import SalesOfferPackagePriceRef
from .series_constraint_price_ref import SeriesConstraintPriceRef
from .time_interval_price_ref import TimeIntervalPriceRef
from .time_unit_price_ref import TimeUnitPriceRef
from .usage_parameter_price_ref import UsageParameterPriceRef
from .validable_element_price_ref import ValidableElementPriceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FarePriceVersionedChildStructure(VersionedChildStructure):
    class Meta:
        name = "FarePrice_VersionedChildStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    private_code: Optional[PrivateCode] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    start_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StartDate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    end_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "EndDate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
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
    is_allowed: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsAllowed",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    pricing_service_ref: Optional[PricingServiceRef] = field(
        default=None,
        metadata={
            "name": "PricingServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    fare_price_ref: Optional[
        Union[
            CustomerPurchasePackagePriceRef,
            ParkingPriceRef,
            TimeIntervalPriceRef,
            TimeUnitPriceRef,
            QualityStructureFactorPriceRef,
            ControllableElementPriceRef,
            ValidableElementPriceRef,
            GeographicalIntervalPriceRef,
            GeographicalUnitPriceRef,
            SeriesConstraintPriceRef,
            SalesOfferPackagePriceRef,
            DistanceMatrixElementPriceRef,
            FareStructureElementPriceRef,
            FulfilmentMethodPriceRef,
            CappingRulePriceRef,
            FareProductPriceRef,
            UsageParameterPriceRef,
            FarePriceRef,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "CustomerPurchasePackagePriceRef",
                    "type": CustomerPurchasePackagePriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingPriceRef",
                    "type": ParkingPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimeIntervalPriceRef",
                    "type": TimeIntervalPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimeUnitPriceRef",
                    "type": TimeUnitPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "QualityStructureFactorPriceRef",
                    "type": QualityStructureFactorPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ControllableElementPriceRef",
                    "type": ControllableElementPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidableElementPriceRef",
                    "type": ValidableElementPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeographicalIntervalPriceRef",
                    "type": GeographicalIntervalPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeographicalUnitPriceRef",
                    "type": GeographicalUnitPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SeriesConstraintPriceRef",
                    "type": SeriesConstraintPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesOfferPackagePriceRef",
                    "type": SalesOfferPackagePriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DistanceMatrixElementPriceRef",
                    "type": DistanceMatrixElementPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareStructureElementPriceRef",
                    "type": FareStructureElementPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FulfilmentMethodPriceRef",
                    "type": FulfilmentMethodPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CappingRulePriceRef",
                    "type": CappingRulePriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareProductPriceRef",
                    "type": FareProductPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UsageParameterPriceRef",
                    "type": UsageParameterPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FarePriceRef",
                    "type": FarePriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    discounting_rule_ref_or_pricing_rule_ref_or_pricing_rule: Optional[Union[LimitingRuleRef, DiscountingRuleRef, PricingRuleRef, LimitingRuleInContext, LimitingRule, DiscountingRule, PricingRule]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "LimitingRuleRef",
                    "type": LimitingRuleRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DiscountingRuleRef",
                    "type": DiscountingRuleRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PricingRuleRef",
                    "type": PricingRuleRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LimitingRuleInContext",
                    "type": LimitingRuleInContext,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LimitingRule",
                    "type": LimitingRule,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DiscountingRule",
                    "type": DiscountingRule,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PricingRule",
                    "type": PricingRule,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    can_be_cumulative: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CanBeCumulative",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    rounding_ref: Optional[RoundingRef] = field(
        default=None,
        metadata={
            "name": "RoundingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    ranking: Optional[int] = field(
        default=None,
        metadata={
            "name": "Ranking",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
