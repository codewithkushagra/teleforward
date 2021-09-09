# from telethon import TelegramClient ,events

# # Remember to use your own values from my.telegram.org!
# api_id = 7219082
# api_hash = '53999c3a55d5148c6620af8d8c224e68'


# client = TelegramClient('anon', api_id, api_hash)

# @client.on(events.NewMessage)
# async def handler(event):
#     # chat_id=event.chat_id
#     # chat=await event.get_chat()
#     # print(chat)
#     #my channel ID -1001218728849
#     chat_id=event.chat_id
#     msg= event.raw_text
#     print(msg," ",chat_id)
#     if chat_id == 1534836973: #<= paste here
#          # print("yes")
#          await client.send_message(-1001218728849,msg)

# client.start()
# client.run_until_disconnected()

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

    # collect_data_from={
    #     'stock':-565276723
    # }
    # send_to_stock={
    #     'stock':-1001572756337
    # }

    #values to put in:
    link_send={
          #let 1534... be x , x is from grp. [grp1id, grp2id]         # y : [grp1,grp2...]
         
          -1001225259718 : [-1001446464850 ],
         -1001391902313 : [-1001554198482],
          -1001298607338 : [-1001218728849]

          #coming from -5627.. send to list
    }

    for datafrom in link_send.keys(): #find all the group from where data is data is collected
        if chat_id==datafrom:    
            for group in link_send[datafrom]:
                await client.send_message(group,msg)  #send message to all the group in the list

client.start()
client.run_until_disconnected()
