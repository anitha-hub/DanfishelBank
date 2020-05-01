from flask_mongoengine import MongoEngine
from BankService.dbconfig import app
from mongoengine import *

db = MongoEngine(app)

class BankRegister(Document):
    bank_id=StringField(primary_key=True)
    bank_name = StringField()
    pan_number = StringField()
    mobile_no = IntField()
    license_number = StringField()
    email = EmailField()
    ssi_number = StringField()
    gst_number = StringField()
    tin_number=StringField()
    created_date=DateTimeField()
    registered_acc_id=StringField()

    def to_json(self):
        return {
            "_id": str(self.pk),
            "Bank Name": self.bank_name,
            "PAN Number": self.pan_number,
            "Mobile Number": self.mobile_no,
            "Email": self.email,
            "License Number": self.license_number,
            "SSI Number": self.ssi_number,
            "GST Number": self.gst_number,
            "TIN Number": self.tin_number,
            "Registered Account Type": self.registered_acc_id
        }

class BankDetails(Document):
    bank_id = ReferenceField(BankRegister,to_field='bank_id')
    address1 = StringField()
    address2 = StringField()
    city = StringField()
    state = StringField()
    country = StringField()
    phone_no1 = IntField()
    phone_no2=IntField()
    bank_acc_no=StringField()
    bank_acc_type=StringField()

    def to_json(self):
        return {
            "_id": str(self.pk),
            "BankId": self.bank_id,
            "Address1": self.address1,
            "Address2": self.address2,
            "City": self.city,
            "State": self.state,
            "Country": self.country,
            "PhoneNo1": self.phone_no1,
            "Phoneno2": self.phone_no2,
            "Bank Account Id": self.bank_acc_no,
            "Bank Account Type": self.bank_acc_type
        }


# disconnect(alias='bankservicedb')