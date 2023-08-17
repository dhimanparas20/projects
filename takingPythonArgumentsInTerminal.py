#USAGE
# python3 test.py -p 5
# python3 test.py -p 5 -s "hi"
# python3 test.py --h

import argparse

# Create an ArgumentParser object
parser = argparse.ArgumentParser(description="Example script with multiple options")

# Define the expected arguments
parser.add_argument("-p", dest="parameter1", required=True, help="Specify the parameter value")
parser.add_argument("-s", dest="parameter2", required=False, default="defaultParam", help="Specify another parameter value")

# Parse the command-line arguments
args = parser.parse_args()

# Access the parsed arguments
parameter_value = args.parameter1
another_parameter_value = args.parameter2

print("Parameter:", parameter_value)
print("Another Parameter:", another_parameter_value)

