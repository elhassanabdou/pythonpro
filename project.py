import datetime
def show_menu():
    print('\nTo-Do List Manager')
    print('1. Show cars')
    print('2. View tasks')
    print('3. Remove a task')
    print('4. Save tasks to a file')
    print('5. Load tasks from a file')
    print('6. Exit')
    choice = input('Enter your choise (1-6): ')
    return choice

def read_file(file_path, delimiter=','):
    data_dict = {}
    with open(file_path,'r') as file:
        for entry in file:
            entries = entry.strip().split(delimiter)
            if entries:
                key = entries[0]
                values = entries[1:]
                data_dict[key] = values
    return data_dict
def show_vechile():
    available_vehicles = read_file('vehicles.txt')
    for key, values in available_vehicles.items():
        properties = ",".join(values)
        print(f'* Reg. nr: {key}, Model: {values[0]}, Price per day: {values[1]}, Properties: {properties}')

def main():
    while True:
        choice = show_menu()
        if choice == '1':
            show_vechile()

if __name__ == "__main__":
    main()