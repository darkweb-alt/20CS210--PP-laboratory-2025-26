# ===============================
# Exercise 2: Employee Payroll System
# ===============================

# Base class
class Employee:
    def __init__(self, name, emp_id):
        # Protected data members
        self._name = name
        self._emp_id = emp_id

    # Method to calculate salary (to be overridden)
    def calculate_salary(self):
        print("Salary calculation not defined for base Employee class.")

    # Method to display employee details
    def display_details(self):
        print(f"Employee Name: {self._name}")
        print(f"Employee ID: {self._emp_id}")


# Full-time employee subclass
class FullTimeEmployee(Employee):
    def __init__(self, name, emp_id, monthly_salary):
        super().__init__(name, emp_id)
        self.monthly_salary = monthly_salary

    # Overriding calculate_salary
    def calculate_salary(self):
        return self.monthly_salary


# Part-time employee subclass
class PartTimeEmployee(Employee):
    def __init__(self, name, emp_id, hours_worked, rate_per_hour):
        super().__init__(name, emp_id)
        self.hours_worked = hours_worked
        self.rate_per_hour = rate_per_hour

    # Overriding calculate_salary
    def calculate_salary(self):
        return self.hours_worked * self.rate_per_hour


# ===============================
# Testing Exercise 2 (Polymorphism)
# ===============================

employees = [
    FullTimeEmployee("Pitambar", 101, 50000),
    PartTimeEmployee("Manoj", 102, 120, 400)
]

for emp in employees:
    print("\n------------------------")
    emp.display_details()
    print("Employee Type:", emp.__class__.__name__)
    print("Calculated Salary: ₹", emp.calculate_salary())
