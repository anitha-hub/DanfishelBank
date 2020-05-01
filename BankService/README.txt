
BANKSERVICE port number-http://0.0.0.0:5001

Database port-27017

-----------------------------------------------------------------------------------------------------------------------------------
Post Method-http://0.0.0.0:5001/bankregister

input:
{
         "bankname" : "Canarabank",
        "pannumber" : "GDH87382",
        "mobileno" :"9536587656",
        "licensenumber" : "8473hvdh23t",
        "email" : "jeyakala@gmail.com",
        "ssinumber" : "76536235261",
        "gstnumber" : "ggste2ge32",
        "tinnumber" : "7656756",
        "registeredaccountid" : "hfegr7463242"

}
Output:
[
  {
    "bankname": "Canarabank",
    "email": "jeyakala@gmail.com",
    "gstnumber": "ggste2ge32",
    "licensenumber": "8473hvdh23t",
    "mobileno": "9536587656",
    "pannumber": "GDH87382",
    "registered account id": "hfegr7463242",
    "ssinumber": "76536235261",
    "tinnumber": "7656756"
  },
  {
    "message": "Bank registered successfully"
  }
]

OutPut:
Fro same bank Name

{
  "message": "Bank Name Already Exists"
}
-----------------------------------------------------------------------------------------------------------------------
PUT Method-http://0.0.0.0:5001//bankupdate/Can397
{

        "pannumber" : "GDH87382",
        "mobileno" :"9536587656",
        "licensenumber" : "8473hvdh23t",
        "email" : "hello@gmail.com",
        "ssinumber" : "76536235261",
        "gstnumber" : "ggste2ge32",
        "tinnumber" : "7656756",
        "registeredaccountid" : "hfegr7463242"
}

Output:

"Bank updated successfully!"
---------------------------------------------------------------------------------------------------------------------------------------
GET-http://0.0.0.0:5001/bank/Can397

Output:
{
  "Bank Name": "Canarabank",
  "Email": "hello@gmail.com",
  "GST Number": "ggste2ge32",
  "License Number": "8473hvdh23t",
  "Mobile Number": 9536587656,
  "PAN Number": "GDH87382",
  "Registered Account Type": "hfegr7463242",
  "SSI Number": "76536235261",
  "TIN Number": "7656756",
  "_id": "Can397"
}

------------------------------------------------------------------------------------------------------
GET-http://0.0.0.0:5001/allbanks

{
  "Bank": [
    {
      "bankname": "Axisbank",
      "email": "anitha@gmail.com",
      "gstnumber": "ggste2ge32",
      "licensenumber": "8473hvdh23t",
      "mobileno": 9536587656,
      "pannumber": "GDH87382",
      "registeredaccid": "hfegr7463242",
      "ssinumber": "76536235261",
      "tinnumber": "765675699"
    },
    {
      "bankname": "Canarabank",
      "email": "hello@gmail.com",
      "gstnumber": "ggste2ge32",
      "licensenumber": "8473hvdh23t",
      "mobileno": 9536587656,
      "pannumber": "GDH87382",
      "registeredaccid": "hfegr7463242",
      "ssinumber": "76536235261",
      "tinnumber": "7656756"
    }
  ]
}
--------------------------------------------------------------------------------

DELETE-http://0.0.0.0:5001/deletebank/Can397

"Bank deleted successfully!"

------------------------------------------------------------------------------------------

POST-http://0.0.0.0:5001/bankdetailscreation
input:
{
	"bankid" : "Axi249",
        "address1" : "colony street",
        "address2" : "annanagar",
        "city" : "Chennai",
        "state" : "Tamilnadu",
        "country" : "India",
        "phoneno1" : "9812735961",
        "phoneno2" : "9984373232",
        "bankacctype" : "monthly payment",
        "digitsvalue":"16",
        "firstcharacters":"Axis bank"
}

Output:
[
  {
    "Address1": "colony street",
    "Address2": "annanagar",
    "Bank Account Type": "monthly payment",
    "City": "Chennai",
    "Country": "India",
    "Phone Number1": "9812735961",
    "Phone Number2": "9984373232",
    "State": "Tamilnadu"
  },
  {
    "message": "Bank Details registered successfully"
  }
]

---------------------------------------------------------------------------------------
PUT-http://0.0.0.0:5001/bankdetailsupdate/Axi249
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
        "bankacctype" : "monthly payment",
        "digitsvalue":"16",
        "firstcharacters":"Axis bank"
}

output:
"Bank Details updated successfully!"
---------------------------------------------------------------------------------------
GET-http://0.0.0.0:5001/bankdetails/Axi249

output:
{
  "Address1": "colony street",
  "Address2": "alandur",
  "Bank Account Id": "Axi0000005247369",
  "Bank Account Type": "monthly payment",
  "BankId": {
    "_id": "Axi249",
    "bank_name": "Axisbank",
    "created_date": {
      "$date": 1588327548158
    },
    "email": "anitha@gmail.com",
    "gst_number": "ggste2ge32",
    "license_number": "8473hvdh23t",
    "mobile_no": 9536587656,
    "pan_number": "GDH87382",
    "registered_acc_id": "hfegr7463242",
    "ssi_number": "76536235261",
    "tin_number": "765675699"
  },
  "City": "Madurai",
  "Country": "India",
  "PhoneNo1": 9812735961,
  "Phoneno2": 9984373232,
  "State": "Tamilnadu",
  "_id": "5eabf85ba360580484a66720"
}

---------------------------------------------------------------------------------------

GET-http://0.0.0.0:5001/bankdetails

{
  "BankDetails": [
    {
      "address1": "colony street",
      "address2": "colony street",
      "bank_acc_type": "monthly payment",
      "city": "Madurai",
      "country": "India",
      "phone_no1": 9812735961,
      "phone_no2": 9984373232,
      "state": "Tamilnadu"
    }
  ]
}

---------------------------------------------------------------------
DELETE-http://0.0.0.0:5001/deletebankdetails/Axi249

"Bank Details deleted successfully"