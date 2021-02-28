import logging

from collections import deque
from dataclasses import dataclass


@dataclass(init=False)
class SimulationCar:
    __slots__ = (
        "id",
        "path",
    )

    id: id
    path: deque

    def __init__(self, id, path):
        self.id = id
        self.path = deque([street.id for street in path])


@dataclass(init=False)
class SimulationIntersection:
    __slots__ = (
        "id",
        "traffic_lights",
        "streets",
        "schedule",
        "current_light",
        "current_light_time",
    )

    id: int

    traffic_lights: dict
    streets: dict

    schedule: tuple
    current_light: int
    current_light_time: int

    def __init__(self, id):
        self.id = id

        self.traffic_lights = dict()
        self.streets = dict()

        self.schedule = []
        self.current_light = -1
        self.current_light_time = -1

    def add_exit(self, street):
        self.streets[street.id] = street

    def add_entrance(self, street):
        self.traffic_lights[street.id] = street

    def set_schedule(self, schedule):
        self.schedule = schedule

        self.current_light = -1
        self.current_light_time = -1

    def cycle_traffic_lights(self):
        if self.current_light_time == -1:
            self.current_light = 0
            self.current_light_time = 0
            self.traffic_lights[self.schedule[self.current_light][0]].set_open(True)
        elif len(self.schedule) > 1:
            self.current_light_time += 1
            if self.current_light_time == self.schedule[self.current_light][1]:
                self.traffic_lights[self.schedule[self.current_light][0]].set_open(
                    False
                )

                self.current_light = (self.current_light + 1) % len(self.traffic_lights)
                self.current_light_time = 0

                self.traffic_lights[self.schedule[self.current_light][0]].set_open(
                    True
                )


@dataclass(init=False)
class SimulationStreet:
    __slots__ = (
        "id",
        "length",
        "intersection",
        "is_open",
        "cars_in_transit",
        "cars_in_light",
    )

    id: int
    length: int
    intersection: SimulationIntersection

    is_open: bool
    cars_in_transit: deque
    cars_in_light: deque

    def __init__(self, id, length, intersection):
        self.id = id
        self.length = length
        self.intersection = intersection

        self.cars_in_transit = deque()
        self.cars_in_light = deque()
        self.is_open = False

    def set_open(self, state):
        logging.debug(
            f"Set street's {self.id} traffic light to {'green' if state else 'red'}"
        )
        self.is_open = state

    def add_car(self, car, end_of_street=False):
        if end_of_street:
            logging.debug(f"Adding car {car.id} to end of street {self.id}")
            self.cars_in_light.append(car)
        else:
            logging.debug(f"Adding car {car.id} to start of street {self.id}")
            self.cars_in_transit.append((car, 0))

    def clear(self):
        self.cars_in_light.clear()
        self.cars_in_transit.clear()
        self.is_open = False

    def finish_cars(self):
        try:
            if self.is_open:
                car = self.cars_in_light.popleft()
                new_street = car.path.popleft()
                logging.debug(
                    f"Moving car {car.id} from street {self.id} to street {new_street}"
                )
                self.intersection.streets[new_street].add_car(car)
        except IndexError:
            # no cars to move, ignore
            pass

    def move_cars(self):
        has_finished = False
        new_cars_in_transit = deque()
        for car, position in self.cars_in_transit:
            logging.debug(
                f"Advancing car {car.id} through street {self.id} to position {position + 1}"
            )
            if position == self.length - 1:
                if len(car.path):
                    self.cars_in_light.append(car)
                else:
                    has_finished = True
            else:
                new_cars_in_transit.append((car, position + 1))
        self.cars_in_transit = new_cars_in_transit
        return has_finished


class Simulator:
    def __init__(self, city, duration, bonus_score):
        self.city = city
        self.duration = duration
        self.bonus_score = bonus_score

        self.streets = {}
        self.intersections = {}

    def prepare(self):
        for street in self.city.get_all_streets():
            sim_entrance = self.__create_intersection(street.end_intersection.id)
            sim_exit = self.__create_intersection(street.start_intersection.id)

            sim_street = self.__create_street(street.id, street.length, sim_entrance)

            if sim_entrance is not None:
                sim_entrance.add_entrance(sim_street)

            if sim_exit is not None:
                sim_exit.add_exit(sim_street)

    def __create_intersection(self, id):
        try:
            return self.intersections[id]
        except KeyError:
            try:
                self.city.get_intersection(id)
            except KeyError:
                return None

            intersection = SimulationIntersection(id)
            self.intersections[intersection.id] = intersection

            return intersection

    def __create_street(self, id, length, exit):
        street = SimulationStreet(id, length, exit)
        self.streets[id] = street

        return street

    def execute(self, scheduler):
        intersections = self.intersections.values()
        streets = self.streets.values()

        for id, intersection in self.intersections.items():
            schedule = scheduler.get_intersection(id)
            intersection.set_schedule(schedule)

        for street in self.streets.values():
            street.clear()

        for car in self.city.get_all_cars():
            sim_car = SimulationCar(car.id, car.path)
            street = sim_car.path.popleft()
            self.streets[street].add_car(sim_car, True)

        tick = 0
        score = 0
        remaining_cars = self.city.get_car_count()
        while tick < self.duration and remaining_cars > 0:
            tick += 1

            logging.info(f"Tick: #{tick}")

            for intersection in intersections:
                intersection.cycle_traffic_lights()

            for street in streets:
                street.finish_cars()

            for street in streets:
                if street.move_cars():
                    score += self.bonus_score + self.duration - tick
                    remaining_cars -= 1

        logging.info(f"Score: {score}")
        return score
