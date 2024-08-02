'''

@Author:Naveen Madev Naik
@Date: 2024-08-02 15:20:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-08-02 
@Title :Compute Employee Wage for multiple companies

'''


import random

class EmployeeWage:

    def __init__(self, wage_per_hour, full_time_hour, part_time_hour, working_day, total_working_hour):
        self.wage_per_hour = wage_per_hour
        self.full_time_hour = full_time_hour
        self.part_time_hour = part_time_hour
        self.working_day = working_day
        self.total_working_hour = total_working_hour


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
                if self.is_present():
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
    

def main():
    EmployeeWage.display_welcome_message()
    companies = [
        {"name": "BridgeLabz", "wage_per_hour": 15, "full_time_hour": 8, "part_time_hour": 4, "working_days": 24, "total_working_hours": 100},
        {"name": "Truemind", "wage_per_hour": 22, "full_time_hour": 8, "part_time_hour": 4, "working_days": 22, "total_working_hours": 110},
        {"name": "Accenture", "wage_per_hour": 18, "full_time_hour": 8, "part_time_hour": 4, "working_days": 25, "total_working_hours": 120}
    ]
    wage_dict={}
    for company in companies:
        print(f"\nComputing wages for {company['name']}:")
        employee_wage = EmployeeWage(
            wage_per_hour=company["wage_per_hour"],
            full_time_hour=company["full_time_hour"],
            part_time_hour=company["part_time_hour"],
            working_day=company["working_days"],
            total_working_hour=company["total_working_hours"]
        )
        wage_dict[company['name']]=employee_wage.compute_wages()
        print(f"Employee wages list in {company['name']}: ")
        print(wage_dict[company['name']]['wage_list'])
        print(f"total wage: {wage_dict[company['name']]['total_wage']}$")
      


if __name__ == "__main__":
    main()
