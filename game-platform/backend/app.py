from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    message = data.get("message")
    response = {"reply": f"Ты написал: {message}"}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)