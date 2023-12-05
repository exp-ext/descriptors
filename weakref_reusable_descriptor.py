import gc
import weakref


class ReusableDescriptor:
    def __init__(self):
        self.values = weakref.WeakKeyDictionary()

    def __get__(self, instance, owner):
        # Возвращает значение атрибута для конкретного экземпляра
        return self.values.get(instance, None)

    def __set__(self, instance, value):
        # Устанавливает значение атрибута для конкретного экземпляра
        self.values[instance] = value


class MyClass:
    attribute1 = ReusableDescriptor()
    attribute2 = ReusableDescriptor()


instance = MyClass()
instance.attribute1 = "Значение 1"
instance.attribute2 = "Значение 2"

# Проверка значений
print(f"Attribute 1: {instance.attribute1}")
print(f"Attribute 2: {instance.attribute2}")

# Проверка освобождения памяти
del instance
gc.collect()  # Принудительный сбор мусора для демонстрации освобождения памяти
print("Экземпляр MyClass удален")
