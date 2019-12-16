import sys


class ValidateData:

    def __init__(self, data):
        self.ip_to_check = data[0]
        self.username_to_check = data[1]
        self.password_to_check = data[2]

    def username_check(self):
        username = self.username_to_check
        not_allowed_symbol = "#@!^&*$%# "
        if username.startswith(tuple(not_allowed_symbol)):
            print("Username srtartwith not alowed symbol")
            sys.exit()
        else:
            return username

    def password_check(self):
        password = self.password_to_check
        not_allowed_symbol = "#@!^&*$%# "
        if password == 'root':
            print("Not test script with usrname root!")
            sys.exit()
        if password.startswith(tuple(not_allowed_symbol)):
            sys.exit()
        else:
            return password

    def ip_check(self):
        octet = self.ip_to_check.split(".")
        if((len(octet) == 4) and (1 <= int(octet[0]) <= 223)):
            return self.ip_to_check
        else:
            print("Len of ip is not recognize as valid format")
            sys.exit()

    def valid_data(self):
        valid_result = {}
        ip = self.ip_check()
        username = self.username_check()
        password = self.password_check()
        valid_result[ip] = [username, password]
        return valid_result

    def __repr__(self):
        return f"IP: {self.ip_to_check}\nUsername: {self.username_to_check}\nPassword: {self.password_to_check}"


if __name__ == '__main__':
    mytest = ValidateData(('192.168.168.1', 'test', 'password'))
    print(mytest.valid_data())
