"""
Для попереднього домашнього завдання.
Для класу Колекціонер Машина і Гараж написати методи, які створюють інстанс обєкту
з (yaml, json, pickle) файлу відповідно

Для класів Колекціонер Машина і Гараж написати методи, які зберігають стан обєкту в файли формату
yaml, json, pickle відповідно.

Для класів Колекціонер Машина і Гараж написати методи, які конвертують обєкт в строку формату
yaml, json, pickle відповідно.

Для класу Колекціонер Машина і Гараж написати методи, які створюють інстанс обєкту
з (yaml, json, pickle) строки відповідно


Advanced
Добавити опрацьовку формату ini

"""

import uuid
from objects_and_classes.homework import constants
import random
import json
import pickle
from ruamel.yaml import YAML


class Car:
    def __init__(self,  price, type, producer, mileage):
        self.price = price
        self.type = type
        self.producer = producer
        self.number = uuid.uuid4()
        self.mileage = mileage

    def compare_by_price(self, another_car):
        if self.price > another_car.price:
            return f"The price of car {self.number} is higher than the price of car { another_car.number}"
        elif self.price < another_car.price:
            return f"The price of {self.number} is lower than the price of car {another_car.number}"
        else:
            return "The prices of both cars are equal"

    def change_number(self, new_number):
        if uuid.UUID(new_number, version=4):
            self.number = new_number
            return f"Car number was changed. A new one {new_number}"
        else:
            return "Please, enter UUID type of number"

    @staticmethod
    def to_json(obj):
        if isinstance(obj, Car):
            return {
                'price': obj.price,
                'type': obj.type,
                'producer': obj.producer,
                'mileage': obj.mileage
            }
        raise TypeError(str(obj) + ' is not serializable')

    def convert_to_json_file(self):
        with open("Car.json", 'w') as file:
            return json.dump(self, file, indent=4, default=self.to_json)

    def convert_to_json_str(self):
        return json.dumps(self, default=self.to_json)

    def convert_to_yaml_file(self):
        yaml = YAML(typ='unsafe')
        with open("Car.yaml", "w") as file:
            return yaml.dump(self, file)

#    def convert_to_yaml_str(self):
#        yaml = YAML(typ='unsafe')
#        return yaml.dump(self)

    def convert_to_pickle_file(self):
        with open("Car.txt", 'wb') as file:
            return pickle.dump(self, file)

    def convert_to_pickle_str(self):
        return pickle.dumps(self)

    def __repr__(self):
        return f"Price: {self.price}, Type: {self.type}, Producer: {self.producer}, " \
            f"Car number: {self.number}, Mileage: {self.mileage}"


class Garage:
    def __init__(self, town, places, owner=None):
        self.town = town
        self.cars = []
        self.places = places
        self.owner = owner

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
            return f"Total price for all cars in the garage: {sum([car.price for car in self.cars])}"
        else:
            return "The garage is empty"

    @staticmethod
    def to_json(obj):
        if isinstance(obj, Garage):
            return {
                'town': obj.town,
                'places': obj.places,
                'owner': obj.owner,
            }
        raise TypeError(str(obj) + ' is not serializable')

    def convert_to_json_file(self):
        with open("Garage.json", 'w') as file:
            json.dump(self, file, indent=4, default=self.to_json)

    def convert_to_json_str(self):
        return json.dumps(self, default=self.to_json)

    def convert_to_yaml_file(self):
        yaml = YAML(typ='unsafe')
        with open("Garage.yaml", "w") as file:
            return yaml.dump(self, file)

#    def convert_to_yaml_str(self):
#        yaml = YAML(typ='unsafe')
#        return yaml.dump(self)

    def convert_to_pickle_file(self):
        with open("Garage.txt", 'wb') as file:
            return pickle.dump(self, file)

    def convert_to_pickle_str(self):
        return pickle.dumps(self)

    def __str__(self):
        return f"Town: {self.town}. Garage capacity: {self.places}. " \
            f"Cars in garage: {self.cars}. Owner: {self.owner}"


