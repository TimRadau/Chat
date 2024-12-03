from flask import Flask, request, jsonify
import requests




app = Flask(__name__)

@app.route("/send", methods=["POST"])
def send():
    data = request.get_json()
    message = data.get("message")
    sender = data.get("sender")
    recipient = data.get("recipient")
    print(f"Message: {message}, Sender: {sender}, Recipient: {recipient}")
    return jsonify({"status": "success", "message": "Message sent!"}), 200


@app.route("/receive", methods=["POST"])
def receive():
    data = request.get_json()
    message = data.get("message")
    recipient = data.get("recipient")
    sender = data.get("sender")
    # Hier könnten Sie z.B. die Daten speichern oder verarbeiten
    print(f"Received Message: {message}, Recipient: {recipient}, Sender: {sender}")
    return jsonify({"status": "success", "message": "Message received!"}), 200


if __name__ == "__main__":
    app.run(debug=True)


