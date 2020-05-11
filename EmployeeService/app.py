import datetime
import time
from flask import abort, request, jsonify, make_response, session
from EmployeeService.dbconfig import app
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
import jwt
from EmployeeService.models import EmployeeDetails, TransactionLimit, EmployeeRole, EmployeeAttendance, EmployeeAuth, \
    EmployeeLogs


def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None

        if 'X-Access-Token' in request.headers:
            token = request.headers['X-Access-Token']
        if not token:
            return jsonify({'message': 'a valid token is missing'})

        data=jwt.decode(token, app.config['SECRET_KEY'])
        current_user = EmployeeDetails.objects.filter(public_id=data['public_id']).first()
        return f(current_user, *args, **kwargs)

    return decorator


@app.route('/transaction-limit', methods=['POST'])
def create_transactionlimit():
    #Getting values
    condition_name=request.json['conditionname']
    condition_one = request.json["conditionone"]
    condition_two = request.json["conditiontwo"]
    #validates the received values.
    if condition_name and condition_one and condition_two and request.method == 'POST':
            #query to insert the Transaction limits table
            translimit = TransactionLimit.objects.create(condition_name=condition_name,condition_one=condition_one,condition_two=condition_two)
            translimit.save()
            return (jsonify({'ConditionName': condition_name, 'ConditionOne': condition_one, 'ConditionTwo': condition_two},{'message': 'Transaction Limit Saved successfully'}))
    else:
        abort(400)  # missing arguments

@app.route('/update-transaction-limit/<id>', methods=['PUT'])
def update_transactionlimit(id):
    # Getting values
    condition_name = request.json['conditionname']
    condition_one = request.json["conditionone"]
    condition_two = request.json["conditiontwo"]
    # validate the received values
    if condition_name and condition_one and condition_two and request.method == 'PUT':
        # save edits
        TransactionLimit.objects.filter(id=id).update( condition_name=condition_name,condition_one=condition_one,condition_two=condition_two)
        resp = jsonify('TransactionLimit updated successfully!')
        return resp

@app.route('/transaction-limit/<id>', methods=['GET'])
def gettransactionlimit(id):
    # query to select one transaction limit for the id
    user = TransactionLimit.objects.get(id=id)
    return user.to_json()

@app.route('/alltransactionlimits', methods=['GET'])
def all_transactionlimits_list():
    # query to select all values from database
    resp = TransactionLimit.objects.all()
    result = []
    for u in resp:
        result.append(u.to_json())
    return jsonify({'Transaction Limits': result})

@app.route('/employee-role', methods=['POST'])
def create_employeerole():
    #Getting values
    rolename = request.json["rolename"]
    create = request.json["create"]
    edit = request.json["edit"]
    delete = request.json['delete']
    restrict_login_count = request.json['restrict_logincount']
    can_access_service_id = request.json['access_service_id']
    transaction_limit_id = request.json['transaction_limit_id']

    #validates the received values.
    if rolename and create and edit and edit and restrict_login_count and can_access_service_id and transaction_limit_id and request.method == 'POST':
            #query to insert the Employee Role Table
            emp_role = EmployeeRole.objects.create(role_name=rolename,can_create=create,can_edit=edit,can_delete=delete,
                                                   restrict_login_count=restrict_login_count,can_access_service_id=can_access_service_id,
                                                   transaction_limit_id=transaction_limit_id)
            emp_role.save()
            return (jsonify({'RoleName': rolename, 'Create': create, 'Edit': edit,'Delete':delete,'Restrict login count':restrict_login_count,'Service Id':can_access_service_id,'Transaction Limit Id':transaction_limit_id},{'message': 'Employee Role Created successfully'}))

    else:
        abort(400)  # missing arguments

@app.route('/update-employeerole/<id>', methods=['PUT'])
def update_employeerole(id):
    # Getting values
    rolename = request.json["rolename"]
    create = request.json["create"]
    edit = request.json["edit"]
    delete = request.json['delete']
    restrict_login_count = request.json['restrict_logincount']
    can_access_service_id = request.json['access_service_id']
    # validate the received values
    if rolename and create and edit and edit and restrict_login_count and can_access_service_id  and request.method == 'PUT':
        # save edits
        EmployeeRole.objects.filter(id=id).update(role_name=rolename,can_create=create,can_edit=edit,can_delete=delete,
                                                   restrict_login_count=restrict_login_count,can_access_service_id=can_access_service_id
                                                   )
        resp = jsonify('Employee Role updated successfully!')
        return resp

@app.route('/allemployee_roles', methods=['GET'])
def all_employeerole_list():
    # query to select all values from database
    resp = EmployeeRole.objects.all()
    result = []
    for u in resp:
        result.append(u.to_json())
    return jsonify({'Employee Roles': result})

