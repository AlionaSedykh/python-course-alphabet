"""
Вам небхідно написати 3 класи. Колекціонери Гаражі та Автомобілі.
Звязкок наступний один колекціонер може мати багато гаражів.
В одному гаражі може знаходитися багато автомобілів.

Автомобіль має наступні характеристики:
    price - значення типу float. Всі ціни за дефолтом в одній валюті.
    type - одне з перечисленних значеннь з CARS_TYPES в docs.
    producer - одне з перечисленних значеннь в CARS_PRODUCER.
    number - значення типу UUID. Присвоюється автоматично при створенні автомобілю.
    mileage - значення типу float. Пробіг автомобіля в кілометрах.


    Автомобілі можна перівнювати між собою за ціною.
    При виводі(logs, print) автомобілю повинні зазначатися всі його атрибути.

    Автомобіль має метод заміни номеру.
    номер повинен відповідати UUID

Гараж має наступні характеристики:

    town - одне з перечислениз значеннь в TOWNS
    cars - список з усіх автомобілів які знаходяться в гаражі
    places - значення типу int. Максимально допустима кількість автомобілів в гаражі
    owner - значення типу UUID. За дефолтом None.


    Повинен мати реалізованими наступні методи

    add(car) -> Добавляє машину в гараж, якщо є вільні місця
    remove(cat) -> Забирає машину з гаражу.
    hit_hat() -> Вертає сумарну вартість всіх машин в гаражі


Колекціонер має наступні характеристики
    name - значення типу str. Його ім'я
    garages - список з усіх гаражів які належать цьому Колекціонеру. Кількість гаражів за замовчуванням - 0
    register_id - UUID; Унікальна айдішка Колекціонера.

    Повинні бути реалізовані наступні методи:
    hit_hat() - повертає ціну всіх його автомобілів.
    garages_count() - вертає кількість гаріжів.
    сars_count() - вертає кількість машиню
    add_car() - додає машину у вибраний гараж. Якщо гараж не вказаний, то додає в гараж, де найбільше вільних місць.
    Якщо вільних місць немає повинне вивести повідомлення про це.

    Колекціонерів можна порівнювати за ціною всіх їх автомобілів.
"""


import uuid
from objects_and_classes.homework import constants
import random


class Car:
    def __init__(self,  price, type, producer, mileage):
        self.price = price
        self.type = type
        self.producer = producer
        self.number = uuid.uuid4()
        self.mileage = mileage

    def __repr__(self):
        return "Price: {0}, Type: {1}, Producer: {2}, Car number: {3}, " \
               "Mileage: {4}".format(self.price, self.type, self.producer, self.number, self.mileage)

    def compare_by_price(self, another_car):
        if self.price > another_car.price:
            return "The price of car {0} is higher than the price of car {1}".format(self.number, another_car.number)
        elif self.price < another_car.price:
            return "The price of {0} is lower than the price of car {1}".format(self.number, another_car.number)
        else:
            return "The prices of both cars are equal"

    def change_number(self, new_number):
        if uuid.UUID(new_number, version=4):
            self.number = new_number
            return "Car number was changed. A new one {0}".format(new_number)
        else:
            return "Please, enter UUID type of number"


class Garage:
    def __init__(self, town, places, owner=None):
        self.town = town
        self.cars = []
        self.places = places
        self.owner = owner

    def __str__(self):
        return "Town: {0}. Garage capacity: {1}. Cars in garage: {2}. Owner: {3}"\
            .format(self.town, self.places, len(self.cars), self.owner)

    def add_car(self, new_car):
        if len(self.cars) < self.places:
            self.cars.append(new_car)
            return "A new car has been added"
        else:
            return "Garage is full of cars. Please find another garage"

    def remove_car(self, car_for_removing):
        if car_for_removing in self.cars:
            self.cars.remove(car_for_removing)
            return "The car has been took off from the garage"
        else:
            return "There is no such a car"

    def hit_hat(self):
        if self.cars:
            return "Total price for all cars in the garage: {0}"\
                .format(sum([car.price for car in self.cars]))
        else:
            return "The garage is empty"


