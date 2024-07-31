'''

@Author:Naveen Madev Naik
@Date: 2024-07-31 15:20:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-31 15:20:00
@Title :Check Employee is Present or Absent


'''


import random

def display_welcome_message():


    """
    Description:
        will print the welcome message

    Paramater:
        None

    Return:
        None        
    """


    print("Hello Everyone welcome to Employee Wage Computation")


def check_attendence():


    """
    Description:
        function return Absent or present based on random value generated

    Parameter:
        None

    Return:
        None  
    """


    random_value=random.randint(0,1)
    if random_value==0:
        print("Employee is Absent")
    else:
        print("Employee is Present")
    

def main():
    try:
        check_attendence()

    except Exception as e:
        print(e)    
    
if __name__=="__main__":
    display_welcome_message()
    main()