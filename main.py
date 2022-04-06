from telethon import TelegramClient
from telethon.sync import events
from telethon.tl.functions.channels import JoinChannelRequest
from telethon. tl. functions.messages import ImportChatInviteRequest
    

api_id = here
api_hash = "here"
bot_token = 'here'

client = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

whitelist = []

@client.on(events.NewMessage)
async def any_message_arrived_handler(event):
  global whitelist
  chat = await event.get_chat()
  user = chat.username
   
  msg = event.text
  
  #replied = 
  if "addwhite" in msg:
    whitelist.append(user)
  if user in whitelist:
    chat = await event.get_chat()
    #getmessage = await client.get_messages(entity='meinheckeranonym',limit=1)
    await client.send_message(entity='onbxzdaoatechannellisbdddidbdejr',message=msg)
  else:
    await client.send_message(entity=user,message="get out mannnhhh")

  

client.run_until_disconnected()
