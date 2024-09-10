#!/usr/bin/env python3
"""This is the starting point of the flask app"""

from flask import Flask, render_template
from typing import Text


app = Flask(__name__)


@app.route('/')
def home() -> Text:
    """This is the home route

    Returns:
        Text: The html template
    """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
