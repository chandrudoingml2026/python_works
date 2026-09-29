# H. Python Operators Use Cases

def internet_data_calculator():
    """Calculate remaining monthly data and warn at 80% usage or higher."""
    limit = float(input("Enter your monthly data limit in GB: "))
    used = float(input("Enter data used so far in GB: "))

    if limit <= 0 or used < 0:
        print("The data limit must be positive and usage cannot be negative.")
        return

    remaining = limit - used
    usage_percentage = (used / limit) * 100

    print(f"Remaining data: {remaining:.2f} GB")
    print(f"Usage: {usage_percentage:.2f}%")

    if usage_percentage >= 80:
        print("Warning: High usage, consider upgrading your plan.")


def shopping_discount_calculator():
    """Calculate a discounted price from an original price and discount percent."""
    price = float(input("Enter the original price: "))
    discount_percent = int(input("Enter the discount percent: "))

    discount_amount = (price * discount_percent) / 100
    final_price = price - discount_amount

    print(f"Original price: {price:.2f}")
    print(f"Discount applied: {discount_amount:.2f}")
    print(f"Final payable amount: {final_price:.2f}")


def voting_eligibility():
    """Check voting eligibility using age and case-insensitive citizenship input."""
    age = int(input("Enter age: "))
    citizen = input("Are you an Indian citizen? (yes/no): ").strip().lower()

    if age >= 18 and citizen == "yes":
        print("Eligible to vote")
    else:
        print("Not eligible")


# I. Conditional Structure

def banking_eligibility():
    """Determine the account type based on age and monthly income."""
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


def room_availability():
    """Offer an upgrade, discount, standard price, or report no available rooms."""
    available = input("Are rooms available? (yes/no): ").strip().lower()

    if available != "yes":
        print("No rooms available")
        return

    is_vip = input("Is the guest a VIP? (yes/no): ").strip().lower()

    if is_vip == "yes":
        print("Offer complimentary upgrade")
    else:
        membership_years = int(input("How many years has the guest been a member? "))
        if membership_years >= 5:
            print("Offer discount")
        else:
            print("Standard price")


def temperature_check():
    """Classify a temperature as normal, fever, or high fever."""
    temp = float(input("Enter body temperature in Celsius: "))

    if temp < 37:
        print("Normal temperature")
    elif temp < 39:
        print("Fever")
    else:
        print("High fever")


# J. Looping Constructs

def multiplication_table():
    """Print the multiplication table from 1 to 10 for one number."""
    number = int(input("Enter a number: "))

    for multiplier in range(1, 11):
        print(f"{number} x {multiplier} = {number * multiplier}")


def sum_even_and_odd():
    """Calculate the sums of even and odd numbers from 1 through n."""
    n = int(input("Enter a positive integer: "))

    if n < 1:
        print("Please enter a positive integer.")
        return

    even_sum = 0
    odd_sum = 0

    for number in range(1, n + 1):
        if number % 2 == 0:
            even_sum += number
        else:
            odd_sum += number

    print(f"Sum of even numbers: {even_sum}")
    print(f"Sum of odd numbers: {odd_sum}")


def nested_multiplication_tables():
    """Print tables for comma-separated numbers or an inclusive range.

    Examples: 2,3,5 or range 2 5
    """
    entry = input("Enter numbers (e.g. 2,3,5) or a range (e.g. range 2 5): ").strip()

    if entry.lower().startswith("range "):
        parts = entry.split()
        if len(parts) != 3:
            print("Enter a range as: range START END")
            return

        start = int(parts[1])
        end = int(parts[2])
        if start > end:
            print("The range start must not be greater than the end.")
            return
        numbers = range(start, end + 1)
    else:
        numbers = [int(value.strip()) for value in entry.split(",") if value.strip()]

    if not numbers:
        print("Enter at least one number.")
        return

    for number in numbers:
        for multiplier in range(1, 11):
            print(f"{number} x {multiplier} = {number * multiplier}")
        print()


def print_numbers_one_to_ten():
    """Print numbers 1 to 10 and stop after printing 10."""
    i = 1

    while i <= 10:
        print(i)
        i += 1


# M. Function-Based Programming

def calculate_food_discount(order_amount, discount_percent=10, minimum_order=1000):
    """Apply a 10% sample discount when an order is at least 1000."""
    if order_amount < 0:
        raise ValueError("Order amount cannot be negative.")

    if order_amount >= minimum_order:
        return order_amount * discount_percent / 100
    return 0


def food_delivery_discount():
    """Get an order amount, handle invalid input, and calculate its discount."""
    try:
        order_amount = float(input("Enter the food order amount: "))
        discount = calculate_food_discount(order_amount)
    except ValueError as error:
        print(f"Invalid input: {error}")
        return

    print(f"Discount: {discount:.2f}")
    print(f"Amount to pay: {order_amount - discount:.2f}")


def calculate_bonus(basic_salary, bonus_percent=10):
    """Calculate bonus; the sample default bonus rate is 10%."""
    return basic_salary * bonus_percent / 100


