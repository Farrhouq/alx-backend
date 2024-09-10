#!/usr/bin/env python3
"""This is the flask app file"""

from flask import (
    Flask,
    render_template,
    request,
    g,
)
from flask_babel import Babel
from typing import (
    Text,
    Optional
)


app = Flask(__name__)
app.url_map.strict_slashes = False
babel = Babel(app)


class Config:
    """This is the config class for the flask app
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale() -> Optional[str]:
    """The function that gets the locale

    Returns:
        Optional[str]: The locale
    """
    if 'locale' in request.args:
        locale = request.args.get('locale')
        if locale in app.config["LANGUAGES"]:
            return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def home() -> Text:
    """This is the home route

    Returns:
        Text: The html template file
    """
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
