def max_calculation(first,second,third):
    if first>second:
        if first>third:
            print(f" the highest number is {first}")
        else:
            if third>second:
                print(f" the highest number is {third}")
            else:
                print(f" the two highest number are {first,second}")
    else:
        if third>second:
            print(f" the highest number is {third}")
        else:
          print(f" the highest number is {second}")

first=int(input("Enter your first number: "))
second=int(input("Enter your second number: "))
third=int(input("Enter your third number: "))

max_calculation(first,second,third)
