from telegram import Update,InlineKeyboardButton,InlineKeyboardMarkup,InputFile,InputFile
from telegram.ext import CallbackContext,CommandHandler, Updater, MessageHandler, Filters,CallbackQueryHandler,ConversationHandler
import logging


print("start bot")
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
img_first_room = ["https://mountain-residence.com/storage/apartments/room_gallery/big/289PqRohhfk3YkGKGJg5kITmxy7JjPZveqdyBElI.jpg",
"https://mountain-residence.com/storage/apartments/room_gallery/big/T7CCsFhMX1jWCIFM3m2l4txrdZsPq1QqguAI9uAn.jpg",
"https://mountain-residence.com/storage/apartments/room_gallery/big/9LGPr4gjlbiLYLaI1P3tVhoH5ksSnY33M1q7F3vk.jpg",
"https://mountain-residence.com/storage/apartments/room_gallery/popup/PWFVOQuQ8QBd0EChNuqfZ16oR2o1eET3aDUNMyvh.jpg",
"https://mountain-residence.com/storage/apartments/room_gallery/popup/wuHYJnaBJnHGSIXCkv9S79klcpVXt4sbUBnPBLQp.jpg",
"https://mountain-residence.com/storage/apartments/room_gallery/popup/xQgiThh14TTcCxMWy00Va6wxrE2cnH6PWbYtQrmk.jpg"

]
img_second_room = [
    "https://mountain-residence.com/storage/apartments/room_gallery/popup/9Av14cjFlgZjRCbsgjA0pquHawXOnUxwez9EpZg7.JPG",
    "https://mountain-residence.com/storage/apartments/room_gallery/popup/yKxJNOfpyfwyBHoczRajSvWjjCUCXO7pC0BqEpeZ.JPG",
    "https://mountain-residence.com/storage/apartments/room_gallery/popup/nOvfWaXUfG6wnDrqf2cjFzJvEsZ9Jy9y9BzA8UTj.JPG",
    "https://mountain-residence.com/storage/apartments/room_gallery/popup/HtgLZAdZ9QkKXIH58NbXa45adm6TkCHhok0VxveG.jpg"
]
img_three_room =[ 
    "https://mountain-residence.com/storage/apartments/room_gallery/popup/8lx749tAKZESe11dk24sDTR8lO0MenES5eE5F3Bo.JPG",
    "https://mountain-residence.com/storage/apartments/room_gallery/popup/Z6R43WtgVI9mrrCQK5RovNyHg9yzLY0W7esBdZS2.JPG",
    "https://mountain-residence.com/storage/apartments/room_gallery/popup/I52hhmfQSXi4WWoj0iGrM3EWpL8z0oidi8LCTJI8.JPG",
    "https://mountain-residence.com/storage/apartments/room_gallery/popup/u78YPcIBrT0Rx2nJeouRIuaAAnjqKnJnHEwZNBsX.JPG"

]
img_four_room =[ 
    'https://mountain-residence.com/storage/apartments/room_gallery/popup/289PqRohhfk3YkGKGJg5kITmxy7JjPZveqdyBElI.jpg',
    'https://mountain-residence.com/storage/apartments/room_gallery/popup/T7CCsFhMX1jWCIFM3m2l4txrdZsPq1QqguAI9uAn.jpg',
    'https://mountain-residence.com/storage/apartments/room_gallery/popup/9LGPr4gjlbiLYLaI1P3tVhoH5ksSnY33M1q7F3vk.jpg',
    'https://mountain-residence.com/storage/apartments/room_gallery/popup/wuHYJnaBJnHGSIXCkv9S79klcpVXt4sbUBnPBLQp.jpg',
    'https://mountain-residence.com/storage/apartments/room_gallery/popup/xQgiThh14TTcCxMWy00Va6wxrE2cnH6PWbYtQrmk.jpg'

]
STEP_ONE, STEP_TWO, STEP_THREE,STEP_FOUR = range(4)

user_info = []

