BRANCHSERVICE port number-http://0.0.0.0:5002

Database port-27017

----------------------------------------------------------------------------------
POST-http://0.0.0.0:5002/branchdetails

input:

{
	"bankid" : "Axi249",
        "address1" : "colony street",
        "address2" : "alandur",
        "city" : "Madurai",
        "state" : "Tamilnadu",
        "country" : "India",
        "phoneno1" : "9812735961",
        "phoneno2" : "9984373232",
        "specid" : "675",
        "branchname":"alandur branch"

}

Output:
[
  {
    "Address1": "colony street",
    "Address2": "alandur",
    "Branch Name": "alandur branch",
    "City": "Madurai",
    "Country": "India",
    "Phone Number1": "9812735961",
    "Phone Number2": "9984373232",
    "Specification ID": "675",
    "State": "Tamilnadu"
  },
  {
    "message": "Branch Details registered successfully"
  }
]
-----------------------------------------------------------------------------------
PUT-http://0.0.0.0:5002/branchdetailsupdate/ala430
{
        "address1" : "colony street",
        "address2" : "alandur",
        "city" : "Madurai",
        "state" : "Tamilnadu",
        "country" : "India",
        "phoneno1" : "9812735961",
        "phoneno2" : "9841375941",
        "specid" : "675"
}
output
"Bank Details updated successfully!"
----------------------------------------------------------------------------------------------------------
GET-http://0.0.0.0:5002/branch/ala430

Output
{
  "Address1": "colony street",
  "Address2": "alandur",
  "Bank Id": "Axi249",
  "Branch Name": "alandur branch",
  "City": "Madurai",
  "Country": "India",
  "Created Date": "Fri, 01 May 2020 16:34:52 GMT",
  "PhoneNo1": 9812735961,
  "Phoneno2": 9841375941,
  "Specification Id": 675,
  "State": "Tamilnadu",
  "Status": "Active",
  "_id": "ala430"
}
------------------------------------------------------------------------------------------
GET-http://0.0.0.0:5002/allbranch

Output
{
  "BranchDetails": [
    {
      "Address1": "1st street",
      "Address2": "1st street",
      "Branch Name": "perambur branch",
      "City": "Chennai",
      "Country": "India",
      "Phone Number1": 9887673643,
      "Phone Number2": 9002336432,
      "Specification Id": 98377,
      "State": "Tamilnadu"
    },
    {
      "Address1": "colony street",
      "Address2": "colony street",
      "Branch Name": "alandur branch",
      "City": "Madurai",
      "Country": "India",
      "Phone Number1": 9812735961,
      "Phone Number2": 9841375941,
      "Specification Id": 675,
      "State": "Tamilnadu"
    }
  ]
}
---------------------------------------------------------------------------------------------------
DELETE-http://0.0.0.0:5002/deletebranch/ala430

"Branch details deleted successfully!"

------------------------------------------------------------------------------------------------------------
POST-http://0.0.0.0:5002/branchspec-creation
{
        "ifsccode" : "per789",
        "micrcode" : "677356987",
        "vaultid" : "653262",
        "branchid" : "per789",
        "settingid" : "7564",
        "digitsvalue":"11",
        "firstcharacters":"Axisbank",
        "secondcharacters":"perambur branch"
}
output:
[
  {
    "Branch Account Number": "Axiper00092",
    "Branch Id": "per789",
    "IFSC Code": "per789",
    "MICR Code": "677356987",
    "Setting Id": "7564",
    "Vault Id": "653262"
  },
  {
    "message": "Branch Specification registered successfully"
  }
]
-------------------------------------------------------------------------------------
GET-http://0.0.0.0:5002/branchspec-details/per789

output
{
  "Branch Account Number": "Axiper00092",
  "Branch Id": {
    "_id": "per789",
    "address1": "1st street",
    "address2": "apparao garden",
    "bank_id": "Axi249",
    "branch_name": "perambur branch",
    "city": "Chennai",
    "country": "India",
    "created_date": {
      "$date": 1588332802642
    },
    "phone_no1": 9887673643,
    "phone_no2": 9002336432,
    "specification_id": 98377,
    "state": "Tamilnadu",
    "status": "Active"
  },
  "IFSC Code": "per789",
  "MICR Code": "677356987",
  "Setting Id": "7564",
  "Vault Id": "653262",
  "_id": "5eac0b68baadf302e55d6eba"
}

-------------------------------------------------------------------------------------------
GET-http://0.0.0.0:5002/allbranchspec-details

{
  "Branch Specification Details": [
    {
      "Branch Account Number": "Axiper00092",
      "Branch Id": {
        "_id": "per789",
        "address1": "1st street",
        "address2": "apparao garden",
        "bank_id": "Axi249",
        "branch_name": "perambur branch",
        "city": "Chennai",
        "country": "India",
        "created_date": {
          "$date": 1588332802642
        },
        "phone_no1": 9887673643,
        "phone_no2": 9002336432,
        "specification_id": 98377,
        "state": "Tamilnadu",
        "status": "Active"
      },
      "IFSC Code": "per789",
      "MICR Code": "677356987",
      "Setting Id": "7564",
      "Vault Id": "653262"
    }
  ]
}
-------------------------------------------------------------------------------------------
DELETE-http://0.0.0.0:5002/delete-branchspec/per789

"Branch Specification Details deleted successfully!"