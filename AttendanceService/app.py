import calendar
import datetime
import time
from flask import abort, request, jsonify
from AttendanceService.dbconfig import app, db
from AttendanceService.models import EmployeeAttendance, LeavePolicy, EmployeeLeave, SalaryCalculation, \
    EmployeeDeductions
from mongoengine.connection import get_db, connect


@app.route('/leavepolicy', methods=['POST'])
def create_leavepolicy():
    # Getting values
    empname = request.json['name']
    noofdays = request.json["noofdays"]

    # validates the received values.
    if empname and noofdays and request.method == 'POST':
        # query to insert the leave policy
        created_at = datetime.datetime.utcnow()
        updated = time.strftime("%x")
        leavepolicy = LeavePolicy.objects.create(name=empname, no_days=noofdays, created_at=created_at,
                                                 updated_at=updated)
        leavepolicy.save()
        return (jsonify({'message': 'Leave policy Created successfully'}))
    else:
        abort(400)  # missing arguments


@app.route('/update-leavepolicy/<id>', methods=['PUT'])
def update_leavepolicy(id):
    # Getting values
    empname = request.json['name']
    noofdays = request.json["noofdays"]

    # validate the received values
    if empname and noofdays and request.method == 'PUT':
        # save edits
        LeavePolicy.objects.filter(id=id).update(name=empname, no_days=noofdays, updated_at=datetime.datetime.utcnow())
        resp = jsonify('Leave Policy updated successfully!')
        return resp


@app.route('/leavepolicy/<id>', methods=['GET'])
def getleavepolicy(id):
    # query to select one employee attendance for the employee d
    user = LeavePolicy.objects.get(id=id)
    return user.to_json()


@app.route('/leavepolicylist', methods=['GET'])
def leave_policy_list():
    # query to select all values from database
    resp = LeavePolicy.objects.all()
    result = []
    for u in resp:
        result.append(u.to_json())
    return jsonify({'Leave Policy List': result})


@app.route('/employeeleave', methods=['POST'])
def create_employeeleave():
    # Getting values
    emp_id = request.json['empid']
    leave_id = request.json['leaveid']
    leave_start = request.json['leavestart']
    leave_end = request.json['leaveend']
    remaining_leave = request.json['remainingleave']

    # validates the received values.
    if emp_id and leave_id and leave_start and leave_end and remaining_leave and request.method == 'POST':
        # query to insert into employee leave
        emp_leave = EmployeeLeave.objects.create(emp_id=emp_id, leave_id=leave_id, leave_start=leave_start,
                                                 leave_end=leave_end, remaining_leave=remaining_leave)
        emp_leave.save()
        return (jsonify({'message': 'Employee Leave policy Created successfully'}))
    else:
        abort(400)  # missing arguments


@app.route('/update-employeeleave/<id>', methods=['PUT'])
def update_employeeleave(id):
    # Getting values
    leave_id = request.json['leaveid']
    leave_start = request.json['leavestart']
    leave_end = request.json['leaveend']
    remaining_leave = request.json['remainingleave']

    leave = LeavePolicy.objects.filter(id=leave_id).first()
    # validate the received values
    if leave_id and leave_start and leave_end and remaining_leave and request.method == 'PUT':
        # save edits
        EmployeeLeave.objects.filter(emp_id=id).update(leave_id=leave.to_dbref(), leave_start=leave_start,
                                                       leave_end=leave_end, remaining_leave=remaining_leave)
        resp = jsonify('Employee Leave updated successfully!')
        return resp


@app.route('/employeeleave/<id>', methods=['GET'])
def getemployeeleave(id):
    # query to select one employee leave list from table
    user = EmployeeLeave.objects.get(emp_id=id)
    return user.to_json()


@app.route('/employeeleavelist', methods=['GET'])
def employee_leave_list():
    # query to select all values from database
    resp = EmployeeLeave.objects.all()
    result = []
    for u in resp:
        result.append(u.to_json())
    return jsonify({'Leave Policy List': result})


