from app import db

class Department(db.Model):
    __tablename__ = 'departments_table'
    id = db.Column(db.Integer,primary_key=True)
    department_name = db.Column(db.String(20),unique= True,nullable =False)
    employee = db.relationship('Employee', backref='employees_table', lazy =True)

    # sending information to the database
    def create (self):
        db.session.add(self)
        db.session.commit()
    
    
    # creating a function to check if department exists
    @classmethod
    def checker_department(cls,dep):
        checker_for_dp =cls.query.filter_by(department_name = dep).first()

        if checker_for_dp:
            return True
        else:
            return False