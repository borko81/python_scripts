import os
from configparser import ConfigParser


class ReturnConfig:
    """
        Validate path, raise exception if not found
    """

    def __init__(self, filename):
        self.filename = filename

    @property
    def filename(self):
        return self._filename

    @filename.setter
    def filename(self, value):
        if not os.path.exists(value):
            raise OSError('Path not found')
        self._filename = value


class Data:
    """
        Return config parser, only one static method
    """
    @staticmethod
    def cfg(filename):
        cfg = ConfigParser()
        cfg.read(ReturnConfig(filename).filename)
        return cfg


class GetData:
    """
        After parser is configure, return data from ini file
    """

    def __init__(self, cfg):
        self.cfg = cfg

    def return_server(self):
        return self.cfg.sections()[0]

    def generate_data(self):
        for key in self.cfg.options(self.return_server()):
            yield key

    def return_data(self):
        data = {}
        server = self.return_server()
        for key in self.generate_data():
            data[key] = self.cfg.get(server, key)
        return data


c = GetData(Data.cfg('my_file.ini'))

c.generate_data()
template = "Hostfile: {sname}: Port: {port}. Root: {root}".format(**c.return_data())
print(template)
