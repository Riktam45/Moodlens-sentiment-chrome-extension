from googleapiclient.discovery import build
from urllib.parse import urlparse, parse_qs

API_KEY = "AIzaSyB26Z1a9DwepLyD0gtxDrUMHa7ZVLeGoYw"


def extract_video_id(url):

    parsed_url = urlparse(url)

    if parsed_url.hostname == 'youtu.be':
        return parsed_url.path[1:]

    if parsed_url.hostname in ('www.youtube.com', 'youtube.com'):
        query = parse_qs(parsed_url.query)
        return query.get('v', [None])[0]

    return None


def get_youtube_comments(video_url):

    video_id = extract_video_id(video_url)

    youtube = build('youtube', 'v3', developerKey=API_KEY)

    comments = []

    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=100,
        textFormat="plainText"
    )

    response = request.execute()

    for item in response['items']:
        comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
        comments.append(comment)

    return comments