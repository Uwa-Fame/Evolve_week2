
# # def divide_num(n):
# #     for i in range(1, n + 1):

# number = 50
for number in range(1, 51):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 10 == 0:
        print("Fizz")
    else:
        print (number)
    


# def classify_number(number):
#     number = 0
#     if number % 2 == 0:
#         return "Fizz"
#     elif number % 5 == 0:
#         return "Buzz"
#     elif number % 3 and 5 == 0:
#         return "FizzBuzz"
#     else: return number

# classify_number()
# def sum_up_to(n):
#     total = 0
#     for i in range(1, n + 1):
# total = total + i
# return total

# # Main program starts here
# for current in range(1, 6):
# category = classify_number(current)
# print(f"{current} is {category}")
# running_total = sum_up_to(5)
# print(f"The sum of numbers from 1 to 5 is {running_total}"