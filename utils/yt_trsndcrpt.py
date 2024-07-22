from youtube_transcript_api import YouTubeTranscriptApi
import urllib.parse
def get_transcript(url):
    # Parse the query string parameters of the URL
    query_params = urllib.parse.parse_qs(urllib.parse.urlsplit(url).query)

    id = query_params['v'][0]
    ##id = 'Y8Tko2YC5hA'
    transcript = YouTubeTranscriptApi.get_transcript(id)
    script = ""

    for text in transcript:
        t = text["text"]
        if t != '[Music]':
            script += t + " "
    transcript, no_of_words = script, len(script.split())

    return transcript, no_of_words