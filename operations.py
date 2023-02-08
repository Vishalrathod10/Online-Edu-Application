import json

def register(filename, name, phone_no, email_id, password):
    details ={
            "Full_name" : name,
            "Contact Number" : phone_no,
            "Email" : email_id,
            "password" : password,
    }
    
    file = open(filename,'r+')
    try:
        data=json.load(file)
        if details not in data:
            data.append(details)
            file.seek(0)
            file.truncate()
            json.dump(data,file)
            file.close()
            return True
    except json.decoder.JSONDecodeError:
        lst=[]
        lst.append(details)
        json.dump(lst,file)
        file.close() 
        return True
    finally:
        file.close()
    return False



def login(filename, email_id, password):
    file = open(filename,'r+')
    data = json.load(file)
    for i in range(len(data)):
        if data[i]["Email"] == email_id and data[i]["password"] == password:
            return True
    return False



def create_model(filename, model_id, model_name, model_start_date, model_end_date):
    details ={
            "Model_id" : model_id,
            "Model_name" : model_name,
            "Model_Start_Date" : model_start_date,
            "Model_End_Date" : model_end_date,
    }
    
    file = open(filename,'r+')
    try:
        data=json.load(file)
        if details not in data:
            data.append(details)
            file.seek(0)
            file.truncate()
            json.dump(data,file)
            file.close()
            return True
    except json.decoder.JSONDecodeError:
        lst=[]
        lst.append(details)
        json.dump(lst,file)
        file.close() 
        return True
    finally:
        file.close()
    return False

def view_model(filename):
    file = open(filename,"r+")
    data = json.load(file)
    return data



def update_model(filename, model_id):
    file = open(filename,"r+")
    data = json.load(file)
    for i in range(len(data)):
        if data[i]["Model_id"] == model_id:
            model_name = input("Enter model name : ")
            model_start_date = input("Enter model start date : ")
            model_end_date = input("Enter model end date : ")
            data[i]["Model_name"] = model_name
            data[i]["Model_Start_Date"] = model_start_date
            data[i]["Model_End_Date"] = model_end_date
            file.seek(0)
            file.truncate()
            json.dump(data, file)
            file.close()
            return True
    return False



def delete_model(filename, model_id):
    file = open(filename, "r+")
    data = json.load(file)
    for i in range(len(data)):
        if data[i]["Model_id"] == model_id:
            data.pop(i)
            file.seek(0)
            file.truncate()
            json.dump(data, file)
            file.close()
            return True
    return False
