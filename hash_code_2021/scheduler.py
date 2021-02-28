class DummyScheduler:
    def __init__(self, city):
        self.__intersections = dict()
        for intersection in city.get_all_intersections():
            schedule = []
            for entrance in intersection.entrances.values():
                schedule.append((entrance, 1))

            self.__intersections[intersection.id] = tuple(schedule)

    def get_intersection(self, id):
        return self.__intersections[id]

    def print(self):
        print(len(self.__intersections))
        for id, schedule in self.__intersections.items():
            print(id)
            print(len(schedule))
            for street, duration in schedule:
                print(street.name, duration)