@app.route('/employee-register', methods=['POST'])
def create_employeedetails():
    #Getting values
    branch_id=request.json['branchid']
    firstname = request.json["firstname"]
    lastname = request.json["lastname"]
    title = request.json["title"]
    address = request.json['address']
    email = request.json['email']
    employeeId = request.json['employeeId']
    dob = request.json['dob']
    mobile1 = request.json['mobileno1']
    mobile2 = request.json['mobileno2']
    designation=request.json['designation']
    localizationid = request.json['localizationid']
    emproleid = request.json['emproleid']
    status = request.json['status']

    #validates the received values.
    if branch_id and firstname and lastname and title and address and email and employeeId and \
            dob and mobile1 and mobile2 and designation and localizationid and emproleid and status and request.method == 'POST':
            #query to insert the employee details
            employee = EmployeeDetails.objects.create(branch_id=branch_id,first_name=firstname,last_name=lastname,title=title, address=address, email=email,
                                              employee_id=employeeId,dob=dob, mobile_one=mobile1, mobile_two=mobile2,designation=designation,
                                                      localization_id=localizationid,emp_role_id=emproleid,is_active=status)
            employee.save()
            empid=employee.id
            username=firstname[0:3] + str(00)
            password='welcome'
            hashed_password = generate_password_hash(password, method='sha256')
            is_two_factor=0
            #query to insert the employee auth table
            emp_auth=EmployeeAuth.objects.create(username=username,password=hashed_password,emp_details_id=empid,is_two_factor=is_two_factor,token='',public_id=str(uuid.uuid4()))
            emp_auth.save()
            return (jsonify({'Branch Id':branch_id,'Firstname':firstname,'Lastname':lastname,'Title':title,'Address':address,
                             'Email':email,'Employee Id':employeeId,'Date of Birth':dob,'Mobile NumberOne':mobile1,'Mobile Number Two':mobile2,'Designation':designation,
                             'Localization Id':localizationid,'Employee Role Id':emproleid},{'message': 'Employee Details registered successfully'}))

    else:
        abort(400)  # missing arguments

@app.route('/update-employedetails/<id>', methods=['PUT'])
def update_employeedetails(id):
    # Getting values
    title = request.json["title"]
    address = request.json['address']
    email = request.json['email']
    mobile1 = request.json['mobileno1']
    mobile2 = request.json['mobileno2']
    designation = request.json['designation']
    localizationid = request.json['localizationid']
    status = request.json['status']
    # validate the received values
    if title and address and email and \
            mobile1 and mobile2 and designation and localizationid  and status and request.method == 'PUT':
        # save edits
        EmployeeDetails.objects.filter(id=id).update(title=title, address=address, email=email,mobile_one=mobile1, mobile_two=mobile2,designation=designation,
                                                      localization_id=localizationid,is_active=status)
        resp = jsonify('Employee Details updated successfully!')
        return resp

@app.route('/employee/<id>', methods=['GET'])
def getemployee(id):
    # query to select one employee details for employee id
    user = EmployeeDetails.objects.get(id=id)
    return user.to_json()


@app.route('/allemployees', methods=['GET'])
def all_employees_list():
    # query to select all values from database
    resp = EmployeeDetails.objects.all()
    result = []
    for u in resp:
        result.append(u.to_json())
    return jsonify({'Employee Details': result})

@app.route('/login', methods=['GET', 'POST'])
def login_employee():
    auth = request.authorization
    # auth=requests.get("http://127.0.0.1:5000/login")
    if not auth or not auth.username or not auth.password:
        return make_response('could not verify', 401, {'WWW.Authentication': 'Basic realm: "login required"'})

    emp = EmployeeAuth.objects.filter(username=auth.username).first()
    #empauthid=emp.emp_details_id
    count=0
    if check_password_hash(emp.password, auth.password):
            token = jwt.encode(
                {'public_id': emp.public_id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},
                app.config['SECRET_KEY'])
            token1=str(token)
            emp_logs=EmployeeAuth.objects.filter(username=auth.username).update(token=token1)
            last_login=time.strftime("%x")
            login_time=time.strftime("%X")
            #logoff=datetime.datetime(2020,5,9,0,0)

            emp_auth=EmployeeLogs.objects.create(emp_auth_id=emp.to_dbref(),last_login=last_login,login_time=login_time,failed_login=0,logoff_time=last_login,err_log='',total_attempts=0)
            emp_auth.save()
            session['username']=auth.username
            return jsonify({'token': token.decode('UTF-8')})
    else:
        errlog="Password does not match"
        count=count+1
        logoff = time.strftime("%x")
        login_time = time.strftime("%X")
        emp_auth = EmployeeLogs.objects.create(emp_auth_id=emp.to_dbref(), failed_login=1,total_attempts=count,err_log=errlog,last_login=logoff,login_time=login_time,logoff_time=logoff)
        emp_auth.save()
        return make_response('could not verify', 401, {'WWW.Authentication': 'Basic realm: "login required"'})

@app.route('/logout', methods=['POST'])
def logoutEmployee():
    auth = request.authorization
    emp = EmployeeAuth.objects.filter(username=auth.username).first()
    emauthid=emp.id
    logoff_time = time.strftime("%X")
    EmployeeLogs.objects.filter(emp_auth_id=emauthid) .update(logoff_time=logoff_time)
    session.pop('username',None)
    return (jsonify({'message': 'Successfully Logged Out'}))

@app.route('/employee-attendance', methods=['POST'])
def create_employeeattendance():
    #Getting values
    empdetails_id=request.json['empdetails_id']
    workdays = request.json["workdays"]
    actualdays = request.json["actualdays"]
    work_hours = request.json["work_hours"]
    paid_leave = request.json['paid_leave']
    permissions = request.json['permissions']


    #validates the received values.
    if empdetails_id and workdays and actualdays and work_hours and paid_leave and permissions and request.method == 'POST':
            #query to insert the employee attendance details
            emp_attendance = EmployeeAttendance.objects.create(emp_details_id=empdetails_id,workdays_month=workdays,actual_days_month=actualdays,
                                                      work_hours=work_hours, paid_leave=paid_leave, permissions=permissions)

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
        EmployeeAttendance.objects.filter(emp_details_id=id).update(workdays_month=workdays,actual_days_month=actualdays,
                                                      work_hours=work_hours, paid_leave=paid_leave, permissions=permissions)
        resp = jsonify('Employee Attendance updated successfully!')
        return resp

@app.route('/employeeattendance/<id>', methods=['GET'])
def getemployeeattendance(id):
    # query to select one employee attendance for the employee d
    user = EmployeeAttendance.objects.get(emp_details_id=id)
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
    app.run(host='0.0.0.0', port=5003, debug=True)