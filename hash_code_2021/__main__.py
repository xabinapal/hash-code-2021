from hash_code_2021 import City, DummyScheduler, Simulator

import sys

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
    simulator.execute(scheduler)
