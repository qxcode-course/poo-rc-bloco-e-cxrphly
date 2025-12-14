from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, idd, entry):
        self.id = idd
        self.entry = entry
        self.type = self.get_type()

    @abstractmethod
    def calc_value(self, exit_time):
        pass

    @abstractmethod
    def get_type(self):
        pass

    def __str__(self):
        return (
            self.type.rjust(10, "_")
            + " : "
            + self.id.rjust(10, "_")
            + " : "
            + str(self.entry)
        )


class Bike(Vehicle):
    def get_type(self):
        return "Bike"

    def calc_value(self, exit_time):
        return 3.00


class Motorcycle(Vehicle):
    def get_type(self):
        return "Moto"

    def calc_value(self, exit_time):
        return (exit_time - self.entry) / 20


class Car(Vehicle):
    def get_type(self):
        return "Carro"

    def calc_value(self, exit_time):
        return max((exit_time - self.entry) / 10, 5.00)


class Parking:
    def __init__(self):
        self.time = 0
        self.vehicles = []

    def advance_time(self, minutes):
        self.time += minutes

    def park(self, v_type, idd):
        if v_type == "bike":
            v = Bike(idd, self.time)
        elif v_type == "moto":
            v = Motorcycle(idd, self.time)
        elif v_type == "carro":
            v = Car(idd, self.time)
        else:
            print("fail: tipo invalido")
            return

        self.vehicles.append(v)

    def pay(self, idd):
        for v in self.vehicles:
            if v.id == idd:
                value = v.calc_value(self.time)
                print(
                    f"{v.type} chegou {v.entry} saiu {self.time}. "
                    f"Pagar R$ {value:.2f}"
                )
                self.vehicles.remove(v)
                return
        print("fail: veiculo nao encontrado")

    def show(self):
        for v in self.vehicles:
            print(v)
        print(f"Hora atual: {self.time}")


def main():
    parking = Parking()

    while True:
        try:
            line = input().strip()
            parts = line.split()
            cmd = parts[0]
            print("$" + line)
            if cmd == "end":
                break
            elif cmd == "tempo":
                parking.advance_time(int(parts[1]))
            elif cmd == "estacionar":
                parking.park(parts[1], parts[2])
            elif cmd == "pagar":
                parking.pay(parts[1])
            elif cmd == "show":
                parking.show()
            else:
                print("fail: comando invalido")
        except EOFError:
            break


main()