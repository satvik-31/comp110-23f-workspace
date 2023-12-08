"""Function writing."""

class Course:
    """Models the idea of a UNC course."""
    name: str
    level: int 
    prerequisites: list[str]

    def is_valid_course(self, pre: str) -> bool:
        """Method to find courses."""
        valid: bool = False
        if self.level >= 400 and pre in self.prerequisites:
            valid = True
        else:
            valid = False
        return valid 


def find_courses(list_of_courses: list[Course], pre: str) -> list[str]:
    """UNC find courses."""
    list_of_courses_above_400: list[str] = []
    for elem in list_of_courses:
        if elem.level >= 400 and pre in elem.prerequisites:
                list_of_courses_above_400.append(elem.name)
                elem.prerequisites.append(pre)
    return list_of_courses_above_400

   

