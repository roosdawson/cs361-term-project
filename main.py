#Author: Dawson Roos
#Course: CS361
#Description: Main implementation of budgeting software for CS361 term project

import os

budget = 0.0
spendings = 0.0
spendings_history = []

#function: introduction()
#definition: greet user with an introduction statement, as well as get their name
#return: name
def print_title():
    print(f"\nWelcome to Beaver Budgeting Software!\n")
def introduction():
    print_title()
    print(f"This is the main implementation, which allows for creating a budget and tracking spendings.\n\n")
    name = input("Please enter your name: ")
    return name

#function:   validate()
#definition: validate any input based on parameters
#parameters: user_input, low, high
#return:     valid input or not
def validate(user_input, low, high):
    if user_input < low or user_input > high:
        print(f"\nPlease enter a valid number")
        return 1
    else:
        return 0


#function:   main_ui_options()
#definition: provide user with all of the main screen options to choose from
#return:     user_main_choice
def main_ui_options():
    os.system('clear')
    print_title()
    print(f"\nOption 1: Update budget / monthly income")
    print(f"Option 2: Update expenses")
    print(f"Option 3: View budget vs spendings")
    print(f"Option 4: View about statement")
    print(f"Option 5: Exit")
    user_main_choice = float(input("\nEnter the number of the desired option: "))
    while validate(user_main_choice, 1, 5):
        user_main_choice = float(input("\nEnter the number of the desired option: "))
    return user_main_choice


#function:   remove_budget()
#definition: remove from budget
def remove_budget():
    global budget
    rm_budget_amt = float(input("\nEnter the amount you want to remove from your budget (in dollars): "))
    while rm_budget_amt > budget:
        print(f"\nPlease enter an amount less than your current budget ($", budget, ")")
        rm_budget_amt = float(input("\nEnter the amount you want to remove from your budget (in dollars): "))
    budget -= rm_budget_amt
    print(f"\nYour new budget is $", budget)


#function:   add_budget()
#definition: add to budget
def add_budget():
    global budget
    add_budget_amt = float(input("\nEnter the amount you want to add to your budget (in dollars): "))
    while add_budget_amt < 0:
        print(f"\nPlease enter a number greater than 0.")
        add_budget_amt = float(input("\nEnter the amount you want to add to your budget (in dollars): "))
    budget += add_budget_amt
    print(f"\nYour new budget is $", budget) 


#function:   update_budget_options()
#definition: provide user with budget add/remove options
def update_budget_options():
    print(f"\nOption 1: Create budget")
    print(f"Option 2: Reduce budget")
    print(f"Option 3: Exit to main page")
    user_choice = float(input("\nEnter the number of the desired option: "))
    while validate(user_choice, 1, 3):
        user_choice = float(input("\nEnter the number of the desired option: "))
    return user_choice


#function:   update_budget()
#definition: provide user with options to add or remove from their budget
def update_budget():
    global budget
    os.system('clear')
    print_title()
    print(f"\nYour current budget is $", budget)
    user_choice = update_budget_options()
    if user_choice == 1:
        add_budget()
    elif user_choice == 2:
        remove_budget()
    else:
        return


#function:   print_spendings_history()
#definition: print all previous spendings
def print_spendings_history():
    
    print(f"\nPrevious spendings:")
    for spending in spendings_history:
        print(f"${spending}")


#function:   remove_spendings_history()
#definition: remove purchase from spendings_history[]
#parameters: rm_spending_amt
def remove_spendings_history(rm_spending_amt):
    while rm_spending_amt not in spendings_history:
        choice = input("\nPlease enter a valid purchase amount. If not sure of previous purchases, enter 1. Else, press enter: ")
        if choice != '':
            print_spendings_history()
        rm_spending_amt = float(input("\nEnter the purchase amount you want to remove from your spendings (in dollars): "))
    spendings_history.remove(rm_spending_amt)
    return rm_spending_amt


#function:   remove_spending()
#definition: remove from spendings
def remove_spending():
    global spendings
    print(f"\nWARNING: All history of previous spending amounts will be deleted. Only remove if you are certain.")
    rm_spending_amt = float(input("\nEnter the purchase amount you want to remove from your spendings (in dollars): "))
    rm_spending_amt = remove_spendings_history(rm_spending_amt)
    spendings -= rm_spending_amt
    print(f"\nYour new total spendings are $", spendings)
    input("\nPress enter to go back to home page")



#function:   add_spending()
#definition: add to spendings
def add_spending():
    global spendings
    add_spending_amt = float(input("\nEnter the amount you want to add to your total spendings (in dollars): "))
    while add_spending_amt < 0:
        print(f"Please enter a number greater than 0.\n")
        add_spending_amt = float(input("\nEnter the amount you want to add to your total spendings (in dollars): "))
    spendings += add_spending_amt
    spendings_history.append(add_spending_amt)
    print(f"\nYour new total spendings are $", spendings)
    input("\nPress enter to go back to home page.")


#function:   update_spending_options()
#definition: provide user with spending add/remove options
def update_spending_options():
    print(f"\nOption 1: Add to spendings")
    print(f"Option 2: Remove from spendings")
    print(f"Option 3: Exit to main page")
    user_choice = float(input("\nEnter the number of the desired option: "))
    while validate(user_choice, 1, 3):
        user_choice = float(input("\nEnter the number of the desired option: "))
    return user_choice


#function:   update_spending()
#definition: provides user with options to add or remove spendings
def update_spending():
    global spendings
    os.system('clear')
    print_title()
    print(f"\nYour current total spendings are $", spendings)
    user_choice = update_spending_options()
    if user_choice == 1:
        add_spending()
    elif user_choice == 2:
        remove_spending()
    else:
        return


#function:   view_current_status()
#definition: provide user with current budget and spendings information
def view_current_status():
    os.system('clear')
    print(f"\nYour current budget is $", budget)
    print(f"Your current total spendings are $", spendings, "\n")
    if spendings > budget:
        print(f"You are over budget by $", spendings - budget, "\n")
    elif spendings < budget:
        print(f"Congrats! You are under budget by $\n", budget - spendings)
    else:
        print(f"Your budget aligns perfectly with your spendings. Keep it up!\n")

    input("\nPress enter to go back to home page.")


#function:   about_page()
#definition: provide user with information about author and budgeting program
def about_page():
    os.system('clear')
    print_title()
    print(f"\n\nABOUT PAGE:\n")
    print(f"Author: Dawson Roos")
    print(f"Course: CS361")
    print(f"Assignment: Beaver Budgeting Software\n")
    print(f"This program allows you to create your own budget, as well as input your spendings.")
    print(f"\nThere are currently 3 different main functionalities implemented:")
    print(f" - Update budget / monthly income")
    print(f" - Update expenses")
    print(f" - View budget vs spendings")
    print(f"\nThis program utilizes python as the main programming language.")
    print(f"\n")
    input("\nPress enter to go back to home page.")

#function:   exit_statement()
#definition: exit statement for the program
#parameters: user_name
def exit_statement(user_name):
    os.system('clear')
    print(f"\nThank you for using Beaver Budgeting!")
    print(f"Have a good day", user_name + ".")
    print(f"\n")

#function:   main()
#definition: main function to act as central point for all services
def main():

    user_name = introduction()
    main_choice = 1

    while main_choice != 5:

        main_choice = main_ui_options()

        if main_choice == 1:
            update_budget()
        elif main_choice == 2:
            update_spending()
        elif main_choice == 3:
            view_current_status()
        elif main_choice == 4:
            about_page()
            
    exit_statement(user_name)


if __name__ == "__main__":
    main()
