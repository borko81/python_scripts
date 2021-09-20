class ImplementName:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class SaveMultipleResult:

    output = []

    def __init__(self, data = None):
        self.data = data

    def append_name_to_output(self):
        if self.data:
            SaveMultipleResult.output.append(self.data)

    @staticmethod
    def show_output():
        return [i.name for i in SaveMultipleResult.output]


random_generated_data = 'First Second Last'.split()


data = [SaveMultipleResult(ImplementName(name)).append_name_to_output() for name in random_generated_data]

print(SaveMultipleResult.show_output())