import numbers


class AlgorithmManager:
    def __init__(self, requested_alg, alg_arguments):
        self.algorithms_list = [
            (0, "add", "dsad"),
            (1, "add", "add_element"),
            (2, "add", "add_element"),
            (3, "add", "add_element"),
            (4, "add", "add_element")
        ]
        self.alg = requested_alg
        self.args = alg_arguments

        self.convert_to_algorithm_id()

    def convert_to_algorithm_id(self):
        if isinstance(self.alg, numbers.Number):
            for (x, y, z) in self.algorithms_list:
                if self.alg == x:
                    return
        else:
            for (x, y, z) in self.algorithms_list:
                if self.alg in y:
                    self.alg = x
                    return
        raise ValueError("Wrong algorithm id!")

