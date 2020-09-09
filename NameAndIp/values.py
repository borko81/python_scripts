class Values:

    def __init__(self, name, ip):
        self.name = self.__validate_and_strip(name)
        self.ip = self.__validate_and_strip(ip)

    def __validate_and_strip(self, data):
        data = data.strip()
        data = data.upper()
        return data

    def get_value(self):
        return ((self.name, self.ip))

    def __repr__(self):
        return f'{self.name}: {self.ip}'


if __name__ == '__main__':
    t1 = Values('comp 1', '1234', '')
    t2 = Values('comp 2', '3345', '')
    print(t1.findall('comp'))