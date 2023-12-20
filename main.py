import telebot
import time
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

TOKEN = "6581334486:AAERuNCGIo5BTlSwM4Trbc6dDdiIJ2yRVCw"


admins=[748626808,5335339346]
chanel_id=-1002089092807
def listener(messages):
    """
    When new messages arrive TeleBot will call this function.
    """
    for m in messages:
        print(m)
        cid = m.chat.id
        if m.content_type == 'text':
            print(str(m.chat.first_name) +
                  " [" + str(m.chat.id) + "]: " + m.text)
        elif m.content_type == 'photo':
            print(str(m.chat.first_name) +
                  " [" + str(m.chat.id) + "]: " + "New photo recieved")
        elif m.content_type == 'document':
            print(str(m.chat.first_name) +
                  " [" + str(m.chat.id) + "]: " + 'New Document recieved')


bot = telebot.TeleBot(TOKEN)
bot.set_update_listener(listener)


def split_(text):
    txt=text.split(" ")
    print(txt)
    if "سیاه" in txt:
        print("yes")
    return txt


@bot.message_handler(commands=['stsrt'])
def command_start_p(m):
    print("llllll")
    cid = m.chat.id
    group_id = m.chat.id
    markup=ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton("محصولات"),KeyboardButton("درباره ما"))
    bot.send_message(group_id,"از دکمه ها برای استفاده از ربات استفاده کنید",reply_markup=markup)

@bot.message_handler(commands=['product'])
def command_start_p(m):
    cid = m.chat.id
    group_id = m.chat.id
    productt(m)

@bot.message_handler(func=lambda m: m.chat.type == 'group' or m.chat.type == 'supergroup' and m.text=="ربات")
def install_robot(m):
    group_id = m.chat.id
    cid=m.from_user.id
    if cid in admins:
        bot.send_message(group_id,"سلام عزیزم جانم امر کن")
    else:
        bot.send_message(group_id,"بنال")


@bot.message_handler(func=lambda m: m.chat.type == 'group' or m.chat.type == 'supergroup' and "سیاه" in split_(m.text))
def syah(m):
    group_id = m.chat.id
    cid=m.from_user.id
    if cid not in admins:
        bot.send_message(group_id,"هوی",reply_to_message_id=m.message_id)
        time.sleep(1)
        bot.send_message(group_id,"کونکش",reply_to_message_id=m.message_id)
        time.sleep(1)
        bot.send_message(group_id,"دیگه از اون کلمه استفاده نمیکنی ها کیصکیش",reply_to_message_id=m.message_id)


@bot.message_handler(func=lambda m: m.chat.type == 'group' or m.chat.type == 'supergroup' and "RGB" in split_(m.text))
def syah(m):
    
    group_id = m.chat.id
    cid=m.from_user.id
    if cid not in admins:
        bot.send_message(group_id,"هوی",reply_to_message_id=m.message_id)
        time.sleep(1)
        bot.send_message(group_id,"حواسم هست بهت باسنی",reply_to_message_id=m.message_id)
        time.sleep(1)
        bot.send_message(group_id,"دیگه از اون کلمه استفاده نمیکنی ها کیصکیش",reply_to_message_id=m.message_id)
@bot.message_handler(func=lambda m: m.chat.type == 'group' or m.chat.type == 'supergroup' and "نیگا" in split_(m.text))
def syah(m):
    
    group_id = m.chat.id
    cid=m.from_user.id
    if cid not in admins:
        bot.send_message(group_id,"هوی",reply_to_message_id=m.message_id)
        time.sleep(1)
        bot.send_message(group_id,"کونکش",reply_to_message_id=m.message_id)
        time.sleep(1)
        bot.send_message(group_id,"دیگه از اون کلمه استفاده نمیکنی ها کیصکیش",reply_to_message_id=m.message_id)
@bot.message_handler(func=lambda m: m.chat.type == 'group' or m.chat.type == 'supergroup' and "Black" in split_(m.text))
def blacj(m):
    group_id = m.chat.id
    cid=m.from_user.id
    if cid not in admins:
        bot.send_message(group_id,"هووووووش ",reply_to_message_id=m.message_id)
        time.sleep(1)
        bot.send_message(group_id,"لاشی",reply_to_message_id=m.message_id)
        time.sleep(1)
        bot.send_message(group_id,"باسنت به خارش اومده؟ حواست باشه نبرمت سایت blacked.com بهت تجاوز کنم",reply_to_message_id=m.message_id)


@bot.message_handler(func=lambda m: m.chat.type == 'group' or m.chat.type == 'supergroup' and "بلک" in split_(m.text))
def blacj(m):
    group_id = m.chat.id
    cid=m.from_user.id
    if cid not in admins:
        bot.send_message(group_id,"هووووووش ",reply_to_message_id=m.message_id)
        time.sleep(1)
        bot.send_message(group_id,"لاشی",reply_to_message_id=m.message_id)
        time.sleep(1)
        bot.send_message(group_id,"باسنت به خارش اومده؟ حواست باشه نبرمت سایت blacked.com بهت تجاوز کنم",reply_to_message_id=m.message_id)
@bot.message_handler(func=lambda m: m.chat.type == 'group' or m.chat.type == 'supergroup' and m.text=="محصولات")
def productt(m):
    group_id = m.chat.id
    cid=m.from_user.id
    for i in range(4,9):
        try:
            bot.copy_message(group_id,chanel_id,i,reply_to_message_id=m.message_id)
        except:
            pass


@bot.message_handler(func=lambda m: m.from_user.id ==2082216862 )
def syah(m):
    group_id = m.chat.id
    cid=m.from_user.id
    bot.send_message(group_id,"اوووووف جوووون سفید مفید تو فقط پیام بده من رباتم شق کردم",reply_to_message_id=m.message_id)
@bot.message_handler(func=lambda m: m.chat.type == 'group' or m.chat.type == 'supergroup' and m.text=="درباره ما")
def abaut(m):
    group_id = m.chat.id
    cid=m.from_user.id
    for i in range(1,4):
        try:
            bot.copy_message(group_id,chanel_id,i,reply_to_message_id=m.message_id)
        except:
            pass


bot.infinity_polling()
