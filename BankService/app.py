import datetime
from BankService.models import BankRegister, BankDetails
from flask import abort, request, jsonify
from BankService.dbconfig import app
from random import random
from random import randint


#BankRegistr Model-Create,Update,delete, view and viewall functions

@app.route('/bankregister', methods=['POST'])
def create_bank():
    bankname = request.json['bankname']
    pan_number = request.json['pannumber']
    license_number = request.json['licensenumber']
    mobile_no = request.json['mobileno']
    ssi_number = request.json['ssinumber']
    gst_number = request.json['gstnumber']
    tin_number = request.json['tinnumber']
    email = request.json['email']
    registered_acc_id=request.json['registeredaccountid']

    if bankname and pan_number and license_number and mobile_no and email and ssi_number and gst_number and tin_number and registered_acc_id and request.method == 'POST':

        existingbank = BankRegister.objects.filter(bank_name=bankname).count()

        if existingbank == 0:
            bank_id=bankid_generation(bankname)

            bank = BankRegister.objects.create(bank_id=bank_id,bank_name=bankname, pan_number=pan_number, mobile_no=mobile_no,
                                              license_number=license_number,
                                              email=email, ssi_number=ssi_number, gst_number=gst_number,tin_number=tin_number,registered_acc_id=registered_acc_id)
            result = bank.save(commit=False)
            result.created_date=datetime.datetime.now()
            result.save()
            return (jsonify({'bankname': bankname, 'mobileno': mobile_no, 'licensenumber': license_number,'pannumber': pan_number,
                         'email': email, 'ssinumber': ssi_number, 'gstnumber': gst_number,'tinnumber': tin_number,'registered account id': registered_acc_id},
                        {'message': 'Bank registered successfully'}))
    else:
        abort(400)  # missing arguments

@app.route('/bankupdate/<id>', methods=['PUT'])
def update_bank(id):
    bank_name = request.json["bankname"]
    pan_number = request.json['pannumber']
    license_number = request.json['licensenumber']
    mobile_no = request.json['mobileno']
    ssi_number = request.json['ssinumber']
    gst_number = request.json['gstnumber']
    tin_number = request.json['tinnumber']
    email = request.json['email']
    registered_acc_id = request.json['registeredaccountid']

    # validate the received values
    if bank_name and pan_number and license_number and mobile_no and email and ssi_number and gst_number \
            and tin_number and registered_acc_id and request.method == 'PUT':
        # save edits
        BankRegister.objects.filter(bank_id=id).update(bank_name=bank_name, pan_number=pan_number, mobile_no=mobile_no,
                                              license_number=license_number,
                                              email=email, ssi_number=ssi_number, gst_number=gst_number,tin_number=tin_number,registered_acc_id=registered_acc_id)
        resp = jsonify('Bank updated successfully!')
        return resp


@app.route('/bank/<id>', methods=['GET'])
def getbank(id):
    user = BankRegister.objects.get(bank_id=id)
    return user.to_json()

@app.route('/allbanks', methods=['GET'])
def bank_list():
    resp = BankRegister.objects.all()
    result = []
    for u in resp:
        bank_data = {}
        bank_data['bankname'] = u.bank_name
        bank_data['mobileno'] = u.mobile_no
        bank_data['email'] = u.email
        bank_data['licensenumber'] = u.license_number
        bank_data['pannumber'] = u.pan_number
        bank_data['ssinumber'] = u.ssi_number
        bank_data['gstnumber'] = u.gst_number
        bank_data['tinnumber'] = u.tin_number
        bank_data['registeredaccid'] = u.registered_acc_id
        result.append(bank_data)

    return jsonify({'Bank': result})

@app.route('/deletebank/<id>', methods=['DELETE'])
def delete_bank(id):
    result=BankRegister.objects.get(bank_id=id)
    result.delete()
    resp = jsonify('Bank deleted successfully!')
    resp.status_code = 200
    return resp

def bankid_generation(bankname):
    randomnumber=round(random() * (99 - 1000) + 1000)
    bankname=bankname[0:3]
    bank_id=bankname + str(randomnumber)
    return bank_id

