from dataclasses import dataclass, field
from typing import List, Union
from .containment_aggregation_structure import ContainmentAggregationStructure
from .type_of_fare_contract_entry import TypeOfFareContractEntry
from .type_of_fare_contract_entry_ref import TypeOfFareContractEntryRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypesOfFareContractEntryRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "typesOfFareContractEntry_RelStructure"

    type_of_fare_contract_entry_ref_or_type_of_fare_contract_entry: List[
        Union[TypeOfFareContractEntryRef, TypeOfFareContractEntry]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TypeOfFareContractEntryRef",
                    "type": TypeOfFareContractEntryRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFareContractEntry",
                    "type": TypeOfFareContractEntry,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
