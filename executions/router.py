from executions.modulo import Modulo


class Router:
    @staticmethod
    def get(alg_id):
        algs = {
            0: Modulo,
        }
        return algs.get(alg_id)
