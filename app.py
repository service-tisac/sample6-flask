from flask import Flask, request, jsonify
from textblob import TextBlob

@app.route('/')
def hello():
    print("Hello sample 6")
    return "Hello sample 6"  # Return a response


@app.route("/test/textblob", methods=["POST"])
def test_textblob():
    try:
        data = request.get_json()
        text = data.get("text", "")
        blob = TextBlob(text)
        sentiment = blob.sentiment
        response = {
            "polarity": sentiment.polarity,
            "subjectivity": sentiment.subjectivity
        }
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
