import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.patches import Patch

from .main import WORLD_SIZE, WATER, GRASS, EMPTY, TYPE_A



def show_world(world):
    cmap = ListedColormap(["beige", "blue", "green"])
    plt.figure(figsize=(8, 8))
    plt.imshow(world, cmap=cmap, vmin=0, vmax=2, interpolation="nearest")
    plt.legend(handles=[Patch(color="beige", label="Empty"),
                        Patch(color="blue", label="Water"),
                        Patch(color="green", label="Grass")],
               loc="upper right", bbox_to_anchor=(1.25, 1))
    plt.axis("off")
    plt.tight_layout()
    plt.show()

def generate_world(grid_size):
    world = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
    for row in range(grid_size):
        for col in range(grid_size):
            rand_num = random.randint(0, 100)
            if rand_num < 10:
                world[row][col] = WATER
            elif rand_num < 30:
                world[row][col] = GRASS
            else:
                world[row][col] = EMPTY
    return np.array(world)


def org_behaviour(organism, world):
    pass


def create_org_a(generation):
    return {
        "age" : 1,
        "generation" : generation+1,
        "type" : "A",
        "strength" : random.random(0,1),
        "speed": random.random(0,1),
        "intelligence": random.random(0,1),
        "energy": 100,
        "hunger": 0,
        "thirst": 0,
        "coordinates": (random.randint(0, WORLD_SIZE-1), random.randint(0, WORLD_SIZE-1))
    }


world = generate_world(WORLD_SIZE)
show_world(world)

organisms = []
def start(world = None):
    if world is None:
        world = generate_world(WORLD_SIZE)

    year = 0
    for _ in range(10):
        organisms.append(create_org_a(0))
    while True:

        show_world(world)
        year += 1
