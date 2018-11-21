import sys
from unittest import TestCase
from unittest.mock import patch

from cli import Cli


class TestCli(TestCase):
    def test_get_all_arguments(self):
        cli = Cli()
        with patch.object(sys, 'argv', ["prog", "something", 4]):
            assert cli.get_all_arguments() == ["prog", "something", 4], "wrong user parameters getting"
        with patch.object(sys, 'argv', ["prog"]):
            assert cli.get_all_arguments() == ["prog"], "wrong user parameters getting"
        with patch.object(sys, 'argv', []):
            assert cli.get_all_arguments() == [], "wrong user parameters getting"

    def test_get_rest_arguments(self):
        cli = Cli()
        cli.user_arguments = ["script_name", "arg1"]
        assert cli.get_rest_arguments() == [], "empty list should be returned (two parameters)"
        cli.user_arguments = ["smth", "arg1", "arg2", "arg3"]
        assert cli.get_rest_arguments() == ["arg2", "arg3"], "[arg2, arg3] should be returned"
        cli.user_arguments = ["bla"],
        assert cli.get_rest_arguments() == [], "empty list should be returned (one parameter)"
        cli.user_arguments = [],
        assert cli.get_rest_arguments() == [], "empty list should be returned (no parameters)"
        cli.user_arguments = ["smth", "arg1", "arg2"]
        assert cli.get_rest_arguments() == ["arg2"], "[arg2] should be returned"

    def test_get_first_arg(self):
        cli = Cli()
        cli.user_arguments = ["script_name", "arg1"]
        assert cli.get_first_arg() == "arg1"
        cli.user_arguments = ["smth", "arg1", "arg2", "arg3"]
        assert cli.get_first_arg() == "arg1", "[arg1] should be returned"
        cli.user_arguments = ["bla"]
        try:
            cli.get_first_arg()
            self.fail("Exception should be thrown")
        except NameError as e:
            assert str(e) == "ERROR: You have to specify at least alg id!"
        cli.user_arguments = []
        try:
            cli.get_first_arg()
            self.fail("Exception should be thrown")
        except NameError as e:
            assert str(e) == "ERROR: You have to specify at least alg id!"
