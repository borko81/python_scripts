from connect import Table
from values import Values
from colors import bcolors
import sys

class Menu:

    def show_me(self):
        return '''
        1: Insert new records
        2: Show all records
        3: Search record
        4: Update records
        5: Delete records
        '''

    
    def insert_records(self):
        name = input("Enter name: ")
        ip = input("Enter ip: ")
        v = Values(name, ip)
        print('Input values :', *v.get_value())
        Table.insert_in_table(self, *v.get_value())

    def show_records(self):
        show = Table()
        result = show.show_all_records()
        for args in result:
            name, ip = args
            name = bcolors.FAIL + name + bcolors.ENDC
            print(f'{name:<20} : {ip:<15}')

    def search_for_record(self):
        name_to_search = input("Enter name to search: ")
        result = Table.get_user_choice(self, name_to_search)
        for args in result:
            name, ip = args
            name = bcolors.FAIL + name + bcolors.ENDC
            print(f'{name:<20}: {ip:<15}')

    def update_records(self):
        name_to_search = input("Enter name to update: ")
        new_ip = input("Enter new ip :")
        v = Values(name_to_search, new_ip)
        Table.change_target(self, *v.get_value())

    def delete_records(self):
        name_to_delete = input("Enter name to delete: ")
        Table.delete_target(self, name_to_delete)


    def choice(self):
        print(self.show_me())
        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print('Enter corect choice')
        else:
            if choice == 1:
                self.insert_records()
            elif choice == 2:
                self.show_records()
            elif choice == 3:
                self.search_for_record()
            elif choice == 4:
                self.update_records()
            elif choice == 5:
                self.delete_records()
            else:
                print('Not corect input')
                self.choice()


if __name__ == '__main__':
    test = Menu()
    if sys.argv[1] == 'show':
        test.show_records()
    elif sys.argv[1] == 'search':
        test.search_for_record()
    else:
        test.choice()