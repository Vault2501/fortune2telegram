# fortune2telegram
Selenium script to post fortune messages on telegram

# Requirements
- Google Chrome Browser
- fortune

# Install
```
python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
```

# Configuration
## Authentication
fortune2telegram starts a chrome browser with own profile when run and connects to the configured Telegram room. When this happens the first time, you will have 60 seconds to login using the started chrom window. This will be stored in the profile, and the next runs you will be authenticated. To change the waiting time, adjust this variable:
```
auth_seconds = 60
```

## Telegram Group
Before you can use the tool, you need to configure the room uri to connect to. You can get it from the url in the browser of the Telegram WebUI:
```
chat = 'https://web.telegram.org/k/<room_id>'
```

## Timing
Post will be done in random intervals, ranging between these values:
```
min_seconds = 3600 # minimum time in between posts
max_seconds = 14400 # maximum time in between posts
```

## Fortune
Edit `fortunate` to add fortune options if needed

# Usage
```
python ./fortun2telegram.py
