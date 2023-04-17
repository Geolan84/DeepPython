class CustomMeta(type):
    def __setattr__(cls, name: str, value):
        custom_key = "custom_{0}".format(name)
        cls.__dict__[custom_key] = value

    def __new__(cls, name, bases, classdict: dict):
        namespace = dict()
        for key, value in classdict.items():
            if not (key.startswith("__") and key.endswith("__")):
                namespace["custom_{0}".format(key)] = value
            else:
                namespace[key] = value

        namespace["__setattr__"] = cls.__setattr__
        return super().__new__(cls, name, bases, namespace)

