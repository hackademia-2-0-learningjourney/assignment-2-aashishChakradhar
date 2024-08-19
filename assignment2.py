'''
    Assignment 2:
    WAP that first gives 2 options: 
    1. Sign up 
    2. Sign in 

    when 1 is pressed user needs to provide following information 
    1. Username, 2. Password, 3. Mobile number 
    All this information is saved in a file everytime a new user signs up the same file is updated 
    (hint Append over the same file)

    when 2 is pressed 
    User needs to provide username and password 
    this username and password is checked with username and password in the database
    if matched: 
    welcome to the device and show their phone number 
    else: 
    terminate the program saying incorrect credentials 


    Do it using json files, save everything to json and load from json 
'''

import json
import os

userDetail = {}

os.system('clear')

while True:
    found = False
    print('----'*20)
    choice = int(input('1. Sign Up\n2. Sign In\n0. Exit\nEnter your choice: '))
    print('----'*20)
    
    # to create json file it doesnot exists
    try:
        with open ('assignments/user_json.json','r') as jsonCheck:
            pass
    except:
        with open ('assignments/user_json.json','w') as jsonCreate:
            json.dump({},jsonCreate)
    
    os.system('clear')

    # for sign up 
    if choice == 1:
        print('----'*20)
        username = input('username:\t')
        password = input('password:\t')
        phone = input('phone:\t')
        print('----'*20)
        
        try:
            with open ('assignments/user_json.json','r') as jsonRead:
                userDetail = json.load(jsonRead)
            userDetail.update({
                username : {
                    'password' : password,
                    'phone' : phone,
                },
            })
        except:
            print('=='*25)
            print(f'File not found!!')
            print('=='*25)

        with open ('assignments/user_json.json','w') as jsonWrite:
            json.dump(userDetail,jsonWrite)
            os.system('clear')
            print('=='*25)
            print('User Created Successfully')
            print('=='*25)

    # for sign in 
    elif choice == 2:
        print('----'*20)
        username = input('username:\t')
        password = input('password:\t')
        print('----'*20)
        try: 
            with open('assignments/user_json.json','r') as jsonRead:
                detail = json.load(jsonRead)

            for db_username,db_auth in detail.items():
                os.system('clear')
                if db_username == username:
                    found = True
                    if db_auth['password'] == password:
                        print('=='*25)
                        print(f'Welcome to this device!!!\nPhone number: {db_auth['phone']}')
                        print('=='*25)
                        break
                    else:
                        print('=='*25)
                        print(f'Invalid Password')
                        print('=='*25)
                        break
            if not found:
                print('=='*25)
                print(f'User Not Found')
                print('=='*25)
        except:
            print('=='*25)
            print(f'No Users found!!\nPlease create an account first.')
            print('=='*25)

    # exit case
    else:
        break
