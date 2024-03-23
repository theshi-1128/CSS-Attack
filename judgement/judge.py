from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification


def truncate_sequence(sequence: str, max_length: int = 512) -> str:
    """
    Truncate the input sequence to the maximum length allowed by the model,
    accounting for [CLS] and [SEP] tokens.
    """
    return sequence[:max_length - 2] if len(sequence) > max_length - 2 else sequence


def judge_harmful(model_dir, text: str) -> int:
    """
    Judge whether the text is harmful using a classifier. Assumes the classifier
    returns a list of dictionaries with a 'label' key indicating harmfulness.

    :param text: Text to classify.
    :return: 1 if text is classified as harmful, 0 otherwise.
    """
    tokenizer = AutoTokenizer.from_pretrained(model_dir)
    model = AutoModelForSequenceClassification.from_pretrained(model_dir)
    classifier = pipeline(task="text-classification", model=model, tokenizer=tokenizer)
    result = classifier(truncate_sequence(text))
    return 1 if result[0]['label'] == 1 else 0

