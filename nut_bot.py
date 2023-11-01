from groupy import Client
import meme as m
import time
import pdb
import json
import logging
from logging.handlers import RotatingFileHandler
import os
import sys


log_file = os.path.join(sys.path[0], "nut_bot.log")
logging.disabled = False
log_level = "DEBUG"
max_bytes = 1000000
backups = 10
logger = logging.getLogger("simple_logger")
logger.setLevel(level=log_level)
handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backups)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.info("Logging started")


txt = ""

nut_names = []
with open("nut_names.json", 'r') as f:
    nut_names = json.load(f)
    f.close()

while True:
    try:
        logger.debug("Starting new client")
        client=Client.from_token("") #auth token
        for group in client.groups.list(): #for each group in list of groups aka group chats
            if group.name=="No Nut November": break
        logger.debug("Fetching messages")
        messages = group.messages.list()  # list object
        for msg in messages:
            if msg.name.casefold() == "groupme":  # was sent by groupme service
                if " has left the group." in msg.text:
                    txt = msg.text.removesuffix(" has left the group.")
                    if txt not in nut_names:
                        logger.debug("Found new name that has left the group: %s", txt)
                        nut_names.append(txt)
                        with open("nut_names.json", "w") as f:
                            f.write(json.dumps(nut_names))
                            f.close()
                        with open ('krabs.png', 'rb') as f:
                            m.caption_image(f,"", txt+" HAS NUTTED")
                        with open ('output.png', 'rb') as f:
                            image1=client.images.from_file(f)
                        group.post(text = txt+' has nutted', attachments=[image1])
        time.sleep(60)
    except Exception as e:
        logger.warning("wah wah, the code nutted: %s", e)
        logger.warning("Restarting client connection")

                    
