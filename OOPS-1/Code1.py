
#constructor basically is function
# constructor is special Function  jisko call krne ki jarrort nhi hoti  bo khude s call ho jata hai .....jab Class ka object bnaate hai  waise hi execute hota hai

class Atm:

  # constructor(special function)->superpower -> 
  def __init__(self):
    # print(id(self))
    self.pin = ''
    self.balance = 0
    #self.menu()

  def menu(self):
    user_input = input("""
    Hi how can I help you?
    1. Press 1 to create pin
    2. Press 2 to change pin
    3. Press 3 to check balance
    4. Press 4 to withdraw
    5. Press 5 to credit Your Balance
    6. Anything else to exit
    """)

    if user_input == '1':
      self.create_pin()
    elif user_input == '2':
      self.change_pin()
    elif user_input == '3':
      self.check_balance()
    elif user_input == '4':
      self.withdraw()
    elif user_input == '5':
      self.credit_balance()
    else:
      exit()

def create_pin(self):
  user_pin= input('Enter Your Pin: ')
  self.pin=user_pin

  user_balance= int(input('Enter balance: '))
  self.balance=user_balance
  
  print('Pin created SuccessFully')

def change_pin(self):
    old_pin = input('enter old pin')

    if old_pin == self.pin:
      # let him change the pin
      new_pin = input('enter new pin')
      self.pin = new_pin
      print('pin change successful')
      self.menu()
    else:
      print('nai karne de sakta re baba')
      self.menu()

def check_balance(self):
    user_pin = input('enter your pin')
    if user_pin == self.pin:
      print('your balance is ',self.balance)
    else:
      print('chal nikal yahan se')


def credit_balance(self):
    new_balance=('Add  your Amount: ')
    if new_balance>0:
      
     self.balance=+new_balance
    else:
      print(self.balance)
  

def withdraw(self):
    user_pin = input('enter the pin')
    if user_pin == self.pin:
      # allow to withdraw
      amount = int(input('enter the amount'))
      if amount <= self.balance:
        self.balance = self.balance - amount
        print('withdrawl successful.balance is',self.balance)
      else:
        print('abe garib')
    else:
      print('sale chor')
    self.menu()


obj=Atm()
