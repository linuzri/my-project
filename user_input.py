calculate_days = 12 * 30
units = "days"


def calculate_age_to_days(user_input):
    return f"{user_input} years is {user_input * calculate_days} {units}"


def validate_and_execute():
    if age.isdigit():
        user_age_integer = int(age)
        if user_age_integer > 0:
            result = calculate_age_to_days(user_age_integer)
            print(result)
        elif user_age_integer == 0:
            print("You entered a 0, please enter a positive number.")
    else:
          print("You input is not valid number. Rerun program!")


age = input("Age:")
validate_and_execute()