#BankDetails model-Create,Update,delete, view and viewall functions

@app.route('/bankdetailscreation', methods=['POST'])
def create_bankdetails():
    address1 = request.json["address1"]
    address2 = request.json['address2']
    city = request.json['city']
    state = request.json['state']
    country = request.json['country']
    phone_no1 = request.json['phoneno1']
    phone_no2 = request.json['phoneno2']
    bank_acc_type = request.json['bankacctype']
    bankid=request.json['bankid']

    if address1 and address2 and city and state and country and phone_no1 and phone_no2 and bank_acc_type and request.method == 'POST':

            bank = BankDetails.objects.create(bank_id=bankid,address1=address1, address2=address2, city=city,
                                              state=state,country=country, phone_no1=phone_no1, phone_no2=phone_no2,bank_acc_type=bank_acc_type)
            result = bank.save(commit=False)
            bankaccountno=bankaccountnogeneration()
            result.bank_acc_no=bankaccountno
            result.created_date=datetime.datetime.now()
            result.save()
            return (jsonify({'Address1': address1, 'Address2': address2, 'City': city,'State': state,
                         'Country': country, 'Phone Number1': phone_no1, 'Phone Number2': phone_no2,'Bank Account Type': bank_acc_type},
                        {'message': 'Bank Details registered successfully'}))
    else:
        abort(400)  # missing arguments

@app.route('/bankdetailsupdate/<id>', methods=['PUT'])
def update_bankdetails(id):
    address1 = request.json["address1"]
    address2 = request.json['address2']
    city = request.json['city']
    state = request.json['state']
    country = request.json['country']
    phone_no1 = request.json['phoneno1']
    phone_no2 = request.json['phoneno2']
    bank_acc_type = request.json['bankacctype']

    # validate the received values
    if address1 and address2 and city and state and country and phone_no1 and phone_no2 and bank_acc_type and request.method == 'PUT':
        # save edits
        BankDetails.objects.filter(bank_id=id).update(address1=address1, address2=address2, city=city,
                                              state=state,country=country, phone_no1=phone_no1, phone_no2=phone_no2,bank_acc_type=bank_acc_type)
        resp = jsonify('Bank Details updated successfully!')
        return resp


@app.route('/bankdetails/<id>', methods=['GET'])
def getbankdetails(id):
    user = BankDetails.objects.get(bank_id=id)
    return user.to_json()

@app.route('/allbanksdetails', methods=['GET'])
def bankdetails_list():
    resp = BankDetails.objects.all()
    result = []
    for u in resp:
        bankdetails_data = {}
        bankdetails_data['address1'] = u.address1
        bankdetails_data['address2'] = u.address1
        bankdetails_data['city'] = u.city
        bankdetails_data['state'] = u.state
        bankdetails_data['country'] = u.country
        bankdetails_data['phone_no1'] = u.phone_no1
        bankdetails_data['phone_no2'] = u.phone_no2
        bankdetails_data['bank_acc_type'] = u.bank_acc_type
        result.append(bankdetails_data)

    return jsonify({'BankDetails': result})

@app.route('/deletebankdetails/<id>', methods=['DELETE'])
def delete_bankdetails(id):
    result=BankDetails.objects.get(bank_id=id)
    result.delete()
    resp = jsonify('Bank Details deleted successfully!')
    resp.status_code = 200
    return resp

def bankaccountnogeneration():
    digitsvalue=request.json['digitsvalue']
    firstcharacters=request.json['firstcharacters']
    if digitsvalue == '11':
        firstcharacters=firstcharacters[0:3]
        number='0000'+ str(random_with_N_digits(4))
        bankaccno=firstcharacters + str(number)
        return bankaccno
    elif digitsvalue == '16':
        firstcharacters = firstcharacters[0:3]
        number = '000000' + str(random_with_N_digits(7))
        bankaccno = firstcharacters + str(number)
        return bankaccno
    else:
        firstcharacters = firstcharacters[0:3]
        number = '00000' + str(random_with_N_digits(5))
        bankaccno = firstcharacters + str(number)
        return bankaccno

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)