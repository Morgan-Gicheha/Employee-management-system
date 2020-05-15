from main import db
# creating tables using orm
class Payroll(db.Model):
    __tablename__='payrolls_table'
    id=db.Column(db.Integer,primary_key=True)
    basic_salary = db.Column(db.Integer,nullable=False)
    benefits = db.Column(db.Integer,nullable=False)
    gross_salary = db.Column(db.Integer,nullable=False)
    taxable_income = db.Column(db.Integer,nullable=False)
    nssf_contribution = db.Column(db.Integer,nullable=False)
    nhif_contribution = db.Column(db.Integer,nullable=False)
    payee = db.Column(db.Integer,nullable=False)
    
    total_tax_payable = db.Column(db.Integer,nullable=False)
    net_salary = db.Column(db.Integer,nullable=False)
    month= db.Column(db.String(),nullable=False,unique=False)
    employee_id= db.Column(db.Integer , db.ForeignKey('employees_table.id'))

    # method to commit to db
    def create(self):
        db.session.add(self)
        db.session.commit()


    # fetching payroll with employee id
    @classmethod
    def fetch_payroll_employee_id(cls,employee_id):
        fetch_payroll_employee_id=cls.query.filter_by(employee_id=employee_id).all()
        return fetch_payroll_employee_id

    # deleting a payroll
    @classmethod
    def deleting_payroll(cls,id):
        payroll_id=cls.query.filter_by(id=id)
        if payroll_id.first():
            payroll_id.delete()
            db.session.commit()
            return True
        else:
            return False



    
    


