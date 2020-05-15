import datetime
from flask_mongoengine import MongoEngine
from AttendanceService.dbconfig import app
from mongoengine import *

db = MongoEngine(app)

class LeavePolicy(Document):
    name=StringField()
    no_days=IntField()
    created_at=DateTimeField()
    updated_at=DateTimeField()

    def to_json(self):
        return {
            "_id": str(self.pk),
            "Name": self.name,
            "Number of Days": self.no_days,
            "Created At": self.created_at,
            "Updated At": self.updated_at,
        }

class EmployeeLeave(Document):
    emp_id = ObjectIdField()
    leave_id=ReferenceField(LeavePolicy,dbref=True)
    leave_start=DateTimeField()
    leave_end=DateTimeField()
    remaining_leave=IntField()

    def to_json(self):
        return {
            "_id": str(self.pk),
            "Employee Id": str(self.emp_id),
            "Leave Id": self.leave_id,
            "Leave Start": self.leave_start,
            "Leave End": self.leave_end,
            "Remaining Leave": self.remaining_leave
        }

class EmployeeAttendance(Document):
    emp_id=ObjectIdField()
    workdays_month=IntField()
    actual_days_month=IntField()
    work_hours=IntField()
    paid_leave=IntField()
    permission_hours=IntField()

    def to_json(self):
        return {
            "_id": str(self.pk),
            "Employee Details Id": str(self.emp_id),
            "WorkDays in Month": self.workdays_month,
            "Actual Days in Month": self.actual_days_month,
            "Work Hours": self.work_hours,
            "Paid Leave": self.paid_leave,
            "Permission Hours": self.permission_hours
        }

class SalaryCalculation(Document):
    emp_id=ObjectIdField()
    emp_name=StringField()
    assigned_salary=DecimalField()
    deductions=DecimalField()
    incentives=DecimalField()
    no_of_leave=IntField()
    total_salary=DecimalField()
    salary_month=StringField()

    def to_json(self):
        return {
            "_id": str(self.pk),
            "Employee Id": str(self.emp_id),
            "Employee Name": self.emp_name,
            "Assigned Salary": self.assigned_salary,
            "Deductions": self.deductions,
            "Incentives": self.incentives,
            "Number of Leave": self.no_of_leave,
            "Total Salary": self.total_salary,
            "Salary Month": self.salary_month
        }

class EmployeeDeductions(Document):
    emp_id=ObjectIdField()
    emp_name=StringField()
    pf=DecimalField()
    esi=DecimalField()
    insurance=DecimalField()
    tax=DecimalField()

    def to_json(self):
        return {
            "_id": str(self.pk),
            "Employee Id": str(self.emp_id),
            "Employee Name": self.emp_name,
            "Provident Fund": self.pf,
            "ESI": self.esi,
            "Insurance": self.insurance,
            "Tax": self.tax
        }
    # def addfield(self):
    #     db.Document.update({},{$set: {"newattribute": attributevalue}}, false, true)


