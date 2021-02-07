def compare_ages():
    user_age = int(input("Please enter your age: ")) # Asking for user's age as an integer input value
    my_age = 21


    if user_age == my_age: # Asses if same age
        return "You are the same age as me."
    elif user_age > my_age: # If not, the difference in ages is calculated to give the age gap
        age_gap = user_age - my_age
        if age_gap != 1:
            return "You are older than me by " + str(age_gap) + " years." # If the age gap is not equal to one, the string will print years (plural)
        else:
            return "You are older than me by " + str(age_gap) + " year." # Otherwise, the string will print year (singular)
    else:
        age_gap = my_age - user_age
        if age_gap != 1:
            return "You are younger than me by " + str(age_gap) + " years."
        else:
            return "You are younger than me by " + str(age_gap) + " year."
