#bus ticket Booking system!

#admin
'''
1)add a new buss
2)check available bus
3)can check bus info
'''
#User:
'''
1)check availabule bus
2)can check bus info
3)can reserve bus
'''

class User:
    def __init__(self,username,password):
        self.username=username
        self.password=password

class Bus:
    def __init__(self,coach,driver,arrival,departure,from_des,to):
        self.coach=coach
        self.driver=driver
        self.arrival=arrival
        self.from_des=from_des
        self.to=to
        self.departure=departure
        self.seat=["Empty" for i in range(20)]

# b=Bus(2,"Rahim","12PM","12:30PM","Dhaka","Chittagong")
# print(vars(b))

class Phitron:
    total_bus=5
    total_bus_lst=[]

    def add_bus(self):
        bus_no=int(input("Enter Bus No : "))

        flag = 1
        for w in self.total_bus_lst:
            if bus_no==w['coach']:
                print("Bus Already Added")
                flag=0
                break
        
        if flag:
            bus_driver=input("Enter Bus Driver Name : ")
            bus_arrival = input("Enter Bus Arrival Time : ")
            bus_departure=input("Enter Bus Departure Time : ")
            bus_from=input("Enter Bus Start From : ")
            bus_to=input("Enter Bus Destination : ")
            self.new_bus=Bus(bus_no,bus_driver,bus_arrival,bus_departure,bus_from,bus_to)
            self.total_bus_lst.append(vars(self.new_bus))
            print("\nBus Added Successfully")

# company=Phitron()
# company.add_bus()

class Counter(Phitron):

    user_lst=[]

    def reservation(self):
        bus_no=int(input("Enter Bus No : "))

        for w in self.total_bus_lst:
            if bus_no==w['coach']:
                passenger=input("Enter Your Name : ")
                seat_no=int(input("Enter Seat No : "))

                if seat_no>20:
                    print("No seats Available!!!")
                elif w['seat'][seat_no-1]!="Empty":
                    print("Seat Alreay Booked")
                else:
                    w['seat'][seat_no-1]=passenger
            else:
                print("No Bus Available")
        
        # for bus in self.total_bus_lst:
        #     print(bus['seat'])
    
    def show_ticket(self):
        bus_no=int(input("Enter Bus Number : "))

        for w in self.total_bus_lst:
            if bus_no==w['coach']:
                print('*'*50)
                print()
                print(f"{' '*10}{'#'*10} BUS INFO {'#'*10}")
                print(f"Bus Number : {bus_no} \t\t\t Driver :{w['driver']}")
                print(f"Arrival : {w['arrival']} \t\t\t Departure Time : {w['departure']} \n From: \t{w['from_des']} \t\t\t To: \t{w['to']}")
                print()

                a=1
                for i in range(5):
                    for j in range(2):
                        print(f"{a}. {w['seat'][a-1]}",end="\t")
                        a+=1
                    for j in range(2):
                        print(f"{a}. {w['seat'][a-1]}",end="\t")
                        a+=1
                    print()
                print('*'*50)
    def get_users(self):
        return self.user_lst

    def create_account(self):
        name=input("enter your username: ")
        password=input('enter your password: ')
        self.new_user=User(name,password)
        self.user_lst.append(vars(self.new_user))

    def available_buses(self):
        if len(self.total_bus_lst)==0:
            print('no bus availbl')
        else:
            print('*'*50)
            for bus in self.total_bus_lst:
                print()
                print(f"{' '*10}{'#'*10} BUS {bus['coach']} INFO {'#'*10}")
                print(f"Bus Number : {bus['coach']} \t Driver : {bus['driver']}")
                print(f"Arrival : {bus['arrival']} \t Departure Time : {bus['departure']} \n From: \t{bus['from_des']} \t\t To: \t{bus['to']}")
            print('*'*50)

while True:
    company=Phitron()
    b=Counter()
    print("1.create an account\n 2.login  to you accoun\n 3,Exit")
    user_input=int(input("enter your ar choice: "))

    if user_input==3:
        break
    elif user_input==1:
        b.create_account()

    elif user_input==2:
        name=input('enter your Username: ')
        password=input('enter your password: ')

        flag=0
        isAdmin=False

        if name=="admin" and password=='1234':
            isAdmin=True
        if isAdmin==False:
            for user in b.get_users():
                if user['username']==name and use['password']==password:
                    flag=1
                    break
            if flag:
                while True:
                    print(f"\n{''*10} welcome to bus sysyem ticket booking system")
                    print("1.Add Bus\n2.Available Buses \n3.Show Bus Info \n4.EXIT")
                    a=int(input("enter the choice: "))
                    if a==4:
                        break
                    elif a==1:
                        b.available_buses()
                    elif a==2:
                        b.show_ticket()
                    elif a==3:
                        b.reservation()
                else:
                    print("No username Found: ")
            else:
                 
               while True:
                 print(f"\n{' '*10}Hello ADMIN Welcome to BUS TICKET BOOKING SYSTEM")
                 print("1.Add Bus\n2.Available Buses \n3.Show Bus Info \n4.EXIT")
                 a=int(input("Enter Your Choice : "))
                 if a==4:
                    break
                 elif a==1:
                    b.add_bus()
                 elif a==2:
                    b.available_buses()
                 elif a==3:
                    b.show_ticket()