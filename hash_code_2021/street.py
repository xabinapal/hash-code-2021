from dataclasses import dataclass

from hash_code_2021 import Intersection


@dataclass
class Street:
    id: int
    name: str
    length: int
    start_intersection: Intersection
    end_intersection: Intersection
