class student:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

    def getdata(self):
        self.name = input("enter your name ")
        self.mark = input("enter your mark ")

    def putdata(self):
        print("name: ", self.name)
        print("mark: ", self.mark)


obj = student("", "")
obj.getdata()
obj.putdata()
