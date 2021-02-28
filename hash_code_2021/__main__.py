import argparse
import logging
import os
import random
import sys

from hash_code_2021 import City, Simulator
from hash_code_2021 import DummyScheduler, CongestionScheduler

LOG_LEVEL = os.environ.get("LOG_LEVEL", "WARN").upper()
logging.basicConfig(level=LOG_LEVEL)

parser = argparse.ArgumentParser()
parser.add_argument("action", type=str, choices=["submit", "simulate", "genetic"])
parser.add_argument("--optimize", action=argparse.BooleanOptionalAction)
parser.add_argument("--scheduler", type=str, choices=["dummy", "congestion"])

arguments = parser.parse_args()

# Read input
duration, num_intersections, num_streets, num_cars, bonus_score = (
    int(x) for x in input().split(" ")
)

city = City()
for _ in range(num_streets):
    city.add_street(input())

for _ in range(num_cars):
    city.add_car(input())

if arguments.optimize:
    city.simplify()

scheduler = None
if arguments.scheduler == "dummy":
    scheduler = DummyScheduler(city)
elif arguments.scheduler == "congestion":
    scheduler = CongestionScheduler(city, int(os.environ.get("CONGESTION_FACTOR", "1")))

if arguments.action == "submit":
    scheduler.print()
elif arguments.action == "simulate":
    simulator = Simulator(city, duration, bonus_score)
    simulator.prepare()
    score = simulator.execute(scheduler)
    print(f"Score: {score}")
elif arguments.action == "genetic":
    seed = int(os.environ.get("SEED"))
    population = int(os.environ.get("POPULATION"))
    iterations = int(os.environ.get("ITERATIONS"))
    mutation_probability = float(os.environ.get("MUTATION_PROBABILITY"))

    random.seed(seed)

    import hash_code_2021.genetic as genetic

    simulator = Simulator(city, duration, bonus_score)
    simulator.prepare()

    car_count = city.get_car_count()
    creatures = genetic.create_population(
        scheduler, population, mutation_probability, car_count
    )

    best_score, best_scheduler = genetic.execute(
        simulator, population, iterations, creatures, mutation_probability, car_count
    )

    scheduler.print()
