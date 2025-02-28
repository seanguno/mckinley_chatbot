import os
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session

app = Flask(__name__)

messages = []  # Simple message store

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", messages=messages)

@app.route("/send_message", methods=["POST"])
def send_message():
    message = request.form.get("message")
    if message:
        messages.append(message)  # Store the message
        print(messages)
    return render_template("index.html", messages=messages)  # Re-render page

if __name__ == "__main__":
    app.run()
