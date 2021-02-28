import os
import logging
import sys

from hash_code_2021 import City, DummyScheduler, Simulator

LOG_LEVEL = os.environ.get("LOG_LEVEL", "WARN").upper()
logging.basicConfig(level=LOG_LEVEL)

# Read input
duration, num_intersections, num_streets, num_cars, bonus_score = (
    int(x) for x in input().split(" ")
)

city = City()
for _ in range(num_streets):
    city.add_street(input())

for _ in range(num_cars):
    city.add_car(input())

city.simplify()

scheduler = DummyScheduler(city)

if sys.argv[1] == "submit":
    scheduler.print()
elif sys.argv[1] == "simulate":
    simulator = Simulator(city, duration, bonus_score)
    simulator.prepare()
    score = simulator.execute(scheduler)
    print(f"Score: {score}")
