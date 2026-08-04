from bankaccount import *

def main():
    print(f"Bank: {BankAccount.bank_name}")

    a1 = BankAccount("Ravi Kumar", "Savings", 5000, 1234)
    print(a1)

    a2 = BankAccount("Anitha Sharma", "Current", 20000, 5678)
    print(a2)

    print(f"Total accounts: {BankAccount.total_accounts}")

    print(f"Deposit 2000 -> {a1.deposit(2000)}")
    print(f"Withdrawal 1500 -> {a1.withdrawal(1500, 1234)}")

    interest = a1.add_annual_interest()
    print(f"Interest added: {interest}")
    print(f"Balance now: {a1.balance}")

    print(a1.change_pin(1234, 4321))

    print(f"Withdrawal 500 -> {a1.withdrawal(500, 4321)}")
    
    try:
        a1.withdrawal(1000, 1111)
    except ValueError as e:
        print(f"Blocked (wrong PIN): {e}")

    try:
        a1.withdrawal(10000, 4321)
    except ValueError as e:
        print(f"Blocked (below min): {e}")

    try:
        a1.deposit(-500)
    except ValueError as e:
        print(f"Blocked (negative): {e}")

    try:
        a1.balance = 999999
    except AttributeError as e:
        print(f"Blocked (write balance): {e}")


if __name__ == "__main__":
    main()