number_grade = int(input("What is your number grade?: "))

if number_grade < 60:
    print("F for 'Fail'.")
elif 60 <= number_grade < 63:
    print("D for Depressing")
elif 63 <= number_grade < 67:
    print("D for Depressing")
elif 67 <= number_grade < 70:
    print("D for Depressing")
elif 70 <= number_grade < 80:
    print("C for Capable")
elif 80 <= number_grade < 90:
    print("B for Best intentions")
elif 90 <= number_grade <= 100:
    print("A for Awesome")
