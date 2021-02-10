import os
import fdb

FOLDER = r'C:\Users\borko\Desktop\test'
NAME = 'PARK.FDB'
BACKUP_NAME = NAME.replace('FDB', 'FBK')
fbclient = r'C:\Program Files\Firebird\Firebird_2_5\bin\fbclient.dll'

original_file = os.path.join(FOLDER, NAME)
backup_file = os.path.join(FOLDER, BACKUP_NAME)


def report_progress(line):
    ''' Function to call back with each output line '''
    print(line)


def info():
    ''' Print pid of script '''
    print(os.getppid())
    print(os.getpid())


def backup(original_file, backup_file):
    info()
    fdb.load_api(fbclient)
    svc = fdb.services.connect(user='sysdba', password='masterkey')
    svc.backup(original_file, backup_file, ignore_checksums=1,
               collect_garbage=0, callback=report_progress)


def show_statistics():
    fdb.load_api(fbclient)
    svn = fdb.services.connect(user='sysdba', password='masterkey')
    svn.get_statistics(original_file, show_only_db_log_pages=0, show_only_db_header_pages=0, show_user_data_pages=1, show_user_index_pages=1, show_system_tables_and_indexes=0, show_record_versions=0, callback=report_progress)


if __name__ == '__main__':
    backup(original_file, backup_file)
