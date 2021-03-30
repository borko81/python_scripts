class MotroCycle:

    def __init__(self):
        self.name = "MotorCycle"

    def TwoWheeler(self):
        return "ThoWheeler"


class Truck:

    def __init__(self):
        self.name = "Truck"

    def FourWheeler(self):
        return "FourWheeler"


class Adapter:

    def __init__(self, obj, **adapter_methods):
        self.obj = obj
        self.__dict__.update(adapter_methods)

    def __getattr__(self, attr):
        return getattr(self.obj, attr)

    def original_dict(self):
        return self.obj.__dict__


if __name__ == '__main__':
    objects = []

    motorcycle = MotroCycle()
    truck = Truck()
    objects.append(Adapter(motorcycle, wheels=motorcycle.TwoWheeler))
    objects.append(Adapter(truck, wheels=truck.FourWheeler))

    for obj in objects:
        print(obj.name, obj.wheels())
