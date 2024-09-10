#!/usr/bin/env python3
"""This is the flask app file"""

from flask import Flask, render_template
from flask_babel import Babel
from typing import Text


app = Flask(__name__)
babel = Babel(app)


class Config:
    """This is the config class for the flask app
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route("/")
def home() -> Text:
    """This is the home route

    Returns:
        Text: The html template file
    """
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
