import argparse
import json

def main():
    parser = argparse.ArgumentParser()

    # Required parameters
    parser.add_argument(
        "--stage",
        default='None',
        type=str,
        required=True,
        help="The stage number",
    )

    # Required parameters
    parser.add_argument(
        "--data_percentage",
        default=None,
        type=str,
        required=True,
        help="Percentage of train data to expose",
    )
    
    # optional parameter
    parser.add_argument(
        "--train_data_file_name",
        default="train_data.json",
        type=str,
        required=False,
        help="File name of the train data",
    )
    
    args = parser.parse_args()

    file = open(args.stage + "_train_processed_data.json")
    lines = file.readlines()
    train_data_len = int(int(args.data_percentage)*len(lines)/100)
    train_data = lines[:train_data_len]
    with open(args.train_data_file_name, "w") as f:
    	for line in train_data:
    		f.write(line)

if __name__ == "__main__":
    main()
