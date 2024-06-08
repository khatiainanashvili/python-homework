# 1. შექმენი ტრანსპორტის კლასი მინიმუმ 4 კლასის პარამეტრით
# 2. დაამატე ერთი სტატიკური მეთოდი.
# 3. დაამატე ორი კლასის მეთოდი.
# 4. დაამატე __init__ magic მეთოდი და მინიმუმ 3 ობიექტის
# პარამეტრი.
# 5. დაამატე მინიმუმ 2, ობიექტის მეთოდი.
# 6. დაამატე __repr__ magic მეთოდი
# 7. ზემოხსენებული კლასისგან შექმენი მინიმუმ 5 ობიექტი და
# გამოიძახე მისი ზოგიერთი მეთოდი და პარამეტრი.

class Transport:
    wheel = 4
    steering_wheel = 1
    horsepower = 200
    weight = 1000
    @staticmethod
    def number_of_drivers():
        driver = 1
        return driver
    @classmethod
    def show_horsepower(cls):
        print(f"car's Horsepower is {cls.horsepower}")

    def __init__(self, name, country, year):

        self.name = name
        self.country = country
        self.year = year

    def __repr__(self):
        return f"Car({self.name}, {self.year}, {self.country})"


my_car = Transport("Toyota", 2020, "Japan")
print(repr(my_car))

print(Transport.number_of_drivers())
Transport.show_horsepower()

car1 = Transport("Fiat", "Italy", 1994)
car2 = Transport("Hyundai", "Korea", 2011)
car3 = Transport("Toyota", "Japan", 2020)
car4 = Transport("BMW", "Germany", 2014)
car5 = Transport("Chevrolet", "USA", 2018)

print(car1.country)

