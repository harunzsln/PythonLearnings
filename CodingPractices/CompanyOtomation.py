class Company():
    def __init__(self, name):
        self.name = name
        self.running = True

    def program(self):
        choose = self.Menu()

        if choose == 1:
            self.AddEmployee()
        if choose == 2:
            self.FireEmployee()
        if choose == 3:
            monthOrYear = input("Do you want to see yearly salary to be paid? (Y/N): ")
            if monthOrYear.lower() == "y":
                self.ShowSalaryToBePaid(calcultion="y")
            else:
                self.ShowSalaryToBePaid()
        if choose == 4:
            self.GiveSalary()
        if choose == 5:
            self.AddCost()
        if choose == 6:
            self.AddIncome()
        if choose == 7:
            self.running = False

    def Menu(self):
        choose = int(input("****Welcome to Otomation of {} ****\n\n1. Add Employee\n2. Fire Employee\n3. Show Salary\n4. Give Salary\n5. Add Cost\n6. Add Income\n7. Exit\n\nChoose an option: ".format(self.name)))
        while choose < 1 or choose > 7 :
            choose = int(input("Invalid option. Please choose between 1 - 7 : "))
        return choose

    def AddEmployee(self):
        name = input("Enter employee name: ")
        surname = input("Enter employee surname: ")
        age = input("Enter employee age: ")
        gender = input("Enter employee gender (M/F): ")
        salary = input("Enter employee salary: ")

        with open("employees.txt","r") as file:
            employeeList = file.readlines()

        if len(employeeList) == 0:
            employeeID = 1
        else:
            with open("employees.txt", "r") as file:
                employeeID = int(file.readlines()[-1].split(")")[0]) + 1

        with open("employees.txt","a+") as file:
            file.write("{}){}-{}-{}-{}-{}\n".format(employeeID,name,surname,age,gender,salary))    

    def FireEmployee(self):
        with open("employees.txt","r") as file:
            employeeList = file.readlines()

        EmpInfo = []

        for employee in employeeList:
            EmpInfo.append(" ".join(employee[:-1].split("-")))

        for employee in EmpInfo:
            print(employee)

        choose = int(input("Enter the employee ID to be fired( 1-{}: ".format(len(EmpInfo))))
        while choose < 1 or choose > len(EmpInfo):
            choose = int(input("Invalid option. Please choose between 1 - {} : ".format(len(EmpInfo))))

        employeeList.pop(choose-1)

        counter = 1

        NewEmpList = []

        for employee in employeeList:
            NewEmpList.append(str(counter) + ")" + employee.split(")")[1])
            counter += 1

        with open("employees.txt","w") as file:
            file.writelines(NewEmpList)

    def ShowSalaryToBePaid(self,calcultion = "m" ):
        """calcultion: m = monthly, y = yearly"""
        with open("employees.txt","r") as file:
            employeeList = file.readlines()

        salaries = []

        for employee in employeeList:
            salaries.append(int(employee.split("-")[-1]))
        if calcultion == "m":
            print("Total salary to be paid in this month: {}".format(sum(salaries)))
        else:
            print("Total salary to be paid in this year: {}".format(sum(salaries)*12))
    def GiveSalary(self):
        pass

    def AddCost(self):
        pass

    def AddIncome(self):
        pass


company = Company("HarunTech")

while company.running:
    company.program()
