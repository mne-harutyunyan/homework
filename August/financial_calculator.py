# Create a dictionary with functions for various financial calculations (e.g., compound interest,
# loan payment, investment return). Write a function financial_calculator(operation, **kwargs) 
# that uses this dictionary to perform the requested calculation.
def compound_interest(p,r,n,t):
    return p*(1+r/n)**(n*t)
def loan_payment(r, pv, n):
    return (pv * r / 100)*n
def investment_return(p,r,t):
    return p*(r/100)*t

def financial_calculator(operation, **kwargs):
    dict = {
        "interest":compound_interest,
        "loan":loan_payment,
        "investment":investment_return
    }
    res = dict[operation](**kwargs)
    return res

operation = input("Enter the operation: ")
if operation == "interest":
    p = int(input("Enter initial principal balance: "))
    r = int(input("enter interest rate: "))
    n = int(input("enter number of times interest applied per time period:"))
    t = int(input("enter number of time periods elapsed: "))
    print(f"{operation} is {financial_calculator(operation, p=p,r=r,n=n,t=t)}.")
elif operation == "loan":
    pv = int(input("enter present value: "))
    r = int(input("enter rate per period: "))
    n = int(input("enter number of periods: "))
    print(f"{operation} interest for {n} years will be {financial_calculator(operation, pv=pv,r=r,n=n)}.")
elif operation == "investment":
    p = int(input("enter principal amount: "))
    r = int(input("enter interest rate per period: "))
    t = int(input("enter number of periods: "))
    print(f"{operation} is {financial_calculator(operation, p=p,r=r,t=t)}.")



