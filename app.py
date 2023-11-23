from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# In-memory log of reminders.
REMINDER_LOG = []

@app.route("/reminder/append", methods=["POST"])
def add_reminder():
  content = request.json.get("reminder")
  if not content:
    return jsonify({"error": "No reminder content provided."}), 400

  reminder = {
    "content": content,
    "creation_timestamp": datetime.now(),
  }

  REMINDER_LOG.append(reminder)
  return jsonify({}), 201


@app.route("/reminder/list/today", methods=["GET"])
def get_todays_reminders():
  today = datetime.now().date()
  todays_reminders = [reminder for reminder in REMINDER_LOG if reminder["creation_timestamp"].date() == today]
  formatted_todays_reminders = {"contents": [r["content"] for r in todays_reminders]}
  return jsonify(formatted_todays_reminders)


if __name__ == "__main__":
  app.run(debug=False)
