import datetime
from flask import abort, request, jsonify
from BranchService.dbconfig import app
from random import random, randint
from BranchService.models import BranchDetails, BranchSpecification

#BranchDetails Model-Create,Update,delete, view and viewall functions


@app.route('/branchdetails', methods=['POST'])
def create_branchdetails():
    #Getting values
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

    #validates the received values.
    if bank_id and branch_name and address1 and address2 and city and state and country and \
            phone_no1 and phone_no2 and specificationid and request.method == 'POST':

        #Check if any branch has the same name.if count is zero it will create new branch

        existingbranch = BranchDetails.objects.filter(branch_name=branch_name).count()

        if existingbranch == 0:
            #branchid generation by calling branchid_generation function
            branchid=branchid_generation(branch_name)
            #query to insert the branch details
            branch = BranchDetails.objects.create(bank_id=bank_id,branch_id=branchid,branch_name=branch_name,address1=address1, address2=address2, city=city,
                                              state=state,country=country, phone_no1=phone_no1, phone_no2=phone_no2,specification_id=specificationid)
            result = branch.save(commit=False)
            result.status='Active'
            result.created_date=datetime.datetime.now()
            result.save()
            return (jsonify({'Branch Name': branch_name, 'Address1': address1, 'Address2': address2, 'City': city,'State': state,
                         'Country': country, 'Phone Number1': phone_no1, 'Phone Number2': phone_no2,'Specification ID': specificationid},
                        {'message': 'Branch Details registered successfully'}))
        else:
            return (jsonify({'message': 'Branch Name Already Exists'}))

    else:
        abort(400)  # missing arguments

@app.route('/branchdetailsupdate/<id>', methods=['PUT'])
def update_bank(id):
    # Getting values
    branch_name = request.json["branchname"]
    bank_id = request.json["bankid"]
    address1 = request.json["address1"]
    address2 = request.json['address2']
    city = request.json['city']
    state = request.json['state']
    country = request.json['country']
    phone_no1 = request.json['phoneno1']
    phone_no2 = request.json['phoneno2']
    specificationId = request.json['specid']

    # validate the received values
    if branch_name and address1 and address2 and city and state and country and \
            phone_no1 and phone_no2 and specificationId and request.method == 'PUT':
        # save edits
        #update query
        BranchDetails.objects.filter(branch_id=id).update(bank_id=bank_id,branch_name=branch_name,address1=address1, address2=address2, city=city,
                                              state=state,country=country, phone_no1=phone_no1, phone_no2=phone_no2,specification_id=specificationId)
        resp = jsonify('Bank Details updated successfully!')
        return resp


@app.route('/branch/<id>', methods=['GET'])
def getbranchdetails(id):
    #query to select one branch with the branch id
    user = BranchDetails.objects.get(branch_id=id)
    return user.to_json()

@app.route('/allbranch', methods=['GET'])
def branch_list():
    #query to select all values from database
    resp = BranchDetails.objects.all()
    result = []
    for u in resp:
        branchdetails_data = {}
        branchdetails_data['Branch Name'] = u.branch_name
        branchdetails_data['Address1'] = u.address1
        branchdetails_data['Address2'] = u.address1
        branchdetails_data['City'] = u.city
        branchdetails_data['State'] = u.state
        branchdetails_data['Country'] = u.country
        branchdetails_data['Phone Number1'] = u.phone_no1
        branchdetails_data['Phone Number2'] = u.phone_no2
        branchdetails_data['Specification Id'] = u.specification_id
        result.append(branchdetails_data)

    return jsonify({'BranchDetails': result})

@app.route('/deletebranch/<id>', methods=['DELETE'])
def delete_branch(id):
    #query to select the branch
    result=BranchDetails.objects.get(branch_id=id)
    #delete the selected branch
    result.delete()
    resp = jsonify('Branch details deleted successfully!')
    resp.status_code = 200
    return resp

def branchid_generation(branchname):
    #generate 3digit random number between 99 to 1000
    randomnumber=round(random() * (99 - 1000) + 1000)

    #substring first 3 letters of branchname
    branchname=branchname[0:3]

    #concatinate the branchname and random number.str converting int to string.
    branch_id=branchname + str(randomnumber)
    return branch_id

#BankSpecification model-Create,Update,delete, view and viewall functions

@app.route('/branchspec-creation', methods=['POST'])
def create_branchspec():
    # Getting values
    ifsccode = request.json["ifsccode"]
    micrcode = request.json['micrcode']
    vaultid = request.json['vaultid']
    branchid = request.json['branchid']
    settingid = request.json['settingid']

    # validating input values
    if ifsccode and micrcode and request.method == 'POST':

        # branch account number generation by calling branchaccountnogeneration function
            branchaccountno=branchaccountnogeneration()

            # query to insert the branch details
            branchspec = BranchSpecification.objects.create(branch_acc_no=branchaccountno,ifsc_code=ifsccode, micr_code=micrcode,vault_id=vaultid,branch_id=branchid,
                                                            setting_id=settingid)
            branchspec.save()
            return (jsonify({'IFSC Code': ifsccode, 'MICR Code': micrcode,'Vault Id': vaultid,'Branch Id': branchid,'Setting Id': settingid,'Branch Account Number': branchaccountno},
                        {'message': 'Branch Specification registered successfully'}))
    else:
        abort(400)  # missing arguments

@app.route('/branchspec-update/<id>', methods=['PUT'])
def update_branchspec(id):
    # Getting values
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
    # query to select one branch with the branchspecification id
    user = BranchSpecification.objects.get(id=id)
    return user.to_json()

@app.route('/allbranchspec-details', methods=['GET'])
def branchspec_list():
    # query to select all values from database
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

@app.route('/delete-branchspec/<id>', methods=['DELETE'])
def delete_branchspec(id):
    # query to select the BranchSpecification
    result=BranchSpecification.objects.get(id=id)
    # delete the selected BranchSpecification
    result.delete()
    resp = jsonify('Branch Specification Details deleted successfully!')
    resp.status_code = 200
    return resp

def branchaccountnogeneration():
        #digitsvalue-how many digits account number want to generate
        digitsvalue = request.json['digitsvalue']

        #firstcharacters-first 3 characters of account number
        firstcharacters = request.json['firstcharacters']

        # secondtcharacters-second 3 characters of account number
        secondcharacters = request.json['secondcharacters']

        if digitsvalue == '11':
            #substring 3charactes from reveived string
            firstcharacters = firstcharacters[0:3]
            secondcharacters = secondcharacters[0:3]

            #generate random 2 digits number and concatinate with 3 zeros
            number = '000' + str(random_with_N_digits(2))

            #concatinate all numbers and characters
            branchaccno = firstcharacters + secondcharacters + str(number)
            return branchaccno
        elif digitsvalue == '16':
            firstcharacters = firstcharacters[0:3]
            secondcharacters = secondcharacters[0:3]
            number = '00000' + str(random_with_N_digits(5))
            branchaccno = firstcharacters + secondcharacters + str(number)
            return branchaccno
        else:
            firstcharacters = firstcharacters[0:3]
            secondcharacters = secondcharacters[0:3]
            number = '0000' + str(random_with_N_digits(3))
            branchaccno = firstcharacters + secondcharacters + str(number)
            return branchaccno

#genarate random numbers
def random_with_N_digits(n):
        range_start = 10 ** (n - 1)
        range_end = (10 ** n) - 1
        return randint(range_start, range_end)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)