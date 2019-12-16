from check_ip_user_info import SourceInfo
from validate_data import ValidateData
import paramiko


def con_with_paramiko(info, port, command):
    for key, val in info.items():
        ip = key
        username = val[0]
        password = val[1]
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(ip, '22', username, password)
            shell = client.invoke_shell()
            data, stdout, stderr = client.exec_command(command)
            print(stdout.read())
        except paramiko.SSHException as e:
            print(f"Error {e} from [{ip}]")
        finally:
            shell.close()
            client.close()


def connect():
    mytest = SourceInfo('list_with_ip.csv')
    for line in mytest.split_info():
        info_validate = ValidateData(line)
        con_with_paramiko(info_validate.valid_data(), 22,  "ip addr show")


if __name__ == '__main__':
    connect()
