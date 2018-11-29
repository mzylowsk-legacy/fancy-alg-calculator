class Execution:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def print(self):
        print("========= %s =========" % self.name)
        print(self.description)
        print("========= Run results =========")

    def execute(self, args):
        pass
