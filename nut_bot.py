from groupy import Client
import meme as m
import time
import pdb
import json
txt = ""
client=Client.from_token("1hLpOWTPR2S6rADtCPFanKvdv20FblNOixHN0Yva") #auth token
for group in client.groups.list(): #for each group in list of groups aka group chats
    if group.name=="No Nut November": break
nut_names = []
with open("nut_names.json", 'r') as f:
    nut_names = json.load(f)
    f.close()

while True:
    messages = group.messages.list()  # list object
    
    for msg in messages:
        if msg.name.casefold() == "groupme":  # was sent by groupme service
            if " has left the group." in msg.text:
                txt = msg.text.removesuffix(" has left the group.")
                if txt not in nut_names:
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

                