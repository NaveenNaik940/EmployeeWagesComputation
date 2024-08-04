'''

@Author:Naveen Madev Naik
@Date: 2024-08-04 15:20:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-08-04 
@Title :Compute Employee Wage for multiple companies and Ability to manage Employee Wage of multiple companies

'''


import random

class EmployeeWage:

    def __init__(self, wage_per_hour, full_time_hour, part_time_hour, working_day, total_working_hour):
        self.wage_per_hour = wage_per_hour
        self.full_time_hour = full_time_hour
        self.part_time_hour = part_time_hour
        self.working_day = working_day
        self.total_working_hour = total_working_hour


    def compute_wages(self):
        
        
        """
        Description:
            Computes the wages for the employee for a month.

        Parameter:
            self: Represents the instance of class.

        Return:
            dictionary
        """
        
        
        try:
            work_day = 1
            work_hour = 0
            wage_list = []
            total_wage = 0
            wages_dict={}

            while work_hour <= self.total_working_hour and work_day <= self.working_day:
                if EmployeeWage.is_present():
                    if EmployeeWage.is_part_time_or_full_time() == "Full_time":
                        work_hour += self.full_time_hour
                        daily_wage = EmployeeWage.employee_daily_wage(self.wage_per_hour, self.full_time_hour)
                    else:
                        work_hour += self.part_time_hour
                        daily_wage = EmployeeWage.employee_daily_wage(self.wage_per_hour, self.part_time_hour)

                    wage_list.append(daily_wage)
                    total_wage += daily_wage
                else:
                    wage_list.append(0)
                
                work_day += 1
            
            wages_dict={"wage_list":wage_list,"total_wage":total_wage}
            return wages_dict
        except Exception as e:
            print(e)


    @staticmethod
    def display_welcome_message():
        
        
        """
        Description:
            Will print the welcome message.

        Parameter:
            None
        Return:
            None        
        """
        
        
        print("Hello Everyone welcome to Employee Wage Computation")


    @staticmethod
    def is_part_time_or_full_time():
        
        
        """
        Description:
            The function will return part time or full time.

        Parameter:
            None.

        Return:
            str:Part_time or Full_time    
        """
        
        
        return random.choice(["Part_time", "Full_time"])

    @staticmethod
    def is_present():
        
        
        """
        Description:
            Function return Absent or present based on random value generated.

        Parameter:
            None

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
    



class EmpWageBuilder:
    def __init__(self):
        self.company_wages = {}

    def add_company(self, company_name, wage_per_hour, full_time_hour, part_time_hour, working_day, total_working_hour):


        """
        Description:
            Adds a company to the wage builder.

        Parameters:
            company_name (str): The name of the company
            wage_per_hour (int): Wage per hour for the company
            full_time_hour (int): Full-time hours for the company
            part_time_hour (int): Part-time hours for the company
            working_day (int): Number of working days for the company
            total_working_hour (int): Total working hours for the company

        Return:
            None
        """


        employee_wage = EmployeeWage(
            company_name=company_name,
            wage_per_hour=wage_per_hour,
            full_time_hour=full_time_hour,
            part_time_hour=part_time_hour,
            working_day=working_day,
            total_working_hour=total_working_hour
        )
        self.company_wages[company_name] = employee_wage

    def compute_wages(self):


        """
        Description:
            Computes the wages for all added companies.

        Parameter:
            None

        Return:
            None
        """

        
        for company, employee_wage in self.company_wages.items():
            wages = employee_wage.compute_wages()
            print(f"\nComputing wages for {company}:")
            print(f"Employee wages list in {company}: ")
            print(wages['wage_list'])
            print(f"Total wage: {wages['total_wage']}$")


class EmpWageBuilder:

    def __init__(self):
        self.company_wages = {}

    def add_company(self, company_name, wage_per_hour, full_time_hour, part_time_hour, working_day, total_working_hour):
        """
        Description:
            Adds a company to the wage builder.

        Parameters:
            company_name (str): The name of the company
            wage_per_hour (int): Wage per hour for the company
            full_time_hour (int): Full-time hours for the company
            part_time_hour (int): Part-time hours for the company
            working_day (int): Number of working days for the company
            total_working_hour (int): Total working hours for the company

        Return:
            None
        """
        employee_wage = EmployeeWage(
            wage_per_hour=wage_per_hour,
            full_time_hour=full_time_hour,
            part_time_hour=part_time_hour,
            working_day=working_day,
            total_working_hour=total_working_hour
        )
        self.company_wages[company_name] = employee_wage

    def compute_wages(self):
        """
        Description:
            Computes the wages for all added companies.

        Parameter:
            None

        Return:
            None
        """
        for company, employee_wage in self.company_wages.items():
            wages = employee_wage.compute_wages()
            print(f"\nComputing wages for {company}:")
            print(f"Employee wages list in {company}: ")
            print(wages['wage_list'])
            print(f"Total wage: {wages['total_wage']}$")

def main():
    EmployeeWage.display_welcome_message()
    
    emp_wage_builder = EmpWageBuilder()
    no_of_company=int(input("enter the number of company you want to add : "))
    for index in range(no_of_company):
        emp_wage_builder.add_company(input("enter the company name: "), int(input("wage per hour: ")), int(input("full time hour: ")), int(input("part time hour: ")),int(input("working day :")),int(input("total working hour: ")))
        print()
    
    emp_wage_builder.compute_wages()
      


if __name__ == "__main__":
    main()
