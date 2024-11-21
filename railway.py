while True:
    ticket=1000
    gender=int(input('''enter the gender:
                  1.Male
                  2.Female'''))
    age=int(input("enter age"))
    if gender==1:
        if age>=60:
            print("senior citizen")
            amount=ticket-((30/100)*ticket)
            print(amount)
        else:
            print("normal citizen")
            print(ticket)
    elif gender==2:
        if age>=60:
            print("senior citizen")
            amount=ticket-((50/100)*ticket)
            print(amount)
        else:
            print("normal citizen")
            amount=ticket-((30/100)*ticket)
            print(amount)
    
        

