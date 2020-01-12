from app import db
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
    month= db.Column(db.String(),nullable=False)
    employee_id= db.Column(db.Integer , db.ForeignKey('employees_table.id'))

    # method to commit to db
    def create(self):
        db.session.add(self)
        db.session.commit()

    
    


