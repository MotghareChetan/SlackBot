# This is test file
import slack
import os
from pathlib import Path
from dotenv import load_dotenv


env_path = Path('.') / '.env'      # locate path of environment file
load_dotenv(dotenv_path=env_path)  # load environment confi file

client = slack.WebClient(token=os.environ['SLACK_TOKEN'])

client.chat_postMessage(channel='testbot1', text="Hello")