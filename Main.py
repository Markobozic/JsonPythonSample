import argparse
import sys
import os
import subprocess

from Serializer import write_json_to_file
from Deserializer import read_json_from_file
from Model import Model


def main():
    target_dir = "target/out.json"
    parser = argparse.ArgumentParser()

    parser.add_argument("-i",
                        "--input",
                        help="binary value: 0 or 1",
                        type=int,
                        required=True)

    parser.add_argument("-f",
                        "--file",
                        help="path to file",
                        type=str,
                        required=True)

    args = parser.parse_args()
    file_path = args.file
    flag = args.input

    directory_exists = os.path.exists(target_dir)

    if directory_exists is False:
        subprocess.run(["mkdir", "target"])

    if flag is 0:
        model = Model(made_with_python=True, backwards_in_python=[9, 8, 7, 6, 5, 4, 3, 2, 1, 0], description="Made with Python")
        write_json_to_file(model, file_path)
    elif flag is 1:
        read_json_from_file(file_path)
    else:
        print("The flag is binary, 0 or 1, try again.")
        sys.exit()


if __name__ == "__main__":
    main()

