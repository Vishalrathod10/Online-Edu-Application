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
    try:
        data = json.load(file)
        for i in data:
            if i["Email"] == email_id and i["password"] == password:
                return True
            else:
                return False
    except json.decoder.JSONDecodeError:
        return False
    finally:
        file.close()
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
    file = open(filename, "r+") 
    data = json.load(file)
    return data
