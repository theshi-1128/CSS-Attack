from tqdm import tqdm
from llm.api import generate
from judgement.judge import judge_harmful
from utils.random_split import split_sentence_randomly

def process_and_judge_responses(df, original_attack_prompt, saver, columns, args):
    """
    Generate responses for each item and judge them.

    :param df: DataFrame containing data on harmful behavior.
    :param original_attack_prompt: The original attack prompt template.
    :param args: Command line argument object.
    :param saver: An IntervalSaver instance for saving results.
    """
    sum_asr_ave = 0
    sum_asr_ens = 0
    for index, row in tqdm(df.iterrows(), total=df.shape[0], desc="Processing"):
        harmful_behaviour = row['goal']
        sentence1, sentence2, first_word, second_word = split_sentence_randomly(harmful_behaviour)
        attack_prompt = f"{original_attack_prompt.format(S1=sentence1, S2=sentence2, FIRST=first_word, SECOND=second_word)}"
        response_results = []
        judgement_results = []
        print("harmful_behaviour:\n", harmful_behaviour)
        print("-------------------------------------------------------------------------------------")
        print("attack_prompt:\n", attack_prompt)
        print("-------------------------------------------------------------------------------------")

        for i in range(args.attack_rounds):
            response = generate(args.model_name, attack_prompt)
            judgement = judge_harmful(args.judgement_dir, response)
            judgement_results.append(judgement)
            response_results.append(response)
            print(f"output{i+1}:\n", response)
            print("-------------------------------------------------------------------------------------")
            print(f"label{i+1}:\n", judgement)
            print("-------------------------------------------------------------------------------------")
            sum_asr_ave += judgement
        overall_judgement = 1 if 1 in judgement_results else 0
        sum_asr_ens += overall_judgement
        print(f"label:\n", overall_judgement)
        print("-------------------------------------------------------------------------------------")
        data_values = [harmful_behaviour, attack_prompt] + \
                      response_results + \
                      judgement_results + \
                      [overall_judgement]
        # Combine column names and data values into a dictionary
        data_dict = dict(zip(columns, data_values))
        saver.add_and_save(data_dict)

    saver.final_save()
    ASR_AVE = round((sum_asr_ave / ((index + 1) * args.attack_rounds)) * 100, 2)
    ASR_ENS = round((sum_asr_ens / index) * 100, 2)
    print("\nASR_AVE = ", ASR_AVE, '%')
    print("\nASR_ENS = ", ASR_ENS, '%')
