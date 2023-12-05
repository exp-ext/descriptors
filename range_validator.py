class RangeValidator:
    def __init__(self, min_value=0, max_value=100):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name, None)

    def __set__(self, instance, value):
        if not (self.min_value <= value <= self.max_value):
            raise ValueError(f"Значение должно быть в диапазоне [{self.min_value}, {self.max_value}]")
        instance.__dict__[self.name] = value


class MyClass:
    number = RangeValidator(0, 100)


example = MyClass()
example.number = 50
# example.number = 150  # Попытка установки некорректного значения вызовет исключение ValueError

print(example.number)
