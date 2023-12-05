import datetime


class LoggingDescriptor:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        value = instance.__dict__.get(self.name, None)
        print(f"{datetime.datetime.now()}: Получен доступ к '{self.name}', значение: {value}")
        return value

    def __set__(self, instance, value):
        print(f"{datetime.datetime.now()}: Значение '{self.name}' изменено на {value}")
        instance.__dict__[self.name] = value


class MyClass:
    attribute = LoggingDescriptor()


example = MyClass()
example.attribute = "Тестовое значение"  # Логирование изменения
example.attribute  # Логирование доступа
