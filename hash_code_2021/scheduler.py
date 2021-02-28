import json
import math


class Scheduler:
    def __init__(self):
        self._intersections = dict()

    def get_intersection(self, id):
        return self._intersections[id]

    def print(self):
        print(len(self._intersections))
        for id, schedule in self._intersections.items():
            print(id)
            print(len(schedule))
            for street, duration in schedule:
                print(street.name, duration)

    def serialize(self):
        return json.dumps(self._intersections)

    @classmethod
    def deserialize(cls, data):
        scheduler = cls()
        scheduler._intersections = json.loads(data)


class DummyScheduler(Scheduler):
    def __init__(self, city):
        super().__init__()

        for intersection in city.get_all_intersections():
            schedule = []
            for entrance in intersection.entrances.values():
                time = 1
                schedule.append((entrance.id, time))

            self._intersections[intersection.id] = tuple(schedule)


class CongestionScheduler(Scheduler):
    def __init__(self, city, factor):
        super().__init__()

        for intersection in city.get_all_intersections():
            schedule = []
            total_cars = sum(
                street.total_cars for street in intersection.entrances.values()
            )
            for entrance in intersection.entrances.values():
                time = math.ceil(
                    len(intersection.entrances) * (entrance.total_cars / total_cars) / factor
                )
                schedule.append((entrance.id, time))

            self._intersections[intersection.id] = tuple(
                sorted(schedule, key=lambda x: intersection.entrances[x[0]].starting_cars, reverse=True)
            )