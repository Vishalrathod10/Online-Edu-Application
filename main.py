import re
from operations import *
import random

if __name__ == "__main__":
    while True:
        try:
            choice = int(input("Enter \n1.Signup \n2.Signin \n3.Quit \nYour choice : "))
        except ValueError:
            print("Please enter valid option")
            continue 

        if choice == 1:                 # To Register
            try:
                register_choice =int(input("Enter \n1.Register as admin \n2.Register as user \n3.Exit \nYour choice : "))
            except ValueError:
                print("Please enter valid option")
                continue 

            if register_choice == 1:                        # To register as admin
                name = input("Enter your name : ")
                phone_no = input("Enter your contact number : ")
                email_id = input("Enter your mail id : ")
                password = input("Enter your password : ")
                
                name_re = re.findall(r'^[A-Za-z]{2,15}\s[A-Za-z]{2,15}$', name)
                phone_no_re = re.findall(r'^[6-9]{1}[0-9]{9}$' , phone_no)
                email_re = re.findall("^[A-z][a-zA-Z0-9._]+[@][a-z]+[.][a-z]+$", email_id)
                password_re = re.findall(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$" , password)

                if name_re and phone_no_re and email_re and password_re:
                    var = register("manager.json", name, phone_no, email_id, password)
                    if var:
                        print("successfully added")
                    else:
                        print("registaration unsuccessful") 
                    

                else:
                    if not name_re:
                        print("Entered name format is incorrect (Vishal Rathod) ")
                        continue
                    if not phone_no_re:
                        print("Entered contact detail format is incorrect (9123456789")
                        continue
                    if not email_re:
                        print("Entered mail format is incorrect (email@gmai.com")
                        continue
                    if not password_re:
                        print("Entered password format is incorrect (Password#123)")
                        continue
            
            if register_choice == 2:                                # To register as student
                name = input("Enter your name : ")
                phone_no = input("Enter your contact number : ")
                email_id = input("Enter your mail id : ")
                password = input("Enter your password : ")
                
                name_re = re.findall(r'^[A-Za-z]{2,15}\s[A-Za-z]{2,15}$', name)
                phone_no_re = re.findall(r'^[6-9]{1}[0-9]{9}$' , phone_no)
                email_re = re.findall("^[A-z][a-zA-Z0-9._]+[@][a-z]+[.][a-z]+$", email_id)
                password_re = re.findall(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$" , password)

                if name_re and phone_no_re and email_re and password_re:
                    var = register("student.json", name, phone_no, email_id, password)
                    if var:
                        print("successfully added")
                    else:
                        print("registration unsuccessfull") 
                    

                else:
                    if not name_re:
                        print("Entered name format is incorrect (Rahul Yadav)")
                        continue
                    if not phone_no_re:
                        print("Entered contact detail format is incorrect (9123456789)")
                        continue
                    if not email_re:
                        print("Entered mail format is incorrect (email@gmail.com)")
                        continue
                    if not password_re:
                        print("Entered password format is incorrect (password#123)")
                        continue

            if register_choice==3:
                print("Bye, Have a nice day")
                quit()

        if choice == 2:                             # To login

            login_choice =int(input("Enter \n1.Login as admin \n2.Login as user \n3.Exit \nYour choice : "))

            if login_choice == 1:                       # To login as admin
                email_id = input("Please enter your user id : ")            
                password = input("Please enter your password : ")
                variable = login("manager.json", email_id, password)
                if variable:
                    print("login Successful")
                    
                    while True:
                        admin_choice = int(input("\n1 : Create Model \n2 : View Model \n3 : Edit Model \n4 : Delete Model \n0 : Exit \nYour Choice : "))
                        if admin_choice == 1:           # To create model   
                            model_id = random.randint(10000, 20000)
                            model_name = input("Enter model name : ")
                            model_start_date = input("Enter model start date (YYYY-MM-DD) : ")
                            model_end_date = input("Enter model end date (YYYY-MM-DD) : ")

                            model_name_re = re.findall(r'^[A-Za-z]{2,15}[A-Za-z]{2,15}$', model_name)
                            model_start_date_re = re.findall(r'^[0-9]{4}[-][0-9]{2}[-][0-9]{2}$', model_start_date)
                            model_end_date_re = re.findall(r'^[0-9]{4}[-][0-9]{2}[-][0-9]{2}$', model_end_date)

                            if model_name_re and model_start_date_re and model_end_date_re:
                                var = create_model("model.json", model_id, model_name, model_start_date, model_end_date)
                                if var:
                                    print("successfully added")
                                else:
                                    print("registration unsuccessfull") 
                        
                            else:
                                if not model_name_re:
                                    print("Entered name format is incorrect (python)")
                                    continue
                                if not model_start_date_re:
                                    print("Entered date format is incorrect")
                                    continue
                                if not model_end_date_re:
                                    print("Entered date format is incorrect")
                                    continue

                        if admin_choice == 2:           # To view model
                            var = view_model("model.json")
                            for i in var:
                                print(i)
                                

                        if admin_choice == 3:           # To Update model
                            model_id = int(input("Please enter model id : "))
                            var = update_model("model.json",model_id)
                            if var:
                                print("Model Updated successfully")
                            else:
                                print("Model did not get updated")


                        if admin_choice == 4:           # To Delete Model
                            model_id = int(input("Please enter model id : "))
                            var = delete_model("model.json", model_id)
                            if var:
                                print("Model deleted successfully")
                            else:
                                print("model is not deleted, please check")


                        if admin_choice == 0:
                            print("Bye, Have a nice day!!")     
                            quit()      


                else:
                    print("login unsuccessful")
 

            if login_choice == 2:                       # To login as user or student
                email_id = input("Please enter your user id : ")            
                password = input("Please enter your password : ")
                variable = login("student.json", email_id, password)
                if variable:
                    print("login Successful")
                else:
                    print("login unsuccessful")


            if login_choice == 3:
                print("Bye, Have a nice day!!")     
                quit()      

        if choice == 3:
            print("Bye, Have a nice day!!")
            quit()
