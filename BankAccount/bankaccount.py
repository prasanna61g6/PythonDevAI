class BankAccount:
    
    bank_name = "State Bank of India"
    total_accounts = 0
    interest_rate = 4.0
    MIN_BALANCE = 500
    _next_account_number = 1001
    
    def __init__(self, holder_name, account_type, balance, pin):
        self.holder_name = holder_name
        self._account_number = BankAccount._next_account_number
        self._account_type = account_type
        self.__balance = balance
        self.__pin = pin
        BankAccount.total_accounts += 1
        
    @property
    def account_number(self):
        return self.account_number
    
    @property
    def balance(self):
        return self.__balance
    
    def deposit(self, amount):
        if not isinstance(amount, (int, float)) :
            raise TypeError("Amount must be a number")
        if amount < 0 :
            raise ValueError("Amount must be Positive")
        self.__balance += amount 
        return self.__balance    
            
    def __verify_pin(self, pin) :
        return self.__pin == pin
    
    def withdrawal(self, amount, pin) :
        if not self.__verify_pin(pin) :
            raise ValueError("Invalid PIN")
        if amount < BankAccount.MIN_BALANCE :
            raise ValueError("Amount must be greater than 500")
        self.__balance -= amount
        return self.__balance    
        
    def change_pin(self, old_pin, new_pin) :
        if not self.__verify_pin(old_pin):
            raise ValueError("Invalid old pin")
        
        if len(str(new_pin)) != 4 or not str(new_pin).isdigit():
            raise ValueError("New PIN must be exactly 4 digits")
        self.__pin = int(new_pin)
        return "PIN changed successfully"
    
    def add_annual_interest(self) :
        interest = self.__balance * (BankAccount.interest_rate / 100)
        self.__balance += interest
        return interest
    
    @classmethod
    def get_total_accounts(cls) :
        return BankAccount.get_total_accounts
    
    @staticmethod
    def is_valid_amount(amount) :
        if amount > 0 :
            return True
    
        
    def __str__(self):
        return (f"Account[{self._account_number}] {self.holder_name} | {self._account_type} | Rs.{self.__balance: ,.2f}")
    
    """ Balance stores the customer's money. If anyone could directly assign account.balance = 999999, money could
        be created without any deposit or validation. Therefore balance is exposed only through a read-only property 
        and can change only through deposit(), withdraw(), and add_annual_interest(), which perform all required 
        validations. holder_name is only descriptive information. Changing a person's name does not affect the bank's
        financial integrity, so it can safely remain public """
    
        
        