'''

@Author:Naveen Madev Naik
@Date: 2024-08-01 15:20:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-08-01 
@Title :Calculate Employee Wages till a condition of total working hours or days is reached for a month


'''


import random

WAGE_PER_HOUR=20
FULL_TIME_HOUR=8
PART_TIME_HOUR=4
WORKING_DAY=20
TOTAL_WORKING_HOUR=100

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


def is_part_time_or_full_time():
    """
    Description:
        The function wil return part time or full time

    Parameter:
        None

    Return:
        string    
    """

    employee_type=random.choice(["Part_time","Full_time"])
    return employee_type


def is_present():


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
    

def employee_daily_wage(wage_per_hour,work_hour):


    """
    Description:
        function will return the employee wage per day 

    Parameter:
        wage_per_hour:employee's wage per hour
        work_hour:employee's working hour

    Return:
        int
    """

    return (int)(work_hour*wage_per_hour)


def main():
    try:
        print("Employee Wage for the month: ")

        work_day=1
        work_hour=0
        wage_list=[]
        total_wage=0
        while work_hour<=TOTAL_WORKING_HOUR and  work_day<=WORKING_DAY:
            if is_present():
                if is_part_time_or_full_time()=="Full_time":
                    work_hour+=FULL_TIME_HOUR
                    wage_list.append(employee_daily_wage(WAGE_PER_HOUR,FULL_TIME_HOUR))
                    total_wage+=employee_daily_wage(WAGE_PER_HOUR,FULL_TIME_HOUR)
                else:
                     work_hour+=PART_TIME_HOUR   
                     wage_list.append(employee_daily_wage(WAGE_PER_HOUR,PART_TIME_HOUR))
                     total_wage+=employee_daily_wage(WAGE_PER_HOUR,PART_TIME_HOUR)
                work_day+=1     

            else:
                wage_list.append(0)
                work_day+=1

        print("wage list of Employee($):") 
        print(wage_list) 
        print(f"total wage: {total_wage}$")      

    except Exception as e:
        print(e)    


if __name__=="__main__":
    display_welcome_message()
    main()