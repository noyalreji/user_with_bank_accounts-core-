class BankAccount:
  def __init__(self,name, int_rate = 0.01, balance = 0):
    self.name = name
    self.int_rate = int_rate
    self.balance = balance

  def deposit(self, amount):
      self.balance += amount
      return self
  
  def withdraw(self, amount):
      if (self.balance < amount):
        print("Insufficient funds: Charging a $5 fee")
        self.balance -= 5
      else:
        self.balance -= amount
      return self

  def display_account_info(self):
      print((f"Bank: {self.name}, Balance: $ {self.balance}"))

  def yield_interest(self):
    yield_interest = self.balance * 0.01
    if (self.balance >= 0):
        self.balance += yield_interest
    return self
  
  # combining the string value to the object in memory 
  def __str__(self) -> str:
      return (f"Bank: {self.name}, Balance: {self.balance}")
  
  #get info from all accounts
  def bank_account_info(accounts):
      for account in accounts:
        print(account)

# //////////////////////////////////////////////////////////////////////////////
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(name,int_rate=0.02, balance=0)	
    
    # adding deposit method to user
    def make_deposit(self, amount):
      self.account_balance += amount

    # adding withdrawal method 
    def make_withdrawal(self, amount):
      self.account_balance -= amount

    # display user balance method 
    def display_user_balance(self):
      print(f"User Name: {self.name} Account Balance: {self.account.balance}")
    
    # transfer money method 
    # Allow a user to have multiple accounts; update methods so the user has to specify which account they are withdrawing or depositing to
    def transfer_money(self, user, amount):
      self.account.balance -= amount
      user.account.balance += amount
    
    #set object in the memory of string
    def __repr__(self):
      return (f"Username: {self.name}, Email id: {self.email}, Account Balance: $ {self.account.balance}")

    #get users
    def get_users(users):
      for user in users:
        print(user)

#Create 3 instances of the User class
users = [User('Jacob Ramsey', 'j4@gmil.com'), User('Lee May', 'leemay@ij.com'), User('Lol Me', 'lol@mian.com')]

users[0].account.deposit(1000)
users[0].account.withdraw(200)

users[0].transfer_money(users[1], 400)
users[0].transfer_money(users[2], 100)

# users[0].display_user_balance()

User.get_users(users)