# 1. შექმენი ქვეყნის აბსტრაქტული კლასი. რომელსაც
# ექნება მინიმუმ სამი აბსტრაქტული მეთოდი.
# 2. შექმენი მისგან საქართველოს კლასი, რომელსაც ექნება
# public, protected და private ცვლადები (მაგალითად
# ბიუჯეტი, მოსახლეობა და ა.შ.).
# 3. შექმენი საქართველოს ობიექტი და გამოიყენე
# ზემოხსენებული მეთოდები.

from abc import ABC, abstractmethod

class Countries(ABC):
    @abstractmethod
    def population(self):
        pass
    @abstractmethod
    def capital_city(self):
        pass
    @abstractmethod
    def constitutional_form(self):
        pass


class Georgia(Countries):
    def __init__(self ):
        self.__budget = "28,7 billion"
        self._perimeter = "69,700 km²"
        self.head_of_state = "Prime minister"

    def population(self):
        return "3.713 million"

    def capital_city(self):
        return "Tbilisi"

    def constitutional_form(self):
        return "Republic"


georgia = Georgia()

print("Head of State: ", georgia.head_of_state)
print("Population: ", georgia.population())
print("Constitutional Form: ", georgia.constitutional_form())
print("Capital City: ", georgia.capital_city())
print("Country perimeter: ", georgia._perimeter)



