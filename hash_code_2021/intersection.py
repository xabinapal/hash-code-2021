from dataclasses import dataclass


@dataclass(init=False)
class Intersection:
    id: int
    exits: dict
    entrances: dict

    def __init__(self, id):
        self.id = id
        self.exits = dict()
        self.entrances = dict()

    def add_exit(self, street):
        self.exits[street.id] = street

    def add_entrance(self, street):
        self.entrances[street.id] = street

    def remove_exit(self, street):
        del self.exits[street.id]

    def remove_entrance(self, street):
        del self.entrances[street.id]
