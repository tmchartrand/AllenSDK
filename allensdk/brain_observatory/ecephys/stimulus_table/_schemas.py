from argschema import ArgSchema, ArgSchemaParser 
from argschema.schemas import DefaultSchema
from argschema.fields import Nested, InputDir, String, Float, Dict, Int


class InputParameters(ArgSchema): 
    stimulus_pkl_path = String(required=True, help="path to pkl file containing raw stimulus information")
    sync_h5_path = String(required=True, help="path to h5 file containing syncronization information")
    output_stimulus_table_path = String(required=True, help="the output stimulus table csv will be written here")
    minimum_spontaneous_activity_duration = Float(default=-1.0, help="detected spontaneous activity sweeps will be rejected if they last fewer that this many seconds")
    maximum_expected_spontanous_activity_duration = Float(default=1225.02541, help='validation will fail if a spontanous activity epoch longer than this one is computed.')
    frame_time_strategy = String(default='use_photodiode', 
        help='technique used to align frame times. Options are \'use_photodiode\', which interpolates frame times between photodiode edge times (preferred when vsync times are unreliable) and \'use_vsyncs\', which is preferred when reliable vsync times are available.'
    )
    stimulus_name_map = Dict(keys=String(), values=String(), allow_none=True, default=None, help='optionally rename stimuli')
    column_name_map = Dict(keys=String(), values=String(), allow_none=True, default=None, help='optionally rename parameters')


class OutputSchema(DefaultSchema): 
    input_parameters = Nested(InputParameters, 
                              description=("Input parameters the module " 
                                           "was run with"), 
                              required=True) 


class OutputParameters(OutputSchema): 
    output_path = String(help="Path to output csv file")