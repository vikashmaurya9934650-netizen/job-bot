import feedparser
import time
import os
from telegram import Bot

TOKEN = os.environ.get("TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

bot = Bot(token=TOKEN)

sent_links = []

def get_jobs():
    feed = feedparser.parse("https://www.sarkariresult.com/feed/")
    return feed.entries

while True:
    jobs = get_jobs()

    for job in jobs:
        title = job.title.lower()

        if "12th" in title or "intermediate" in title:
            if job.link not in sent_links:
                message = f"🔥 New Job Alert!\n\n{job.title}\n{job.link}"
                bot.send_message(chat_id=CHAT_ID, text=message)
                sent_links.append(job.link)

    time.sleep(300)

