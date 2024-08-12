import random
from data import DataForOrder


def generate_name():
    return random.choice(DataForOrder.NAMES)

def generate_surname():
    return random.choice(DataForOrder.SURNAMES)

def generate_address():
    return random.choice(DataForOrder.ADDRESSES)

def generate_station():
    return random.choice(DataForOrder.STATIONS)

def generate_phone():
    number = random.randint(1111111111, 9999999999)
    return f'+7{number}'

def generate_rental_period():
    return random.choice(DataForOrder.RENTAL_PERIODS)

def generate_color():
    return random.choice(DataForOrder.COLORS)

def generate_comment():
    return random.choice(DataForOrder.COMMENTS)
