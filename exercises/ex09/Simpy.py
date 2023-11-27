"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730517765"


class Simpy:
    values: list[float]

    # TODO: Your constructor and methods will go here.
    def __init__(self, ones: list[float]):
        """Initialize arguments to attirbute value."""
        self.values = ones

    def __str__(self):
        """Prints result of the attributes."""
        result: str = f"Simpy({self.values})"
        return result
    
    def fill(self, number_to_fill: float, number_of_vals_to_fill: int):
        """Fill Simpy's values with a specific number of repeating values."""
        filled_with = []
        i: int = 0
        while i < number_of_vals_to_fill:
            filled_with.append(number_to_fill)
            i += 1
        self.values = filled_with        
        return None
    
    def arange(self, start: float, stop: float, step: float = 1.0):
        """Fill in the values attribute with a range of values between start and stop."""
        assert step != 0.0
        list_w_ranges = []
        i: float = start
        while i != stop:
            list_w_ranges.append(i)
            i += step
        self.values = list_w_ranges
        return None
    
    def sum(self) -> float:
        """Adds the values in Simpy."""
        result: list[float] = self.values
        return sum(result)
    
    def __add__(self, factor: Simpy | float ) -> Simpy:
        """Returns a new Simpy Object."""
        result = Simpy([])
        if type(factor) != float:
            assert len(self.values) == len(factor.values)
            for idx in range(len(self.values)):
                result.values.append(self.values[idx] + factor.values[idx])
        else:
            for elem in self.values:
                result.values.append(elem + factor)
        return result
    
    def __pow__(self, factor: Simpy | float) -> Simpy:
        """Exponent function."""
        result = Simpy([])
        if type(factor) != float:
            assert len(self.values) == len(factor.values)
            for idx in range(len(self.values)):
                result.values.append(self.values[idx] ** factor.values[idx])
        else:
            for elem in self.values:
                result.values.append(elem ** factor)
        return result
    
    def __eq__(self, factor: Simpy | float) -> list[bool]:
        """Called when == operator is used."""
        list: list[bool] = []
        if type(factor) is float:
            for elem in self.values:
                if elem == factor:
                    list.append(True)
                else:
                    list.append(False) 
        else:
            idx: int = 0
            while idx < len(self.values):
                if self.values[idx] == factor.values[idx]:
                    list.append(True)
                else:
                    list.append(False) 
                idx += 1    
        return list
    
    def __gt__(self, factor: Simpy | float):
        """Called when == operator is used."""
        list: list[bool] = []
        if type(factor) is float:
            for elem in self.values:
                if elem > factor:
                    list.append(True)
                else:
                    list.append(False) 
        else:
            idx: int = 0
            while idx < len(self.values):
                if self.values[idx] > factor.values[idx]:
                    list.append(True)
                else:
                    list.append(False) 
                idx += 1
        return list
    
    def __getitem__(self, factor: int | Simpy) -> float | Simpy:
        """Susbcription Notation with SImpy."""
        result: float = 0.0
        result_simpy: Simpy = Simpy([])
        if type(factor) is int:
            result = self.values[factor]
            return result
        else:
            i: int = 0
            while i < len(factor):
                if factor[i] is True:
                    result_simpy.values.append(self.values[i])
                i += 1
            return result_simpy

"""
pull = Simpy([1.,1.,1.,1.])
print(pull)
twos = Simpy([])
twos.fill(2.0,3)
print("Actual: ", twos, " - Expected: Simpy([2.0, 2.0, 2.0])")
negative = Simpy([])
negative.arange
"""
            
            

            
            



    

