#Simple calcuator function in py
def add(a,b):
    return a+b

def multi(a,b):
    return a*b

def dev(a,b):
    return a/b

def subt(a,b):
    return a-b


def main():
    print("This is the simple calculator in py")
    print("====================================")
    
    num1 = float(input("Enter first number here: "))
    num2 = float(input("Enter Second number here: "))
    txt = str(input("What you want to do? addkar/gunakar/bhagkar/ghatade: "))
    
    if txt=="addkar":
        result = add(num1,num2)
    elif txt=="gunakar":
        result = multi(num1,num2)
    elif txt=="bhagkar":
        result= dev(num1,num2)
    elif txt=="ghatade":
        result= subt(num1,num2)
    else:
        result = "Ma chuda bhosdile..Fuck You...."
        
    print("Output is: ", result)
        
# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()