@app.route('/salary-calculation', methods=['POST'])
def create_salarycalculation():
    # Getting values
    emp_id = request.json['empid']
    emp_name = request.json["empname"]
    assigned_salary = request.json["assignedsalary"]
    deductions = request.json["deductions"]
    incentives = request.json['incentives']
    no_of_leave = request.json['noofleave']
    # validates the received values.
    if emp_id and emp_name and assigned_salary and deductions and incentives and no_of_leave and request.method == 'POST':
        # Get the today date
        today = str(datetime.date.today())
        # Get Year from the date
        curr_year = int(today[:4])
        # Get month from the date
        curr_month = int(today[5:7])
        month = calendar.month_name[curr_month]
        # Get the no of days from the current month.calendar.monthrange() this returns a tuple.
        # the first item in the tuple is the weekday that
        # the month starts on and the second item is the
        # number of days in the month.select the second item in the tuple only
        # i.e. the number of days in the month
        noofdays = calendar.monthrange(curr_year, curr_month)[1]
        oneday_salary = int(assigned_salary) / (noofdays)
        leave_amt = int(no_of_leave) * oneday_salary
        reduction = int(deductions) + leave_amt
        total_salary = int(assigned_salary) + int(incentives) - (reduction)
        round_salary = round(total_salary)
        salary_month = month
        # query to insert values into salary calculation table
        salary_calc = SalaryCalculation.objects.create(emp_id=emp_id, emp_name=emp_name,
                                                       assigned_salary=assigned_salary,
                                                       deductions=deductions, incentives=incentives,
                                                       no_of_leave=no_of_leave, total_salary=round_salary,
                                                       salary_month=salary_month)

        salary_calc.save()
        return (jsonify({'Current Month': salary_month, 'salary': round_salary},
                        {'message': 'Salary Calculation Created successfully'}))

    else:
        abort(400)  # missing arguments


@app.route('/update-salarycalculation/<id>', methods=['PUT'])
def update_salarycalculation(id):
    # Getting values
    emp_name = request.json["empname"]
    assigned_salary = request.json["assignedsalary"]
    deductions = request.json["deductions"]
    incentives = request.json['incentives']
    no_of_leave = request.json['noofleave']

    # validate the received values
    if emp_name and assigned_salary and deductions and incentives and no_of_leave and request.method == 'PUT':
        # Get the today date
        today = str(datetime.date.today())
        # Get Year from the date
        curr_year = int(today[:4])
        # Get month from the date
        curr_month = int(today[5:7])
        month = calendar.month_name[curr_month]
        # Get the no of days from the current month.calendar.monthrange() this returns a tuple.
        # the first item in the tuple is the weekday that
        # the month starts on and the second item is the
        # number of days in the month.select the second item in the tuple only
        # i.e. the number of days in the month
        noofdays = calendar.monthrange(curr_year, curr_month)[1]
        oneday_salary = int(assigned_salary) / noofdays
        leave_amt = int(no_of_leave) * oneday_salary
        reduction = int(deductions) + leave_amt
        total_salary = int(assigned_salary) + int(incentives) - (reduction)
        total_salary1 = round(total_salary)
        salary_month = month
        # save edits
        SalaryCalculation.objects.filter(emp_id=id).update(emp_name=emp_name, assigned_salary=assigned_salary,
                                                           deductions=deductions, incentives=incentives,
                                                           no_of_leave=no_of_leave, total_salary=total_salary1,
                                                           salary_month=salary_month)
        resp = jsonify({'Current Month': salary_month, 'salary': total_salary1},
                       {'message': 'Salary Calculation updated successfully!'})
        return resp


@app.route('/salarycalculation/<id>', methods=['GET'])
def getemployeesalary(id):
    # query to select one employee attendance for the employee id
    user = SalaryCalculation.objects.get(emp_id=id)
    return user.to_json()


@app.route('/allsalary', methods=['GET'])
def all_employees_salarycalculation_list():
    # query to select all values from database
    resp = SalaryCalculation.objects.all()
    result = []
    for u in resp:
        result.append(u.to_json())
    return jsonify({'Salary Details': result})


