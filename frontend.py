from telegram.ext import Updater, CommandHandler
from telegram.ext import Filters, MessageHandler
import backend
from backend import ia, Get_Best_Films
lstgood = []
lstbad = []
used = []
i = 0


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
                "Okay, now type three bad, your least favourite films")
        if len(lstgood) == 3 and len(lstbad) == 3:
            i = 0
            update.message.reply_text("All films are entered!")
            update.message.reply_text(
                "Please wait for some hours and pray for the server not to fall.")
            try:
                best_lst = Get_Best_Films(lstgood, lstbad)
                update.message.reply_text(
                    "Enjoy this films:")
                for elem in best_lst:
                    update.message.reply_text(str(elem))
            except:
                update.message.reply_text("Oooops... Server connection error")


def tester(bot, update):
    update.message.reply_text("Good films: " + ", ".join(lstgood))
    update.message.reply_text("Bad films: " + ", ".join(lstbad))


def helper(bot, update):
    update.message.reply_text(
        "Commands for bot:\n/advice - Asks for 3 good and 3 bad films and gives best relating films for you.\n/test - Gives already entered good and bad films.")


def advice(bot, update):
    global i
    lstgood.clear()
    lstbad.clear()
    i = 1
    update.message.reply_text("Please enter three of your favourite films")
    # update.message.reply_text("And now please enter 3 worst films")


updater = Updater('787053848:AAF_lcSiJTT0AAIWKX5KmAwbHfxVcTh_KwM')

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('advice', advice))
updater.dispatcher.add_handler(MessageHandler(Filters.text, saveanswer))
updater.dispatcher.add_handler(CommandHandler('test', tester))
updater.dispatcher.add_handler(CommandHandler('help', helper))
updater.start_polling()
updater.idle()