def sum_incentives(*incentives):
    """Sum any number of incentive amounts."""
    return sum(incentives)


def calculate_net_salary(gross_salary, pf_amount, tax_percent=10):
    """Subtract PF and sample 10% tax from gross salary."""
    tax_amount = gross_salary * tax_percent / 100
    return gross_salary - pf_amount - tax_amount, tax_amount


def salary_processing():
    """Compose salary functions; sample PF is 12% of basic salary."""
    basic_salary = float(input("Enter basic salary: "))
    bonus_percent = float(input("Enter bonus percent (default example: 10): ") or 10)
    incentives_input = input("Enter incentive amounts separated by commas, or leave blank: ").strip()

    if incentives_input:
        incentives = [float(value.strip()) for value in incentives_input.split(",")]
    else:
        incentives = []

    bonus = calculate_bonus(basic_salary, bonus_percent)
    incentive_total = sum_incentives(*incentives)
    gross_salary = basic_salary + bonus + incentive_total
    pf_amount = basic_salary * 12 / 100
    net_salary, tax_amount = calculate_net_salary(gross_salary, pf_amount)

    print(f"Basic salary: {basic_salary:.2f}")
    print(f"Bonus: {bonus:.2f}")
    print(f"Total incentives: {incentive_total:.2f}")
    print(f"Gross salary: {gross_salary:.2f}")
    print(f"PF deduction: {pf_amount:.2f}")
    print(f"Tax deduction: {tax_amount:.2f}")
    print(f"Net salary: {net_salary:.2f}")


def is_even(num):
    """Return True when num is even; otherwise return False."""
    return num % 2 == 0


def find_max(*numbers):
    """Return the highest number supplied as arguments."""
    if not numbers:
        raise ValueError("Provide at least one number.")
    return max(numbers)


def perform_operation(num, operation):
    """Perform a supported single-number operation."""
    operations = {
        "square": lambda value: value ** 2,
        "cube": lambda value: value ** 3,
        "absolute": abs,
    }

    if operation not in operations:
        raise ValueError("Choose square, cube, or absolute.")

    return operations[operation](num)


def number_utility_tool():
    """Test number utility functions using at least five integers."""
    numbers = [
        int(value.strip())
        for value in input("Enter at least 5 integers, separated by commas: ").split(",")
        if value.strip()
    ]

    if len(numbers) < 5:
        print("Please enter at least five integers.")
        return

    print("Even-number checks:")
    for number in numbers:
        print(f"{number}: {is_even(number)}")

    print(f"Maximum: {find_max(*numbers)}")

    operation = input("Choose an operation (square/cube/absolute): ").strip().lower()
    for number in numbers:
        try:
            result = perform_operation(number, operation)
        except ValueError as error:
            print(error)
            return
        print(f"{operation}({number}) = {result}")


def find_square():
    """Read an integer, print its square, and return the result."""
    num = int(input("Enter a number: "))
    result = num * num
    print(f"Square of the number is {result}")
    return result


def generate_invoice(**products):
    """Print each product and price, followed by the invoice total."""
    total = 0

    for product_name, price in products.items():
        print(f"{product_name}: {price:.2f}")
        total += price

    print(f"Total amount: {total:.2f}")


def invoice_generator():
    """Collect product names and prices, then generate an invoice."""
    products = {}

    print("Enter products one at a time. Leave the product name blank to finish.")
    while True:
        product_name = input("Product name: ").strip()
        if not product_name:
            break

        try:
            price = float(input(f"Price for {product_name}: "))
        except ValueError:
            print("Please enter a valid numeric price.")
            continue

        if price < 0:
            print("Price cannot be negative.")
            continue

        products[product_name] = price

    generate_invoice(**products)


def main():
    """Display task descriptions and run the selected task."""
    tasks = {
        "1": ("Internet data usage calculator", internet_data_calculator),
        "2": ("Shopping discount calculation", shopping_discount_calculator),
        "3": ("Voting eligibility bug fix", voting_eligibility),
        "4": ("Banking eligibility check", banking_eligibility),
        "5": ("Room availability check", room_availability),
        "6": ("Temperature classification bug fix", temperature_check),
        "7": ("Multiplication table (one number)", multiplication_table),
        "8": ("Sum of even and odd numbers", sum_even_and_odd),
        "9": ("Multiplication tables (list or range)", nested_multiplication_tables),
        "10": ("Infinite loop bug fix: print 1 to 10", print_numbers_one_to_ten),
        "11": ("Food delivery discount with exception handling", food_delivery_discount),
        "12": ("Salary processing with composed functions", salary_processing),
        "13": ("Number utility tool", number_utility_tool),
        "14": ("Square function bug fix", find_square),
        "15": ("Invoice generator using **kwargs", invoice_generator),
    }

    print("Python Use Cases")
    for option, (description, _) in tasks.items():
        print(f"{option}. {description}")

    choice = input("Choose a task (1-15): ").strip()
    task = tasks.get(choice)

    if task is None:
        print("Invalid choice. Please run the program again and choose 1-15.")
        return

    task[1]()


if __name__ == "__main__":
    main()