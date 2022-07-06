class Computer:
    def __init__(self, processor, os, monitor, weight):
        self.processor = processor
        self.os = os
        self.monitor = monitor
        self.weight = weight

    def get_specs(self):
        self.processor = input("Enter the name of processor ")
        self.os = input("Enter the name of Operating System ")

    def display_specs(self):
        print("________________________________________\n")
        print("Processor:", self.processor)
        print("Operating System:", self.os)


class Desktop(Computer):
    def get1(self):
        self.monitor = input("Enter your  screen display size ")

    def dis1(self):
        print("Screen Display Size:", self.monitor)


class Laptop(Desktop):
    def get2(self):
        self.weight = input("Enter your laptop weight ")

    def dis2(self):
        print("Weight:", self.weight)


obj = Laptop("", "", "", "")
obj.get_specs()
obj.get1()
obj.get2()
obj.display_specs()
obj.dis1()
obj.dis2()
