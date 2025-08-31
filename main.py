money_to_collect_from_customers= 0

available_rooms=100

def save_data(x):
    with open('Hotel_Data.csv', 'a') as file:
        file.write(str(x) + '\n')


def load_data():
    with open('Hotel_Data.csv','r') as fi :
        a1=fi.readline()
        print(a1)
def rooms_availabl():
    with open('Available-Rooms.csv','r') as ty:
        tu= ty.read()
        print(tu)

Room_price_per_night= (1000 ,'rupees')
while True :
    menu_options= int(input('1.View available rooms\n 2.Book a room\n 3.Check out\n 4.View all guests\n 5. Exit the system:  '))

    if menu_options == 1:

        print(f'{rooms_availabl()}, Rooms are available sir , {Room_price_per_night} , Per night')
        #removed pass the useless function from here.

    elif menu_options == 2:
        confirmation= input('Sir for booking a room you have to pay rupees 1000 per night\n Are you ready to pay it while checking out (y/n) :   ')

        if confirmation=="y" :
            number_of_days = int(input('Sir tell us for how many nights you want to check in:  '))
            guests_details1 = input('Sir please enter your Name:    ')

            calculation = (number_of_days * 1000)
            print('All set sir we have booked a room for you\n Thank you sir ')

            available_rooms -= 1

            a12= {'Name': guests_details1, 'Amount to be paid': calculation, 'available_rooms currently': available_rooms}
            save_data(a12)

            money_to_collect_from_customers+=calculation
        elif guests_details1.isdigit():
            print('Sir please enter a valid name...\n Process is incomplete \n Thank you.')
        elif number_of_days.isalpha():
            print('Sir you have entered a invalid syntax\n Process incomplete \n Thank you')
        elif confirmation=='n' :
            print('Sir due to your confirmation denial \n No room is booked \n Thank you')

    elif menu_options == 3:
        payment_confirmation = input('Sir please do your payment on the payment counter(ok/no):   ')
        guest_name = input('Sir please enter your name before checking out: ')
        lines = []

        if payment_confirmation == 'ok':
            print('Thank you sir now you have succesfully checked out...')
            available_rooms += 1
            with open('Hotel_Data.csv', 'r') as p:
                for line in p:
                    if f"'Name': '{guest_name}'".lower() in line.lower() and "'Checked_out': True" not in line:
                        line = line.strip()[:-1] + ", 'Checked_out': True}\n"
                    lines.append(line)
            with open("Hotel_Data.csv", "w") as f:
                f.writelines(lines)

        elif payment_confirmation == 'no':
            print(f'Alert!! , A guest named {guest_name} is not ready to do the payment before checking out \nTalk to him\nThank you')
        elif guest_name.isdigit() :
            print('Sir please enter a valid name...\n Process is incomplete \n Thank you.')
        elif guest_name=="" :
            print('It should not be empty sir...\n Thank you')
        elif payment_confirmation not in ['ok', 'no']:
            print('Sir please write these instructions in lower case \n Thank you sir')
        elif f"'Name': '{guest_name}'" not in line :
            print('Sir we are unable to recognize you\n Kindly enter a valid name..\n Thank You')


    elif menu_options==4:
        load_data()
    elif menu_options==5 :
        exit_confirmation= input('Sir are you sure to exit(yes/no):  ')
        if exit_confirmation.isdigit() :
            print('Sir you have to answer in Yes or No \n Thank You \n Try again sir...\n')
        elif exit_confirmation=='no':
            print('Sure sir you can continue using our app...\n')
        elif exit_confirmation=='yes' :
            print('Sure sir in you have logged out succesfully...\n Thank You Sir\n')
            break

    with open('Available-Rooms.csv','w') as io :
        io.write(str(available_rooms))
