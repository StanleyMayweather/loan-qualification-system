"""
For this activity, you will implement a simplistic system to determine if a user can 
qualify for a loan.

The Problem: Qualifying for a loan
When loaning money to someone, you want to have some level of confidence that they will
be able to repay the loan.

There are different characteristics you might base this decision on, or different
questions you might ask someone. And depending on their answers to those questions,
you might ask other questions. For example, consider the following possible questions:

Does the person have a job, and if so, how long have they worked there, and how much 
money do they make?

Is there good collateral for the loan? (for example, is the loan against a car or home
that is worth at least the amount of the loan?)

Does the person have a good credit score or history of paying back loans?

How much other debt does the person have?

How much money does the person have?

Will the person have a down payment, and if so, what percentage of the loan does it 
amount to?

Program Specification
Write a program to determine whether to loan money based on the following rules.

First, ask for a rating from 1–10 on the following:

How large is the loan?

How good is your credit history?

How high is your income?

How large is your down payment?

Then, you will create a boolean variable for whether you should loan the money that will
be set to either True or False. Set up a series of if statements to decide if your 
decision to loan is "yes" or "no" according to the following rules:

First, check if the loan size is at least 5. If it is, use the following rules:

If the credit history and income are both at least 7, then the decision is "yes"

If either the credit history or income is at least 7, then check if the down payment
is at least 5, if it is, the decision is "yes", if not, the decision is "no"

Otherwise (if neither the credit history nor income is at least 7), the decision is
"no"

Otherwise (if the loan is not 5 or greater), use these rules:

If the credit is less than 4, then the decision is "no"

Otherwise, check the following:

If either the income or the down payment is at least 7, the decision is "yes"

If both the income and the down payment are at least 4, then the answer is "yes"

Otherwise, the decision is "no"

Finally, display the decision to the user.
"""

#Coding starts here
# Ask for the ratings from 1 to 10 on various factors
loan_size = int(input("How large is the loan? (1-10): "))
credit_history = int(input("How good is your credit history? (1-10): "))
your_income = int(input("How high is your income? (1-10): "))
down_payment = int(input("How large is your down payment? (1-10): "))

# Initialize the loan decision variable
loan_decision = False

# Decision based on loan size and other factors
if loan_size >= 5:
    if credit_history >= 7 and your_income >= 7:
        loan_decision = True
    elif credit_history >= 7 or your_income >= 7:
        if down_payment >= 5:
            loan_decision = True
        else:
            loan_decision = False
    else:
        loan_decision = False
else:
    if credit_history < 4:
        loan_decision = False
    else:
        if your_income >= 7 or down_payment >= 7:
            loan_decision = True
        elif your_income >= 4 and down_payment >= 4:
            loan_decision = True
        else:
            loan_decision = False

# Display the loan decision
if loan_decision:
    print("The decision is: Yes, you qualify for the loan!")
else:
    print("The decision is: No, you do not qualify for the loan.")
print("-----------------------------------------------")
