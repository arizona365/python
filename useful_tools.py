import random
feet_in_mile = 5280
meters_inkilometer = 1000
beatles = ["John Lennon", "Paul McCartney", "Garry Merry"]

def get_file_ext(filename):
    return filename[filename.index(".") + 1:]

def roll_dice(num):
    return random.randint(1, num)