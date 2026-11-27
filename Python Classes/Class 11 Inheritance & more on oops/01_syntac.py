class Employee :
    company = "BrandLocus"
    language = "Python"

    def e_details(self):
            print(f'The Employee Name is Default Name and he is working in {self.company} and he works on a {self.language} language .')


class Programmer(Employee):

      def check(self):
            print('He is the one of the best employee.')


a = Programmer()
a.e_details()
a.check()