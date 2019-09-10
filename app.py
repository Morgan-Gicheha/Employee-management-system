
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# Adding a config

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:morgan8514@127.0.0.1:5432/ems'
app.config['SECRET_KEY'] = 'secret key'

db = SQLAlchemy(app)

# importing models
from models.department_model import Department
from models.employee_model import Employee
# creating tables for the database
@app.before_first_request
def create():
    db.create_all()


@app.route('/')
def home_page():

    return render_template('homepage.html')


@app.route("/employees", methods=['GET', 'POST'])
def employees():

     # fetching all departments available inthe department tables
    all_deps = Department.query.all()
    # print(type(all_deps))

    # fetchting all employees in the db
    all_employees = Employee.query.all()
    # print(type(all_employees))

    if request.method == 'POST':
        name = request.form['full_names']
        email = request.form['email']
        gender = request.form['gender']
        national_id_number = request.form['national_id_no']
        age = request.form['age']
        kra_pin = request.form['kra_pin']

        # sending info to the db
        # create an object of the Employee class
        if Employee.checking_employee(national_id_number):

            print(' employee exists')

            # returns you to ur previous stage.it takes the function name of the route
            return redirect(url_for('employees'))

            # calling function to check if kra exists.
        elif Employee.check_kra_exists(kra_pin):
            print('kra pin is used')
            return redirect(url_for('employees'))
        else:
            # this equates the  the columns where data will be inputed and values to be inputed
            emp = Employee(employee_name=name, employee_email=email,
                           employee_gender=gender, employee_national_id=national_id_number, employee_age=age, employee_KRA_PIN=kra_pin)
            # this calls the function fro the employee_models to commit te data to the db

            emp.create()
            print('imeingia')
            return redirect(url_for('employees'))

    return render_template('employees.html', depart=all_deps, all_emps=all_employees)


@app.route('/departments', methods=['GET', 'POST'])
def departments():

    # fetchting all departments
    all_dep = Department.query.all()

    if request.method == 'POST':
        department = request.form['department_name_entered']

        if Department.checker_department(department):

            print('dep exists')
            return redirect(url_for('departments'))
        else:
            dep = Department(department_name=department)
            dep.create()
            print('imeungia')
            return redirect(url_for('departments'))

    return render_template('departments.html', all_depart=all_dep)


# CREATING A ROUTE FOR EDITING THE DEPARTMENT
@app.route('/departments/edit/<int:id>', methods=['POST', 'GET'])
def update_department(id):
    if request.method == 'POST':
        name = request.form['updated_department']
        # print(name)

        update_depart = Department.update_by_id(id=id, department=name)

        if update_depart:
            print('updated')

        return redirect(url_for('departments'))

# CREATING A ROUTE TO EDIT EMPLOYEE DETAILS
@app.route('/employees/edit/<int:id>', methods=['POST', 'GET'])
def update_employee(id):
    if request.method == 'POST':
        name = request.form['updated_name']
        email = request.form['updated_email']
        kra = request.form['updated_kra']
# caling the method to update
        update_to_db = Employee.update_details(id=id, employee_name=name,email=email,kra=kra  )

        return redirect(url_for('employees'))


if __name__ == '__main__':
    app.run()