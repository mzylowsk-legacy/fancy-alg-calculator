class AlgorithmManager:
    def __init__(self, requested_alg, alg_arguments):
        self.algorithms_list = [
            (0, "modulo", "modulo of two numbers", 2),
            (1, "sort_desc", "sort desc elements", -1),
            (2, "sort", "sort elements", -1),
            (3, "sum", "sum all elements", -1),
            (4, "pi", "return to pi with {param} digits after dot", 0),
            (5, "showtime", "add_element", 0)
        ]
        self.alg = requested_alg
        self.args = alg_arguments

        self.convert_to_algorithm_id()

    def convert_to_algorithm_id(self):
        ids = list(zip(*self.algorithms_list))[0]
        names = list(zip(*self.algorithms_list))[1]

        try:
            self.alg = int(self.alg)
            if self.alg in ids:
                return
        except ValueError:
            for i in names:
                if self.alg == i:
                    self.alg = ids[names.index(self.alg)]
                    return
        raise ValueError("ERROR: Wrong algorithm id!")
