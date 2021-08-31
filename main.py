from telethon import TelegramClient ,events

# Remember to use your own values from my.telegram.org!
api_id = 7603172
api_hash = '525114eecdf18bb18303d765b475a866'

client = TelegramClient('anon', api_id, api_hash)

@client.on(events.NewMessage)
async def handler(event):
    # chat_id=event.chat_id
    # chat=await event.get_chat()
    # print(chat)
    chat_id=event.chat_id
    msg= event.raw_text
    print(msg," ",chat_id)
    if chat_id == -586656319:
        # print("yes")
        await client.send_message(-489795707,msg)

client.start()
client.run_until_disconnected()