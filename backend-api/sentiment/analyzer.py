from transformers import pipeline

classifier = None


def get_classifier():
    global classifier

    if classifier is None:
        classifier = pipeline(
            "sentiment-analysis",
            model="cardiffnlp/twitter-roberta-base-sentiment"
        )

    return classifier


def analyze_comments(comments):

    model = get_classifier()

    positive = 0
    negative = 0
    neutral = 0

    analyzed_comments = []

    for comment in comments:

        try:
            result = model(comment[:512])[0]

            label = result["label"]
            score = round(result["score"] * 100, 2)

            if label == "LABEL_2":
                sentiment = "Positive"
                positive += 1

            elif label == "LABEL_0":
                sentiment = "Negative"
                negative += 1

            else:
                sentiment = "Neutral"
                neutral += 1

            analyzed_comments.append({
                "comment": comment,
                "sentiment": sentiment,
                "confidence": score
            })

        except Exception as e:
            print(e)

    total = max(len(comments), 1)

    return {
        "total_comments": len(comments),
        "positive": positive,
        "negative": negative,
        "neutral": neutral,
        "comments": analyzed_comments
    }