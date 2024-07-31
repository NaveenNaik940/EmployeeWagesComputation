'''

@Author:Naveen Madev Naik
@Date: 2024-07-31 15:20:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-31 
@Title :Calculating employee Wages for a Month(20days)


'''


import random

WAGE_PER_HOUR=20
FULL_TIME_HOUR=8
PART_TIME_HOUR=4
WORKING_DAY=20

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
        Boolean 
    """


    random_value=random.randint(0,1)
    if random_value==0:
        return False
    else:
        return True
    

def calculate_employee_wage(wage_per_hour,work_hour,working_day):


    """
    Description:
        function will return the employee wage 

    Parameter:
        wage_per_hour:employee's wage per hour
        work_hour:employee's working hour
        working_day:employee's working day

    Return:
        None
    """

    print(f"employee wage is: {wage_per_hour*work_hour*working_day}$\n")


def main():
    try:
        no_of_employee=int(input("enter number of employees you want to check their wages: "))
        if no_of_employee<1:
            raise ValueError("Enter positive integer greater than 0")   
        for index in range(no_of_employee):
            print(f"enter employee {index+1} type: full time(f,F) or part time(p,P)")
            employee_type=input("F,f/p,P: ")[0]
            if employee_type not in "fFpP":
                raise ValueError("enter proper employee type")
            if employee_type=="p" or employee_type=='P':
                if check_attendence():
                    print(f"Employee {index+1} Present and his wage:")
                    calculate_employee_wage(WAGE_PER_HOUR,PART_TIME_HOUR,WORKING_DAY)
                else:    
                    print(f"Employee {index+1}is Absent and his wage: {0}$")
            else:
                if check_attendence():
                    print(f"Employee {index+1} Present and his wage:")
                    calculate_employee_wage(WAGE_PER_HOUR,FULL_TIME_HOUR,WORKING_DAY)
                else:    
                    print(f"Employee {index+1}is Absent and his wage: {0}$")    

    except Exception as e:
        print(e)    


if __name__=="__main__":
    display_welcome_message()
    main()