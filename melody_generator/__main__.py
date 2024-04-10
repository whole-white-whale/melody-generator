"""Веб-приложение для генерации мелодий."""

from tempfile import NamedTemporaryFile

from flask import Flask, render_template, request, send_file

from melody_generator.audio import Audio
from melody_generator.system import System

app = Flask(__name__)


@app.route("/")
def response_with_home_page():
    """Одать главную страницу приложения."""

    return render_template("index.html")


@app.route("/generate")
def response_with_audio():
    """Отдать сгенерированный аудиофайл."""

    length, speed = float(request.args["length"]), int(request.args["speed"])

    with open("resources/aeolian.conf", encoding="utf_8") as file:
        configuration = file.readlines()

    melody, system = [], System.from_configuration(configuration)

    for melody in system.produce():
        if 15.0 * len(melody) / speed >= length:
            break

    audio = Audio(melody, 48000, speed)

    with NamedTemporaryFile(suffix=".wav") as file:
        audio.dump(file.name)

        return send_file(file.name)
