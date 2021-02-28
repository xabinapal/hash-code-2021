from hash_code_2021 import Car, Intersection, Street


class City:
    def __init__(self):
        self.__intersections = dict()
        self.__streets = dict()
        self.__streets_by_name = dict()
        self.__cars = list()

    def __get_or_create_intersection(self, id):
        if id not in self.__intersections:
            self.__intersections[id] = Intersection(id)
        return self.__intersections[id]

    def get_intersection(self, id):
        return self.__intersections[int(id)]

    def get_all_intersections(self):
        for street in self.__intersections.values():
            yield street

    def get_street(self, id: int):
        return self.__streets[id]

    def get_street_by_name(self, name):
        return self.__streets_by_name[name]

    def get_all_streets(self):
        for street in self.__streets.values():
            yield street

    def add_street(self, data):
        start, end, name, length = data.split(" ")
        id = len(self.__streets_by_name)

        start_intersection = self.__get_or_create_intersection(int(start))
        end_intersection = self.__get_or_create_intersection(int(end))

        street = Street(id, name, int(length), start_intersection, end_intersection)
        self.__streets[id] = street
        self.__streets_by_name[name] = street

        start_intersection.add_exit(street)
        end_intersection.add_entrance(street)

    def get_all_cars(self):
        for car in self.__cars:
            yield car

    def get_car_count(self):
        return len(self.__cars)

    def add_car(self, data):
        id = len(self.__cars) + 1
        path = [self.get_street_by_name(name) for name in data.split(" ")[1:]]

        car = Car(id, path)
        self.__cars.append(car)

        for street in car.path:
            street.total_cars += 1

    def simplify(self):
        unused_streets = {x.id for x in self.__streets.values() if x.total_cars == 0}
        for street_id in unused_streets:
            street = self.__streets[street_id]
            street.start_intersection.remove_exit(street)
            street.end_intersection.remove_entrance(street)
            del self.__streets[street_id]

        unused_intersections = [
            id
            for id, intersection in self.__intersections.items()
            if len(intersection.exits) == 0 or len(intersection.entrances) == 0
        ]
        for intersection_id in unused_intersections:
            del self.__intersections[intersection_id]
