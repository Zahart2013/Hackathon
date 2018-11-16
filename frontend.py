from telegram.ext import Updater, CommandHandler
from telegram.ext import Filters, MessageHandler
import backend
from imdb import IMDb
lstgood = []
lstbad = []
i = 0
ia = IMDb()


def start(bot, update):
    greetings = 'Hello {}\n'.format(update.message.from_user.first_name)
    greetings += "I am ready to start."
    update.message.reply_text(greetings)


def saveanswer(bot, update):
    global i
    if i == 1:
        if len(lstgood) < 3:
            lstgood.append(update.message.text)
        elif len(lstbad) < 3:
            lstbad.append(update.message.text)
        if len(lstgood) == 3 and len(lstbad) == 0:
            update.message.reply_text(
                "Okey, now type three bad, your least favourite films")
        if len(lstgood) == 3 and len(lstbad) == 3:
            i = 0
            update.message.reply_text("All films are entered!")
            best_lst = backend.Get_Best_Films(lstgood, lstbad)


def testik(bot, update):
    update.message.reply_text("Good films: " + ", ".join(lstgood))
    update.message.reply_text("Bad films: " + ", ".join(lstbad))


def helpa(bot, update):
    update.message.reply_text(
        "Commands for bot:\n/advice - Asks for 3 good and 3 bad films and gives best relating films for you.\n/test - Gives already entered good and bad films.")


def advice(bot, update):
    lstgood.clear()
    lstbad.clear()
    global i
    i = 1
    update.message.reply_text("Please enter three your favourite films")
    # update.message.reply_text("And now please enter 3 worst films")


updater = Updater('787053848:AAF_lcSiJTT0AAIWKX5KmAwbHfxVcTh_KwM')

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('advice', advice))
updater.dispatcher.add_handler(MessageHandler(Filters.text, saveanswer))
updater.dispatcher.add_handler(CommandHandler('test', testik))
updater.dispatcher.add_handler(CommandHandler('help', helpa))
updater.start_polling()
updater.idle()
