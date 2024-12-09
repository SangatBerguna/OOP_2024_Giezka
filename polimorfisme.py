class Gojek:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")


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
    print(Gojek.name + " says " + Gojek.speak())
