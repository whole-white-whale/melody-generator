"""Веб-приложение для генерации мелодий."""

from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def response_with_home_page():
    """Одать главную страницу приложения."""

    return render_template("index.html")
