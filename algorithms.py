class AlgorithmManagerException(Exception):
    pass


class AlgorithmManager:
    def __init__(self, requested_alg, alg_arguments):
        self.algorithms_list = [
            (0, "modulo", "modulo of two numbers", 2),
            (1, "sort_desc", "sort desc elements", -1),
            (2, "sort", "sort elements", -1),
            (30, "sum", "sum all elements", -1),
            (4, "pi", "return to pi with {param} digits after dot", 0),
            (5, "showtime", "add_element", 0)
        ]
        self.alg = requested_alg
        self.args = alg_arguments

        self.convert_to_algorithm_id()
        self.check_arguments_count()

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

    def get_arguments_count_for_alg(self):
        return list(zip(*self.algorithms_list))[3][self.alg]

    def check_arguments_count(self):
        req_args = self.get_arguments_count_for_alg()
        if not req_args == len(self.args):
            raise AlgorithmManagerException("Requested alg needs %s arguments but %s is given."
                                            % (req_args, len(self.args)))
