from cli import Cli
from algorithms import AlgorithmManager

if __name__ == '__main__':
    cli = Cli()
    requested_alg = cli.get_first_arg()
    alg_args = cli.get_rest_arguments()
    alg = AlgorithmManager(requested_alg, alg_args)
    alg.run()
