# importing the db from the app model
from app import db

# creating a class

class Employee(db.Model):
    __tablename__='employees_table'
    id= db.Column(db.Integer,primary_key=True)
    employee_name=db.Column(db.String(20),nullable=False)
    employee_email=db.Column(db.String(50),nullable=False)
    employee_phone_number=db.Column(db.Integer, nullable=False, unique=True)
    employee_gender = db.Column(db.String(50), nullable=False)
    employee_national_id = db.Column(db.Integer, nullable=False, unique=True)
    employee_age = db.Column(db.Integer, nullable=False)
    employee_KRA_PIN = db.Column(db.String(), nullable=False, unique=True)
    employee_salary = db.Column(db.Integer, nullable=False)
    employee_benefits = db.Column(db.Integer, nullable=False)
    department_id= db.Column(db.Integer,db.ForeignKey('departments_table.id'))




#     # creating function to commit to db

    def create(self):
        db.session.add(self)
        db.session.commit()

    # fetching all employee by id
    @classmethod
    def fetching_all_emps_by_id(cls,id):
        fetching_all_emps_by_id=cls.query.filter_by(id=id).first()
        if fetching_all_emps_by_id:
            return True
        else:
            return False

    # creating a function to check if employee already exists
    @classmethod
    def checking_employee(cls, id):
        checker = cls.query.filter_by(employee_national_id=id).first()

        if checker:
            return True
        else:
            return False

    @classmethod
    def check_kra_exists(cls, kra):
        check_kra = cls.query.filter_by(employee_KRA_PIN=kra).first()
        if check_kra:
            return True
        else:
            return False
# this is a method to update data already in the db
    @classmethod
    def update_details(cls, id, employee_name=None, email=None, kra=None, salary=None, benefits=None, age=None, gender=None, national_id=None,phone_number=None,update_department_id=None):
        record = cls.query.filter_by(id=id).first()

        if record:
            record.employee_name = employee_name
            record.employee_email = email
            record.employee_KRA_PIN = kra
            record.employee_salary = salary
            record.employee_benefits = benefits
            record.department_id=update_department_id
            record.employee_age = age
            record.employee_phone_number=phone_number
            record.employee_gender = gender
            record.employee_national_id = national_id
            db.session.commit()
            return True

        else:
            return False

# creating a function to delete record
    @classmethod
    def delete_employee(cls, var_id):
        searched_by_id = cls.query.filter_by(id=var_id)
        if searched_by_id.first():
            searched_by_id.delete()
            db.session.commit()
            return False
        else:
            return False
