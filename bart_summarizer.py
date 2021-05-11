import time
from transformers import BartTokenizer, BartForConditionalGeneration, BartConfig
BART_PATH = 'facebook/bart-large-cnn'
bart_model = BartForConditionalGeneration.from_pretrained(BART_PATH, output_past=True)
print("Initializing BART model . . .")
bart_tokenizer = BartTokenizer.from_pretrained(BART_PATH, output_past=True)
print("Initializing BART tokenizer . . .")
import nltk
# nltk.download('punkt')
# nltk.download('stopwords')
from youtube_transcript_api import YouTubeTranscriptApi

def fetch_video_transcripts(video_id):
    video_summary = []
    try:
        transcripts_arr = YouTubeTranscriptApi.get_transcript(video_id)
        for elem in transcripts_arr:
            # print(elem)
            text = elem["text"]
            elem = text.replace("\n",' ')
            # elem = text.replace('\t',"")
            # print(elem)
            video_summary.append(elem)
        separator = " "
        video_summary_string = separator.join(video_summary)
        # print(video_summary_string)
        # print(len(video_summary_string))
        return video_summary_string
    except:
        return 'Transcripts not found!'

def nest_sentences(document):
  nested = []
  sent = []
  length = 0
  for sentence in nltk.sent_tokenize(document):
    length += len(sentence)
    if length < 1024:
      sent.append(sentence)
    else:
      nested.append(sent)
      sent = []
      length = 0

  if sent:
    nested.append(sent)

  return nested

def generate_summary(nested_sentences):
  # device = 'cuda'
  print('inside generate summary')
  summaries = []
  for nested in nested_sentences:
    print('nesting new sentence. . .')
    input_tokenized = bart_tokenizer.encode(' '.join(nested), truncation=True, return_tensors='pt')
    # input_tokenized = input_tokenized.to(device)
    print('generating summary id. . .')
    summary_ids = bart_model.generate(input_tokenized,
                                      length_penalty=3.0,
                                      min_length=30,
                                      max_length=100)
    print('generating output. . .')
    output = [bart_tokenizer.decode(g, skip_special_tokens=True, clean_up_tokenization_spaces=False) for g in summary_ids]
    summaries.append(output)
    print('appending output. . .')
  summaries = [sentence for sublist in summaries for sentence in sublist]
  return summaries

def begin_summary_generation(videoID):
    print(videoID)
    start = time.time()
    print('===== Fetching Transcripts =====')
    transcript2 = fetch_video_transcripts(videoID)
    print('===== Nesting Sentences =====')
    nested_vid_2 = nest_sentences(transcript2)
    print('===== Generate 1st level summary =====')
    summ1_vid_2 = generate_summary(nested_vid_2)
    print("===== Generate 2nd level summary =====")
    nested_summ = nest_sentences(' '.join(summ1_vid_2))
    summ2 = generate_summary(nested_summ)
    print(" ".join(summ2))
    end = time.time()
    time_taken = (end - start) / 60
    print(time_taken)
    return summ2, time_taken
    # print(f"Time taken to generate summary: {end - start}")
    

