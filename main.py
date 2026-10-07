import random
import numpy as np
from constants import TYPE_A, WATER, GRASS, EMPTY, WORLD_SIZE
from world_renderer import WorldRenderer


death_counter = 0

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
    if organism["energy"] <= 0:
        organisms.remove(organism)
        death_counter += 1
        return
    if organism["hunger"] >= 100:
        organisms.remove(organism)
        death_counter += 1
        return
    if organism["thirst"] >= 100:
        organisms.remove(organism)
        death_counter += 1
        return
    # TODO: Implement movement, figure out closest water and grass source and do a random selection of which one to go to



def create_org_a(generation):
    return {
        "age": 1,
        "generation": generation + 1,
        "type": "A",
        "strength": random.random(),
        "speed": random.random(),
        "intelligence": random.random(),
        "energy": 100,
        "hunger": 0,
        "thirst": 0,
        "coordinates": (
            random.randint(0, WORLD_SIZE - 1),
            random.randint(0, WORLD_SIZE - 1),
        ),
    }


organisms = []


def start(world=None):
    if world is None:
        world = generate_world(WORLD_SIZE)
    renderer = WorldRenderer(world)

    day = 0
    year = 0
    for _ in range(10):
        organisms.append(create_org_a(0))
        # add to world
        world[organisms[-1]["coordinates"]] = TYPE_A

        # while True:
        #     for organism in organisms:
        #         org_behaviour(organism, world)

        renderer.save(world, organisms, day, year)
        day += 1
        if day % 365 == 0:
            year += 1
            print("Year: ", year)
            day = 0

    renderer.close()


if __name__ == "__main__":
    world = generate_world(WORLD_SIZE)
    start(world)
