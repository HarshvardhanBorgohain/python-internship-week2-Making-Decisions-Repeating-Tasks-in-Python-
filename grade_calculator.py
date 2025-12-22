"""
Student Grade Calculator
A program that takes student marks and returns grade with encouraging messages
"""


def get_student_info():
    """
    Get student name and marks with validation
    Returns: tuple (name, marks)
    """
    print("\n" + "=" * 50)
    print("🎓 STUDENT GRADE CALCULATOR")
    print("=" * 50)

    # Get student name
    name = input("\n👤 Enter student name: ").strip()
    while not name:
        print("❌ Name cannot be empty. Please try again.")
        name = input("👤 Enter student name: ").strip()

    # Get marks with validation
    marks = None
    while marks is None:
        try:
            marks_input = input("📊 Enter marks (0-100): ").strip()
            marks = float(marks_input)

            # Validate range
            if marks < 0 or marks > 100:
                print("❌ Marks must be between 0 and 100. Please try again.")
                marks = None
            elif not marks_input.replace('.', '').isdigit():
                print("❌ Please enter a valid number.")
                marks = None

        except ValueError:
            print("❌ Invalid input. Please enter a number between 0-100.")
            marks = None

    return name.title(), marks


def calculate_grade(marks):
    """
    Calculate grade based on marks
    Returns: tuple (grade, message)
    """
    # Grading logic
    if marks >= 90:
        grade = "A"
        message = "🎉 Excellent! You're a star performer! 🌟"
    elif marks >= 80:
        grade = "B"
        message = "👍 Very Good! Keep up the great work!"
    elif marks >= 70:
        grade = "C"
        message = "✅ Good job! You're doing well!"
    elif marks >= 60:
        grade = "D"
        message = "💪 Satisfactory. Keep practicing to improve!"
    else:
        grade = "F"
        message = "📚 Needs improvement. Don't give up! You can do better next time!"

    return grade, message


def display_result(name, marks, grade, message):
    """
    Display formatted result to user
    """
    print("\n" + "=" * 50)
    print(f"📊 RESULT FOR {name.upper()}:")
    print("=" * 50)
    print(f"\n📝 Name: {name}")
    print(f"🎯 Marks: {marks}/100")
    print(f"🏆 Grade: {grade}")
    print(f"💬 Message: {message}")

    # Additional encouraging note
    if grade == "A":
        print("\n✨ Outstanding achievement! You should be proud!")
    elif grade in ["B", "C"]:
        print("\n✨ You're making great progress. Keep learning!")
    elif grade == "D":
        print("\n✨ Every expert was once a beginner. Keep going!")
    else:
        print("\n✨ Remember: Failure is just practice for success!")

    print("\n" + "=" * 50)


def get_grade_symbol(grade):
    """
    Return symbol for grade display
    """
    grade_symbols = {
        'A': '⭐⭐⭐⭐⭐',
        'B': '⭐⭐⭐⭐',
        'C': '⭐⭐⭐',
        'D': '⭐⭐',
        'F': '⭐'
    }
    return grade_symbols.get(grade, '')


def main():
    """
    Main function to run the grade calculator
    """
    print("\n" + "=" * 60)
    print("          🎓 WELCOME TO GRADE CALCULATOR 🎓")
    print("=" * 60)
    print("\nThis program calculates grades based on marks (0-100)")
    print("with encouraging messages for every student!")

    while True:
        try:
            # Get student information
            name, marks = get_student_info()

            # Calculate grade
            grade, message = calculate_grade(marks)

            # Get grade symbol
            symbols = get_grade_symbol(grade)

            # Display result
            display_result(name, marks, grade, message)

            # Show grade symbols
            if symbols:
                print(f"\n{symbols}")

            # Ask if user wants to continue
            print("\n" + "-" * 40)
            choice = input("\n📋 Calculate another grade? (yes/no): ").strip().lower()

            if choice not in ['yes', 'y', 'yeah', 'yep']:
                print("\n" + "=" * 50)
                print("👋 Thank you for using Grade Calculator!")
                print("📚 Keep learning and growing!")
                print("=" * 50 + "\n")
                break

        except KeyboardInterrupt:
            print("\n\n⚠️  Program interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"\n⚠️  An error occurred: {e}")
            print("Please try again.\n")


# Run the program
if __name__ == "__main__":
    main()