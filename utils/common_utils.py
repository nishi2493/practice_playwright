import random


def generate_random_email():
    number = random.randint(1000, 9999)
    return f"testuser{number}@example.com"