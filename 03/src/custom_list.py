from __future__ import annotations


class CustomList(list):

    @staticmethod
    def __lists_addition(first, second) -> CustomList:
        result = CustomList([0] * max(len(first), len(second)))
        for i in range(len(result)):
            if i < len(first):
                result[i] += first[i]
            if i < len(second):
                result[i] += second[i]
        return result

    @staticmethod
    def __lists_subtraction(first, second) -> CustomList:
        result = CustomList([0] * max(len(first), len(second)))
        for i in range(len(result)):
            if i < len(first):
                result[i] += first[i]
            if i < len(second):
                result[i] -= second[i]
        return result

    def __add__(self, other) -> CustomList:
        if isinstance(other, list) or isinstance(other, CustomList):
            return CustomList.__lists_addition(self, other)
        else:
            raise AttributeError(
                "Addition is posible only for CustomLists and lists!")

    def __radd__(self, other) -> CustomList:
        if isinstance(other, list) or isinstance(other, CustomList):
            return CustomList.__lists_addition(other, self)
        else:
            raise AttributeError(
                "Addition is posible only for CustomLists and lists!")

    def __sub__(self, other) -> CustomList:
        if isinstance(other, list) or isinstance(other, CustomList):
            return CustomList.__lists_subtraction(self, other)
        else:
            raise AttributeError(
                "Subtraction is posible only for CustomLists and lists!")

    def __rsub__(self, other) -> CustomList:
        if isinstance(other, list) or isinstance(other, CustomList):
            return CustomList.__lists_subtraction(other, self)
        else:
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
