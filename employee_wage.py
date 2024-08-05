'''

@Author:Naveen Madev Naik
@Date: 2024-08-04 15:20:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-08-04 
@Title :Compute Employee Wage for multiple companies and Ability to manage wage for multiple companies with CRUD operations for companies and employees

'''


import random

class Employee:
    def __init__(self, name):
        self.employee_name = name
        self.total_wage = 0
        self.wage_list = []

    def __str__(self):
        return f"Employee: {self.employee_name}, Total Wage: {self.total_wage}, Wage List: {self.wage_list}"

class CompanyEmpWage:
    def __init__(self, company_name, wage_per_hour, full_time_hour, part_time_hour, working_day, total_working_hour):
        self.company_name = company_name
        self.wage_per_hour = wage_per_hour
        self.full_time_hour = full_time_hour
        self.part_time_hour = part_time_hour
        self.working_day = working_day
        self.total_working_hour = total_working_hour
        self.employees = []

    def add_employee(self, employee):

        """
        Descriptionn:
            function adds the employee to employee list

        Parameter:
            employee:input from user 

        Return:
            None
        """

        self.employees.append(employee)

    def remove_employee(self, employee_name):


        """
        Descriptionn:
            function removes the employee from employee list

        Parameter:
            employee_name:name of employee which want to remove from employee list 

        Return:
            None
        """

        self.employees = [emp for emp in self.employees if emp.name != employee_name]


    def update_employee(self, old_name, new_name):


        """
        Descriptionn:
            function updates the employee name from old name to new name in  employee list

        Parameter:
            old_name:old name of employee
            new_name:new name of employee 
        
        Return:
            None
        """

        employee = self.get_employee(old_name)
        if employee:
            employee.name = new_name


    def get_employee(self, employee_name):


        """
        Descriptionn:
            function will get the employee information

        Parameter:
            employee_name:input from user 

        Return:
            string
        """  


        for employee in self.employees:
            if employee.name == employee_name:
                return employee
        return None


    def __str__(self):
        return (f"Company: {self.company_name}, Wage Per Hour: {self.wage_per_hour}, "
                f"Full Time Hour: {self.full_time_hour}, Part Time Hour: {self.part_time_hour}, "
                f"Working Day: {self.working_day}, Total Working Hour: {self.total_working_hour}, "
                f"Employees: {[str(emp) for emp in self.employees]}")


