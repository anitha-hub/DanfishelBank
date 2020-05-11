EMPLOYEESERVICE port number-http://0.0.0.0:5003
Database port-27017
----------------------------------------------------------------------------------
POST http://0.0.0.0:5003/transaction-limit

input:
{
        "conditionname" : "transaction",
        "conditionone" : ["daylimit 100000","firstcondition"],
        "conditiontwo":["overseas transaction 500000","secondcondition"]
}

output:
[
  {
    "ConditionName": "transaction",
    "ConditionOne": [
      "daylimit 100000",
      "firstcondition"
    ],
    "ConditionTwo": [
      "overseas transaction 500000",
      "secondcondition"
    ]
  },
  {
    "message": "Transaction Limit Saved successfully"
  }
]
-----------------------------------------------------------------------------------
PUT http://0.0.0.0:5003/update-transaction-limit/5eb6a591c66ec0e0a5590f8d
input:
{
        "conditionname" : "Withdraw",
        "conditionone" : ["daylimit 100000","firstcondition"],
        "conditiontwo":["overseas transaction 500000","secondcondition"]
}

output:
"TransactionLimit updated successfully!"
----------------------------------------------------------------------------------------------------------
GET http://0.0.0.0:5003/transaction-limit/5eb6a591c66ec0e0a5590f8d
output:

{
  "Condition Name": "Withdraw",
  "Condition One": [
    "daylimit 100000",
    "firstcondition"
  ],
  "Condition Two": [
    "overseas transaction 500000",
    "secondcondition"
  ],
  "_id": "5eb6a591c66ec0e0a5590f8d"
}
------------------------------------------------------------------------------------------
GET http://0.0.0.0:5003/alltransactionlimits

output:

{
  "Transaction Limits": [
    {
      "condition_name": "Withdraw",
      "condition_one": [
        "daylimit 100000",
        "firstcondition"
      ],
      "condition_two": [
        "overseas transaction 500000",
        "secondcondition"
      ]
    },
    {
      "condition_name": "transaction",
      "condition_one": [
        "daylimit 100000",
        "firstcondition"
      ],
      "condition_two": [
        "overseas transaction 500000",
        "secondcondition"
      ]
    }
  ]
}
------------------------------------------------------------------------------------------------------------
POST http://0.0.0.0:5003/employee-role

input:
{
        "rolename" : "Manager",
        "create":"1",
        "edit":"1",
        "delete":"1",
        "restrict_logincount" : "5",
        "access_service_id":["2","3","5","9"],
        "transaction_limit_id":"5eb6a591c66ec0e0a5590f8d"
}
output:
[
  {
    "Create": "1",
    "Delete": "1",
    "Edit": "1",
    "Restrict login count": "5",
    "RoleName": "Manager",
    "Service Id": [
      "2",
      "3",
      "5",
      "9"
    ],
    "Transaction Limit Id": "5eb6a591c66ec0e0a5590f8d"
  },
  {
    "message": "Employee Role Created successfully"
  }
]
-------------------------------------------------------------------------------------
PUT http://0.0.0.0:5003/update-employeerole/5eb6a92541246004f42b9265
input:
{
	"rolename" : "Teller",
        "create":true,
        "edit":true,
        "delete":true,
        "restrict_logincount" : "10",
        "access_service_id":["2","3","5","9"]
}

output:

"Employee Role updated successfully!"
-------------------------------------------------------------------------------------------
GET http://0.0.0.0:5003/allemployee_roles

{
  "EmployeeRoles": [
    {
      "Access Service Id": [
        2,
        3,
        5,
        9
      ],
      "Create": true,
      "Delete": true,
      "Edit": true,
      "Login Count": 10,
      "Role name": "Teller"
    }
  ]
}

-------------------------------------------------------------------------------------------

POST http://0.0.0.0:5003/employee-register
input:
{
        "branchid" : "per789",
        "firstname":"anitha",
        "lastname":"j",
        "title":"hghjfg",
        "address" : "apparao garden",
        "email":"anitha@gmail.com",
        "employeeId":"2",
        "dob":"07/05/1990",
        "mobileno1":"9887658765",
        "mobileno2":"9866632456",
        "designation":"manager",
        "localizationid":"764",
        "emproleid":"5eb6a92541246004f42b9265",
        "status":"1"
}

output:

[
  {
    "Address": "apparao garden",
    "Branch Id": "per789",
    "Date of Birth": "07/05/1990",
    "Designation": "manager",
    "Email": "anitha@gmail.com",
    "Employee Id": "2",
    "Employee Role Id": "5eb6a92541246004f42b9265",
    "Firstname": "anitha",
    "Lastname": "j",
    "Localization Id": "764",
    "Mobile Number Two": "9866632456",
    "Mobile NumberOne": "9887658765",
    "Title": "hghjfg"
  },
  {
    "message": "Employee Details registered successfully"
  }
]
---------------------------------------------------------------------------------------------------------
PUT http://0.0.0.0:5003/update-employedetails/5eb6c1f2a4d7a2ed01dc6939

input:

{

        "title":"head of the branch",
        "address" : "apparao garden",
        "email":"anitha@gmail.com",
        "employeeId":"2",
        "mobileno1":"9887658765",
        "mobileno2":"9866632456",
        "designation":"manager",
        "localizationid":"764",
        "status":true
}

output:

"Employee Details updated successfully!"

