import argparse
import json

def get_score(actual_answer, predicted_answer, in_domain):
    if(in_domain):
        if("," in actual_answer):
            # stage 3 
            if("," in predicted_answer):
            # sort both actual_answer and predicted_answer and compare
                actual_answer = actual_answer.split(",")
                predicted_answer = predicted_answer.split(",")
                actual_answer.sort()
                predicted_answer.sort()
                if(actual_answer == predicted_answer):
                    return 10
                else:
                    return 0

            else:
                if(predicted_answer == "OOD"):
                    return -7.5
                else:
                    return 0

        else:
            # stage 1 or 2
            if(actual_answer == predicted_answer):
                return 10
            elif(predicted_answer == "OOD"):
                return -7.5
            else:
                return 0
    else:
        if("," in actual_answer):
            # stage 3 
            if("," in predicted_answer):
            # sort both actual_answer and predicted_answer and compare
                actual_answer = actual_answer.split(",")
                predicted_answer = predicted_answer.split(",")
                actual_answer.sort()
                predicted_answer.sort()
                if(actual_answer == predicted_answer):
                    return -6
                else:
                    return -5

            else:
                if(predicted_answer == "OOD"):
                    return 10
                else:
                    return -5

            

        else:
            # stage 1 or 2
            if(actual_answer == predicted_answer):
                return -6
            elif(predicted_answer == "OOD"):
                return 10
            else:
                return -5

def main():
    parser = argparse.ArgumentParser()

    # Required parameters
    parser.add_argument(
        "--stage",
        default=None,
        type=str,
        required=True,
        help="The stage number",
    )

    parser.add_argument(
        "--test_data_file",
        default=None,
        type=str,
        required=True,
        help="test data file",
    )

    # parser.add_argument(
    #     "--output_file",
    #     default=None,
    #     type=str,
    #     required=True,
    #     help="File name of the output file",
    # )
    
    args = parser.parse_args()

    file = open("data/" + args.stage + "_test_with_answer.json")
    answer_dict = {}
    lines = file.readlines()
    for line in lines:
        data = json.loads(line)
        answer_dict[data["Id"]] = {
        "Answer" : data["Answer"],
        "Stage": data["Stage"],
        }
    
    user_file = open("data/" + args.stage + "_test_with_answer.json")
    Correct = 0
    Wrong = 0
    Score = 0
    lines = user_file.readlines()
    for line in lines:
        data = json.loads(line)
        current_answer = answer_dict[data["Id"]]
        current_score = get_score( current_answer["Answer"], data["Answer"], args.stage == current_answer["Stage"])
        Score += current_score
        print(current_answer["Stage"] + " : " + str(current_score))

    print("Total score : ")
    print(Score)
    
    
if __name__ == "__main__":
    main()


# format of test file {id, answer}