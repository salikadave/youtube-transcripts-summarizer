# YouTube API
from youtube_transcript_api import YouTubeTranscriptApi


# Return transcripts from Video ID
def fetch_video_subtitles(video_id):
    subtitles = YouTubeTranscriptApi.get_transcript(video_id)
    return subtitles

video_id = "Hu4Yvq-g7_Y"
print(fetch_video_subtitles(video_id))