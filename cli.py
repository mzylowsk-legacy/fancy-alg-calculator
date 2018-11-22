import sys


class Cli:
    def __init__(self):
        self.user_arguments = self.get_all_arguments()

    @staticmethod
    def get_all_arguments():
        return sys.argv

    def get_rest_arguments(self):
        if len(self.user_arguments) > 2:
            return self.user_arguments[2::]
        return []

    def get_first_arg(self):
        if len(self.user_arguments) > 1:
            return self.user_arguments[1]
        else:
            raise NameError("ERROR: You have to specify at least alg id!")
