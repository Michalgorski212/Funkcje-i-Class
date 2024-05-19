def exercise1():
    import array

    # Wyświetlenie przestrzeni nazw modułu array
    print(dir(array))
def exercise2():
    class MyClass:
        class_variable = "A class variable"

        def __init__(self, instance_variable):
            self.instance_variable = instance_variable

        def my_method(self):
            return "This is a method"

    # Tworzenie instancji klasy
    my_instance = MyClass("An instance variable")

    # Wyświetlenie przestrzeni nazw klasy
    print("Namespace of MyClass:")
    print(dir(MyClass))

    # Alternatywnie, wyświetlenie przestrzeni nazw instancji klasy
    print("\nNamespace of my_instance:")
    print(dir(my_instance))
def exercise3():
    class SampleClass:
        def __init__(self, value):
            self.value = value
            self.description = "This is a sample class"

    # Tworzenie instancji klasy
    instance = SampleClass(42)

    # Wyświetlenie przestrzeni nazw instancji
    print("Namespace of the instance:")
    print(vars(instance))  # 'vars' pokazuje słownik zawierający przestrzeń nazw

    # Alternatywnie, używając 'dir' dla bardziej kompleksowego przeglądu
    print("\nDetailed namespace using dir():")
    print(dir(instance))
def exercise4():
    import builtins

    # Importowanie funkcji abs z modułu builtins
    absolute = builtins.abs

    # Wyświetlenie dokumentacji funkcji abs
    print("Documentation of abs():")
    print(absolute.__doc__)

    # Obliczenie i wyświetlenie wartości bezwzględnej liczby -155
    result = absolute(-155)
    print("\nThe absolute value of -155 is:", result)
def exercise5():
    import inspect

    def student(**kwargs):
        # Wyświetlenie nazw i wartości wszystkich argumentów przekazanych do funkcji
        for name, value in kwargs.items():
            print(f"{name}: {value}")

        # Dodatkowo, pokazanie nazw argumentów za pomocą atrybutów funkcji
        args = inspect.signature(student).parameters
        print("\nNames of all arguments:")
        print(list(args))

    # Wywołanie funkcji z przykładowymi argumentami
    student(name="Alice", age=22, major="Computer Science")
def exercise6():
    def student_data(student_id=None, student_name=None, student_class=None):
        if student_id and not (student_name or student_class):
            print(f"Student ID: {student_id}")
        elif student_name and student_class:
            print(f"Student Name: {student_name}")
            print(f"Student Class: {student_class}")
        else:
            print("Invalid or incomplete data provided")

    # Przykładowe wywołania funkcji
    student_data(student_id=101)
    student_data(student_name="Alice", student_class="12A")
def exercise7():
    class Student:
        def __init__(self, name, id):
            self.name = name
            self.id = id

    # Tworzenie instancji klasy Student
    student = Student("John Doe", 12345)

    # Wyświetlenie typu klasy Student
    print("Type of Student class:", type(Student))

    # Wyświetlenie kluczy __dict__ dla instancji student
    print("Keys of student.__dict__:", student.__dict__.keys())

    # Wyświetlenie wartości atrybutu __module__ klasy Student
    print("Module of Student class:", Student.__module__)
def exercise8():
    # Definiowanie dwóch pustych klas
    class Student:
        pass

    class Marks:
        pass

    # Tworzenie instancji klas
    student_instance = Student()
    marks_instance = Marks()

    # Sprawdzenie, czy instancje należą do podanych klas
    print("Czy student_instance jest instancją klasy Student?", isinstance(student_instance, Student))
    print("Czy marks_instance jest instancją klasy Marks?", isinstance(marks_instance, Marks))

    # Sprawdzenie, czy podane klasy są podklasami wbudowanej klasy object
    print("Czy Student jest podklasą klasy object?", issubclass(Student, object))
    print("Czy Marks jest podklasą klasy object?", issubclass(Marks, object))
def exercise9():
    class Student:
        def __init__(self, name, marks):
            self.student_name = name
            self.marks = marks

    # Tworzenie instancji klasy Student
    student = Student("John Doe", 75)

    # Wyświetlenie oryginalnych wartości atrybutów
    print("Original Name:", student.student_name)
    print("Original Marks:", student.marks)

    # Modyfikacja atrybutów
    student.student_name = "Jane Doe"
    student.marks = 85

    # Wyświetlenie zmodyfikowanych wartości atrybutów
    print("Modified Name:", student.student_name)
    print("Modified Marks:", student.marks)
