from dataclasses import dataclass

from .customer_payment_means_ref_structure import CustomerPaymentMeansRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CustomerPaymentMeansRef(CustomerPaymentMeansRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
