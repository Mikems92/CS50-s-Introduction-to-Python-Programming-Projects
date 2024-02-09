from jar import Jar
import pytest


def test_init():
    jar = Jar ()
    assert jar.capacity == 12
    jar = Jar(100)
    assert jar.capacity == 100

def test_str():
    jar = Jar()
    assert str(jar) == ""


def test_deposit():
    jar = Jar()
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_withdraw():
    jar = Jar()
    jar.deposit(5)
    jar.withdraw(3)
    assert str(jar) == "🍪🍪"

