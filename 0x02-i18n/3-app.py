#!/usr/bin/env python3

"""
3-app.py
"""

from flask import Flask, render_template, request
from flask_babel import Babel, _  # Import the _ function for translation

app = Flask(__name__)

babel = Babel(app)


class Config:
    """Configuration class for the Flask app."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """
    Determine the best-matching language for the user.

    Returns:
        str: The best-matching language code.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    Render the index page with parametrized titles and headers.

    Returns:
        str: Rendered HTML content for the index page.
    """
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run()
