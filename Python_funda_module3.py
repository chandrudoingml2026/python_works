"""Inceptez Technologies - Python training exercises.

Each section below demonstrates the requested concept. Interactive examples
are implemented as functions so the file can also be imported safely.
"""


# A. Python is an indent-based programming language
def section_a_indentation():
    teams = ["Data", "AI", "DevOps"]
    for team in teams:
        print("Hello", team, "Team from Inceptez Technologies")
        print("Keep Learning and Exploring!")


# B. Comments in Python
def section_b_comments():
    # Single-line comment: store the number of students and trainers.
    students = 100
    trainers = 2

    """
    This is a multi-line comment-style string.
    The tracker adds students and trainers to get the total people.
    """
    total = students + trainers
    print("Training tracker total:", total)

    # Dead code can be disabled by commenting it out:
    # print("Welcome to Inceptez Python Learning")

    # Reactivated code:
    print("Welcome to Inceptez Python Learning")


# C. Playing with quotes
def section_c_quotes():
    single_quoted = 'This is Inceptez\'s "Python" class for Data Engineers & AI Engineers'
    double_quoted = "This is Inceptez's \"Python\" class for Data Engineers & AI Engineers"
    triple_quoted = """This is Inceptez's "Python" class for Data Engineers & AI Engineers"""

    print(single_quoted)
    print(double_quoted)
    print(triple_quoted)

    multiline_message = """Welcome to Inceptez Technologies!
Python Training: Basics
Enjoy your learning journey."""
    print(multiline_message)


# D. Variables, dynamic typing, and strong typing
def section_d_variables():
    student_name = "Arun"
    course_name = "Python Fundamentals"
    institute_name = "Inceptez Technologies"
    print(
        f"Name: {student_name} is learning the course {course_name} "
        f"at the institute {institute_name}"
    )

    # Python infers the type from the assigned value and permits reassignment.
    fee = 45000
    print("Initial fee type:", type(fee).__name__)
    fee = float(fee)
    gst = fee * 0.18
    total_fee = fee + gst
    print(f"Fee: {fee:.2f}, GST @ 18%: {gst:.2f}, Total: {total_fee:.2f}")

    # Strong typing prevents arithmetic between unrelated string and numeric types.
    try:
        print("Fee with text GST:", fee + "Eighteen percent GST")
    except TypeError as error:
        print("Strong typing demonstration:", error)


# E. Variable naming conventions
def section_e_naming():
    print("Invalid names: 2student (starts with a digit), class name (contains a space)")
    print("_student_id =", 1001)
    print("studentName =", "Priya")
    print("inceptez_batch =", "Morning")

    DataEngineeringBatch = "PascalCase"
    dataEngineeringBatch = "camelCase"
    data_engineering_batch = "snake_case"
    print(DataEngineeringBatch, dataEngineeringBatch, data_engineering_batch)


# F. Type identification and casting
def section_f_input_and_casting():
    age = input("Enter employee's age: ")
    print("Input type:", type(age).__name__)
    age_as_int = int(age)
    years_pending = 60 - age_as_int
    print(
        f"You will retire in {max(years_pending, 0)} years "
        "at Inceptez Technologies."
    )


def section_f_salary_fix():
    salary = "50000"
    bonus = 10000
    print("Total Salary in Inceptez:", int(salary) + bonus)


# G. Data types and casting
def employee_salary_breakdown():
    employee_name = input("Enter employee name: ")
    base_salary = float(input("Enter base salary: "))
    hra_percent = int(input("Enter HRA percentage: "))
    bonus_amount = float(input("Enter bonus amount: "))

    hra = base_salary * (hra_percent / 100)
    total_salary = base_salary + hra + bonus_amount
    print(f"\nEmployee: {employee_name}")
    print(f"Base Salary: {base_salary}")
    print(f"HRA @ {hra_percent}%: {hra}")
    print(f"Bonus: {bonus_amount}")
    print(f"Total Salary Payable: INR{total_salary}")


def classify_student_result():
    marks_text = input("Enter marks: ")
    try:
        marks = float(marks_text)
    except ValueError:
        print("Invalid marks entered - Please provide numeric input.")
        return

    if marks >= 90:
        result = "Outstanding"
    elif marks >= 75:
        result = "Excellent"
    elif marks >= 50:
        result = "Pass"
    else:
        result = "Fail"
    print("Result:", result)


def calculate_product_total():
    item_name = input("Enter product name: ")
    price = float(input("Enter price per item: "))
    quantity = int(input("Enter quantity: "))
    total_cost = price * quantity
    print(f"You purchased {quantity} units of {item_name}")
    print(f"Total payable: {total_cost} INR")


# H. Python operators
def internet_data_usage():
    limit = float(input("Enter total monthly data limit (GB): "))
    used = float(input("Enter data used so far (GB): "))
    if limit <= 0:
        raise ValueError("The data limit must be greater than zero.")
    remaining = limit - used
    usage_percentage = (used / limit) * 100
    print(f"Remaining data: {remaining:.2f} GB")
    print(f"Usage percentage: {usage_percentage:.2f}%")
    if usage_percentage >= 80:
        print("Warning: High usage, consider upgrading your plan.")


def shopping_discount():
    original_price = float(input("Enter original price: "))
    discount_percent = int(input("Enter discount percent: "))
    discount_amount = (original_price * discount_percent) / 100
    final_price = original_price - discount_amount
    print(f"Original price: {original_price:.2f}")
    print(f"Discount applied: {discount_amount:.2f}")
    print(f"Final payable amount: {final_price:.2f}")


def voting_eligibility():
    age = int(input("Enter age: "))
    citizen = input("Are you an Indian citizen? (yes/no): ").strip().lower()
    if age >= 18 and citizen == "yes":
        print("Eligible to vote")
    else:
        print("Not eligible")


# I. Conditional structures
def banking_eligibility():
    age = int(input("Enter age: "))
    income = float(input("Enter monthly income: "))
    if age < 18:
        print("Not eligible for a bank account.")
    elif income < 15000:
        print("Eligible for basic savings account.")
    elif income <= 50000:
        print("Eligible for savings + salary account.")
    else:
        print("Eligible for premium account.")


def room_availability(available, is_vip, membership_years):
    if available:
        if is_vip:
            print("Offer complimentary upgrade")
        elif membership_years >= 5:
            print("Offer discount")
        else:
            print("Standard price")
    else:
        print("No rooms available")


def temperature_check():
    temp = float((input("Enter body temperature in Celsius: ")))
    if temp < 37:
        print("Normal temperature")
    elif temp < 39:
        print("Fever")
    else:
        print("High fever")


def main():
    """Run non-interactive demonstrations; call input-based functions as needed."""
    section_a_indentation()
    section_b_comments()
    section_c_quotes()
    section_d_variables()
    section_e_naming()
    section_f_salary_fix()
    room_availability(available=True, is_vip=False, membership_years=6)
    temperature_check()


if __name__ == "__main__":
    main()
