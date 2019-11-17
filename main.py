import sys
import os


from Parser import Parser

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 {} <file1> <file2> ... <fileN>".format(sys.argv[0]))
        sys.exit(1)
    filenames = []
    for f in sys.argv[1:]:
        try:
            if f.endswith(".csv"):
                filenames.append(f)
            else:
                print("Unsupported file type for: {}".format(f))
        except Exception as e:
            print("Skipping file: {}. Error: {}".format(f, e))

    print("Parsing files: {}".format(filenames))
    parser = Parser(filenames)
    parser.parse()

if __name__ == '__main__':
    main()