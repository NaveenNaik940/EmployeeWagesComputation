'''

@Author:Naveen Madev Naik
@Date: 2024-08-01 15:20:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-08-01 
@Title :Refactoring the Code to write a Class Method to Compute Employee Wage

'''


import random

class EmployeeWage:
    WAGE_PER_HOUR = 20
    FULL_TIME_HOUR = 8
    PART_TIME_HOUR = 4
    WORKING_DAY = 20
    TOTAL_WORKING_HOUR = 100
     
    @staticmethod
    def display_welcome_message(cls):
        
        
        """
        Description:
            Will print the welcome message.

        Parameter:
            cls: Represents the class itself.

        Return:
            None        
        """
        
        
        print("Hello Everyone welcome to Employee Wage Computation")

    @classmethod
    def is_part_time_or_full_time(cls):
        
        
        """
        Description:
            The function will return part time or full time.

        Parameter:
            cls: Represents the class itself.

        Return:
            string    
        """
        
        
        return random.choice(["Part_time", "Full_time"])

    @classmethod
    def is_present(cls):
        
        
        """
        Description:
            Function return Absent or present based on random value generated.

        Parameter:
            cls: Represents the class itself.

        Return:
            Boolean 
        """
        
        
        return random.choice([True, False])

    @classmethod
    def employee_daily_wage(cls, wage_per_hour, work_hour):
        
        
        """
        Description:
            Function will return the employee wage per day.

        Parameter:
            cls: Represents the class itself.
            wage_per_hour: employee's wage per hour
            work_hour: employee's working hour

        Return:
            int
        """
        
        
        return work_hour * wage_per_hour
    @classmethod
    def compute_wages(cls):
        
        
        """
        Description:
            Computes the wages for the employee for a month.

        Parameter:
            cls: Represents the class itself.

        Return:
            None
        """
        
        
        try:
            work_day = 1
            work_hour = 0
            wage_list = []
            total_wage = 0
            print("Employee Wage for the month:")

            while work_hour <= cls.TOTAL_WORKING_HOUR and work_day <= cls.WORKING_DAY:
                if EmployeeWage.is_present():
                    if EmployeeWage.is_part_time_or_full_time() == "Full_time":
                        work_hour += cls.FULL_TIME_HOUR
                        daily_wage = EmployeeWage.employee_daily_wage(cls.WAGE_PER_HOUR, cls.FULL_TIME_HOUR)
                    else:
                        work_hour += cls.PART_TIME_HOUR
                        daily_wage = EmployeeWage.employee_daily_wage(cls.WAGE_PER_HOUR, cls.PART_TIME_HOUR)

                    wage_list.append(daily_wage)
                    total_wage += daily_wage
                else:
                    wage_list.append(0)
                
                work_day += 1

            print("Wage list of Employee ($):")
            print(wage_list)
            print(f"Total wage: {total_wage}$")

        except Exception as e:
            print(e)

def main():
    EmployeeWage.display_welcome_message()
    EmployeeWage.compute_wages()


if __name__ == "__main__":
    main()
