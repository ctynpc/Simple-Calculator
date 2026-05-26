def calc():
    while True:
        x=input("Mode(add/sub/mul/div/rem/quit):")
        if x=="quit":
            print("Exiting the calculator. Goodbye!")
            return
        z=1
        if x=="add":
            # Perform addition
            y=input("Enter numbers separated by space: ")
            lst=y.split(" ")
            print("Result:" + str(sum(map(float,lst))))
        elif x=="sub":
            # Perform subtraction
            y=input("Enter numbers separated by space: ")
            lst=y.split(" ")
            print("Result:" + str(float(lst[0])-sum(map(float,lst[1:]))))
        elif x=="mul":
            # Perform multiplication
            y=input("Enter numbers separated by space: ")   
            lst=y.split(" ")
            for t in range(len(lst)):
                z*=float(lst[t])
            print("Result:" + str(z))
        elif x=="div":
            # Perform division
            y=input("Enter numbers separated by space: ")
            lst=y.split(" ")
            if 0 in map(float,lst[1:]):
                print("Input error, divisor must be non-zero")
                break
            for t in range(1,len(lst)):
                z/=float(lst[t])
            print("Result:"+str(z))
        elif x=="rem":
            y=input("Enter numbers separated by space: ")
            lst=y.split(" ")
            if 0 in map(float,lst[1:]):
                print("Input error, divisor must be non-zero")
                break
            for t in range(1,len(lst)):
                z*=float(lst[t])
            print("Quotient:" + str(float(lst[0])//z))
            print("Remainder:" + str(float(lst[0])%z))
        else:
            print("Invalid mode. Please enter a valid mode.")
while True:
    print("Type calc for the calculator function, exit to exit")
    p=input("")
    if p.lower()=="calc":
        calc()
    if p.lower()=="exit":
        print("Exiting the program. Goodbye!")
        break