# pip install Flask
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample employee data
employees = {
    1: {"ENAME": "Amal", "DNO": 10, "SALARY": 30000},
    2: {"ENAME": "Shyamal", "DNO": 30, "SALARY": 50000},
    3: {"ENAME": "Kamal", "DNO": 40, "SALARY": 10000},
    4: {"ENAME": "Nirmal", "DNO": 50, "SALARY": 60000},
    5: {"ENAME": "Bimal", "DNO": 20, "SALARY": 40000},
    6: {"ENAME": "Parimal", "DNO": 10, "SALARY": 20000}
}

@app.route('/api', methods=['GET'])
def get_employee_details():
    try:
        eno = int(request.args.get('ENO'))
        if eno in employees:
            return jsonify(employees[eno])
        else:
            return jsonify({"message": "Employee not found"}), 404
    except ValueError:
        return jsonify({"message": "Invalid ENO format"}), 400

if __name__ == '__main__':
    app.run(port=9000)

#To design an API in Python that returns the details of an employee based on their ENO, you can use the Flask framework. Here's a step-by-step implementation:

#First, make sure you have Flask installed. You can install it using pip.

#Create a Python script.

#Here's an explanation of the code:

#We import Flask to create a web application.
#Sample employee data is stored in the employees dictionary.
#We define a route /api for the API endpoint.
#In the get_employee_details function, we get the ENO from the request query parameters.
#We convert the ENO to an integer, handle exceptions for invalid values, and return the corresponding employee details if found.
#If the employee with the specified ENO is not found, we return a 404 response with a message.
#If the ENO is not provided in the correct format, we return a 400 response with a message.
#The server is set to run on port 9000.
#To run the API, execute the script employee_api.py. Make sure the Flask server is running on port 9000.

#You can use a tool like Postman to test the API by making GET requests to URLs like http://localhost:9000/api?ENO=1.

#This API will return the details of the employee whose ENO matches the provided value, handle exceptions, and ensure type safety for casting.