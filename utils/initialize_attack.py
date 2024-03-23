import pandas as pd
from utils.interval_saver import IntervalSaver

def initialize_attack_pipeline(args):
    # Build a list of column names
    columns = ['harmful_behaviour', 'prompt'] + \
              [f'output{i}' for i in range(1, args.attack_rounds + 1)] + \
              [f'label{i}' for i in range(1, args.attack_rounds + 1)] + \
              ['label']

    # Read the dataset and prompt file
    df = pd.read_csv(args.dataset_dir)
    pdf = pd.read_csv(args.prompt_dir)
    original_attack_prompt = pdf['prompt'].iloc[0]

    # Initialize an IntervalSaver instance
    saver = IntervalSaver(args.output_dir, interval=args.save_interval, columns=columns)

    return {
        'df': df,
        'original_attack_prompt': original_attack_prompt,
        'saver': saver,
        'columns': columns
    }
