import enum


class ChoiceEnum(enum.Enum):
    @classmethod
    def choices(cls):
        return tuple((x.name, x.value) for x in cls)
