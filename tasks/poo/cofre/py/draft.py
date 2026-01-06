from abc import ABC, abstractmethod
from enum import Enum
from typing import List

class Valuable(ABC):
    @abstractmethod
    def getLabel(self) -> str:
        pass

    @abstractmethod
    def getValue(self) -> float:
        pass

    @abstractmethod
    def getVolume(self) -> int:
        pass

    def __str__(self) -> str:
        return f"{self.getLabel()}:{self.getValue():.2f}:{self.getVolume()}"

class Coin(Enum):
    M10 = ("M10", 0.10, 1)
    M25 = ("M25", 0.25, 2)
    M50 = ("M50", 0.50, 3)
    M100 = ("M100", 1.00, 4)

    def __init__(self, label: str, value: float, volume: int):
        self._label = label
        self._value = value
        self._volume = volume

    def getLabel(self) -> str:
        return self._label
    def getValue(self) -> float:
        return self._value

    def getVolume(self) -> int:
        return self._volume
    
    def __str__(self) -> str:
        return f"{self.getLabel()}:{self.getValue():.2f}:{self.getVolume()}"
class Item(Valuable):
    def __init__(self, label: str, value: float, volume: int):
        self.label = label
        self.value = value
        self.volume = volume

    def getLabel(self) -> str:
        return self.label

    def getValue(self) -> float:
        return self.value

    def getVolume(self) -> int:
        return self.volume





class Pig:
    def __init__(self, volumeMax: int):
        self.volumeMax = volumeMax
        self.items: List[Valuable] = []
        self.broken = False

    def addValuable(self, valuable: Valuable) -> bool:
        if self.broken:
            print("fail: the pig is broken")
            return False
        if self.getVolume() + valuable.getVolume() > self.volumeMax:
            print("fail: the pig is full")
            return False
        self.items.append(valuable)
        return True

    def breakPig(self) -> bool:
        if self.broken:
            return False
        self.broken = True
        return True

    def getItems(self) -> List[Item]:
        if not self.broken:
            print("fail: you must break the pig first")
            return []
        items = [i for i in self.items if isinstance(i, Item)]
        self.items = [i for i in self.items if not isinstance(i, Item)]
        return items

    def getCoins(self) -> List[Coin]:
        if not self.broken:
            print("fail: you must break the pig first")
            return []
        coins = [i for i in self.items if isinstance(i, Coin)]
        self.items = [i for i in self.items if not isinstance(i, Coin)]
        return coins

    def calcValue(self) -> float:
        return sum(i.getValue() for i in self.items)

    def getVolume(self) -> int:
        if self.broken:
            return 0
        return sum(i.getVolume() for i in self.items)

    def getVolumeMax(self) -> int:
        return self.volumeMax

    def isBroken(self) -> bool:
        return self.broken

    def __str__(self) -> str:
        content = ", ".join(str(i) for i in self.items)
        status = "broken" if self.broken else "intact"
        return f"[{content}] : {self.calcValue():.2f}$ : {self.getVolume()}/{self.volumeMax} : {status}"










def main():
    pig = None

    while True:
    
        line = input().strip()
        print(f"$" + line)
        if line == "end":
            break
        
        parts = line.split()
        cmd = parts[0]

        if cmd == "init":
            pig = Pig(int(parts[1]))

        elif cmd == "show":
            print(pig)

        elif cmd == "addCoin":
            coin_map = {
                "10": Coin.M10,
                "25": Coin.M25,
                "50": Coin.M50,
                "100": Coin.M100
            }
            coin = coin_map.get(parts[1])
            if coin:
                pig.addValuable(coin)
            else:
                print("fail: invalid coin")

        elif cmd == "addItem":
            pig.addValuable(Item(parts[1], float(parts[2]), int(parts[3])))

        elif cmd == "break":
            pig.breakPig()

        elif cmd == "extractItems":
            items = pig.getItems()
            if items:
                print(f"[{', '.join(str(i) for i in items)}]")

        elif cmd == "extractCoins":
            coins = pig.getCoins()
            if coins:
                print(f"[{', '.join(str(c) for c in coins)}]")


main()
