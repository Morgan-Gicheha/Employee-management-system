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
    
    
    # creating a method to check if department exists
    @classmethod
    def checker_department(cls,dep):
        checker_for_dp =cls.query.filter_by(department_name = dep).first()

        if checker_for_dp:
            return True
        else:
            return False

    # creating method
    @classmethod
    def update_by_id(cls,id,department=None):
        record = cls.query.filter_by(id=id).first()
        
        if record:
            record.department_name = department
            db.session.commit()
            return True
        else:
            return False
   
    