def exercise10():
    class Student:
        def __init__(self, student_id, student_name):
            self.student_id = student_id
            self.student_name = student_name

    # Tworzenie instancji klasy Student
    student = Student(123, "John Doe")

    # Wyświetlenie oryginalnych atrybutów
    print("Original attributes and values:")
    print(student.__dict__)

    # Dodanie nowego atrybutu student_class
    student.student_class = "12A"

    # Wyświetlenie atrybutów po dodaniu student_class
    print("\nAttributes and values after adding student_class:")
    print(student.__dict__)

    # Usunięcie atrybutu student_name
    del student.student_name

    # Wyświetlenie atrybutów po usunięciu student_name
    print("\nAttributes and values after removing student_name:")
    print(student.__dict__)
def exercise11():
    class Student:
        def __init__(self, student_id, student_name):
            self.student_id = student_id
            self.student_name = student_name

        def add_student_class(self, student_class):
            self.student_class = student_class

        def display_attributes(self):
            for attr, value in self.__dict__.items():
                print(f"{attr}: {value}")

    # Tworzenie instancji klasy Student
    student = Student(123, "John Doe")

    # Dodanie nowego atrybutu student_class
    student.add_student_class("12A")

    # Wyświetlenie wszystkich atrybutów i ich wartości
    student.display_attributes()
def exercise12():
    class Student:
        def __init__(self, student_id, student_name, student_class):
            self.student_id = student_id
            self.student_name = student_name
            self.student_class = student_class

        def display_attributes(self):
            for attr, value in self.__dict__.items():
                print(f"{attr}: {value}")

    # Tworzenie dwóch instancji klasy Student
    student1 = Student(1, "Alice", "10A")
    student2 = Student(2, "Bob", "12B")

    # Wyświetlanie atrybutów instancji student1
    print("Attributes of student1:")
    student1.display_attributes()

    # Wyświetlanie atrybutów instancji student2
    print("\nAttributes of student2:")
    student2.display_attributes()
