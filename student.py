class student:
    college_name="BGSIT"
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
    @classmethod
    def change_college(cls,new_name):
        cls.college_name=new_name
    def is_pass(marks):
        if marks>=35:
            return "Pass"
        else:
            return "Fail"
    def display(self):
        print("name:",self.name)
        print("roll no:",self.roll_no)
s1=student("Poorvi","114")
s2=student("Priya","115")
s1.display()
s2.display()
print(student.college_name)
student.change_college("JSS College")
print(s1.college_name)
student.is_pass(40)
student.is_pass(30)
