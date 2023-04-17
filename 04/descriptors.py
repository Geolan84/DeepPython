"""That's a descriptors for experience, telegram and qualification fields (for example in resume)."""


class Experience:
    """Descriptor for count of experience years."""

    def __init__(self):
        self.__years = 0

    def __delete__(self, instance):
        return delattr(instance, "__years")

    def __get__(self, instance, owner):
        return getattr(instance, "__years")

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError("Years should be integer!")
        if value < 0:
            raise ValueError("Count of years should be positive!")
        return setattr(instance, "__years", value)


class Qualification:
    """Descriptor for qualification field."""

    values = ['Intern', 'Junior', 'Middle', 'Senior', 'Lead']

    def __init__(self):
        self.__qualification = self.values[0]

    def __delete__(self, instance):
        return delattr(instance, "__qualification")

    def __get__(self, instance, owner):
        return getattr(instance, "__qualification")

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError("Qualification is a string!")
        if value in self.values:
            return setattr(instance, "__qualification", value)
        raise ValueError(
            "Qualification can be: 'Intern', 'Junior', 'Middle', 'Senior' or 'Lead!")


class Telegram:
    """Descriptor for telegram link."""

    def __init__(self):
        self.__telegram = ""

    def __delete__(self, instance):
        return delattr(instance, "__telegram")

    def __get__(self, instance, owner):
        return getattr(instance, "__telegram")

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError("Telegram link should be string!")
        if len(value) < 5 or len(value) > 32 or value[0] != '@' or ' ' in value:
            raise ValueError(
                "Telegram format is @***** with length greater than 4 and lower than 33 and without spaces!")
        return setattr(instance, "__telegram", value)


class Data:

    experience = Experience()
    qualification = Qualification()
    telegram = Telegram()

    def __init__(self, experience=0, qualification='Intern', telegram="@nolink"):
        self.telegram = telegram
        self.qualification = qualification
        self.experience = experience
