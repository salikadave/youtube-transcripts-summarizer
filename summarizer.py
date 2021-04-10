# YouTube API
from youtube_transcript_api import YouTubeTranscriptApi
import json


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
    


video_id = "emBoDloCze8"
transcript = fetch_video_transcripts(video_id)