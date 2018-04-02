class Employee:
    raise_amount = 1.02

    def __init__(self, fname, lname, pay):
        self.first_name = fname
        self.last_name = lname
        self.salary = pay
        self.email = fname + '.' + lname + '@email.com'

    def fullname(self):
        return "{} {}".format(self.first_name, self.last_name)

    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amount)


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, fname, lname, pay, prog_lang):
        super().__init__(fname, lname, pay)  # this passes off the first arguments to the Employee init method
        # Employee.__init__(self, fname, lname, pay) # also works
        self.programming_lang = prog_lang


class Manager(Employee):
    def __init__(self, fname, lname, pay, employees=None):
        super().__init__(fname, lname, pay)  # this passes off the first arguments to the Employee init method
        if employees is None:
            self.employees_list = []
        else:
            self.employees_list = employees

    def add_employee(self, emp):
        if emp not in self.employees_list:
            self.employees_list.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees_list:
            self.employees_list.remove(emp)

    def print_emps(self):
        for emp in self.employees_list:
            print('-->', emp.fullname())


dev_1 = Developer('Remington', 'Henderson', 60000, 'Python')

mgr_1 = Manager('Mary', 'Jane', 9000, [dev_1])

# print(dev_1.fullname())
# dev_1.apply_raise()
# print(dev_1.salary)
# print(dev_1.programming_lang)

print(mgr_1.fullname())
print(mgr_1.print_emps())

print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Developer))
print(issubclass(Manager, Employee))