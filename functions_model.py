#!/usr/bin/env python3

from transformers import pipeline

# --------------------------------------------------------------------------------------------------
#  from huggingface_example_translation.ipynb
def encode(examples, tokenizer, max_input_length=128, max_target_length=128):
  """
  Function to truncate the inputs
  """
  # Prefix required by the T5 checkpoints:
  prefix = "Translate French to Alsacien: "

  inputs  = [prefix + ex[tokenizer.src_lang] for ex in examples["translation"]] # If 'Datasets' format
  targets = [ex[tokenizer.tgt_lang]          for ex in examples["translation"]] # If 'Datasets' format
#  inputs  = [prefix + ex[tokenizer.src_lang] for ex in examples]
#  targets = [ex[tokenizer.tgt_lang]          for ex in examples]
  model_inputs = tokenizer(inputs, max_length=max_input_length, truncation=True)

  # Setup the tokenizer for targets
  with tokenizer.as_target_tokenizer():
    labels = tokenizer(targets, max_length=max_target_length, truncation=True)

  model_inputs["labels"] = labels["input_ids"]
  return model_inputs

# --------------------------------------------------------------------------------------------------
def compute_metrics(eval_preds):
    preds, labels = eval_preds
    if isinstance(preds, tuple):
        preds = preds[0]
    decoded_preds = tokenizer.batch_decode(preds, skip_special_tokens=True)

    # Replace -100 in the labels as we can't decode them.
    labels = np.where(labels != -100, labels, tokenizer.pad_token_id)
    decoded_labels = tokenizer.batch_decode(labels, skip_special_tokens=True)

    # Some simple post-processing
    decoded_preds, decoded_labels = postprocess_text(decoded_preds, decoded_labels)

    result = metric.compute(predictions=decoded_preds, references=decoded_labels)
    result = {"bleu": result["score"]}

    prediction_lens = [np.count_nonzero(pred != tokenizer.pad_token_id) for pred in preds]
    result["gen_len"] = np.mean(prediction_lens)
    result = {k: round(v, 4) for k, v in result.items()}
    return result

# --------------------------------------------------------------------------------------------------
def do_translation(text, model_name, return_text=True, return_token=False):
  """
  Do the translation using the trained model.
  return either the translation or the tokens
  """
  # make the text a correct format for translation :
  translator = pipeline("translation_XX_to_YY", model=model_name)
  translator(text)

  # Tokenize the text: text -> tokens :
  tokenizer = AutoTokenizer.from_pretrained(model_name)
  inputs = tokenizer(text, return_tensors="pt").input_ids

  model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
  # Do the translation using the tokenized text:
  outputs = model.generate(inputs, max_new_tokens=40, do_sample=True, top_k=30, top_p=0.95)

  # Token -> text:
  translation = tokenizer.decode(outputs[0], skip_special_tokens=True)

  if return_text:
    return translation
  if return_tokens:
    return output[0]
