
student_data = {}


# --- Styling 
def style1():
    print("\n")
    print("*" * 80)
def style2():
    print("\n") 
    print("-" * 80)
def style_error():
    print("x" * 50)

# ---- Add Student to dict student_data
def add_student(name):
    if name not in student_data:
        student_data[name] = []
        print(f"Student '{name}' added successfully!")
    else:
        print(f"Student '{name}' already exists!")


#  --- Adding grades
def add_grade(name, grade):
    if name in student_data:
        student_data[name].append(grade)
        print(f"Grade '{grade}' added to student '{name}'!")
    else:
        print(f"Student '{name}' not found!")
    

def calculate_average_grade(name):
    if name in student_data:
        grades = student_data[name]
        average_grade = sum(grades) / len(grades)
        return average_grade
    else:
        return None

def determine_letter_grade(average_grade):
    if average_grade >= 90:
        return "A"
    elif average_grade >= 80:
        return "B"
    elif average_grade >= 70:
        return "C"
    elif average_grade >= 60:
        return "D"
    else:
        return "F"

def view_student_report(name):
    if name in student_data:
        average_grade = calculate_average_grade(name)
        letter_grade = determine_letter_grade(average_grade)
        print(f"Student '{name}' Average: {average_grade:.2f} (Grade: {letter_grade})")
        print(f"Grades: {student_data[name]}")
    else:
        print(f"Student '{name}' not found!")


def display_class_stats():
    if student_data:
        class_average = sum(sum(grades) for grades in student_data.values()) / sum(len(grades) for grades in student_data.values())
        highest_performing_student = max(student_data, key=lambda student: calculate_average_grade(student))
        lowest_performing_student = min(student_data, key=lambda student: calculate_average_grade(student))
        print(f"Class Average: {class_average:.2f}")
        print(f"Highest Performing Student: {highest_performing_student} (Average: {calculate_average_grade(highest_performing_student):.2f})")
        print(f"Lowest Performing Student: {lowest_performing_student} (Average: {calculate_average_grade(lowest_performing_student):.2f})")
    else:
        print("No students in the class!")
            

while(True):
    try:
        style1()
        print("== STUDENT GRADEBOOK MANAGER ===")
        userInput = int(input("1. Add Student\n2. Add Grade\n3. View Student Report\n4. Class Statistics\n5. Exit\nChoice: "))
        if userInput == 1:
            style2()
            print("+++ Add Student +++")
            name = input("Enter student name: ")
            add_student(name)
        elif userInput == 2:
            name = input("Enter student name: ")
            grade = float(input(f"Enter {name}'s grade: "))
            add_grade(name, grade)
            
        elif userInput == 3:
            name = input("Enter student name: ")
            view_student_report(name)
        elif userInput == 4:
            display_class_stats()
        elif userInput == 5:
            style2()
            print("Goodbye!")
            style2()
            break
        else:
            style_error()
            print("xxx --- Enter a Valud Input please (1-5) --- xxx")
            style_error()
    except ValueError:
        style_error()
        print("xxx --- Please Enter valid input (Integers only) --- xxx")
        style_error()

















# Flavours = []

# pizza = {"Flavour": "", "ingredients": ['cheese', 'sausage', 'peppers']}

# # for ingredient in pizza:
# #     ingredient = '' + ingredient
# #     print(pizza['ingredients'])

# pizza['ingredients'].append('sugar')

# pizza["State"] = [23, 2, 89, 50]

# print(pizza['ingredients'])
# print(pizza)

# Flavours.append(pizza)
# print(Flavours)

# print(Flavours[0]['State'])

# average = sum(pizza['State']) / len(pizza['State'])

# print(average)



