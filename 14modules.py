#Modules logically organizes your python code. Module should contain related code
#one way is using import <file name> and specifying below on functions
#another way is to do from helper import <function name>

from helper import validate_and_execute
user_input = ""
while user_input != "exit":
    user_input = input("Hey user, enter number of days and conversion unit, separated by colon(:)!\n")
    days_and_unit = user_input.split(":")
    days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    print("You entered: ")
    print(days_and_unit_dictionary)
    print(type(days_and_unit_dictionary))
    validate_and_execute(days_and_unit_dictionary)
    