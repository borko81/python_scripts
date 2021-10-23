from openpyxl import Workbook

workbook = Workbook()
sheet = workbook.active

informations = [
    {"name": "Борко", "town": "Plovdiv"},
    {"name": "Ivan", "town": "Velingrad"},
    {"name": "Mary", "town": "Plovdiv"}
]

FILE = 'work.xlsx'

sheet["A1"] = "Name"
sheet["B1"] = "Town"


class WriteData:
    counter = 1

    def __init__(self, name, town) -> None:
        self.name = name
        self.town = town
        WriteData.counter += 1

    def write_to_excel(self):
        sheet[f'A{WriteData.counter}'] = self.name
        sheet[f'B{WriteData.counter}'] = self.town
        workbook.save(FILE)


if __name__ == '__main__':
    for line in informations:
        WriteData(**line).write_to_excel()
