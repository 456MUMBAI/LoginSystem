"""up"""


def transaction(total_amount):
    # global money
    # money=total_amount
    print('#Make your payment HERE...##')
    print('Select the mode of payment')
    print('Press 1 for net banking.')
    print('Press 2 for Debit card.')
    print('Press 3 for UPI Autopay')

    ch = input('Enter your choice here: ')
    if ch == '1':
        print("## NET BANKING WINDOW ##")
        ans = input('Press 1 to change mode of payment else press any key to proceed: ')
        if ans == '1':
            transaction(total_amount)
        else:
            banking()
            print(f'Your total amount is= Rs. {total_amount}')
            print(f'Press 1 to pay Rs. {total_amount}')
            print('Press any key to skip the transaction, you can pay later by logging into your account')
            Ans = input('Enter your choice here: ')
            if Ans == '1':

                query = f"insert into user_info(paid) values({total_amount});"
                mycursor.execute(query)
                mycon.commit()
                print('Payment made successfully!!')
            else:
                query = f"insert into user_info(paid) values(0);"
                mycursor.execute(query)
                mycon.commit()

                menu()


    elif ch == '2':
        print('## DEBIT CARD WINDOW ##')
        ans = input('Press 1 to change mode of payment else press any key to proceed: ')
        if ans == '1':
            transaction(total_amount)
        else:

            Card_no = card_no()
            Card_Holder = cardholder()
            Exp_date = expiry_date()
            CVV = cvv()
            print(f'Your total amount is= Rs. {total_amount}')
            print(f'Press 1 to pay Rs. {total_amount}')
            print('Press any key to skip the transaction, you can pay later by logging into your account')
            Ans = input('Enter your choice here: ')
            if Ans == '1':

                query = f"insert into user_info(paid) values({total_amount});"
                mycursor.execute(query)
                mycon.commit()
                print('Payment made successfully!!')
            else:
                query = f"insert into user_info(paid) values(0);"
                mycursor.execute(query)
                mycon.commit()

                menu()
    if ch == "3":
        print(
            "UPI AutoPay is a new way to pay with UPI that will charge you automatically every month. That way you’ll never miss out on your shows and movies.")
        print("Now accepting: @upi, @paytm, @ibl, @axl, @ybl, @apl")
        upi = input("enter you UPI Id".capitalize())
        print("press 1 to confirm your payment else press any key to edit")
        ans = input("enter your choice= ")
        if ans == "1":
            print(f'Your total amount is= Rs. {total_amount}')
            print(f'Press 1 to pay Rs. {total_amount}')
            print('Press any key to skip the transaction, you can pay later by logging into your account')
            Ans = input('Enter your choice here: ')
            if Ans == '1':

                query = f"insert into user_info(paid) values({total_amount});"
                mycursor.execute(query)
                mycon.commit()
                print('Payment made successfully!!')
            else:
                query = f"insert into user_info(paid) values(0);"
                mycursor.execute(query)
                mycon.commit()

                menu()
        else:
            transaction(total_amount)



