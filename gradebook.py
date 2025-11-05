'''
Name: Kirti Saini
Date: 05/11/2025
Project Title: Gradebook Analyzer
'''

import statistics

#--------------------------------------------
#             Project Setup
#--------------------------------------------
def print_menu():
    """Displays the main menu options."""
    print("\n========== GradeBook Analyzer ==========")
    print("1. Enter student data and analyze")
    print("2. Exit")
    print("========================================")

def welcome_message():
    """Prints welcome message at program start."""
    print("\nWelcome to the GradeBook Analyzer!")
    print("Analyze and report student performance easily.\n")


#--------------------------------------------
#               Data Input
#--------------------------------------------
def manual_entry():
    marks={}
    num=int(input("Enter number of students: "))
    for i in range(num):
        name=input("Enter student name: ")
        score=float(input(f"Enter marks for {name}: "))
        marks[name]=score
    return marks

#--------------------------------------------
#              Statistical Functions
#--------------------------------------------
def calculate_average(marks_dict):
    return sum(marks_dict.values())/len(marks_dict)

def calculate_median(marks_dict):
    return statistics.median(marks_dict.values())

def find_max_score(marks_dict):
    return max(marks_dict.values())

def find_min_score(marks_dict):
    return min(marks_dict.values())

#--------------------------------------------
#              Grade Assignment
#--------------------------------------------
def assign_grades(marks_dict):
    grades = {}
    for name, score in marks_dict.items():
        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        elif score >= 70:
            grade = "C"
        elif score >= 60:
            grade = "D"
        else:
            grade = "F"
        grades[name] = grade
    return grades

def grade_distribution(grades):
    distribution = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    for grade in grades.values():
        distribution[grade] += 1
    return distribution

#--------------------------------------------
#             Pass/Fail Analysis
#--------------------------------------------
def pass_fail_lists(marks_dict):
    passed_students = [name for name, score in marks_dict.items() if score >= 40]
    failed_students = [name for name, score in marks_dict.items() if score < 40]
    return passed_students, failed_students

#--------------------------------------------
#             Display Results
#--------------------------------------------
def display_table(marks_dict, grades):
    """Displays results in a formatted table."""
    print("\nName\t\tMarks\tGrade")
    print("-" * 35)
    for name, marks in marks_dict.items():
        print(f"{name:<15}{marks:<10}{grades[name]}")
    print("-" * 35)

def analyze_data(marks_dict):
    """Performs full analysis and displays results."""
    # Compute statistics
    avg = calculate_average(marks_dict)
    med = calculate_median(marks_dict)
    high = find_max_score(marks_dict)
    low = find_min_score(marks_dict)

    # Grade and pass/fail analysis
    grades = assign_grades(marks_dict)
    distribution = grade_distribution(grades)
    passed, failed = pass_fail_lists(marks_dict)

    # Output formatted results
    display_table(marks_dict, grades)
    print(f"\n📊 Average Marks: {avg:.2f}")
    print(f"📈 Median Marks: {med:.2f}")
    print(f"🏆 Highest Score: {high}")
    print(f"📉 Lowest Score: {low}")

    print("\nGrade Distribution:")
    for grade, count in distribution.items():
        print(f"  {grade}: {count}")

    print(f"\n✅ Passed ({len(passed)}): {', '.join(passed)}")
    print(f"❌ Failed ({len(failed)}): {', '.join(failed)}")

# -------------------------- Main Loop --------------------------------
def main():
    """Runs the main program loop."""
    welcome_message()
    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            marks = manual_entry()
            analyze_data(marks)
        elif choice == "2":
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice. Please try again.")

        again = input("\nDo you want to analyze another class? (y/n): ").lower()
        if again != 'y':
            print("Exiting program. Have a great day!")
            break

# ---------------------- Program Entry Point ---------------------------
if __name__ == "__main__":
    main()