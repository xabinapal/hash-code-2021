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


class DummyScheduler(Scheduler):
    def __init__(self, city):
        super().__init__()

        for intersection in city.get_all_intersections():
            schedule = []
            for entrance in intersection.entrances.values():
                schedule.append((entrance, 1))

            self._intersections[intersection.id] = tuple(schedule)
