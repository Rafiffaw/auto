import telegram

def notify(message):
    token = '1959542063:AAGCe7w-2TGCZ_P3ZJPX-NbhB-EERllFSFY'
    chat_id = 1767730053
    bot = telegram.Bot(token=token)
    bot.sendMessage(chat_id=chat_id, text=message)
