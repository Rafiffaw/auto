import telegram
import json
import requests

def notify(message):
    with open('E:/VsCode/06-AutoElearning/keys.json') as keys_file:
        k = json.load(keys_file)
        token = k['telegram_token']
        chat_id = k['telegram_chat_id']
    bot = telegram.Bot(token=token)
    bot.sendMessage(chat_id=chat_id, text=message)

i = 1
def notify_ending(message):
    token = '1959542063:AAGCe7w-2TGCZ_P3ZJPX-NbhB-EERllFSFY'
    response = requests.get('https://api.telegram.org/bot1959542063:AAGCe7w-2TGCZ_P3ZJPX-NbhB-EERllFSFY/getupdates').text
    data = json.loads(response)
    a = data["result"] [0] ["message"] ["chat"] ["id"]
    chat_id = a
    bot = telegram.Bot(token=token)
    bot.sendMessage(chat_id=chat_id, text=message)

#while i <= 5:
    #notify_ending('hehe')
    #i +=1