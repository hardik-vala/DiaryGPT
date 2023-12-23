# DiaryGPT

Source code behind DiaryGPT: https://chat.openai.com/g/g-cA770mkRY-diarygpt.

Inspired by [GPT-3 Is the Best Journal I’ve Ever Used](https://every.to/chain-of-thought/gpt-3-is-the-best-journal-you-ve-ever-used).

## Motivation

Maintaining a diary can help you,
* Get your thoughts out of your head, rendering them less scary.
* Understand issues in your life better.
* Pull out patterns in your thinking (which increases your self-awareness).
* Create a record of your journey through life, which can tell you who you are at crucial moments.
* Bring more gratitude (or other positive emotions) into your life.
* Reveal your values.

## Problem

Problems with traditional journalling:
* It can be difficult to stare at a blank page and know what to write.
* If you use a static set of prompts (e.g. “What are you grateful for today?”), the practice can feel stale after some time.
* You don’t read through your old entries often, so the act of writing down your thoughts and experiences doesn’t compound in the way that it should. 

## Solution

* Journalling with GPT puts the practice of self-reflection on steroids.
* Journalling becomes more like a conversation, so you don’t have to feel paralyzed by a blank page.
* It reacts to you with genuinely fresh and personal prompts, so journalling is much less likely to get stale or old.
* It can summarize things you’ve shared in concise language that helps you learn from past experiences.

DiaryGPT is a mashup of journaling and more involved forms of support, like talking to an empathetic friend. It becomes a guide through your mind -- one that shows unconditional positive regard and acceptance for whatever you’re feeling. It asks thoughtful questions, and doesn’t judge. It’s around 24/7, it never gets tired or sick, and it’s not very expensive.

You can find the Custom GPT configuration in `configuration.md`.

### Supporting Reminders (Optional)

If you want to give DiaryGPT the ability to remember things, you can run the reminder service in this repository and allow DiaryGPT to communicate with it.

Follow these steps:

#### 1) Deploy service

Install command:

```
pip install -r requirements.txt
```

Run command:

```
python app.py
```

#### 2) Add Actions

Add the following Action schema:

```
{
  "openapi": "3.1.0",
  "info": {
    "title": "Diary Reminders",
    "description": "Reminders for subjects to reflect on.",
    "version": "v0.1.0"
  },
  "servers": [
    {
      "url": "${SERVICE_URL}"
    }
  ],
  "paths": {
    "/reminder/append": {
      "post": {
        "description": "Save a diary reminder to journal about later.",
        "operationId": "AppendReminder",
        "parameters": [],
        "requestBody": {
          "description": "JSON reminder to save.",
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "reminder": {
                    "type": "string",
                    "description": "The contents of the reminder to save."
                  }
                },
                "required": ["reminder"]
              }
            }
          }
        },
        "responses": {
          "201": {
            "description": "Reminder saved successfully."
          }
        },
        "deprecated": false
      }
    },
    "/reminder/list/today": {
      "get": {
        "description": "Get diary reminders for today to prepare for an entry.",
        "operationId": "GetTodaysReminders",
        "parameters": [],
        "deprecated": false
      }
    }
  },
  "components": {
    "schemas": {}
  }
}
```

And append this information to the instructions:

```
Action Information:

Use the "GetTodaysReminders" action when I'm reflecting on my day to retrieve subjects I want to reflect on in a diary session.
Use the "AppendReminder" action when I ask you to explicitly remind to journal about something later. The content of the reminder should be added as a value against the key "reminder" in a JSON object passed using the request body.
```

#### 3) Add a privacy policy

To get around this requirement, I just use https://api.example-weather-app.com/privacy.
