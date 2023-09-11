# Departments database (DNO, DNAME)
departments = {
    10: "Admin",
    20: "Accounts",
    30: "Sales",
    40: "Marketing",
    50: "Purchasing"
}

# Employees database (ENO, ENAME, DNO, SALARY)
employees = {
    1: {"ENAME": "Amal", "DNO": 10, "SALARY": 30000},
    2: {"ENAME": "Bob", "DNO": 20, "SALARY": 35000},
    3: {"ENAME": "Charlie", "DNO": 30, "SALARY": 40000},
    4: {"ENAME": "David", "DNO": 40, "SALARY": 45000},
    5: {"ENAME": "Eva", "DNO": 50, "SALARY": 50000}
}

# Function to query and display departments
def query_departments():
    print("Departments (DNO, DNAME):")
    for dno, dname in departments.items():
        print(f"{dno}: {dname}")

# Function to query and display employees
def query_employees():
    print("\nEmployees (ENO, ENAME, DNO, SALARY):")
    for eno, data in employees.items():
        print(f"{eno}: {data['ENAME']}, {data['DNO']}, {data['SALARY']}")

# Query and display the databases
query_departments()
query_employees()
