import random
grandma = 42

random.seed(grandma)

def is_train():
    return random.random() <= 0.9