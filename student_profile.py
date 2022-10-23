from calendar import c
import sqlite3



#create a profile
#it will take first name and last name as parameters
def create_profile():

    conn = sqlite3.connect('profile.db')

    connect = conn.cursor()

    firstname = input("Please enter first  name: ").title()
    lastname = input("Please enter last  name: ").title()

    title = input("Please enter your title: ").title()
    
    major = input("Please enter your major: ").title()

    university = input("Please enter your university name: ").title()

    information = input("Please enter information about yourself:").title()

    print("\nEnter your experience! \n")
    jobTitle1 = input("Please enter your first past job: ").title()
    jobEmployer1 = input("Please enter your first past job employer: ").title()
    startingDate1 = input("Date started: ").title()
    endingDate1 = input("Date ended: ").title()
    location1 = input("Location: ").title()
    description1 = input("Enter description: ").title()

    jobTitle2 = input("Please enter your second past job: ").title()
    jobEmployer2 = input("Please enter your first past job employer: ").title()
    startingDate2 = input("Date started: ").title()
    endingDate2 = input("Date ended: ").title()
    location2 = input("Location: ").title()
    description2 = input("Enter description: ").title()

    jobTitle3 = input("Please enter your third past job: ").title()
    jobEmployer3 = input("Please enter your first past job employer: ").title()
    startingDate3 = input("Date started: ").title()
    endingDate3 = input("Date ended: ").title()
    location3 = input("Location: ").title()
    description3 = input("Enter description: ").title()

    print("\nYour Education!\n")
    schoolName = input("Enter your school name: ").title()
    degree = input("Enter your degree: ").title()
    years = input("Enter your years attended: ").title()
    

  

    connect.execute("""CREATE TABLE profile (
                    firstname_db text,
                    lastname_db text,
                    title_db text,
                    major_db text,
                    university_db text,
                    information_db text,
                    jobTitle1_db text,
                    employer1_db text,
                    startingDate1_db text,
                    endingDate1_db text,
                    location1_db text,
                    description1_db text,
                    jobTitle2_db text,
                    employer2_db text,
                    startingDate2_db text,
                    endingDate2_db text,
                    location2_db text,
                    description2_db text,
                    jobTitle3_db text,
                    employer3_db text,
                    startingDate3_db text,
                    endingDate3_db text,
                    location3_db text,
                    description3_db text,
                    schoolName_db text,
                    degree_db text,
                    years_db text

                    )""")


    connect.execute("INSERT INTO profile VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
    (firstname, lastname, title, major, university, information, jobTitle1, jobEmployer1, startingDate1, endingDate1, location1, description1, 
    jobTitle2, jobEmployer2, startingDate2, startingDate2, location2, description2, jobTitle3, jobEmployer3, startingDate3, endingDate3,
     location3, description3, schoolName, degree, years))


    # connect.execute("SELECT * FROM profile WHERE firstname_db = 'ABC' ")

    # print(connect.fetchall())

    conn.commit()

    conn.close()



#it may take first name or both first name and last name
def display_profile(first_name):

    #condition:
    #if they're friends, display below
    #if not, display nothing 
    #if they're friends, but this person hasn't completed their profile, also display nothing

    first_name = first_name.title()

    new_firstname = (first_name,)
    conn = sqlite3.connect('profile.db')

    connect = conn.cursor()


    connect.execute("SELECT * FROM profile WHERE firstname_db =?", new_firstname)

    data = connect.fetchall()

    print(data)

    for x in data:
        print("___________________________________")
        print("Name: " + x[0] + ' ' + x[1])
        print("")
        print("Title: " + x[2])
        print("Major: " + x[3])
        print("University: " + x[4])
        print("Information: " + x[5])
        print("")
        print("First Job: " + x[6])
        print("FIrst Job Employer: " + x[7])
        print("Starting Date: " + x[8])
        print("Ending Date: " + x[9])
        print("Location: " + x[10])
        print("Description About The Job: " + x[11])
        print("")
        print("Second Job: " + x[12])
        print("Second Job Employer: " + x[13])
        print("Starting Date: " + x[14])
        print("Ending Date: " + x[15])
        print("Location: " + x[16])
        print("Description About The Job: " + x[17])
        print("")
        print("Third Job: " + x[18])
        print("Thid Job Employer: " + x[19])
        print("Starting Date: " + x[20])
        print("Ending Date: " + x[21])
        print("Location: " + x[22])
        print("Description About The Job: " + x[23])
        print("")
        print("School Name: " + x[24])
        print("Degree: " + x[25])
        print("Years: " + x[26])



   

create_profile()

display_profile('ABC')

