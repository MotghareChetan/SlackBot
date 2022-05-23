# SlackBot 

# Required to use the Bot script

# A) Slack Bot App
  1. A slack Bot / App https://api.slack.com/apps?new_app=1 
  2. API TOKEN from slack App  (OAUTH AND PERMISSION PAGE)
  3. Signing Secret Key from slack app ( Basic Enviroment Page)
  4. Select BOT Token scope "Chat:write"  (OAUTH AND PERMISSION PAGE)
  5. Add bot event
  6. Bot is connected to the App ( Create channel in slack and add Bot )

# B)ngrok install

# C)Python packages required 
  1. slackclient (pip install slackclient)
  2. python-dotenv (pip install python-dotenv) to read .env file
  3. flask (pip install flask)
  4. slackeventsapi ( pip install slackeventsapi ) to grab events from slack channel

# Installation
 1. Clone the repo
 2. Create a bot user if you don't have one yet, and copy the API Token
 3. export SLACK_TOKEN="your-api-token" and Signing secret key 
 4. Invite Bot into any channels you want it in, or just message it in #general. 
 5. make run (or make repl for local testing)
 6. Open ngrok and type cmd --> "ngrok http 5000"     [5000 is port no]  
 

