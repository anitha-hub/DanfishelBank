from flask_mongoengine import MongoEngine
from EmployeeService.dbconfig import app
from mongoengine import *

db = MongoEngine(app)

class TransactionLimit(Document):
    condition_name=StringField()
    condition_one=ListField(StringField())
    condition_two=ListField(StringField())
    #created_by=ReferenceField(EmployeeDetails)

    def to_json(self):
        return {
            "_id": str(self.pk),
            "Condition Name": self.condition_name,
            "Condition One": self.condition_one,
            "Condition Two": self.condition_two
        }

class EmployeeRole(Document):
    role_name=StringField()
    can_create=BooleanField()
    can_edit=BooleanField()
    can_delete=BooleanField()
    restrict_login_count=IntField()
    can_access_service_id=ListField(IntField())
    transaction_limit_id=ReferenceField(TransactionLimit,dbref=True)

    def to_json(self):
        return {
            "_id": str(self.pk),
            "Role Name": self.role_name,
            "Create": self.can_create,
            "Edit": self.can_edit,
            "Delete": self.can_delete,
            "Login Count": self.restrict_login_count,
            "Service Id": self.can_access_service_id,
            "Transaction Limit Id": self.transaction_limit_id
        }

class EmployeeDetails(Document):
    branch_id = StringField()   #Reference field to branchService
    first_name=StringField()
    last_name=StringField()
    email=StringField()
    address=StringField()
    title=StringField()
    employee_id=StringField()
    dob=DateField()
    designation=StringField()
    mobile_one=IntField()
    mobile_two=IntField()
    localization_id=IntField()  #ReferenceField to location model
    is_active=BooleanField()
    emp_role_id=ReferenceField(EmployeeRole)

    def to_json(self):
        return {
            "_id": str(self.pk),
            "Branch Id": self.branch_id,
            "First Name": self.first_name,
            "Last Name": self.last_name,
            "Email1": self.email,
            "Address": self.address,
            "Title": self.title,
            "EmployeeId": self.employee_id,
            "Date of Birth": self.dob,
            "Designation": self.designation,
            "Phone Number": self.mobile_one,
            "Mobile Number": self.mobile_two,
            "Localization Id": self.localization_id,
            "Employee Role Id": self.emp_role_id,
            "Status": self.is_active
        }

class EmployeeAuth(Document):
    username=StringField()
    password=StringField()
    token=StringField()
    public_id = StringField()
    emp_details_id=ReferenceField(EmployeeDetails)
    is_two_factor=BooleanField()

class EmployeeLogs(Document):
    emp_auth_id=ReferenceField(EmployeeAuth,dbref=True)
    last_login=DateTimeField()
    failed_login=BooleanField()
    login_time=DateTimeField()
    logoff_time = DateTimeField()
    total_attempts=IntField()
    err_log=StringField()

class EmployeeAttendance(Document):
    emp_details_id=ReferenceField(EmployeeDetails)
    workdays_month=IntField()
    actual_days_month=IntField()
    work_hours=IntField()
    paid_leave=IntField()
    permissions=IntField()

    def to_json(self):
        return {
            "_id": str(self.pk),
            "Employee Details Id": self.emp_details_id,
            "WorkDays in Month": self.workdays_month,
            "Actual Days in Month": self.actual_days_month,
            "Work Hours": self.work_hours,
            "Paid Leave": self.paid_leave,
            "Permissions": self.permissions
        }



# disconnect(alias='branchservicedb')