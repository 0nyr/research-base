from enum import Enum
import os
from research_base.params.base_program_params import BaseProgramParams
from research_base.results.base_result_writer import BaseResultWriter

from .cli import CLIArguments

class PipelineParams(Enum):
    PIPELINE1 = "PIPELINE1"
    PIPELINE2 = "PIPELINE2"

class ResultWriter(BaseResultWriter):
    def __init__(self, pipeline_name: Enum):
        super().__init__(
            csv_file_path="test_output/result.csv", 
            more_header=[], 
            pipeline_name=pipeline_name,
        )

class ProgramParams(BaseProgramParams):
    """
    Wrapper class for program parameters.
    """
    cli_args: CLIArguments
    
    ### env vars
    # NOTE: all CAPITAL_PARAM_VALUES values NEED to be overwritten by the .env file
    # NOTE: lowercase values are from the CLI

    # data
    ANNOTATED_GRAPH_DOT_GV_DIR_PATH: str

    def __init__(
            self, 
            load_program_argv : bool = True, 
            debug : bool = False,
            **kwargs
    ):
        # determine dotenv path
        # NOTE: the .env file is in the same path as this current file
        dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
        assert os.path.exists(dotenv_path) and os.path.isfile(dotenv_path), (
            "ERROR: .env file not found: {0} in folder: {1}".format(dotenv_path, os.path.dirname(__file__))
        )
        print("Found .env file: {0}".format(dotenv_path))


        super().__init__("GCN_ML", PipelineParams, ResultWriter, load_program_argv, debug, dotenv_path=dotenv_path)

        # to be done last
        self._log_program_params()
    
    
    def _load_program_argv(self):
        """
        Load given program arguments.
        """
        self.cli_args = CLIArguments()


    def _consume_program_argv(self):
        """
        Consume given program arguments.
        """
        if self.cli_args.args.debug is not None:
            self.DEBUG = self.cli_args.args.debug
            assert isinstance(self.DEBUG, bool)

        if self.cli_args.args.max_ml_workers is not None:
            self.MAX_ML_WORKERS = int(self.cli_args.args.max_ml_workers)
            assert isinstance(self.MAX_ML_WORKERS, int)
        
        if self.cli_args.args.annotated_graph_dot_gv_dir_path is not None:
            self.ANNOTATED_GRAPH_DOT_GV_DIR_PATH = self.cli_args.args.annotated_graph_dot_gv_dir_path
            assert isinstance(self.ANNOTATED_GRAPH_DOT_GV_DIR_PATH, str)
        