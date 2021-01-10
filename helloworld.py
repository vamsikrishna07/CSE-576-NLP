import argparse
print("Hello world")
parser = argparse.ArgumentParser()
parser.add_argument(
"--num",
default=None,
type=str,
required=True,
help="The stage number",
)

args = parser.parse_args()
print("printing argument: ",args.num)