import json
import sys

from Utility import convert_object_to_dict


def write_json_to_file(json_model, file_path):
    try:
        with open(file_path, 'w') as outfile:
            json.dump(json_model,
                      outfile,
                      default=convert_object_to_dict,
                      indent=4)
    except Exception as err:
        print("Error trying to write out json file: {}".format(err))
        sys.exit()
