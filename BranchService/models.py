from flask_mongoengine import MongoEngine
from BranchService.dbconfig import app
from mongoengine import *

db = MongoEngine(app)

class BranchDetails(Document):
    bank_id = StringField()
    branch_id=StringField(primary_key=True)
    branch_name = StringField()
    address1 = StringField()
    address2 = StringField()
    city = StringField()
    state = StringField()
    country = StringField()
    phone_no1 = IntField()
    phone_no2 = IntField()
    created_date=DateTimeField()
    status=StringField()
    specification_id=IntField()

    def to_json(self):
        return {
            "_id": str(self.pk),
            "Bank Id": self.bank_id,
            "Branch Name": self.branch_name,
            "Address1": self.address1,
            "Address2": self.address2,
            "City": self.city,
            "State": self.state,
            "Country": self.country,
            "PhoneNo1": self.phone_no1,
            "Phoneno2": self.phone_no2,
            "Created Date": self.created_date,
            "Status": self.status,
            "Specification Id": self.specification_id
        }

class BranchSpecification(Document):
    branch_id = ReferenceField(BranchDetails)
    branch_acc_no = StringField()
    vault_id = StringField()
    ifsc_code = StringField()
    micr_code = StringField()
    setting_id = StringField()

    def to_json(self):
        return {
            "_id": str(self.pk),
            "Branch Id": self.branch_id,
            "Branch Account Number": self.branch_acc_no,
            "Vault Id": self.vault_id,
            "IFSC Code": self.ifsc_code,
            "MICR Code": self.micr_code,
            "Setting Id": self.setting_id

        }


# disconnect(alias='branchservicedb')