class Computer:
    def __init__(self):
        self.cpu = ""
        self.ram = ""
        self.storage = ""

    def show_details(self):
        print("CPU :", self.cpu)
        print("RAM :", self.ram)
        print("Storage :", self.storage)

class ComputerBuilder:
    def __init__(self):
        self.computer = Computer()
    def set_cpu(self, cpu):
        self.computer.cpu = cpu
    def set_ram(self, ram):
        self.computer.ram = ram
    def set_storage(self, storage):
        self.computer.storage = storage
    def get_computer(self):
        return self.computer

builder = ComputerBuilder()
builder.set_cpu("Intel i7")
builder.set_ram("16 GB")
builder.set_storage("512 GB SSD")
pc = builder.get_computer()
pc.show_details()