def exercise13():
    class IntegerToRoman:
        def __init__(self):
            self.value_map = [
                (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
                (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
                (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
            ]

        def int_to_roman(self, num):
            roman_numeral = ''
            for value, symbol in self.value_map:
                while num >= value:
                    roman_numeral += symbol
                    num -= value
            return roman_numeral

    # Przykłady użycia
    converter = IntegerToRoman()
    print(converter.int_to_roman(1))  # I
    print(converter.int_to_roman(58))  # LVIII
    print(converter.int_to_roman(1994))  # MCMXCIV
def exercise14():
    class RomanToInteger:
        def __init__(self):
            self.roman_map = {
                'I': 1, 'V': 5, 'X': 10, 'L': 50,
                'C': 100, 'D': 500, 'M': 1000,
                'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900
            }

        def roman_to_int(self, roman):
            i = 0
            num = 0
            while i < len(roman):
                if i + 1 < len(roman) and roman[i:i + 2] in self.roman_map:
                    num += self.roman_map[roman[i:i + 2]]
                    i += 2
                else:
                    num += self.roman_map[roman[i]]
                    i += 1
            return num

    # Przykłady użycia
    converter = RomanToInteger()
    print(converter.roman_to_int("I"))  # 1
    print(converter.roman_to_int("LVIII"))  # 58
    print(converter.roman_to_int("MCMXCIV"))  # 1994
def exercise15():
    class ParenthesesValidator:
        def __init__(self):
            self.pair_map = {
                ')': '(',
                '}': '{',
                ']': '['
            }

        def is_valid(self, s):
            stack = []
            for char in s:
                if char in self.pair_map.values():
                    stack.append(char)
                elif char in self.pair_map.keys():
                    if stack == [] or stack.pop() != self.pair_map[char]:
                        return False
            return stack == []

    # Przykłady użycia
    validator = ParenthesesValidator()

    print(validator.is_valid("()"))  # True
    print(validator.is_valid("()[]{}"))  # True
    print(validator.is_valid("(]"))  # False
    print(validator.is_valid("([)]"))  # False
    print(validator.is_valid("{[]}"))  # True
def exercise16():
    class SubsetGenerator:
        def __init__(self, nums):
            self.nums = nums

        def get_subsets(self):
            result = []
            self._backtrack(result, [], 0)
            return result

        def _backtrack(self, result, current, start):
            result.append(list(current))
            for i in range(start, len(self.nums)):
                current.append(self.nums[i])
                self._backtrack(result, current, i + 1)
                current.pop()

    # Przykłady użycia
    generator = SubsetGenerator([4, 5, 6])
    subsets = generator.get_subsets()
    print(subsets)
def exercise17():
    class PairFinder:
        def __init__(self, numbers, target):
            self.numbers = numbers
            self.target = target

        def find_pair(self):
            num_to_index = {}
            for index, num in enumerate(self.numbers):
                complement = self.target - num
                if complement in num_to_index:
                    return (num_to_index[complement], index)
                num_to_index[num] = index
            return None

    # Przykłady użycia
    numbers = [10, 20, 10, 40, 50, 60, 70]
    target = 50
    finder = PairFinder(numbers, target)
    result = finder.find_pair()
    print(result)  # Output: (3, 4)
def exercise18():
    class ThreeSumZero:
        def __init__(self, numbers):
            self.numbers = numbers

        def find_triplets(self):
            self.numbers.sort()
            triplets = []
            n = len(self.numbers)

            for i in range(n - 2):
                if i > 0 and self.numbers[i] == self.numbers[i - 1]:
                    continue
                left, right = i + 1, n - 1
                while left < right:
                    current_sum = self.numbers[i] + self.numbers[left] + self.numbers[right]
                    if current_sum == 0:
                        triplets.append([self.numbers[i], self.numbers[left], self.numbers[right]])
                        while left < right and self.numbers[left] == self.numbers[left + 1]:
                            left += 1
                        while left < right and self.numbers[right] == self.numbers[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif current_sum < 0:
                        left += 1
                    else:
                        right -= 1
            return triplets

    # Przykłady użycia
    numbers = [-25, -10, -7, -3, 2, 4, 8, 10]
    finder = ThreeSumZero(numbers)
    result = finder.find_triplets()
    print(result)  # Output: [[-10, 2, 8], [-7, -3, 10]]
def exercise19():
    class Power:
        def __init__(self, x, n):
            self.x = x
            self.n = n

        def pow(self):
            return self._pow_recursive(self.x, self.n)

        def _pow_recursive(self, x, n):
            if n == 0:
                return 1
            if n < 0:
                return 1 / self._pow_recursive(x, -n)
            half = self._pow_recursive(x, n // 2)
            if n % 2 == 0:
                return half * half
            else:
                return half * half * x

    # Przykłady użycia
    p = Power(2, 10)
    print(p.pow())  # Output: 1024

    p = Power(2, -2)
    print(p.pow())  # Output: 0.25

    p = Power(2, 0)
    print(p.pow())  # Output: 1
def exercise20():
    class StringReverser:
        def __init__(self, s):
            self.s = s

        def reverse_words(self):
            words = self.s.split()
            reversed_words = words[::-1]
            return ' '.join(reversed_words)

    # Przykłady użycia
    reverser = StringReverser('hello .py')
    print(reverser.reverse_words())  # Output: '.py hello'
def exercise21():
    class StringManipulator:
        def __init__(self):
            self.string = ""

        def get_String(self):
            self.string = input("Enter a string: ")

        def print_String(self):
            print(self.string.upper())

    # Przykłady użycia
    manipulator = StringManipulator()
    manipulator.get_String()
    manipulator.print_String()
def exercise22():
    class Rectangle:
        def __init__(self, length, width):
            self.length = length
            self.width = width

        def area(self):
            return self.length * self.width

    # Przykłady użycia
    rect = Rectangle(10, 5)
    print(f"The area of the rectangle is: {rect.area()}")  # Output: The area of the rectangle is: 50
def exercise23():
    import math

    class Circle:
        def __init__(self, radius):
            self.radius = radius

        def area(self):
            return math.pi * self.radius ** 2

        def perimeter(self):
            return 2 * math.pi * self.radius

    # Przykłady użycia
    circle = Circle(5)
    print(f"The area of the circle is: {circle.area():.2f}")  # Output: The area of the circle is: 78.54
    print(f"The perimeter of the circle is: {circle.perimeter():.2f}")  # Output: The perimeter of the circle is: 31.42
def exercise24():
    class SampleClass:
        pass

    # Tworzenie instancji klasy
    instance = SampleClass()

    # Pobieranie nazwy klasy instancji
    class_name = type(instance).__name__
    print(f"The class name of the instance is: {class_name}")
def exercise25():
    class Employee:
        def __init__(self, emp_name, emp_id, emp_salary, emp_department):
            self.emp_name = emp_name
            self.emp_id = emp_id
            self.emp_salary = emp_salary
            self.emp_department = emp_department

        def emp_assign_department(self, new_department):
            self.emp_department = new_department

        def calculate_emp_salary(self, hours_worked):
            if hours_worked > 50:
                overtime = hours_worked - 50
                overtime_amount = overtime * (self.emp_salary / 50)
                total_salary = self.emp_salary + overtime_amount
            else:
                total_salary = self.emp_salary
            return total_salary

        def print_employee_details(self):
            print(f"Name: {self.emp_name}")
            print(f"ID: {self.emp_id}")
            print(f"Salary: {self.emp_salary}")
            print(f"Department: {self.emp_department}")

    # Przykłady użycia
    employee1 = Employee("ADAMS", "E7876", 50000, "ACCOUNTING")
    employee2 = Employee("JONES", "E7499", 45000, "RESEARCH")
    employee3 = Employee("MARTIN", "E7900", 50000, "SALES")
    employee4 = Employee("SMITH", "E7698", 55000, "OPERATIONS")

    # Przypisanie nowego działu
    employee1.emp_assign_department("FINANCE")

    # Obliczenie wynagrodzenia z nadgodzinami
    print(f"{employee1.emp_name}'s Total Salary: {employee1.calculate_emp_salary(60)}")

    # Wydrukowanie szczegółów pracownika
    employee1.print_employee_details()
def exercise26():
    class Restaurant:
        def __init__(self):
            self.menu_items = {}  # Słownik przechowujący pozycje menu
            self.booked_tables = {}  # Słownik przechowujący rezerwacje stolików
            self.customer_orders = {}  # Słownik przechowujący zamówienia klientów

        def add_item_to_menu(self, item_name, price):
            self.menu_items[item_name] = price
            print(f"Added {item_name} to menu with price ${price:.2f}")

        def book_table(self, customer_name, table_number):
            if table_number in self.booked_tables:
                print(f"Table {table_number} is already booked.")
            else:
                self.booked_tables[table_number] = customer_name
                print(f"Table {table_number} has been booked for {customer_name}.")

        def customer_order(self, table_number, order_list):
            if table_number not in self.booked_tables:
                print(f"Table {table_number} is not booked.")
                return

            if table_number not in self.customer_orders:
                self.customer_orders[table_number] = []
            self.customer_orders[table_number].extend(order_list)
            print(f"Added order for table {table_number}: {', '.join(order_list)}")

        def print_menu(self):
            print("\nMenu:")
            for item_name, price in self.menu_items.items():
                print(f"{item_name}: ${price:.2f}")

        def print_table_reservations(self):
            print("\nTable Reservations:")
            for table_number, customer_name in self.booked_tables.items():
                print(f"Table {table_number}: Reserved by {customer_name}")

        def print_customer_orders(self):
            print("\nCustomer Orders:")
            for table_number, orders in self.customer_orders.items():
                print(f"Table {table_number} Orders: {', '.join(orders)}")

    # Przykłady użycia
    restaurant = Restaurant()

    # Dodawanie pozycji do menu
    restaurant.add_item_to_menu("Pizza", 12.99)
    restaurant.add_item_to_menu("Pasta", 9.99)
    restaurant.add_item_to_menu("Salad", 5.99)

    # Rezerwacja stolików
    restaurant.book_table("Alice", 1)
    restaurant.book_table("Bob", 2)

    # Przyjmowanie zamówień klientów
    restaurant.customer_order(1, ["Pizza", "Salad"])
    restaurant.customer_order(2, ["Pasta"])

    # Drukowanie menu
    restaurant.print_menu()

    # Drukowanie rezerwacji stolików
    restaurant.print_table_reservations()

    # Drukowanie zamówień klientów
    restaurant.print_customer_orders()

def exercise27():
    class Inventory:
        def __init__(self):
            self.items = {}

        def add_item(self, item_id, item_name, stock_count, price):
            if item_id in self.items:
                print(f"Item with ID {item_id} already exists.")
            else:
                self.items[item_id] = {
                    'item_name': item_name,
                    'stock_count': stock_count,
                    'price': price
                }
                print(f"Item {item_name} added.")

        def update_item(self, item_id, item_name=None, stock_count=None, price=None):
            if item_id not in self.items:
                print(f"Item with ID {item_id} does not exist.")
            else:
                if item_name is not None:
                    self.items[item_id]['item_name'] = item_name
                if stock_count is not None:
                    self.items[item_id]['stock_count'] = stock_count
                if price is not None:
                    self.items[item_id]['price'] = price
                print(f"Item {item_id} updated.")

        def check_item_details(self, item_id):
            if item_id not in self.items:
                print(f"Item with ID {item_id} does not exist.")
            else:
                item = self.items[item_id]
                print(f"Item ID: {item_id}")
                print(f"Name: {item['item_name']}")
                print(f"Stock Count: {item['stock_count']}")
                print(f"Price: ${item['price']:.2f}")

    # Przykłady użycia
    inventory = Inventory()

    # Dodawanie przedmiotów
    inventory.add_item(1, "Laptop", 10, 999.99)
    inventory.add_item(2, "Mouse", 50, 19.99)

    # Aktualizacja przedmiotów
    inventory.update_item(1, stock_count=15)

    # Sprawdzanie szczegółów przedmiotów
    inventory.check_item_details(1)
    inventory.check_item_details(2)

    # Próba dodania przedmiotu z istniejącym item_id
    inventory.add_item(1, "Keyboard", 30, 49.99)

    # Próba aktualizacji nieistniejącego przedmiotu
    inventory.update_item(3, stock_count=20)
def exercise28():
    class BankAccount:
        def __init__(self, account_number, customer_name, date_of_opening, balance=0.0):
            self.account_number = account_number
            self.customer_name = customer_name
            self.date_of_opening = date_of_opening
            self.balance = balance

        def deposit(self, amount):
            if amount > 0:
                self.balance += amount
                print(f"Deposited {amount}. New balance is {self.balance}.")
            else:
                print("Deposit amount must be positive.")

        def withdraw(self, amount):
            if 0 < amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew {amount}. New balance is {self.balance}.")
            else:
                print("Insufficient funds or invalid amount.")

        def check_balance(self):
            print(f"Current balance is {self.balance}.")

    # Przykłady użycia
    account = BankAccount("123456789", "John Doe", "2023-01-01", 1000.0)

    # Sprawdzanie salda
    account.check_balance()

    # Wpłacanie środków
    account.deposit(500.0)

    # Wypłacanie środków
    account.withdraw(300.0)

    # Ponowne sprawdzanie salda
    account.check_balance()

def get_exercise_function(name):
    # Dictionary mapping exercise names to functions
    exercises = {
        'exercise1': exercise1,
        'exercise2': exercise2,
        'exercise3': exercise3,
        'exercise4': exercise4,
        'exercise5': exercise5,
        'exercise6': exercise6,
        'exercise7': exercise7,
        'exercise8': exercise8,
        'exercise9': exercise9,
        'exercise10': exercise10,
        'exercise11': exercise11,
        'exercise12': exercise12,
        'exercise13': exercise13,
        'exercise14': exercise14,
        'exercise15': exercise15,
        "exercise16": exercise16,
        "exercise17": exercise17,
        "exercise18": exercise18,
        "exercise19": exercise19,
        "exercise20": exercise20,
        "exercise21": exercise21,
        "exercise22": exercise22,
        "exercise23": exercise23,
        "exercise24": exercise24,
        "exercise25": exercise25,
        "exercise26": exercise26,
        "exercise27": exercise27,
        "exercise28": exercise28,
    }
    return exercises.get(name)


def main():
    while True:
        # Prompt for entering the exercise name
        exercise_name = input("Enter the exercise name (e.g., 'exercise1') or 'exit' to quit: ")
        if exercise_name == 'exit':
            break

        # Retrieve the function based on the name
        exercise_function = get_exercise_function(exercise_name)
        if exercise_function:
            result = exercise_function()
            print(result)
        else:
            print("No exercise found with that name.")

# This makes sure the script can be run directly, and main() will be executed
if __name__ == "__main__":
    main()