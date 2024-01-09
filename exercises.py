import json
### Ex: 1-9
# 1. Create a variable called fanduel and assign a value with your first name.

fanduel = "Cristian"

# 2. Create a variable called year_of_participation to equal any value between 3 and 9.
year_of_participation = 4

# 3. Create a variable called is_employee to equal True.
is_employee = True

# 4. Create a variable called pi to equal 3.14.
pi = 3.14

# 5. Create a variable declared as a string called betfair. Assign value 2024 to it.
betfair = "2024"

# 6. Create a variable declared as bool called participated. Assign value "Betfair" to it.
participated = "Betfair"

# 7. Create another variable and perform string interpolation with + with all the variables from steps 1-5.
interpolation1 = fanduel + str(year_of_participation) + str(is_employee) + str(pi) + betfair

# 8. Comment the variable created at step 6 and create another variable and perform string interpolation with f-string with all the variables from steps 1-5.

interpolation2 = f"{fanduel}{year_of_participation}{is_employee}{pi}{betfair}"

# 9. Create a variable and perform string interpolation with .format with all the variables from steps 1-5.
interpolation3 = "{}{}{}{}{}".format(fanduel, year_of_participation, is_employee, pi, betfair)

print(interpolation2)

### Ex: 10-24

# 10. Print the type of the variable declared at step 1 and add an inline comment next to the declaration with the output.
print(type(fanduel))

# 11. Create a list called employees which stores 3 strings of your choosing and 2 integers.
employees = ["Andrei", "Dragos", "Alina", 21, 32]

# 12. Append your favorite Disney character name to the list created at step 11 and print the list afterwards.
employees.append("Pluto")
print(employees)

# 13. Print the last element of the list created at step 12.
print(employees[-1])

# 14. Remove element from index 1 from the array created at step 12. Print the array afterwards.
del employees[1]
print(employees)

# 15. Create a dictionary called employee_info which has two key-value pairs: name: betfair, your_age: 123.
employees = {"name": "betfair", "your_age": 123}

# 16. Print the value using f-string of keys name and your_age.
print(f"Name: {employees['name']}, Your Age: {employees['your_age']}")

# 17. Print all the keys of the dictionary using .keys() builtin function.
print(employees.keys())

# 18. Print all the values of the dictionary using .values() builtin function.
print(employees.values())

# 19. Print the value of your_age key using .get() function. Give as the second argument to the function the default value "Python".
print(employees.get("your_age", "Python"))
print(employees.get("your_age_what", "Python"))

# 20. Create a set called cnp_information and add 456, 678, 434234, 65654 value into it.
cnp_information = {456, 678, 434234, 65654}

# 21. Create another set called cnp_information_2 and add 456, 678, 434234, 12345677889 into it.
cnp_information_2 = {456, 678, 434234, 12345677889}

# 22. Add value 456 again to the set cnp_information_2 and print the set afterwards.
cnp_information_2.add(456)
print(cnp_information_2)

# 23. Print the values which are different between the sets. So the output should be {65654, 12345677889}.
different_values = cnp_information.symmetric_difference(cnp_information_2)
print("Diferent values: ", different_values)


###Ex:25-26

# 24. Create a function called my_calculation which takes two arguments called x and y.
# Inside the function, print the sum between x and y. Call the function with x=6 and y=8.

def my_calculation(x, y):
    result = x + y
    print(f"The sum of {x} and {y} is {result}")


my_calculation(6, 8)


# 25. Create a function called my_conditional which takes three arguments: is_employee with default value True,
# first_name without any default value, and last_name without any default value.
# a) Fix the red error highlighted.
# b) Inside the function, print the first_name and last_name if is_employee is True and return the value True.
#    If is_employee is False, then print "Forbidden. You are not an employee." and return False.

def my_conditional(is_employee=True, first_name="", last_name=""):
    if is_employee:
        print(f"First Name: {first_name}, Last Name: {last_name}")
        return True
    else:
        print("Forbidden. You are not an employee.")
        return False

my_conditional(True, "Ionel", "Fantasticul")  # Should print and return True
my_conditional(False, "Serenada", "Cosmina")  # Should print and return False

# 26. Open a JSON file called hula.json with w+ and use .dumps() to write the content of the dictionary created
# at step 15 to the file.

hula_json = "hula.json"
with open(hula_json, "w+") as json_file:
    json.dump(employees, json_file)