class Cesar:
    def __init__(self, name):
        self.name = name
        self.garages = []
        self.register_id = uuid.uuid4()

    def hit_hat_garages(self, ):
        total_cars_price = 0
        for garage in self.garages:
            for car in garage.cars:
                total_cars_price += car.price
        return total_cars_price
        # return "Total price of all {0}'s cars is {1}".format(self.name, total_cars_price)

    def garages_count(self):
        return f"Number of garages owned by {self.name} is {self.garages}."

    def add_car_in_garage(self, new_car, garage=None):
        if garage is not None:  # if garage was mentioned
            if garage in self.garages:  # check if garage belong to the owner
                if garage.places - len(garage.cars) > 0:  # check if garage have free places
                    garage.cars.append(new_car)
                    return f"The car has been added to the garage {garage}"
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
                            return f"The car has been added in garage {garage}"

    def compare_cesars(self, other_cesar):
        if self.hit_hat_garages() > other_cesar.hit_hat_garages():
            return f"The owner {self.name} is richer than the owner {other_cesar.name}"
        elif self.hit_hat_garages() < other_cesar.hit_hat_garages():
            return f"The owner {self.name} is poorer than the owner {other_cesar.name}"
        else:
            return "The total price of their cars is equal"

    @staticmethod
    def to_json(obj):
        if isinstance(obj, Cesar):
            return {
                'name': obj.name,
            }
        raise TypeError(str(obj) + ' is not serializable')

    def convert_to_json_file(self):
        with open("Cesar.json", 'w') as file:
            return json.dump(self, file, indent=4, default=self.to_json)

    def convert_to_json_str(self):
        return json.dumps(self, default=self.to_json)

    def convert_to_yaml_file(self):
        yaml = YAML(typ='unsafe')
        with open("Cesar.yaml", "w") as file:
            return yaml.dump(self, file)

#    def convert_to_yaml_str(self):
#        yaml = YAML(typ='unsafe')
#        return yaml.dump(self)

    def convert_to_pickle_file(self):
        with open("Cesar.txt", 'wb') as file:
            return pickle.dump(self, file)

    def convert_to_pickle_str(self):
        return pickle.dumps(self)

    def __str__(self):
        return str(self.name)


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

"""Check"""

"""написати методи, які зберігають стан обєкту в файли формату
yaml, json, pickle відповідно"""

"""JSON"""
car_1.convert_to_json_file()
garage_1.convert_to_json_file()
owner_1.convert_to_json_file()
"""YAML"""
car_1.convert_to_yaml_file()
garage_1.convert_to_yaml_file()
owner_1.convert_to_yaml_file()
"""PICKLE"""
car_1.convert_to_pickle_file()
garage_1.convert_to_pickle_file()
owner_1.convert_to_pickle_file()

"""написати методи, які конвертують обєкт в строку формату
yaml, json, pickle відповідно"""

"""JSON"""
print("JSON str")
car_2_json_str = car_2.convert_to_json_str()
print(type(car_2_json_str), car_2_json_str)
garage_2_json_str = garage_2.convert_to_json_str()
print(type(garage_2_json_str), garage_2_json_str)
owner_2_json_str = owner_2.convert_to_json_str()
print(type(owner_2_json_str), owner_2_json_str)
"""PICKLE"""
print("PICKLE str")
car_2_pickle_str = car_2.convert_to_pickle_str()
print(type(car_2_pickle_str), car_2_pickle_str)
garage_2_pickle_str = garage_2.convert_to_pickle_str()
print(type(garage_2_pickle_str), garage_2_pickle_str)
owner_2_pickle_str = owner_2.convert_to_pickle_str()
print(type(owner_2_pickle_str), owner_2_pickle_str)


"""написати методи, які створюють інстанс обєкту
з (yaml, json, pickle) файлу відповідно"""

yaml = YAML(typ='unsafe')


def load_from_json_file():
    with open("Car.json", 'r') as file:
        return json.load(file)


def load_from_yaml_file():
    with open("Car.yaml", 'r') as file:
        return yaml.load(file)


def load_from_pickle_file():
    with open("Car.txt", 'rb') as file:
        return pickle.load(file)


print('Deserialize from JSON file')
car_11 = Car(**load_from_json_file())
print(type(car_11), car_11)

print('Deserialize from YAML file')
car_12 = load_from_yaml_file()
print(type(car_12), car_12)

print('Deserialize from PICKLE file')
car_13 = load_from_pickle_file()
print(type(car_13), car_13)

"""методи, які створюють інстанс обєкту
з (yaml, json, pickle) строки відповідно"""


def load_from_json_str(json_str):
    return json.loads(json_str)


def load_from_pickle_str(pickle_str):
    return pickle.loads(pickle_str)


print('Deserialize from JSON str')
car_14 = Car(**load_from_json_str(car_2_json_str))
print(type(car_14), car_14)

print('Deserialize from PICKLE str')
car_15 = load_from_pickle_str(car_2_pickle_str)
print(type(car_15), car_15)
