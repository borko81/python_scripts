class Connection:

    error = "Connection close"

    def __init__(self):
        self.state = 'CLOSED'

    def check_is_status_open(self):
        if self.state != 'OPEN':
            raise RuntimeError(Connection.error)

    def read(self):
        self.check_is_status_open()
        print('Now reading')

    def write(self):
        self.check_is_status_open()
        print('Now Writing')

    def open(self):
        if self.state == 'OPEN':
            raise RuntimeError("Connection already open")
        self.state = 'OPEN'


if __name__ == '__main__':
    t = Connection()
    # t.open()
    t.write()
