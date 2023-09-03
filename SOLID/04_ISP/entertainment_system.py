from abc import ABC, abstractmethod


class Cable(ABC):
    @abstractmethod
    def connect(self,d1, d2):
        pass


class HDMICable(Cable):
    def connect(self,device1, device2):
        return f"Connect {device1} to {device2} via HDMI"


class RCACable(Cable):
    def connect(self,device1, device2):
        return f"Connect {device1} to {device2} via RCA"


class EthernetCable(Cable):
    def connect(self,device1, device2):
        return f"Connect {device1} to {device2} via Ethernet"


class PowerOutlet(Cable):
    def connect(self, destination, _):
        return f"Connect evice to power"


class DvDPlayer(Cable):
    pass


class EntertainmentDevice:
    def connect_to_device_via_hdmi_cable(self, device): pass
    def connect_to_device_via_rca_cable(self, device): pass
    def connect_to_device_via_ethernet_cable(self, device): pass
    def connect_device_to_power_outlet(self, device): pass


class Television(EntertainmentDevice):
    def connect_to_dvd(self, dvd_player):
        self.connect_to_device_via_rca_cable(dvd_player)

    def connect_to_game_console(self, game_console):
        self.connect_to_device_via_hdmi_cable(game_console)

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)


class DVDPlayer(EntertainmentDevice):
    def connect_to_tv(self, television):
        self.connect_to_device_via_hdmi_cable(television)

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)


class GameConsole(EntertainmentDevice):
    def connect_to_tv(self, television):
        self.connect_to_device_via_hdmi_cable(television)

    def connect_to_router(self, router):
        self.connect_to_device_via_ethernet_cable(router)

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)


class Router(EntertainmentDevice):
    def connect_to_tv(self, television):
        self.connect_to_device_via_ethernet_cable(television)

    def connect_to_game_console(self, game_console):
        self.connect_to_device_via_ethernet_cable(game_console)

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)
