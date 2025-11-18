# without abstraction
class Laptop():
    def usb_slot(self):
        pass
    def hdmi_slot(self):
        pass
    def c_port(self):
        pass

class Lenovo(Laptop):
    def usb_slot(self):
        print("Lenovo USB slot")
    def hdmi_slot(self):
        print("Lenovo HDMI slot")


class Dell(Laptop):
    def usb_slot(self):
        print("Dell USB slot")
    def c_port(self):
        print("Dell C port")

# user
print("user buying lenovo laptop")
lenovo = Lenovo()
lenovo.usb_slot()
lenovo.hdmi_slot()

print("user buying dell laptop")
dell = Dell()
dell.usb_slot()
dell.c_port()



# achieve abstraction - we use abc (abstract base class)
from abc import ABC, abstractmethod

class Laptop(ABC):
    @abstractmethod
    def usb_slot(self):
        pass

    @abstractmethod
    def hdmi_slot(self):
        pass

    @abstractmethod
    def c_port(self):
        pass

class Lenovo(Laptop):
    def usb_slot(self):
        print("Lenovo USB slot")

    def hdmi_slot(self):
        print("Lenovo HDMI slot")

    def c_port(self):
        print("Lenovo C port")

class Dell(Laptop):
    def usb_slot(self):
        print("Dell USB slot")

    def hdmi_slot(self):
        print("Dell HDMI slot")

    def c_port(self):
        print("Dell C port")

    def bluetooth(self):
        print("Dell Bluetooth")
 
# user
print("user buying lenovo laptop")
lenovo = Lenovo()   
lenovo.usb_slot()
lenovo.hdmi_slot()
lenovo.c_port()

print("user buying dell laptop")
dell = Dell()
dell.usb_slot()
dell.hdmi_slot()
dell.c_port()
dell.bluetooth()