------------------------------------------------------------------------------------------------------------------
GET http://0.0.0.0:5003/employee/5eb6e6d00f3b2b7392c1c577
output:
{
  "Address": "Dubai",
  "Branch Id": "per789",
  "Date of Birth": "Tue, 17 Jul 2012 00:00:00 GMT",
  "Designation": "Teller",
  "Email1": "asmitha@gmail.com",
  "Employee Role Id": {
    "_id": {
      "$oid": "5eb6a92541246004f42b9265"
    },
    "can_access_service_id": [
      2,
      3,
      5,
      9
    ],
    "can_create": true,
    "can_delete": true,
    "can_edit": true,
    "restrict_login_count": 10,
    "role_name": "Teller",
    "transaction_limit_id": {
      "$id": {
        "$oid": "5eb6a591c66ec0e0a5590f8d"
      },
      "$ref": "transaction_limit"
    }
  },
  "EmployeeId": "1",
  "First Name": "Asmitha",
  "Last Name": "T",
  "Localization Id": 87131,
  "Mobile Number": 9866632456,
  "Phone Number": 9887658765,
  "Status": true,
  "Title": "hghjfg",
  "_id": "5eb6e6d00f3b2b7392c1c577"
}
------------------------------------------------------------------------------------
GET http://0.0.0.0:5003/allemployees

{
  "Employee Details": [
    {
      "Address": "apparao garden",
      "Branch Id": "per789",
      "Designation": "Accountant",
      "Email": "tanuj@gmail.com",
      "First Name": "Arunkumar",
      "Last Name": "R",
      "Localization Id": 764,
      "Mobile One": 9887658765,
      "Mobile Two": 9866632456,
      "Status": true,
      "Title": "hghjfg"
    },
    {
      "Address": "Dubai",
      "Branch Id": "per789",
      "Designation": "Teller",
      "Email": "asmitha@gmail.com",
      "First Name": "Asmitha",
      "Last Name": "T",
      "Localization Id": 87131,
      "Mobile One": 9887658765,
      "Mobile Two": 9866632456,
      "Status": true,
      "Title": "hghjfg"
    }
  ]
}
-----------------------------------------------------------------------------------------

http://0.0.0.0:5003/login

input:

username: Asm0
password:welcome

{
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwdWJsaWNfaWQiOiI1MDRlMDg4MS05MTBjLTRhOGMtODMyMS03N2M1NzUxY2Q2YjMiLCJleHAiOjE1ODkwNDkyNDZ9.gErcmcXUSaIRFWSkRh0VxCTo08DDnvQru0PQxvdA-Os"
}

---------------------------------------------------------------------------------------

http://0.0.0.0:5003/logout

{
  "message": "Successfully Logged Out"
}

-----------------------------------------------------------------------------------------
POST  http://0.0.0.0:5003/employee-attendance
input:
{
        "empdetails_id" : "5eb6e6d00f3b2b7392c1c577",
        "workdays":"30",
        "actualdays":"28",
        "work_hours":"79",
        "paid_leave" : "4",
        "permissions":"4"
}
output:
{
  "message": "Employee Attendance Created successfully"
}
---------------------------------------------------------------------------------------
PUT http://0.0.0.0:5003/update-employeattendance/5eb6e6d00f3b2b7392c1c577
input:
{
        "workdays":"25",
        "actualdays":"31",
        "work_hours":"79",
        "paid_leave" : "4",
        "permissions":"4"
}
output:

"Employee Attendance updated successfully!"
------------------------------------------------------------------------------------------
GET http://0.0.0.0:5003/employeeattendance/5eb6e6d00f3b2b7392c1c577

{
  "Actual Days in Month": 31,
  "Employee Details Id": {
    "_id": {
      "$oid": "5eb6e6d00f3b2b7392c1c577"
    },
    "address": "Dubai",
    "branch_id": "per789",
    "designation": "Teller",
    "dob": {
      "$date": 1342483200000
    },
    "email": "asmitha@gmail.com",
    "emp_role_id": {
      "$oid": "5eb6a92541246004f42b9265"
    },
    "employee_id": "1",
    "first_name": "Asmitha",
    "is_active": true,
    "last_name": "T",
    "localization_id": 87131,
    "mobile_one": 9887658765,
    "mobile_two": 9866632456,
    "title": "hghjfg"
  },
  "Paid Leave": 4,
  "Permissions": 4,
  "Work Hours": 79,
  "WorkDays in Month": 25,
  "_id": "5eb6f8289e4ceafa27c5c251"
}
-----------------------------------------------------------------------------------
GET http://0.0.0.0:5003/allemployeesattendance
{
  "Actual Days in Month": 31,
  "Employee Details Id": {
    "_id": {
      "$oid": "5eb6e6d00f3b2b7392c1c577"
    },
    "address": "Dubai",
    "branch_id": "per789",
    "designation": "Teller",
    "dob": {
      "$date": 1342483200000
    },
    "email": "asmitha@gmail.com",
    "emp_role_id": {
      "$oid": "5eb6a92541246004f42b9265"
    },
    "employee_id": "1",
    "first_name": "Asmitha",
    "is_active": true,
    "last_name": "T",
    "localization_id": 87131,
    "mobile_one": 9887658765,
    "mobile_two": 9866632456,
    "title": "hghjfg"
  },
  "Paid Leave": 4,
  "Permissions": 4,
  "Work Hours": 79,
  "WorkDays in Month": 25,
  "_id": "5eb6f8289e4ceafa27c5c251"
}
------------------------------------------------------------------------------------------------