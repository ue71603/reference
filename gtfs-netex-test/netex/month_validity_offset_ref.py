from dataclasses import dataclass

from .month_validity_offset_ref_structure import MonthValidityOffsetRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class MonthValidityOffsetRef(MonthValidityOffsetRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
