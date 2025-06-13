from flask import Flask, render_template, request, session, url_for, redirect, jsonify
app = Flask(__name__,  template_folder='.', static_folder='static')
app.secret_key = "aidev10337"

import replicate


@app.route("/", methods=["GET","POST"])
def home():
    return render_template("chatbot.html")

@app.route("/reply", methods=["POST"])
def reply():
    user_message = request.json.get("message", "")
    input = {
        "prompt": user_message,
        "system_prompt": "You're a helpful assistant."
    }  
    reply=""
    for event in replicate.stream("openai/o1",input=input):
        reply+=str(event)
        print(event, end="")
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
