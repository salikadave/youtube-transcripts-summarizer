# YouTube API
from youtube_transcript_api import YouTubeTranscriptApi
import json
from transformers import pipeline
from transformers import T5ForConditionalGeneration, T5Tokenizer


# Return transcripts from Video ID
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
        return video_summary_string
    except:
        return 'Transcripts not found!'
    
# convert using pipeline api
def transcript_to_summary_pipeline(video_transcript):
    # using pipeline API for summarization task
    print("Using Pipeline API. . . .")
    summarization = pipeline("summarization")
    print("Preparing summary. . .")
    summary_text = summarization(video_transcript)[0]['summary_text']
    print("Summary:", summary_text)
    return summary_text

# convert using T5 transformer
def transcript_to_summary_t5(video_transcript):
    model = T5ForConditionalGeneration.from_pretrained("t5-base")
    tokenizer = T5Tokenizer.from_pretrained("t5-base")
    # T5 uses a max_length of 512 so we cut the article to 512 tokens.
    inputs = tokenizer.encode("summarize: " + video_transcript, return_tensors="pt", max_length=512, truncation=True)
    outputs = model.generate(inputs, max_length=500, min_length=40, length_penalty=4.0, num_beams=4, early_stopping=True)
    print(outputs)
    print(tokenizer.decode(outputs[0]))

# Sample
# transcipts_under_1024 = ["NiKtZgImdlY","_Nq4Z5i7lcs","ZyYqyYAKGC0","yj8sAnZ6c3g","1K5SycZjGhI","1o4mJdt4TzA"]
# transcript = fetch_video_transcripts(transcipts_under_1024[1])
# print("="*50)
# # transcript_to_summary_pipeline(transcript)
# transcript_to_summary_t5(transcript)





