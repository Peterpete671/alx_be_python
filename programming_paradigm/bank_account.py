class BankAccount:
	def __init__(self, initial balance=0):
		"""Initialize a new bank account with an optional initial balance."""
		self.__account_balance = initial_balance  #Encapsulated attribute

	def deposit(self, amount):
		"""Deposit a given amount into the account."""
		if amount > 0:
			self.__account_balance += amount
		else:
			print("Deposit amount must be positive.")

	def withdraw(self, amount):
		"""Withdraw a given amount if suffecient funds are available."""
		if amount <= 0:
			print("Withdrawal amount must be positive.")
			return False
		if amount <= self.__account.balance:
			self.__account_balance -= amount
			return True
		else:
		return False

	def display_balance(self):
		"""Display the current account balance."""
		print(f"Current Balance: ${self.__account_balance:2f}")