@app.route('/employee-deductions', methods=['POST'])
def create_employeedeductions():
    # Getting values
    emp_id = request.json['empid']
    emp_name = request.json["empname"]
    pf = request.json["pf"]
    esi = request.json["esi"]
    insurance = request.json['insurance']
    tax = request.json['tax']

    # validates the received values.
    if emp_id and pf and emp_name and esi and insurance and tax and request.method == 'POST':
        # query to insert the employee deduction details
        emp_deductions = EmployeeDeductions.objects.create(emp_id=emp_id, emp_name=emp_name, pf=pf,
                                                           esi=esi, insurance=insurance, tax=tax)

        emp_deductions.save()
        return (jsonify({'message': 'Employee Deduction Created successfully'}))

    else:
        abort(400)  # missing arguments


@app.route('/addfield', methods=['POST'])
def addingnewfield():
    newattribute = request.json['newattribute']
    attributevalue = request.json['attributevalue']

    db = get_db()
    print("Database name: ", db.name)

    db.employee_deductions.update(
        {},
        {
            '$set': {
                newattribute: attributevalue
            }
        }, False, True
    )
    return jsonify({"message": "New field added to the Employee Deduction Document"})


@app.route('/update-employeedeductions/<id>', methods=['PUT'])
def update_employeedeductions(id):
    # Getting values
    emp_name = request.json["empname"]
    pf = request.json["pf"]
    esi = request.json["esi"]
    insurance = request.json['insurance']
    tax = request.json['tax']
    # validate the received values
    if pf and emp_name and esi and insurance and tax and request.method == 'PUT':
        # save edits
        EmployeeDeductions.objects.filter(emp_id=id).update(emp_name=emp_name, pf=pf,
                                                            esi=esi, insurance=insurance, tax=tax)
        resp = jsonify('Employee Deduction updated successfully!')
        return resp


@app.route('/employeededuction/<id>', methods=['GET'])
def getemployeededuction(id):
    # query to select one employee deductions for the employee id
    user = EmployeeDeductions.objects.get(emp_id=id)
    return user.to_json()


@app.route('/alldeductions', methods=['GET'])
def all_employees_deductions_list():
    # query to select all values from database
    resp = EmployeeDeductions.objects.all()
    result = []
    for u in resp:
        result.append(u.to_json())
    return jsonify({'Deductions Details': result})


@app.route('/employee-attendance', methods=['POST'])
def create_employeeattendance():
    # Getting values
    empdetails_id = request.json['empdetails_id']
    workdays = request.json["workdays"]
    actualdays = request.json["actualdays"]
    work_hours = request.json["work_hours"]
    paid_leave = request.json['paid_leave']
    permissions = request.json['permissions']

    # validates the received values.
    if empdetails_id and workdays and actualdays and work_hours and paid_leave and permissions and request.method == 'POST':
        # query to insert the employee attendance details
        emp_attendance = EmployeeAttendance.objects.create(emp_id=empdetails_id, workdays_month=workdays,
                                                           actual_days_month=actualdays,
                                                           work_hours=work_hours, paid_leave=paid_leave,
                                                           permission_hours=permissions)

        emp_attendance.save()
        return (jsonify({'message': 'Employee Attendance Created successfully'}))

    else:
        abort(400)  # missing arguments


@app.route('/update-employeattendance/<id>', methods=['PUT'])
def update_employeeattendance(id):
    # Getting values
    workdays = request.json["workdays"]
    actualdays = request.json["actualdays"]
    work_hours = request.json["work_hours"]
    paid_leave = request.json['paid_leave']
    permissions = request.json['permissions']
    # validate the received values
    if workdays and actualdays and work_hours and paid_leave and permissions and request.method == 'PUT':
        # save edits
        EmployeeAttendance.objects.filter(emp_id=id).update(workdays_month=workdays, actual_days_month=actualdays,
                                                            work_hours=work_hours, paid_leave=paid_leave,
                                                            permission_hours=permissions)
        resp = jsonify('Employee Attendance updated successfully!')
        return resp


@app.route('/employeeattendance/<id>', methods=['GET'])
def getemployeeattendance(id):
    # query to select one employee attendance for the employee d
    user = EmployeeAttendance.objects.get(emp_id=id)
    return user.to_json()


@app.route('/allemployeesattendance', methods=['GET'])
def all_employees_attendance_list():
    # query to select all values from database
    resp = EmployeeAttendance.objects.all()
    result = []
    for u in resp:
        result.append(u.to_json())
    return jsonify({'Employee Details': result})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004, debug=True)