class EmpWageBuilder:
    def __init__(self):
        self.company_emp_wage_list = []

    def add_company_emp_wage(self, company_emp_wage):

        """
        Descriptionn:
            function adds the company employee wage to company wage list

        Parameter:
            company_emp_wage:input from user that is company employee wage

        Return:
            None
        """

        self.company_emp_wage_list.append(company_emp_wage)


    def remove_company_emp_wage(self, company_name):

        """
        Descriptionn:
            function removes the company name from company wage list

        Parameter:
            company_name:input from user to remove its details from list 

        Return:
            None
        """

        self.company_emp_wage_list = [company for company in self.company_emp_wage_list if company.company_name != company_name]

    def update_company_emp_wage(self, old_company_name, new_company_emp_wage):

        """
        Descriptionn:
            function updates the old company name to new company name from company wage list

        Parameter:
            old_company_name:input from user that old company name
            new_company_name:input from user that is new company name 

        Return:
            None
        """

        for index, company in enumerate(self.company_emp_wage_list):
            if company.company_name == old_company_name:
                self.company_emp_wage_list[index] = new_company_emp_wage



    def get_company_emp_wage(self, company_name):

        """
        Descriptionn:
            function gets the company details from company wage list

        Parameter:
            company_name:input from user to get its details from list 

        Return:
            dict
        """    
        for company in self.company_emp_wage_list:
            if company.company_name == company_name:
                return company
        return None


    def compute_wages(self):

        
        """
        Description:
            Computes the wages for the employee for a month different company and its employee.

        Parameter:
            self: Represents the instance of class.

        Return:
            None
        """
        for company in self.company_emp_wage_list:
            for employee in company.employees:
                self.compute_monthly_wage(company, employee)


    @staticmethod
    def get_employee_type():

        """
        Description:
            The function will return whether employee is part time or full time.

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

    @staticmethod
    def employee_daily_wage(wage_per_hour, work_hour):
        
        
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


    def compute_monthly_wage(self, company, employee):
        
        """
        Description:
            Computes the wages for the employee in a company  for a month.

        Parameter:
            self: Represents the instance of class.
            company:dict of company details
            employee:dict of employee details

        Return:
            None
        """        
        work_day = 1
        work_hour = 0
        total_wage = 0

        while work_hour <= company.total_working_hour and work_day <= company.working_day:
            if self.is_present() == "Present":
                daily_work_hours = company.full_time_hour if self.get_employee_type() == "Full_time" else company.part_time_hour
                work_hour += daily_work_hours
                daily_wage = self.employee_daily_wage(company.wage_per_hour, daily_work_hours)
                employee.wage_list.append(daily_wage)
                total_wage += daily_wage
            else:
                employee.wage_list.append(0)
            work_day += 1

        employee.total_wage = total_wage
        print(f"\n{employee.name}'s Wage List: {employee.wage_list}")
        print(f"Total wage for {employee.name} in {company.company_name}: ${employee.total_wage}")

def main():
    try:
        empBuilder = EmpWageBuilder()
        
        while True:
            print("\n1. Add Company\n2. Update Company\n3. Delete Company\n4. Manage Employees\n5. Compute Wages\n6. Display Companies\n7. Exit")
            choice = int(input("Enter your choice(integer): "))

            if choice == 1:
                company_name = input("Enter company name: ").upper()
                wage_per_hour = int(input("Enter wage per hour: "))
                full_time_hour = int(input("Enter full-time hours: "))
                part_time_hour = int(input("Enter part-time hours: "))
                working_day = int(input("Enter working days: "))
                total_working_hour = int(input("Enter total working hours: "))
                new_company = CompanyEmpWage(company_name, wage_per_hour, full_time_hour, part_time_hour, working_day, total_working_hour)
                empBuilder.add_company_emp_wage(new_company)

            elif choice == 2:
                old_company_name = input("Enter the name of the company to update: ").upper()
                company = empBuilder.get_company_emp_wage(old_company_name)
                if company:
                    company_name = input("Enter new company name: ").upper()
                    wage_per_hour = int(input("Enter new wage per hour: "))
                    full_time_hour = int(input("Enter new full-time hours: "))
                    part_time_hour = int(input("Enter new part-time hours: "))
                    working_day = int(input("Enter new working days: "))
                    total_working_hour = int(input("Enter new total working hours: "))
                    updated_company = CompanyEmpWage(company_name, wage_per_hour, full_time_hour, part_time_hour, working_day, total_working_hour)
                    empBuilder.update_company_emp_wage(old_company_name, updated_company)
                else:
                    print("Company not found!")

            elif choice == 3:
                company_name = input("Enter the name of the company to delete: ").upper()
                empBuilder.remove_company_emp_wage(company_name)
                print(f"Company {company_name} is  removed from database.")

            elif choice == 4:
                company_name = input("Enter the name of the company to manage employees: ").upper()
                company = empBuilder.get_company_emp_wage(company_name)
                if company:
                    while True:
                        print("\n1. Add Employee\n2. Update Employee\n3. Delete Employee\n4. Back to Main Menu")
                        emp_choice = int(input("Enter your choice(integer): "))

                        if emp_choice == 1:
                            emp_name = input("Enter employee name: ").upper()
                            new_employee = Employee(emp_name)
                            company.add_employee(new_employee)

                        elif emp_choice == 2:
                            old_emp_name = input("Enter the name of the employee to update: ").upper()
                            new_emp_name = input("Enter new employee name: ").upper()
                            company.update_employee(old_emp_name, new_emp_name)

                        elif emp_choice == 3:
                            emp_name = input("Enter the name of the employee to delete: ").upper()
                            company.remove_employee(emp_name)
                            print(f"Employee {emp_name} removed from {company.company_name}.")

                        elif emp_choice == 4:
                            break

                        else:
                            print("Invalid choice! Please try again.")
                else:
                    print("Company not found!")

            elif choice == 5:
                empBuilder.compute_wages()

            elif choice == 6:
                for company in empBuilder.company_emp_wage_list:
                    print(company)

            elif choice == 7:
                break

            else:
                print("Invalid choice! Please try again.")

    except ValueError as e:
        print(f"enter integer input.{e}")      
    except Exception as e:
        print(e)          

if __name__ == "__main__":
    main()
