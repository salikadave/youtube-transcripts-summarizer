# YouTube API
from youtube_transcript_api import YouTubeTranscriptApi
import json
from transformers import pipeline


# Return transcripts from Video ID
def fetch_video_transcripts(video_id):
    video_summary = []
    try:
        transcripts_arr = YouTubeTranscriptApi.get_transcript(video_id)
        for elem in transcripts_arr:
            # print(elem)
            text = elem["text"]
            elem = text.replace('\n'," ")
            # elem = text.replace('\t',"")
            # print(elem)
            video_summary.append(elem)
        video_summary_string = " ".join(video_summary)
        return video_summary_string
    except:
        return 'Transcripts not found!'
    
# convert transcript to abstractive summary
def transcript_to_summary(video_transcript):
    # using pipeline API for summarization task
    summarization = pipeline("summarization")
    summary_text = summarization(video_transcript)[0]['summary_text']
    print("Summary:", summary_text)



transcipts_under_1024 = ["NiKtZgImdlY","_Nq4Z5i7lcs","ZyYqyYAKGC0","yj8sAnZ6c3g"]
transcript = fetch_video_transcripts(transcipts_under_1024[3])
print("="*50)
transcript_to_summary(transcript)





