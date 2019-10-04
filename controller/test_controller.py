from unittest import TestCase

from controller.controller import cmd_dispatcher


class Test(TestCase):
    def test_cmd_dispatcher(self):
        cmd_dispatcher("abc when")
        self.fail()
