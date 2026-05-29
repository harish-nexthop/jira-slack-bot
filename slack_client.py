import os
from slack_bolt import App
from dotenv import load_dotenv

load_dotenv()

app_token = App(token=os.getenv("SLACK_BOT_TOKEN"))

def post_report(report_text):
    get_channel_id = os.getenv("SLACK_CHANNEL_ID")
    app_token.client.chat_postMessage(
        channel=get_channel_id,
        text=report_text
    )

post_report("Hello from the IT Bot!")

