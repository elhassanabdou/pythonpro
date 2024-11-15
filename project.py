import datetime

def show_menu():
    print('\nYou may select one of the following:')
    print('1. List available cars')
    print('2. Rent a car')
    print('3. Return a car')
    print('4. Count the money')
    print('0. Exit')
    choice = input('What is your selection? ')
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

def write_file(file_path, data, delimiter=","):
    with open(file_path,'w') as file:
        for key, values in data.items():
            line = delimiter.join([key]+values)
            file.write(line + '\n')

def show_vehicle():
    available_vehicles = read_file('vehicles.txt')
    for key, values in available_vehicles.items():
        properties = ",".join(values)
        print(f'* Reg. nr: {key}, Model: {values[0]}, Price per day: {values[1]}, Properties: {properties}')

def add_customer(customers):
    BD = input("Enter Birthday: ")
    first_name = input("First name: ")
    last_name = input("Last name: ")
    customers[BD]=[first_name,last_name]
    #write to customers file
    write_file('customers.txt',customers)

def calculate_cost(rented_date, cost):
    delta = datetime.datetime.now() - datetime.datetime.strptime(rented_date,"%d/%m/%Y %H:%M")
    days = int(delta.days)
    if(days < 1):
        days =1
    return days * cost

def return_vehicle():
    regNumber = input("Give the register number of the car you want to rent: ")
    available_vehicles = read_file('vehicles.txt')
    rentedCars = read_file('rentedVehicles.txt')

    if regNumber in available_vehicles:
        if regNumber in rentedCars:
            cost = float(available_vehicles[regNumber][1])
            rented_date = rentedCars[regNumber][1]
            totalCost = calculate_cost(rented_date,cost)
            print(f"Total cost '{totalCost}'")
            #remove from rentedCars
            del rentedCars[regNumber]
            write_file('rentedVehicles.txt',rentedCars)
        else:
            print("Car was not rented")
    else:
        print("Car does not exist")


def rent_vehicle():
    available_vehicles = read_file('vehicles.txt')
    customers = read_file('customers.txt')
    rentedCars = read_file('rentedVehicles.txt')
    regNumber = input("Give the register number of the car you want to rent: ")
    
    if regNumber in available_vehicles:
        customerBD = input("Please enter your birthday in form DD/MM/YYYY: ")
        if customerBD in customers:
            customer = customers[customerBD]
            print(f"Hello f'{customer[0]}' f'{customer[1]}'")


        elif customerBD > ('01/01/2006'):
            print("You are too young to rent a car")
        elif customerBD > ('01/01/1950'):
            print("You are too old for rent a car")
            
        else:
            add_customer(customers)
        #move the vehicle to rented file
        currentdate = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
        rentedCars[regNumber]=[customerBD,currentdate]
        write_file('rentedVehicles.txt',rentedCars)   
    elif regNumber in rentedCars:
        print("Car is already rented")
    else:
        print("Car does not exist")
def count_the_money():

    money = 0.00

    with open('transActions.txt', 'r') as i:
        for line in i:
            total_price = float(line.strip().split(",")[-1])
            total_earning =+ total_price

        print(f"Total Earnings: ${total_earning:2f}")
    

def main():
    while True:
        choice = show_menu()
        if choice == '1':
            show_vehicle()
        elif choice == '2':
            rent_vehicle()
        elif choice == '3':
            return_vehicle()
        elif choice == '4':
            count_the_money()
            
        elif choice == '0':
            print("Bye!")
            break
            
        else:
        print("invalid selection. Try again")


if __name__ == "__main__":
    main()




if __name__ == "__main__":
    main()
