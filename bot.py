from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def greet_user(bot,update):
    print('Какой-то перец вызвал /start')
    bot.sendMessage(update.message.chat_id, text='Привет, добрый человек! Это второй Танин бот для разговоров с инопланетянами. Пиши мне о любви на азбуке Морзе <3')
    

def show_error(bot, update, error):
       print('Update "{}" caused error "{}"'.format(update,error))


def talk_to_me(bot,update):
    print('Пришло сообщение: {}'.format(update.message.text))
    bot.sendMessage(update.message.chat_id, update.message.text)


def main():
    updater = Updater('324665814:AAHxPqdMKo6tYqAO4MboolgBWBlsVPk0lbk')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler([Filters.text], talk_to_me))
    dp.add_error_handler(show_error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()