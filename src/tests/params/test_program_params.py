import unittest
import os
from .program_params import ProgramParams

OUTPUT_FOLDER="./test_output/"

class TestProgramParamsSmoke(unittest.TestCase):

    def test_program_params_instanciation(self):
        """
        Test program params instanciation.
        No exception should be raised.
        """
        # create the output folder (to pass the PATH check)
        os.makedirs(OUTPUT_FOLDER, exist_ok=True)
        try:
            program_params = ProgramParams(load_program_argv=True, debug=True)
        except Exception as e:
            self.fail(f"ProgramParams initialization raised an exception: {e}")


if __name__ == '__main__':
    
    unittest.main()
