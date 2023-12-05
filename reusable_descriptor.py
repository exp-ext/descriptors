class ReusableDescriptor:
    def __init__(self):
        self.values = {}

    def __get__(self, instance, owner):
        return self.values.get(instance, None)

    def __set__(self, instance, value):
        self.values[instance] = value


class MyClass:
    attribute1 = ReusableDescriptor()
    attribute2 = ReusableDescriptor()


# Создание экземпляра и установка значений
instance = MyClass()
instance.attribute1 = "Значение 1"
instance.attribute2 = "Значение 2"

# Проверка значений
print(f"Attribute 1: {instance.attribute1}")
print(f"Attribute 2: {instance.attribute2}")
