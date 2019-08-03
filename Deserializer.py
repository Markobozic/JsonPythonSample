import sys
import json

from Utility import convert_dict_to_object


def read_json_from_file(file_path):
    try:
        with open(file_path, 'r') as infile:
            data = json.load(infile, object_hook=convert_dict_to_object)
            print(json.dumps(data.__dict__, indent=4))
    except Exception as err:
        print("Error trying to read json file: {}".format(err))
        sys.exit()
