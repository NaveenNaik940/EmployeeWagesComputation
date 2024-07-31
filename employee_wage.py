'''

@Author:Naveen Madev Naik
@Date: 2024-07-31 15:20:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-31 
@Title :Add Part time Employee & Wage


'''


import random

WAGE_PER_HOUR=20
FULL_DAY_HOUR=8
PART_TIME_HOUR=4

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
        return 0
    else:
        return 1
    

def calculate_employee_wage(wage_per_hour,work_hour):


    """
    Description:
        function will return the employee wage 

    Parameter:
        wage_per_hour:employee's wage per hour
        work_hour:employee's working hour

    Return:
        None
    """

    print(f"employee wage is: {wage_per_hour*work_hour}$")


def main():
    try:
        print("Part time employee wage details:")
        if check_attendence()==1:
            print(f"Employee is Present")
            calculate_employee_wage(WAGE_PER_HOUR,PART_TIME_HOUR)
        else:
            print(f"Employee is Absent") 
            print(f"employee wage is: {0}$") 

        print("\nFull time employee wage details:")
        if check_attendence()==1:
            print(f"Employee is Present")
            calculate_employee_wage(WAGE_PER_HOUR,FULL_DAY_HOUR)
        else:
            print(f"Employee is Absent") 
            print(f"employee wage is: {0}$")    

    except Exception as e:
        print(e)    


if __name__=="__main__":
    display_welcome_message()
    main()