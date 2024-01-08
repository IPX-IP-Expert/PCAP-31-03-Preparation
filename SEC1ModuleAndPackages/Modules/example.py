class ExampleModule:
    def __init__(self):
        print("ExampleModule.__init__()")
        self.name = "ExampleModule"

    def print_name(self):
        print("ExampleModule.print_name()")
        print(self.name)

    def __new__(cls):
        print("ExampleModule.__new__()")
        return super().__new__(cls)