class Cesar:
    def __init__(self, name):
        self.name = name
        self.garages = []
        self.register_id = uuid.uuid4()

    def __str__(self):
        return str(self.name)

    def hit_hat_garages(self, ):
        total_cars_price = 0
        for garage in self.garages:
            for car in garage.cars:
                total_cars_price += car.price
        return total_cars_price
        # return "Total price of all {0}'s cars is {1}".format(self.name, total_cars_price)

    def garages_count(self):
        return "Number of garages owned by {0} is {1}.".format(self.name, len(self.garages))

    def add_car_in_garage(self, new_car, garage=None):
        if garage is not None:  # if garage was mentioned
            if garage in self.garages:  # check if garage belong to the owner
                if garage.places - len(garage.cars) > 0:  # check if garage have free places
                    garage.cars.append(new_car)
                    return "The car has been added to the garage {0}".format(garage)
                else:  # garage doesn't have free places
                    return "No places in this garage. Try another."
            else:  # the garage doesn't belong to the owner
                return "It is not your garage. Try another."
        else:  # if garage wasn't mentioned
            garages_with_free_places = dict()  # create a dictionary with garages and number of free places in them
            for garage in self.garages:
                garages_with_free_places[garage] = garage.places - len(garage.cars)
            #  create a dictionary with garage with maximum number of free places
            garage_with_max_free_place = {k: v for k, v in garages_with_free_places.items()
                                          if v == max(garages_with_free_places.values())}
            for value in garage_with_max_free_place.values():  # if value(free places) in garage with maximum number
                # of free places = 0 it means all places in garage are full
                if value == 0:
                    return "No free places in your garages. Buy one more garage."
                else:
                    for garage in self.garages:
                        if garage in garage_with_max_free_place.keys():
                            garage.cars.append(new_car)
                            return "The car has been added in garage {0}".format(garage)

    def compare_cesars(self, other_cesar):
        if self.hit_hat_garages() > other_cesar.hit_hat_garages():
            return "The owner {0} is richer than the owner {1}".format(self.name, other_cesar.name)
        elif self.hit_hat_garages() < other_cesar.hit_hat_garages():
            return "The owner {0} is poorer than the owner {1}".format(self.name, other_cesar.name)
        else:
            return "The total price of their cars is equal"


"""Input data"""
car_1 = Car(float(20000), random.choice(constants.CARS_TYPES), random.choice(constants.CARS_PRODUCER), float(17000))
car_2 = Car(float(18600), random.choice(constants.CARS_TYPES), random.choice(constants.CARS_PRODUCER), float(180002))
car_3 = Car(float(16500), random.choice(constants.CARS_TYPES), random.choice(constants.CARS_PRODUCER), float(100000))
car_4 = Car(float(1500), random.choice(constants.CARS_TYPES), random.choice(constants.CARS_PRODUCER), float(90000))
car_5 = Car(float(100005), random.choice(constants.CARS_TYPES), random.choice(constants.CARS_PRODUCER), float(80002))
car_6 = Car(float(128900), random.choice(constants.CARS_TYPES), random.choice(constants.CARS_PRODUCER), float(70002))
car_7 = Car(float(8500), random.choice(constants.CARS_TYPES), random.choice(constants.CARS_PRODUCER), float(60002))
car_8 = Car(float(11650), random.choice(constants.CARS_TYPES), random.choice(constants.CARS_PRODUCER), float(50002))
car_9 = Car(float(33600), random.choice(constants.CARS_TYPES), random.choice(constants.CARS_PRODUCER), float(40002))
car_10 = Car(float(58900), random.choice(constants.CARS_TYPES), random.choice(constants.CARS_PRODUCER), float(30002))
garage_1 = Garage(random.choice(constants.TOWNS), int(8), str(uuid.uuid4()))
garage_2 = Garage(random.choice(constants.TOWNS), int(2), str(uuid.uuid4()))
garage_3 = Garage(random.choice(constants.TOWNS), int(2), str(uuid.uuid4()))
garage_4 = Garage(random.choice(constants.TOWNS), int(5), str(uuid.uuid4()))
owner_1 = Cesar('Tom')
owner_2 = Cesar('John')


"""Check of Car Class"""
print(car_1)
print(car_2)
print(car_1.compare_by_price(car_2))
print("Car number before changes: ", car_1.number)
new_number = str(uuid.uuid4())
print(car_1.change_number(new_number))


"""Check of Garage Class"""
garage_1.cars = [car_1, car_2, car_3]
garage_2.cars = [car_4, car_5]
garage_3.cars = [car_6]
garage_4.cars = [car_7, car_8, car_9]
print(garage_1)
print(garage_1.add_car(car_9))
print(garage_1.remove_car(car_5))
print('Total number of cars after removing: ', len(garage_1.cars))
print(garage_1.hit_hat())
print(garage_2.hit_hat())
print(garage_3.hit_hat())
print(garage_4.hit_hat())


"""Check of Cesar Class"""
owner_1.garages = [garage_1, garage_2, garage_3]
owner_2.garages = [garage_4]
print(owner_1.hit_hat_garages())
print(owner_2.hit_hat_garages())
print(owner_1.garages_count(), owner_2.garages_count())
print(owner_1.add_car_in_garage(car_10, garage_3))
print(owner_1.add_car_in_garage(car_10, garage_2))
print(owner_2.add_car_in_garage(car_10, garage_1))
print(owner_2.add_car_in_garage(car_10))
print(owner_1.add_car_in_garage(car_10))
print(owner_2.compare_cesars(owner_1))
