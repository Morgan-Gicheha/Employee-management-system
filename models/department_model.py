from app import db


class Department(db.Model):
    __tablename__ = 'departments_table'
    id=db.Column(db.Integer,primary_key=True)
    department_name=db.Column(db.String(20),nullable=False,unique=True)
    employee= db.relationship('Employee',backref='employee_')


# class Department(db.Model):
#     __tablename__ = 'departments_table'
#     id = db.Column(db.Integer,primary_key=True)
#     department_name = db.Column(db.String(20),unique= True,nullable =False)
#     employee = db.relationship('Employee',backref='department')
    

    # sending information to the database
    def create (self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def fetch_all(cls):
        return cls.query.all()

    # creating a method to check if department exists
    @classmethod
    def checker_department(cls,dep):
        checker_for_dp =cls.query.filter_by(department_name = dep).first()

        if checker_for_dp:
            return True
        else:
            return False

            

    # creating method to update department
    @classmethod
    def update_by_id(cls,id,department=None):
        record = cls.query.filter_by(id=id).first()
        
        if record:
            record.department_name = department
            db.session.commit()
            return True
        else:
            return False
# creating method to delete department
    @classmethod
    def deleting_department_by_id(cls,var_id):
        to_del_finder=cls.query.filter_by(id=var_id)
        if to_del_finder.first():
            to_del_finder.delete()
            db.session.commit()
            return True
        else:
            return False
   
#    fetching all departments by id '/departments/employees/ route

    @classmethod
    def fetching_department_by_id(cls,id):
        return cls.query.filter_by(id=id).first()



        
    