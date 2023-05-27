"""Module with custom metaclass."""


class CustomMeta(type):
    """Custom meta class which adds 'custom_' prefix to attributes."""
    def __setattr__(cls, name: str, value):
        if not (name.startswith("__") and name.endswith("__")):
            cls.__dict__[f"custom_{name}"] = value
        else:
            cls.__dict__[name] = value

    def __new__(mcs, name, bases, classdict: dict):
        namespace = {}
        for key, value in classdict.items():
            if not (key.startswith("__") and key.endswith("__")):
                namespace[f"custom_{key}"] = value
            else:
                namespace[key] = value

        namespace["__setattr__"] = mcs.__setattr__
        return super().__new__(mcs, name, bases, namespace)
