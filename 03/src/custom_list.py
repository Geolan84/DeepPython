"""Module with CustomList class."""
from __future__ import annotations


class CustomList(list):
    """Custom list with overrided addition, subtraction, comparisons and str."""
    @staticmethod
    def __lists_addition(first, second) -> CustomList:
        result = CustomList([0] * max(len(first), len(second)))
        for index, _ in enumerate(result):
            if index < len(first):
                result[index] += first[index]
            if index < len(second):
                result[index] += second[index]
        return result

    @staticmethod
    def __lists_subtraction(first, second) -> CustomList:
        result = CustomList([0] * max(len(first), len(second)))
        for index, _ in enumerate(result):
            if index < len(first):
                result[index] += first[index]
            if index < len(second):
                result[index] -= second[index]
        return result

    def __add__(self, other) -> CustomList:
        if isinstance(other, (list, CustomList)):
            return CustomList.__lists_addition(self, other)
        raise AttributeError(
                "Addition is posible only for CustomLists and lists!")

    def __radd__(self, other) -> CustomList:
        if isinstance(other, (list, CustomList)):
            return CustomList.__lists_addition(other, self)
        raise AttributeError(
                "Addition is posible only for CustomLists and lists!")

    def __sub__(self, other) -> CustomList:
        if isinstance(other, (list, CustomList)):
            return CustomList.__lists_subtraction(self, other)
        raise AttributeError(
                "Subtraction is posible only for CustomLists and lists!")

    def __rsub__(self, other) -> CustomList:
        if isinstance(other, (list, CustomList)):
            return CustomList.__lists_subtraction(other, self)
        raise AttributeError(
                "Subtraction is posible only for CustomLists and lists!")

    def __str__(self) -> bool:
        return f"Items: {super().__str__()}; Sum: {sum(self)}"

    def __lt__(self, other) -> bool:
        return sum(self) < sum(other)

    def __le__(self, other) -> bool:
        return sum(self) <= sum(other)

    def __eq__(self, other) -> bool:
        return sum(self) == sum(other)

    def __ne__(self, other) -> bool:
        return sum(self) != sum(other)

    def __gt__(self, other) -> bool:
        return sum(self) > sum(other)

    def __ge__(self, other) -> bool:
        return sum(self) >= sum(other)
