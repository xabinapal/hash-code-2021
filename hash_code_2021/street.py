from dataclasses import dataclass

from hash_code_2021 import Intersection


@dataclass
class Street:
    id: int
    name: str
    length: int
    start_intersection: Intersection
    end_intersection: Intersection

    total_cars: int = 0
    starting_cars: int = 0
