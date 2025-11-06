def printStudent():
    info = input("Enter student name and surname: ")


    midterm = float(input("Enter midterm grade: "))
    final = float(input("Enter final grade: "))

    success_grade = (midterm * 0.4) + (final * 0.6)
    letter_grade = ""

    if success_grade >= 85:
        letter_grade = "AA"
    elif success_grade >= 70:
        letter_grade = "BA"
    elif success_grade >= 60:
        letter_grade = "BB"
    elif success_grade >= 50:
        letter_grade = "CB"
    elif success_grade >= 40:
        letter_grade = "CC"
    elif success_grade >= 30:
        letter_grade = "DC"
    elif success_grade >= 20:
        letter_grade = "DD"
    else:
        letter_grade = "FF"
 

    with open("grades.txt", "a") as file:
       file.writelines(" {} 's Succes Grade: {} and Letter Grade: {}\n".format(info, success_grade, letter_grade))

student_count = int(input("Enter number of students: "))
for _ in range(student_count):
    printStudent()