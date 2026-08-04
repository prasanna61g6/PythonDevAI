from student import *

def main() :
    print(f"College: {Student.college_name}")
    
    s1 = Student("Ravi Kumar", 101, "CSE")
    s2 = Student("Anitha Sharma", 102, "ECE")
    
    print(f"Total students: {Student.total_students}") 
    
    s1.add_marks("Maths", 92)
    s1.add_marks("Physics", 88)
    s1.add_marks("Chemistry", 76)

    s2.add_marks("Maths", 45)
    s2.add_marks("Physics", 30)
    
    print(s1)
    print(s2)
    
    print(f"s1 marks : {s1.get_marks()}")

    print(f"s1 passed : {s1.has_passed()}")
    print(f"s2 passed : {s2.has_passed()}")

    print(s1.change_branch("IT"))

    print("is_valid_mark(105):", Student.is_valid_mark(105))

    try:
        s1.add_marks("English", 150)
    except ValueError as e:
        print("Blocked (mark 150):", e)

    try:
        s1.average = 99
    except AttributeError as e:
        print("Blocked (write average):", e)

    try:
        s1.roll_number = 500
    except AttributeError as e:
        print("Blocked (write roll):", e)

    marks = s1.get_marks()
    marks["Maths"] = 100

    print("protected :", s1._branch)
    print("private :", s1.get_marks())
    
    
if __name__ == "__main__" :
    main()