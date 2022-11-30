import random


def produce_characters(start:int =1, stop:int = 82)-> int:
    return (random.randint(1,82) for item in range(1,16))

