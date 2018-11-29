from executions.execution import Execution


class Modulo(Execution):
    def __init__(self, name, desc):
        super().__init__(name, desc)
        self.result = None

    def execute(self, args):
        self.result = int(args[0]) % int(args[1])

    def print(self):
        super().print()
        print(str(self.result))
