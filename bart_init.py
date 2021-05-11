from transformers import BartTokenizer, BartForConditionalGeneration, BartConfig
BART_PATH = 'facebook/bart-large-cnn'
bart_model = BartForConditionalGeneration.from_pretrained(BART_PATH, output_past=True)
print("Initializing BART model . . .")
bart_tokenizer = BartTokenizer.from_pretrained(BART_PATH, output_past=True)
print("Initializing BART tokenizer . . .")
import nltk