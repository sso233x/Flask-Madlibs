from flask import Flask, render_template, request
from stories import story

app = Flask(__name__)

@app.route("/")
def show_questions():
    """Shows questions form to ask for words"""
    prompts = story.prompts
    return render_template("questions.html", prompts=prompts)

@app.route("/story")
def show_story():
    """Shows the story with the given words"""
    text = story.generate(request.args)
    return render_template("story.html", text=text)