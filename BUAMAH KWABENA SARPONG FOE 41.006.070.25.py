# Parent class
class TrafficDevice:
    def activate(self):
        print("Traffic device activated")


# Child classes
class TrafficLight(TrafficDevice):
    def activate(self):
        print("Green light is ON")


class SpeedCamera(TrafficDevice):
    def activate(self):
        print("Speed camera is capturing vehicles")


class PedestrianSignal(TrafficDevice):
    def activate(self):
        print("Walk signal is ON")


class EmergencySiren(TrafficDevice):
    def activate(self):
        print("Emergency siren is ON")


# Store objects in a list
devices = [
    TrafficLight(),
    SpeedCamera(),
    PedestrianSignal(),
    EmergencySiren()
]

# Activate all devices
for device in devices:
    device.activate()