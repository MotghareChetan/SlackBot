import slack
import os
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask
from slackeventsapi import SlackEventAdapter

env_path = Path('.') / '.env'      # locate path of environment file
load_dotenv(dotenv_path=env_path)  # load environment confi file

app = Flask(__name__)      # Flask constructor takes the name of current module (__name__) as argument.

slack_event_adapter = SlackEventAdapter(
    os.environ['SIGN_SECRET'], '/slack/events', app)  # to handle different events that sends to slack

client = slack.WebClient(token=os.environ['SLACK_TOKEN'])    # Bot token to interact with

Bot_id = client.api_call("auth.test")["user_id"]    # Get Bot user_id

@slack_event_adapter.on('message')    # handle on message events
def message(payload):
    event = payload.get('event', {})   # give info about events on channel ( use to get slack message event)
    channel_name = event.get('channel')
    user_id = event.get('user')
    user_text = event.get('text')
    if Bot_id != user_id:
     client.chat_postMessage(channel=channel_name, text=user_text)


if __name__ == "__main__": # To run flash application
    app.run(debug=True)

