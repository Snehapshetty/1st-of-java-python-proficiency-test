# Define the Departments and Employees databases as dictionaries
departments = {
    10: "Admin",
    20: "Accounts",
    30: "Sales",
    40: "Marketing",
    50: "Purchasing",
}

employees = {
    1: {"ENAME": "Amal", "DNO": 10, "SALARY": 30000},
}

# Function to query the Departments database
def query_departments():
    print("Departments (DNO, DNAME):")
    for dno, dname in departments.items():
        print(f"{dno}: {dname}")

# Function to query the Employees database
def query_employees():
    print("\nEmployees (ENO, ENAME, DNO, SALARY):")
    for eno, data in employees.items():
        print(f"{eno}: {data['ENAME']}, {data['DNO']}, {data['SALARY']}")

# Query and display the databases
query_departments()
query_employees()
