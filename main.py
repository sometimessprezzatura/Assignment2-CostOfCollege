"""
CS 1430 Assignment 2: The Cost of College

All of your Python for this assignment goes in this file.
The student guide explains what to build. Run check.py to test your work.
"""

# ---- CONSTANTS: do not change ----
SEMESTERS_PER_YEAR = 2
MONTHS_PER_YEAR = 9
CLASS_DAYS_PER_SEMESTER = 75
CS1430_CREDITS = 3
CS1430_MEETINGS_PER_SEMESTER = 45

SOCKS_USED_PER_WEEK = .3125 # I found it online, please don't fact check it.


# ---- FUNCTIONS: replace each return 0 ----

def cost_per_semester(annual_cost):
    per_semester = annual_cost / SEMESTERS_PER_YEAR
    return per_semester


def cost_per_month(annual_cost):
    per_month = annual_cost / MONTHS_PER_YEAR
    return per_month

def cost_per_day(annual_cost):
    per_day = annual_cost / (SEMESTERS_PER_YEAR * CLASS_DAYS_PER_SEMESTER)
    return per_day

def cost_per_credit(annual_cost, credits):
    per_credit = annual_cost / credits / SEMESTERS_PER_YEAR
    return per_credit

def cost_per_class(annual_cost, credits):
    per_class = cost_per_credit(annual_cost, credits) * CS1430_CREDITS / CS1430_MEETINGS_PER_SEMESTER
    return per_class

def worth_it(perpair, annual_cost):
    weeks_in_school_year = SEMESTERS_PER_YEAR * CLASS_DAYS_PER_SEMESTER / 5
    total_socks_cost = perpair * SOCKS_USED_PER_WEEK * weeks_in_school_year
    total_plus_socks = annual_cost + total_socks_cost
    return total_plus_socks


# ---- PROGRAM ----

def main():
    # Ask for the total cost for one year here.
    # Then ask for the credits this semester.
    TOTAL_COST = float(input("Enter the annual cost of college: "))
    CREDITS_PER = int(input("Enter the number of credits this semester: "))
    while True:
        # Show your menu here.
        print("1. Cost per semester")
        print("2. Cost per month")
        print("3. Cost per day")
        print("4. Cost per credit")
        print("5. Cost per class")
        print("6. Worth it?")
        print("Q. Quit")
    
        choice = input("Choose an option: ")

        if choice == "Q":
            break
        elif choice == "1":
            print("The cost of one semester of college is: $" + f"{cost_per_semester(TOTAL_COST):.2f}")
        elif choice == "2":
            print("The cost of one month of college is: $" + f"{cost_per_month(TOTAL_COST):.2f}")
        elif choice == "3":
            print("The cost of one day of college is: $" + f"{cost_per_day(TOTAL_COST):.2f}")
        elif choice == "4":
            print("The cost of one credit of college is: $" + f"{cost_per_credit(TOTAL_COST, CREDITS_PER):.2f}")         
        elif choice == "5":
            print("The cost of one class of CS1430 is: $" + f"{cost_per_class(TOTAL_COST, CREDITS_PER):.2f}")
        elif choice == "6":
            perpair = float(input("Enter the price of one pair of socks:"))
            print("The total cost of college is: $" + f"{TOTAL_COST:.2f}")
            print("The total cost of college plus socks is: $" + f"{worth_it(perpair, TOTAL_COST):.2f}")
        # Add a branch for each menu option here.
    

# ---- LAUNCH: do not change ----
if __name__ == "__main__":
    main()
