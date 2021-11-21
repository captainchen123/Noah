from datetime import datetime

def mainMenu():
    try:
        print("Hello and Welcome to Noah!")
        socialSecurityN = input("Please enter your social security number:")

        birthdate = socialSecurityN[0:6]
        day = int(birthdate[0:2])
        month = int(birthdate[2:4])
        year = int(birthdate[4:6])
        

        if socialSecurityN[6] == "A":
            year_complete = int(year) + 2000
        elif socialSecurityN[6] == "-":
            year_complete = int(year) + 1900
        birthDate = str((birthdate[0:2])+'/'+str(birthdate[2:4])+'/'+str(year_complete))
        age_calculation(birthDate)
        
        if int(age_calculation.age) >= 65:
            older_pop(socialSecurityN)
        else:
            younger_pop(socialSecurityN)
    except (Exception,ValueError):
        print("Please check that the entered social security number is correct.")
        return mainMenu()


def age_calculation(birthDate):
    birthdate = datetime.strptime(birthDate, '%d/%m/%Y')
    date_current = datetime.now()
    timedelta = (date_current - birthdate).days
    age_calculation.age =round(timedelta/365.2425)
    
def older_pop(socialSecurityN):
    name = input("Enter your name:")
    User_info = [socialSecurityN,":",name,":",str(age_calculation.age)]
    with open("Older.txt","a") as A:
        A.writelines(User_info)
        A.write("\n")
    print("There are two options for you to choose from:")
    print("Communicate\t\t\t1\nAlternative option\t\t2")
    try:
        selection = int(input("Select your choice:"))
        
        if selection == 1:
            select_1_older()
        elif selection == 2:
            print("This part has yet to be finished.")
            #this is to demonstrate the function of the menu,
            #different options can be added to the application later on
            #for example providing needs-based services, such as
            #contact with emergency services
            pass

    except ValueError:
        print("Please check your selection again.")
        mainMenu()

def select_1_older():
    print("Who would you like to contact?")
    print("Turku resident\t\t1\nVolunteer\t\t2")
    selection2 = int(input("Select your choice:"))
    if selection2 == 1:
        print("You will be connected with another Turku resident shortly.")

    elif selection2 == 2:
        print("A volunteer will call you shortly.")
    

#if want to contact another elderly, reads .txt file
#and asks if want to be matched based on age, interests etc?? maybe

def younger_pop(socialSecurityN):
    print("Basic information about app for younger population --> communication + community")
    name = input("Enter your name:")
    print("Interest menu:")
    interests = input("Enter some of your interests:")
    try:
        status = input("Choose your status(Free or Busy)")
        if status == "Free" or status == "busy":
            User_info = [socialSecurityN,":",name,":",str(age_calculation.age),":",interests,":",status]
            with open("younger.txt","a") as A:
                A.writelines(User_info)
                A.write("\n")
        else:
            raise ValueError
    except ValueError:
        print("Please enter Free or Busy.")
    



mainMenu() 
        
