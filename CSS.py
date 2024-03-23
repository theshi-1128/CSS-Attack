import argparse
from utils.attack_judge import process_and_judge_responses
from utils.initialize_attack import initialize_attack_pipeline


parser = argparse.ArgumentParser(description='Process input parameters for generating text and judging harmfulness.')
parser.add_argument('--model_name', type=str, default='gpt4', help='[gpt3, gpt4, claude3, glm4, qwen]')
parser.add_argument('--dataset_dir', type=str, default='./dataset/harmful_behaviors.csv', help='Directory of the dataset')
parser.add_argument('--output_dir', type=str, default='./output/output_gpt4.csv', help='Directory for output CSV file')
parser.add_argument('--prompt_dir', type=str, default='./prompt/ICL_attack_prompt.csv', help='Directory of the prompt CSV file')
parser.add_argument('--judgement_dir', type=str, default='./judgement/model', help='Directory of the judgement model')
parser.add_argument('--save_interval', type=int, default=1 * 1 * 30, help='Interval of saving CSV file')
parser.add_argument('--attack_rounds', type=int, default=3, help='Number of attack rounds')

args = parser.parse_args()


if __name__ == '__main__':
    initialize_data = initialize_attack_pipeline(args)
    process_and_judge_responses(**initialize_data, args=args)
