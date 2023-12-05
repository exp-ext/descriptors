import time


class LazyProperty:
    def __init__(self, func):
        self.func = func
        self.name = func.__name__

    def __get__(self, instance, owner):
        if instance is None:
            return self
        if self.name not in instance.__dict__:
            instance.__dict__[self.name] = self.func(instance)
        return instance.__dict__[self.name]


def complex_computation(instance):
    # Имитация сложного вычисления
    time.sleep(1)
    return "Результат сложного вычисления"


class MyClass:
    expensive_computation = LazyProperty(complex_computation)


instance = MyClass()

# Первый вызов - вычисление происходит и результат кэшируется
print(instance.expensive_computation)

# Второй вызов - возвращается кэшированный результат, новое вычисление не происходит
print(instance.expensive_computation)
