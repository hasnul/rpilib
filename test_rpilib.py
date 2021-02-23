import RPi.GPIO as GPIO
from rpilib import InputOutput


def test_output_setup():
    testio = InputOutput()
    unavailable = 15
    assert not testio.setup(unavailable, "output", initial=1)
    assert not testio.setup(12, "output", initial=3.3)
    assert not testio.setup(12, "output", initial=5)
    bad_direction = "out"
    assert not testio.setup(22, bad_direction, initial=1)
    assert not testio.setup(3, "output", initial=1)
    assert testio.setup(4, "output", initial=0)
    assert testio.setup(4, "output", initial=1)
    assert testio.setup(5, "output", initial="low")
    assert testio.setup(5, "output", initial="high")
    assert testio.setup(6, GPIO.OUT, initial=1)
    assert testio.setup(16, 0, initial=1)
    assert not testio.setup(7, "output", initial=1)
    assert not testio.setup(28, "output", initial=1)


def test_input_setup():
    testio = InputOutput()
    assert testio.setup(5, "input", pull=GPIO.PUD_UP)
    assert testio.setup(17, GPIO.IN, pull=GPIO.PUD_UP)
    assert testio.setup(19, 1, pull=GPIO.PUD_UP)


def test_is_output():
    testio = InputOutput()
    assert not testio.is_output(100)
    testio.ports[20].direction = GPIO.IN 
    assert not testio.is_output(20)
    assert not testio.is_output(5)
    testio.setup(4, "output", 1)
    assert testio.is_output(4)


def test_is_avail():
    testio = InputOutput()
    assert not testio.is_avail(10)
    assert testio.is_avail(5)
