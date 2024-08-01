from flask import Flask, request, jsonify
from textblob import TextBlob
import time
import numpy as np

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

@app.route("/test/cpu", methods=["GET"])
def heavy_computation():
    try:
        # Perform a CPU-intensive task
        def fibonacci(n):
            if n <= 1:
                return n
            else:
                return fibonacci(n-1) + fibonacci(n-2)
        
        # Example of a large Fibonacci number calculation
        start_time = time.time()
        result = fibonacci(35)  # Change this number to make it more intensive
        end_time = time.time()
        
        response = {
            "result": result,
            "computation_time": end_time - start_time
        }
        return jsonify(response)  # Return JSON response
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Return error response
        
@app.route("/test/memory", methods=["GET"])
def memory_intensive():
    try:
        start_time = time.time()  # Start timing

        # Create a large array to simulate high memory usage
        size = 10**7  # Adjust size as needed for testing
        large_array = np.zeros(size)

        end_time = time.time()  # End timing
        compute_time = end_time - start_time

        result = {
            "message": "Memory intensive task completed successfully!",
            "compute_time_seconds": compute_time
        }
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Return error response

if __name__ == '__main__':
    app.run(debug=True)
