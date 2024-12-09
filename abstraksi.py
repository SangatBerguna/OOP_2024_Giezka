from abc import ABC, abstractmethod

class Gojek(ABC):
    def __init__(self, name):
        self._name = name

    @abstractmethod
    def speak(self):
        pass

    def get_name(self):
        return self._name

class GoRide(Gojek):
    def speak(self):
        return "Perjalanan pendek"

class GoCar(Gojek):
    def speak(self):
        return "Taksi online"

class GoFood(Gojek):
    def speak(self):
        return "Pesan-antar makanan"

Ojek_Online = [GoRide("Buddy"), GoCar("Whiskers"), GoFood("Daisy")]

for Gojek in Ojek_Online:
    print(Gojek.get_name() + " says " + Gojek.speak())