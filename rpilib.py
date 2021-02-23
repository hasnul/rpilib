import RPi.GPIO as GPIO
from dataclasses import dataclass

@dataclass
class Port:
    portnum: int
    direction: 'typing.Any'
    is_setup: bool
    pull: 'typing.Any'

class InputOutput:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        self.available_ports = []
        self.available_ports.extend(range(4, 7))
        self.available_ports.extend([12, 13, 16, 17, 19])
        self.available_ports.extend(range(20, 28))
        self.ports = {}
        for port in self.available_ports:
            self.ports[port] = Port(port, GPIO.OUT, False, None)

    def print(self):
        for port in self.ports:
            print(self.ports[port])

    def setup(self, port, direction, initial=None, pull=None):
        if (port not in self.ports):
            print(f'Unavailable port: {port}')
            return False
        if (direction == "output" or direction == GPIO.OUT or direction == 0):
            io = GPIO.OUT
            if (initial == 0 or initial == "low"):
                initial = GPIO.LOW
            elif (initial == 1 or initial == "high"):
                initial = GPIO.HIGH
            elif (initial != GPIO.LOW and initial != GPIO.HIGH):
                print(f'Invalid initial value: {initial}')
                return False
            GPIO.setup(port, io, initial=initial)
            self.ports[port] = Port(port, io, True, None)
            return True
        elif (direction == "input" or direction == GPIO.IN or direction == 1):
            io = GPIO.IN
            # TODO:
            return True
        else:
            print(f'Error: port direction: {direction}')
            return False

    def is_output(self, port):
        if (port not in self.ports):
            print(f'Unavailable port: {port}')
            return False
        if (self.ports[port].direction != GPIO.OUT):
            print(f'Port: {port} is not output')
            return False
        if (not self.ports[port].is_setup):
            print(f'Port: {port} is not set up')
            return False
        return True

    def output_high(self, port):
        if (is_output(port)):
            GPIO.output(port, GPIO.HIGH)

    def output_low(port):
        if (is_output(port)):
            GPIO.output(port, GPIO.LOW)
