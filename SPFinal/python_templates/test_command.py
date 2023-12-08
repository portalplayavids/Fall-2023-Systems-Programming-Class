import unittest
from command import Command


class TestCommand(unittest.TestCase):

    def test_run_command(self):
        """
        Test the run_command method of the Command class.
        """
        result = Command.run_command('echo "Hello World"')
        self.assertIn("Hello World", result)


if __name__ == '__main__':
    unittest.main()
