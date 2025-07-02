#code to mimic ATM functionalities 

balance = 10000
pin = 1234

attempt = 0
while attempt < 3:
    user_pin = int(input("Enter PIN: "))
    if (user_pin == pin):
        print("Welcome to XYZ Bank!")
        while True:
            choice = int(input("\n1.Check Balance\n2.Withdraw\n3.exit\n"))
            if choice == 1:
                print("Current Balance: ", balance)
            elif choice == 2:
                with_amt = int(input("Enter amount to withdraw: "))
                balance-=with_amt
                print(f"You have successfully withdrawn Rs.{with_amt}. New Balance: Rs{balance}")
            elif choice == 3:
                print("Thank you for using our ATM")
                break
            else:
                print("Choose from 1-3")
        break
    else:
        print("Wrong Pin")
        attempt+=1
    
if(attempt == 3):
    print("Account Blocked due to 3 incorrect entries")
