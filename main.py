# # choice1=("rock")
# # choice2=("paper")
# # choice3=("scissors")
# # user1=input("please enter your choice(user1): ").upper().lower()
# # user2=input("please enter your choice(user2): ").upper().lower()
# # if user1 == user2:
# #     print("draw")
# # elif user1 == choice1 and user2 == choice2:
# #     print("user2 wins!")
# # elif user1 == choice1 and user2 ==choice3:
# #     print(" user1 wins!")
# # elif user1 == choice2 and user2 == choice1:
# #     print("user1 wins!")
# # elif user1 == choice2 and user2 == choice3:
# #     print("user2 wins!")
# # elif user1 == choice3 and user2 == choice1:
# #     print("user2 wins")
# # elif user1 == choice3 and user2 == choice2:
# #     print("user1 wins!")
# # else:
# #     print("invalid choice")

# # Program to calculate tax based on salary range

# # Ask the user to input the salary
# salary_input = input("Enter your monthly salary: ")

# if salary_input.replace('.', '', 1).isdigit():
#     salary = float(salary_input)

#     if salary < 0:
#         print("Salary cannot be negative. Please enter a valid amount.")
#     else:
#         if salary <= 5000:
#             tax = salary * 0.10
#         elif salary <= 20000:
#             tax = salary * 0.15
#         elif salary <= 40000:
#             tax = salary * 0.20
#         elif salary <= 50000:
#             tax = salary * 0.25
#         else: 
#             tax = salary * 0.30

        
#         tax = round(tax, 2)

#         print(f"Your salary: ${round(salary, 2):,.2f}")
#         print(f"Calculated tax: ${tax:,.2f}")
# else:
#     print("Invalid input. Please enter a valid numeric value.")