import datetime
from flask import abort, request, jsonify
from BankService.dbconfig import app
from random import random, randint
from BranchService.models import BranchDetails, BranchSpecification

#BranchDetails Model-Create,Update,delete, view and viewall functions


@app.route('/branchdetails', methods=['POST'])
def create_branchdetails():
    bank_id=request.json['bankid']
    branch_name = request.json["branchname"]
    address1 = request.json["address1"]
    address2 = request.json['address2']
    city = request.json['city']
    state = request.json['state']
    country = request.json['country']
    phone_no1 = request.json['phoneno1']
    phone_no2 = request.json['phoneno2']
    specificationid=request.json['specid']

    if bank_id and branch_name and address1 and address2 and city and state and country and \
            phone_no1 and phone_no2 and specificationid and request.method == 'POST':

        existingbranch = BranchDetails.objects.filter(branch_name=branch_name).count()

        if existingbranch == 0:
            branch = BranchDetails.objects.create(bank_id=bank_id,branch_name=branch_name,address1=address1, address2=address2, city=city,
                                              state=state,country=country, phone_no1=phone_no1, phone_no2=phone_no2,specification_id=specificationid)
            result = branch.save(commit=False)
            branchid=branchid_generation(branch_name)
            result.status='Active'
            result.branch_id=branchid
            result.created_date=datetime.datetime.now()
            result.save()
            return (jsonify({'branchname': branch_name, 'Address1': address1, 'Address2': address2, 'City': city,'State': state,
                         'Country': country, 'Phone Number1': phone_no1, 'Phone Number2': phone_no2,'SpecificationID': specificationid},
                        {'message': 'Branch Details registered successfully'}))
    else:
        abort(400)  # missing arguments

@app.route('/branchdetailsupdate/<id>', methods=['PUT'])
def update_bank(id):
    branch_name = request.json["branchname"]
    bank_id = request.json["bankid"]
    address1 = request.json["address1"]
    address2 = request.json['address2']
    city = request.json['city']
    state = request.json['state']
    country = request.json['country']
    phone_no1 = request.json['phoneno1']
    phone_no2 = request.json['phoneno2']
    specificationId = request.json['specId']

    # validate the received values
    if branch_name and address1 and address2 and city and state and country and \
            phone_no1 and phone_no2 and specificationId and request.method == 'PUT':
        # save edits
        BranchDetails.objects.filter(branch_id=id).update(bank_id=bank_id,branch_name=branch_name,address1=address1, address2=address2, city=city,
                                              state=state,country=country, phone_no1=phone_no1, phone_no2=phone_no2,specification_id=specificationId)
        resp = jsonify('Bank Details updated successfully!')
        return resp


@app.route('/branch/<id>', methods=['GET'])
def getbranchdetails(id):
    user = BranchDetails.objects.get(branch_id=id)
    return user.to_json()

@app.route('/allbranch', methods=['GET'])
def branch_list():
    resp = BranchDetails.objects.all()
    result = []
    for u in resp:
        branchdetails_data = {}
        branchdetails_data['branchname'] = u.branch_name
        branchdetails_data['address1'] = u.address1
        branchdetails_data['address2'] = u.address1
        branchdetails_data['city'] = u.city
        branchdetails_data['state'] = u.state
        branchdetails_data['country'] = u.country
        branchdetails_data['phone_no1'] = u.phone_no1
        branchdetails_data['phone_no2'] = u.phone_no2
        branchdetails_data['speificationId'] = u.specification_id
        result.append(branchdetails_data)

    return jsonify({'BranchDetails': result})

@app.route('/delete/<id>', methods=['DELETE'])
def delete_branch(id):
    result=BranchDetails.objects.get(branch_id=id)
    result.delete()
    resp = jsonify('Branch details deleted successfully!')
    resp.status_code = 200
    return resp

def branchid_generation(branchname):
    randomnumber=round(random() * (99 - 1000) + 1000)
    branchname=branchname[0:3]
    branch_id=branchname + str(randomnumber)
    return branch_id

#BankSpecification model-Create,Update,delete, view and viewall functions

@app.route('/branchspec-creation', methods=['POST'])
def create_branchspec():
    ifsccode = request.json["ifsccode"]
    micrcode = request.json['micrcode']

    if ifsccode and micrcode and request.method == 'POST':

            branchspec = BranchSpecification.objects.create(ifsc_code=ifsccode, micr_code=micrcode)
            result = branchspec.save(commit=False)
            branchaccountno=branchaccountnogeneration()
            result.branch_acc_no=branchaccountno
            result.vault_id=''
            result.branch_id=''
            result.setting_id =''
            result.save()
            return (jsonify({'IFSC Code': ifsccode, 'MICR Code': micrcode},
                        {'message': 'Branch Specification registered successfully'}))
    else:
        abort(400)  # missing arguments

@app.route('/branchspec-update/<id>', methods=['PUT'])
def update_branchspec(id):
    ifsccode = request.json["ifsccode"]
    micrcode = request.json['micrcode']

    # validate the received values
    if ifsccode and micrcode  and request.method == 'PUT':
        # save edits
        BranchSpecification.objects.filter(id=id).update(ifsc_code=ifsccode, micr_code=micrcode)
        resp = jsonify('Branch Specification updated successfully!')
        return resp


@app.route('/branchspec-details/<id>', methods=['GET'])
def getbranchspec(id):
    user = BranchSpecification.objects.get(id=id)
    return user.to_json()

@app.route('/allbranchspec-details', methods=['GET'])
def branchspec_list():
    resp = BranchSpecification.objects.all()
    result = []
    for u in resp:
        branchdetails_data = {}
        branchdetails_data['IFSC Code'] = u.ifsc_code
        branchdetails_data['MICR Code'] = u.micr_code
        branchdetails_data['Vault Id'] = u.vault_id
        branchdetails_data['Branch Id'] = u.branch_id
        branchdetails_data['Setting Id'] = u.setting_id
        branchdetails_data['Branch Account Number'] = u.branch_acc_no

        result.append(branchdetails_data)

    return jsonify({'Branch Specification Details': result})

@app.route('/delete/<id>', methods=['DELETE'])
def delete_branchspec(id):
    result=BranchSpecification.objects.get(id=id)
    result.delete()
    resp = jsonify('Branch Specification Details deleted successfully!')
    resp.status_code = 200
    return resp

def branchaccountnogeneration():

        digitsvalue = request.json['digitsvalue']
        firstcharacters = request.json['firstcharacters']
        secondcharacters = request.json['secondcharacters']
        if digitsvalue == 11:
            firstcharacters = firstcharacters[0:3]
            secondcharacters = secondcharacters[0:3]
            number = '000' + random_with_N_digits(2)
            branchaccno = firstcharacters + secondcharacters + number
            return branchaccno
        elif digitsvalue == 16:
            firstcharacters = firstcharacters[0:3]
            secondcharacters = secondcharacters[0:3]
            number = '00000' + random_with_N_digits(5)
            branchaccno = firstcharacters + secondcharacters + number
            return branchaccno
        else:
            firstcharacters = firstcharacters[0:3]
            secondcharacters = secondcharacters[0:3]
            number = '0000' + random_with_N_digits(3)
            branchaccno = firstcharacters + secondcharacters + number
            return branchaccno

def random_with_N_digits(n):
        range_start = 10 ** (n - 1)
        range_end = (10 ** n) - 1
        return randint(range_start, range_end)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)