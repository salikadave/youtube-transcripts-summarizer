# adding flask boilerplate for REST APIs
from flask import Flask, render_template, request, jsonify
from datetime import datetime
import os
import sys
import json
from flask import make_response
from flask_cors import CORS
# Import Custom Module
# import summarizer
# import bart_init
import bart_summarizer


# define a variable to hold your app
app = Flask(__name__)
CORS(app)

# define your resource endpoints
@app.route('/')
def index_page():
    return render_template('index.html',os_type = sys.platform,os_name = os.name)

@app.route('/time')
def get_time():
    return str(datetime.datetime.now())

@app.route('/api/summarize', methods=["GET"])
def perform_summarization():
    youtube_url = request.args.get('youtube')
    video_id = youtube_url.split("=")
    video_transcript = summarizer.fetch_video_transcripts(video_id[1])
    transcript_summary = summarizer.transcript_to_summary_pipeline(video_transcript)
    return json.dumps(transcript_summary, indent = 4)
    # return json.dumps(video_url,indent=4)

@app.route('/api/bart', methods=["GET"])
def perform_bart_summary():
    youtube_url = request.args.get('youtube')
    video_id = youtube_url.split("=")
    # video_transcript = summarizer.fetch_video_transcripts(video_id[1])
    transcript_summary, time = bart_summarizer.begin_summary_generation(video_id[1])
    content = {
        "summary": transcript_summary,
        "time_taken": time
    }
    return json.dumps(content, indent = 4)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

# serve the app when this file is run
if __name__=='__main__':
    app.run(use_reloader=True)
    print('server running')



