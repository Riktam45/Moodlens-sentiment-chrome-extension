from fastapi import APIRouter
from pydantic import BaseModel

from sentiment.analyzer import analyze_comments
from scraper.youtube import get_youtube_comments
from scraper.reddit import get_reddit_comments

router = APIRouter()

class AnalyzeRequest(BaseModel):
    url: str

class ManualComment(BaseModel):
    comment: str

@router.post("/analyze")
def analyze_post(data: AnalyzeRequest):

    url = data.url

    comments = []

    if "youtube.com" in url or "youtu.be" in url:
        comments = get_youtube_comments(url)

    elif "reddit.com" in url:
        comments = get_reddit_comments(url)

    else:
        return {
            "error": "Platform not supported yet"
        }

    result = analyze_comments(comments)

    return result


@router.post("/manual")
def manual_analysis(data: ManualComment):

    result = analyze_comments([data.comment])

    return result