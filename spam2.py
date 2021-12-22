#!/bin/python3
import json, time
import vk_api, random
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import requests

def send(message,tok,peer_id,reply=None):
    return json.loads(requests.post("https://api.vk.com/method/messages.send?v=5.131&random_id=0",data={'peer_ids': [peer_id], 'reply_to': reply,'message': message,'access_token':tok}).content.decode('utf-8'))

TOKEN = "cb56b10218234278153f364897471a1ff83fbf0c1e9503e15d1e3b9645fe5d9ea8237db081942db73fe28"
vks = vk_api.VkApi(token=TOKEN)
vks._auth_token()
longpoll = VkBotLongPoll(vks, "209718332")
vk = vks.get_api()
for event in longpoll.listen():
    print(event)
    if event.type == VkBotEventType.MESSAGE_NEW:
        if 'хохляндия' in event.message['text'].lower():
            for _ in range(10000):
                for i in range(500):
                    send(f'Хохлы {random.choice(["пидорасы", "геи", "сосут", ", забытые спросить", "пендосы", "свиньи", "хрю-хрю"])}',TOKEN,event.message['peer_id'])
                time.sleep(10)