def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привіт, я бот по бронювання номерів в  готелі команда  /help тобі допоможе)")
    

def ask_user_info(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Ведіть Прізвище, email, телефон через пробіл ,відміти бронювання /stop")
    return STEP_ONE
    

def ask_room_info(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Ведіть на скільки осіб ви хочете кімнату ,відміти бронювання /stop")
    return STEP_THREE


def user_finish(update: Update, context: CallbackContext):
    global user_input_how
    user_input_how = int(update.message.text)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Вільна кімната , відміти бронювання /stop")
    if user_input_how == 1:
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=(img_second_room[0]))
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=(img_second_room[1]))
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=(img_second_room[2]))
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=(img_second_room[3]))
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=(img_second_room[4]))
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=(img_second_room[5]))
    elif user_input_how == 2:
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=(img_first_room[0]))
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=(img_first_room[1]))
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=(img_first_room[2]))
    elif user_input_how == 3:
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=(img_three_room[0]))
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=(img_three_room[1]))
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=(img_three_room[2]))
    elif user_input_how == 4:
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=(img_four_room[0]))
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=(img_four_room[1]))
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=(img_four_room[2]))
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text=":(")
    
    update.message.reply_text('ведіть дату заїзду зразок (з 27 серпня по 23 лютого)')
    return STEP_FOUR

    


def reservation(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [
            InlineKeyboardButton("Зарезервувати", callback_data="reservationnn"),
        
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Зарезервувати зараз", reply_markup=reply_markup)


def help(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="/call - Звязатися з нами \n /reservation - резервувати номер  ")

def call(update, context):
    
    context.bot.send_message(chat_id=update.effective_chat.id, text="Гаряча лінія готелю, +380981703139")
   
def summariess(update, context):
    global user_input_data
    user_input_data = update.message.text
    context.bot.send_message(chat_id=update.effective_chat.id, text="Дата подана,натисніть на команду /summaries щоб побачити підсумк бронювання")
    return ConversationHandler.END
def summaries(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Ви забронювали кімнату на прізвище {user_name_1} на {user_input_how} людей, {user_input_data} , Гарного відпочинку)")
    context.bot.send_message(chat_id=update.effective_chat.id, text='Якщо хочете відміти бронювання натисніть команду /abolition')
def abolition(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Ви відмінили бронювання /help')


def cancel(update: Update, context: CallbackContext):
    update.message.reply_text('Cancelled by user. Send /help to start again')
    return ConversationHandler.END

def save_user_info(update: Update, context: CallbackContext):
    user_input = update.message.text
    user_input = user_input.split()
    global user_name_1
    global user_email_2
    global user_phone_3
    user_name_1  = user_input[0]
    user_email_2 = user_input[1]
    user_phone_3 = user_input[2]
    
    context.bot.send_message(chat_id=update.effective_chat.id, text="Інформацію про користувача збереженоn натисніть /select_room для вибору номеру")

    return STEP_TWO


updater = Updater(token='5513941464:AAGk31z6jIisw2Ih10vo-FEu-QSq_lcdc2Y')
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(CommandHandler('call', call))
dispatcher.add_handler(CommandHandler('abolition',abolition ))
dispatcher.add_handler(CommandHandler('reservation', reservation))
dispatcher.add_handler(CommandHandler('summaries', summaries))

branch_user_handler = ConversationHandler(
    entry_points = [CallbackQueryHandler(ask_user_info,'reservationnn')],
    states={
        STEP_ONE:       [MessageHandler(Filters.text & (~ Filters.command), save_user_info)],
        STEP_TWO:       [CommandHandler('select_room', ask_room_info)],
        STEP_THREE:     [MessageHandler(Filters.text & (~ Filters.command), user_finish)],
        STEP_FOUR:      [MessageHandler(Filters.text & (~ Filters.command), summariess)]
    }, 
    fallbacks=[CommandHandler("stop", cancel)]
)
dispatcher.add_handler(branch_user_handler)

updater.start_polling()
updater.idle()
