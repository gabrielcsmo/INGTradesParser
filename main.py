import sys
import os
import json

from Parser import Parser
FILENAMES_KEY = "input_files"
SELF_IBANS = "ibans"

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 {} input.json".format(sys.argv[0]))
        sys.exit(1)

    input_dict = json.load(open(sys.argv[1]))

    filenames = input_dict[FILENAMES_KEY]
    ibans = input_dict[SELF_IBANS]

    for f in filenames:
        try:
            if not f.endswith(".csv"):
                print("Unsupported file type for: {}".format(f))
                filenames.remove(f)
        except Exception as e:
            print("Skipping file: {}. Error: {}".format(f, e))

    print("Parsing files: {}".format(filenames))
    parser = Parser(filenames, ibans)
    parser.parse()

if __name__ == '__main__':
    main()