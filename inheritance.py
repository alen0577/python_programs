class student:
    def __init__(self, name, mark, hod_name):
        self.name = name
        self.mark = mark
        self.hod_name = hod_name

    def getdata(self):
        self.name = input("enter your name ")
        self.mark = input("enter your mark ")


class hod_name(student):
    def putdata(self):
        self.hod_name = input('enter name of "HOD" ')

    def display(self):
        print("name: ", self.name)
        print("mark: ", self.mark)
        print("HOD_name: ", self.hod_name)


obj = hod_name("", "", "")
obj.getdata()
obj.putdata()
obj.display()
