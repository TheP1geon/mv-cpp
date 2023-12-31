#!/bin/python3

import os
import sys
from colorama import Fore


def run_test(file_name: str):

    output: str = os.popen(f"../bin/mvi {file_name}.mv").read()

    if str(file_name + ".test") not in list(os.listdir('.')):
        return [False, "", output]

    with open(f"{file_name}.test", "r") as f:
        expected_output = f.read()

    return [output == expected_output, expected_output, output]


def record_test(file_name: str):
    os.system(f"../bin/mvi {file_name}.mv > {file_name}.test")


def main():
    os.chdir("./tests")

    if (len(sys.argv) > 1):

        if (sys.argv[1] == "run"):
            for file in os.listdir("."):
                if (file.split('.')[1] != "mv"):
                    continue

                output, e, a = run_test(file.split('.')[0])

                color = Fore.GREEN if output else Fore.RED
                passed = "[ OK ]" if output else "[ FAIL ]"

                print(f"{file}: {color}{passed}{Fore.WHITE}")

                if not output:
                    print("Expected output:")
                    print(f"{e}")
                    print("Actual output:")
                    print(f"{a}")

        elif (sys.argv[1] == "record"):
            os.system("rm -f *.test")
            for file in os.listdir("."):
                record_test(file.split('.')[0])

    os.chdir("..")


if __name__ == "__main__":
    main()
