

from flask import Flask, render_template, request, redirect, url_for,flash
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# Adding a config

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:morgan8514@127.0.0.1:5432/ems'
app.config['SECRET_KEY'] = 'secret key'

db = SQLAlchemy(app)

# importing models
from models.payroll_model import Payroll
from models.payroll_class import Payroll_C
from models.employee_model import Employee
from models.department_model import Department

# creating tables for the database
@app.before_first_request
def create():
    db.create_all()

@app.route('/login',methods=['GET','POST'])
def login():

     return render_template('login.html')


@app.route('/')
def home_page():

    return render_template('homepage.html')


@app.route("/employees", methods=['GET', 'POST'])
def employees():

     # fetching all departments available inthe department tables
    all_deps = Department.query.all()
    # print(type(all_deps))
    # for any in all_deps:
    #     print(any.department_name)

    # fetchting all employees in the db
    all_employees = Employee.query.all()
    # print(type(all_employees))
    # for employee in all_employees:
    #     print(employee.employee_name)
    if request.method == 'POST':
        name = request.form['full_names']
        email = request.form['email']
        gender = request.form['gender']
        phone_number=request.form['phone_number']
        national_id_number = request.form['national_id_no']
        age = request.form['age']
        kra_pin = request.form['kra_pin']
        dep_id = request.form['dep_id']
        salary = request.form['entered_salary']
        benefits = request.form['entered_benefits']
        

        # sending info to the db
        # create an object of the Employee class
        print(name)
        if Employee.checking_employee(national_id_number):

            print(' employee exists')
            flash('Employee exists.Similar nationall id number exists','warning')

            # returns you to ur previous stage.it takes the function name of the route
            return redirect(url_for('employees'))

            # calling function to check if kra exists.
        elif Employee.check_kra_exists(kra_pin):
            print('kra pin is used')
            flash(' Cannot create employee! KRA PIN exists in this system','warning')
            return redirect(url_for('employees'))
        else:
            # this equates the  the columns where data will be inputed and values to be inputed
            emp = Employee(employee_name=name, employee_email=email,
                           employee_gender=gender, employee_national_id=national_id_number, employee_age=age, employee_KRA_PIN=kra_pin, department_id=dep_id,employee_salary=salary,employee_benefits=benefits,employee_phone_number=phone_number)
            # this calls the function fro the employee_models to commit te data to the db

            emp.create()
            print('imeingia')
            flash('Successfully created','info')
            return redirect(url_for('employees'))

    return render_template('employees.html', depart=all_deps, all_emps=all_employees)


@app.route('/departments', methods=['GET', 'POST'])
def departments():

    # fetchting all departments
    all_dep = Department.fetch_all()

    if request.method == 'POST':
        department = request.form['department_name_entered']
        

        if Department.checker_department(department):

            print('dep exists')
            flash('Department alredy exists','warning')
            return redirect(url_for('departments'))
        else:
            dep = Department(department_name=department)
            dep.create()
            print('imeungia')
            flash('Success! Department created','info')
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
            flash('Update succesfull','info')

        return redirect(url_for('departments'))

# CREATING A ROUTE TO EDIT EMPLOYEE DETAILS
@app.route('/employees/edit/<int:id>', methods=['POST', 'GET'])
def update_employee(id):
    if request.method=='POST':
        full_names= request.form['full_names']
        email=request.form['email']
        national_id_no=request.form['national_id_no']
        phone_number=request.form['phone_number']
        gender=request.form['gender']
        age=request.form['age']
        kra_pin=request.form['kra_pin']
        update_salary=request.form['update_salary']
        update_benefits=request.form['update_benefits']
        dep_id=request.form['dep_id']

        try:
    
            updates = Employee.update_details(id=id,employee_name=full_names,email=email,kra=kra_pin,salary=update_salary,benefits=update_benefits,age=age,gender=gender,national_id=national_id_no,phone_number=phone_number,update_department_id=dep_id)
            flash(f'updates on employee named {full_names} done succesfully','info')
            return redirect(url_for('employees'))
        except Exception:
            flash('un error occured .plz retry','danger')
            return redirect(url_for('employees'))




# 
# work
# on this

# creating a deleting route
@app.route('/employees/delete/<int:id>', methods=['POST', 'GET'])
def delete_employee(id):
    # print('my delete id is',id)
    # calling function to delete the employee
    deleted_employee_of_id = Employee.delete_employee(id)
    flash('Employee DELETED')

    return redirect(url_for('employees'))

# creating a route to delete department
@app.route('/departments/delete/<int:id>', methods=['POST', 'GET'])
def delete_department_by_id(id):

    # print("delete id",id, " recieved")
    # calling method to delete from the departments model
    try:
        recieved_delete_content = Department.deleting_department_by_id(id)
    except Exception:
        flash('cannot delete department because it has employees','warning')

    return redirect(url_for('departments'))


# creating route to view  employees in a department
@app.route('/department/employees/<int:id>', methods=['POST', 'GET'])
def geting_employees_in_deps(id):

    deprt = Department.fetching_department_by_id(id)
        # fetchting all employees in the db
    all_employees = Employee.query.all()
    # print(all_employees)
    
    emp = deprt.employee
    # print(type(emp))
    # go to the templete and use the emp. which is all deps and employees linked together

    return render_template('view_emps_in_dps.html', sekta=deprt,all_employees=all_employees,emp=emp)


if __name__ == '__main__':
    app.run(debug=True)
