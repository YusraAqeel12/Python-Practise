class atm:
    def __init__(self):
        self.__pin = " "   # user nai jo kuch bhee pin diya aap nai usko is variable mai daal diya
        self.__balance = 0   #instance var
        self.menu()  # Call menu method to initiate ATM menu

    # Aik method define kardiya jismai user can follow instructions for atm
    # Her method mai self argument laina is important
    def menu(self):
        while True:  # Keep the menu running until the user exits
            user_input = input("Enter the Following Number:\nPress 1: If you want to deposit money\nPress 2: If you want to withdraw amount\nPress 3: If you want to create pin\nPress 4: If you want to check balance\nPress 5: To exit\n")
            if user_input == '1':  # Convert to string
                print("Deposit")
                self.deposit()
            elif user_input == '2':  # Convert to string
                print("Withdraw")
                self.with_draw()
            elif user_input == '3':  # Convert to string
                print("Create Pin")
                self.create_pin()  # createpin waala method aap nai yahaan call kardiya
            elif user_input == '4':  # Convert to string
                print("Check Balance")
                self.Check_Balance()
            elif user_input == '5':  # Convert to string
                print("Exiting...")
                break  # Exit the loop
            else:
                print("Invalid option")

    # Method laingay createpin ka jismai aik variable laingay self.pin ka
    def create_pin(self):
        self.pin = input("Enter Your Pin: ")
        print("Pin Entered successfully")

    # Method create kiya hai deposit ka jismai humnai aik input liya hai aur usmai temp ka var diya hai
    # agar hamara pin barabar hai hamaray temp sai toh deposit amount enter karo
    def deposit(self):
        temp = input("Enter Your Pin: ")
        if temp == self.__pin:
            amount = int(input("Enter Your deposit amount: "))  # Convert to integer
            self.__balance += amount
            print("Deposit Successful")
        else:
            print("Invalid Pin")

    def with_draw(self):
        temp = input("Enter Your Pin: ")
        if temp == self.__pin:
            amount = int(input("Enter Your Withdraw amount: "))  # Convert to integer
            if amount <= self.__balance:  # Changed to <=
                self.__balance -= amount
                print("Successfully Withdrawn")
            else:
                print("Insufficient Balance")
        else:
            print("Enter Valid Pin")

    def Check_Balance(self):
        temp = input("Enter Your Pin: ")
        if temp == self.__pin:
            print("Your Balance: ", self.__balance)
        else:
            print("Invalid Pin")


# Testing a is the object
a = atm()

