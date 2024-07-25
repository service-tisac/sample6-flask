from flask import Flask, request, jsonify
from textblob import TextBlob

app = Flask(__name__)  # Initialize Flask app

@app.route('/')
def hello():
    print("Hello sample 6")
    return "Hello sample 6"  # Return a response

@app.route("/test/textblob", methods=["POST"])
def test_textblob():
    try:
        data = request.get_json()  # Get JSON data from request
        text = data.get("text", "")  # Extract 'text' field
        blob = TextBlob(text)  # Create TextBlob object
        sentiment = blob.sentiment  # Get sentiment
        response = {
            "polarity": sentiment.polarity,
            "subjectivity": sentiment.subjectivity
        }
        return jsonify(response)  # Return JSON response
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Return error response

if __name__ == "__main__":
    app.run(debug=True)  # Run the app with debugging enabled
