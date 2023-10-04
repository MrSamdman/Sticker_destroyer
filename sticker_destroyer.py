import telebot, os, dotenv

dotenv.load_dotenv()

bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))

# Белый список стикеров
white_list = []


@bot.message_handler(content_types=['sticker'])
def delete_stickers(message):
    if message.sticker.set_name not in white_list:
        try:
            bot.delete_message(message.chat.id, message.message_id)
            print("Deleted!", message.sticker.set_name)

        except telebot.apihelper.ApiException as e:
            print(e)


@bot.message_handler(commands=["addsp"])
def sp_adding(mes):

    if mes.from_user.username == "Maxlosif":
        sp_name = mes.text[mes.text.find("addsp")+6:]
        print(sp_name, "---Added")
        try:
            white_list.append(sp_name)
        except telebot.apihelper.ApiException as e:
            print(e)


bot.infinity_polling()
