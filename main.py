
import time
import theater_info,user_info

user_input = 20
s = theater_info.seats()
total_seats, no_of_rows, no_of_seats= s.capacity()
st=theater_info.statistics()
total_seats_booked=0
total_income = 0
current_income=0
while user_input != 0:
    print("1: Buy a Ticket\n2: Statistics\n3: Show booked Tickets User Info\n0: Exit")
    user_input = int(input())
    
    if user_input == 1:
        t = theater_info.tickets()
        if t.book_row<=no_of_rows and t.book_column<=no_of_seats :
            b,current_income=t.buy_ticket(total_seats,no_of_rows,total_income,total_seats_booked)
            if b != None:
                total_income = total_income + current_income
            if b == True:
                total_seats_booked += 1
        else:
            print("you are trying to book the wrong seat")

        time.sleep(2)

    elif user_input == 2:
        t1=st.stats(total_seats_booked,total_seats,current_income,total_income)

    elif user_input == 3:
        u1=user_info.user_info()

        checkR = int(input("Enter the row you want to check: "))
        checkC = int(input("Enter the column you want to check: "))
        u1.booked_tickets_user_info(checkR, checkC,current_income)
        

    
    


