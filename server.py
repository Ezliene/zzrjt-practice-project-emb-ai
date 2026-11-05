"""Flask web server for the sentiment analysis application."""
from flask import Flask, render_template, request
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

app = Flask("Sentiment Analyzer")


@app.route("/sentimentAnalyzer")
def sent_analyzer():
    """Analyze the text sent from the web page and return a sentence."""
    # Get the text the user typed on the web page
    text_to_analyze = request.args.get('textToAnalyze')
    # Send it to the AI function
    response = sentiment_analyzer(text_to_analyze)
    # Pull out the label and score
    label = response['label']
    score = response['score']
    # If label is None, the input was invalid
    if label is None:
        return "Invalid input! Try again."
    sentiment = label.split('_')[1]
    return f"The given text has been identified as {sentiment} with a score of {score}."


@app.route("/")
def render_index_page():
    """Show the main web page."""
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    