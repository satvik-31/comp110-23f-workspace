"""function practice."""

from __future__ import annotations

class Course:
    """Models UNC course."""
    name: str
    level: int
    prerequisites: list[str]

def find_courses(course_list: list[Course], prerequisite: str) -> list[str]:
    """"""

    def is_valid_course(self, course_name: str) -> bool:
        """Takes in course name and checks if course level is above 400."""
        i: int = 0 
        while i < len(self.prerequisites):
            if course_name == self.prerequisites[i] and 

