# importing the db from the app model
from app import db

# creating a class
class Employee(db.Model):
    __tablename__ = 'employees_table'
    id = db.Column(db.Integer, primary_key=True)
    employee_name = db.Column(db.String(20),nullable=False)
    employee_email = db.Column(db.String(70),nullable=True)
    employee_gender = db.Column(db.String(10),nullable=False)
    employee_national_id = db.Column(db.Integer,nullable=False , unique= True)
    employee_age = db.Column(db.Integer,nullable=False)
    employee_KRA_PIN = db.Column(db.String(),nullable=False,unique=True)
    department_id = db.Column(db.Integer, db.ForeignKey('departments_table.id'))


    # creating function to commit to db
    def create(self):
        db.session.add(self)
        db.session.commit()

    # creating a function to check if employee already exists
    @classmethod
    def checking_employee(cls,id):
        checker= cls.query.filter_by(employee_national_id=id).first()

        if checker :
            return True
        else:
            return False


    @classmethod
    def check_kra_exists(cls,kra):
        check_kra = cls.query.filter_by(employee_KRA_PIN =kra).first()
        if check_kra :
            return True
        else:
            return False
# this is a method to update data already in the db
    @classmethod
    def update_details(cls,id, employee_name=None, email=None, kra=None):
        record = cls.query.filter_by(id=id).first()
        
        if record:
            record.employee_name=employee_name
            record.employee_email = email
            record.employee_KRA_PIN=kra
            db.session.commit()
            return True

        else:
            return False







