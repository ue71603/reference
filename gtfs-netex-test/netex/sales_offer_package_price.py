from dataclasses import dataclass
from .sales_offer_package_price_versioned_child_structure import (
    SalesOfferPackagePriceVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SalesOfferPackagePrice(SalesOfferPackagePriceVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
