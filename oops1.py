class ATM:
    def __init__(self):
        print("hello")
        self.pin = ""
        self.balance = 0
        self.menu()
    def menu(self):
        user_input = input("enter 1 to create pin, enter 2 to deposit")
        
        if user_input ==1 :
            print("create pin")
        if user_input==2:
            print("deposit money")   
            
    def create_pin(self):
        self.pin = input("enter pin") 
    def display_pin(self):
        print("your pinr is ",self.pin)
        
df = ATM()        
df.create_pin()
df.display_pin()