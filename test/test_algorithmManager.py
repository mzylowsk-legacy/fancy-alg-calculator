from unittest import TestCase
from algorithms import AlgorithmManager


class TestAlgorithmManager(TestCase):
    def test_convert_to_algorithm_id(self):
        algmng = AlgorithmManager("modulo", "")
        assert algmng.alg == 0, "wrong alg mapping"
        algmng = AlgorithmManager(4, "")
        assert algmng.alg == 4, "wrong alg mapping"
        algmng = AlgorithmManager(30, "")
        assert algmng.alg == 30, "wrong alg mapping"
        algmng = AlgorithmManager("sort", "")
        assert algmng.alg == 2, "wrong alg mapping"
        try:
            AlgorithmManager("nope", "")
            self.fail("Exception should be thrown")
        except ValueError as e:
            assert str(e) == "ERROR: Wrong algorithm id!"
        try:
            AlgorithmManager(59, "")
            self.fail("Exception should be thrown")
        except ValueError as e:
            assert str(e) == "ERROR: Wrong algorithm id!"
        try:
            AlgorithmManager(-1, "")
            self.fail("Exception should be thrown")
        except ValueError as e:
            assert str(e) == "ERROR: Wrong algorithm id!"
