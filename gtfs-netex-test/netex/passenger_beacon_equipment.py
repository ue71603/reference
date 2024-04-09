from dataclasses import dataclass

from .passenger_beacon_equipment_version_structure import PassengerBeaconEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PassengerBeaconEquipment(PassengerBeaconEquipmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
