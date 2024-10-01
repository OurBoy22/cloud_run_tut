import os, json, time

from flask import Flask, request

app = Flask(__name__)

from google.cloud import bigquery

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    """Example Hello World route."""

    return f"Hello World!!!!!!"

@app.route("/user", methods=['GET', 'POST'])
def user():
    """Example user route."""
    # Get the user name from the request
    user_name = request.args.get('name')
    # Return the user name
    return f"Hello {user_name}!"

    # return f"User Page"
    
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
