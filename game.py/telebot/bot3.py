import telebot

TOKEN = "7440544362:AAGhdwZ3l8FnX6apPCTgOwrSUOS3l6C32QU"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "hello world ")


@bot.message_handler(commands=['adodo'])
def send_adodo(message):
    adodo_url = "https://soundboardguy.com/sounds/suuuuui/suuuuui.mp3"
    bot.send_adodo(message.chat.id, f"got video: {adodo_url}")



@bot.message_handler(commands=['photo'])
def send_photo(message):
    photo_url = "https://yandex.ru/images/search?text=suuuui&img_url=https%3A%2F%2Fkartinkof.club%2Fuploads%2Fposts%2F2022-03%2F1648292943_3-kartinkof-club-p-ronaldo-siii-mem-3.jpg&pos=0&rpt=simage&serp_list_type=all&stype=image&lr=10309&parent-reqid=1740026399407144-12290212448798791310-balancer-l7leveler-kubr-yp-sas-240-BAL&source=serp"
    bot.send_photo(message.chat.id,f"got video: {photo_url}")



@bot.message_handler(commands=['video'])
def send_video(message):
    video_url = "https://youtu.be/nHB1dl67pGc"
    bot.send_video(message.chat.id, f"got video: {video_url}")    




@bot.message_handler(commands=['games'])
def send_games(message):
    games_url = "https://yandex.ru/images/search?text=suuuui&img_url=https%3A%2F%2Fkartinkof.club%2Fuploads%2Fposts%2F2022-03%2F1648292943_3-kartinkof-club-p-ronaldo-siii-mem-3.jpg&pos=0&rpt=simage&serp_list_type=all&stype=image&lr=10309&parent-reqid=1740026399407144-12290212448798791310-balancer-l7leveler-kubr-yp-sas-240-BAL&source=serp"
    bot.send_games(message.chat.id,f"got video: {photo_url}")




@bot.message_handler(commands=['photo'])
def send_photo(message):
    photo_url = "https://yandex.ru/images/search?text=suuuui&img_url=https%3A%2F%2Fkartinkof.club%2Fuploads%2Fposts%2F2022-03%2F1648292943_3-kartinkof-club-p-ronaldo-siii-mem-3.jpg&pos=0&rpt=simage&serp_list_type=all&stype=image&lr=10309&parent-reqid=1740026399407144-12290212448798791310-balancer-l7leveler-kubr-yp-sas-240-BAL&source=serp"
    bot.send_photo(message.chat.id,f"got video: {photo_url}")


@bot.message_handler(commands=['photo'])
def send_photo(message):
    photo_url = "https://yandex.ru/images/search?text=suuuui&img_url=https%3A%2F%2Fkartinkof.club%2Fuploads%2Fposts%2F2022-03%2F1648292943_3-kartinkof-club-p-ronaldo-siii-mem-3.jpg&pos=0&rpt=simage&serp_list_type=all&stype=image&lr=10309&parent-reqid=1740026399407144-12290212448798791310-balancer-l7leveler-kubr-yp-sas-240-BAL&source=serp"
    bot.send_photo(message.chat.id,f"got video: {photo_url}")



@bot.message_handler(commands=['photo'])
def send_photo(message):
    photo_url = "https://yandex.ru/images/search?text=suuuui&img_url=https%3A%2F%2Fkartinkof.club%2Fuploads%2Fposts%2F2022-03%2F1648292943_3-kartinkof-club-p-ronaldo-siii-mem-3.jpg&pos=0&rpt=simage&serp_list_type=all&stype=image&lr=10309&parent-reqid=1740026399407144-12290212448798791310-balancer-l7leveler-kubr-yp-sas-240-BAL&source=serp"
    bot.send_photo(message.chat.id,f"got video: {photo_url}")




bot.infinity_polling()