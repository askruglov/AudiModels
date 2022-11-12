import telebot;
bot = telebot.TeleBot('5380251559:AAE1b2ENNHTrR8_sL5MpMrCdB-4eyMkDLbg');
from telebot import types
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id,'Как работает бот:\nБот принимает запрос и выдает общую информацию о выбранном автомобиле. Для начала работы напишите "Go".\n\nКоманды:\n/start - запуск бота\n/help - если возникли проблемы с запуском программы\n/about - подробнее о боте, его авторе и обратной связи')
@bot.message_handler(commands=["about"])
def about(m, res=False):
    bot.send_message(m.chat.id,' AudiModels - сайт-каталог популярных моделей марки Audi. Бот предоставляет основную информацию о модели: тип кузова, платформа, варианты двигателей, коробок передач, привод, длина, ширина, высота, масса.\n\nБот AudiModels - полностью некомерческий проект, созданный для поклонников марки. Ассортимент моделей будет пополняться с течением времени, модели лтинейки S и RS находятся на стадии разработки.\n\nДанный бот создан как эксперимент, поэтому может содержать недостоверную информацию. Если вы нашли ошибку или у вас есть предложения по улучшению бота, напишите об этом создателю @askruglov.') 
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Go":
        audikeyboard = types.InlineKeyboardMarkup()
        key_80 = types.InlineKeyboardButton(text='80', callback_data='80gen')
        audikeyboard.add(key_80)
        key_100 = types.InlineKeyboardButton(text='100', callback_data='100gen')
        audikeyboard.add(key_100)
        key_a1 = types.InlineKeyboardButton(text='A1', callback_data='a1gen')
        audikeyboard.add(key_a1)
        key_a3 = types.InlineKeyboardButton(text='A3', callback_data='a3gen')
        audikeyboard.add(key_a3)
        key_a4 = types.InlineKeyboardButton(text='A4/A4 allroad', callback_data='a4gen')
        audikeyboard.add(key_a4)
        key_a5 = types.InlineKeyboardButton(text='A5', callback_data='a5gen')
        audikeyboard.add(key_a5)
        key_a6 = types.InlineKeyboardButton(text='A6/A6 allroad', callback_data='a6gen')
        audikeyboard.add(key_a6)
        key_a7 = types.InlineKeyboardButton(text='A7', callback_data='a7gen')
        audikeyboard.add(key_a7)
        key_a8 = types.InlineKeyboardButton(text='A8', callback_data='a8gen')
        audikeyboard.add(key_a8)
        key_q2 = types.InlineKeyboardButton(text='Q2', callback_data='q2gen')
        audikeyboard.add(key_q2)
        key_q3 = types.InlineKeyboardButton(text='Q3', callback_data='q3gen')
        audikeyboard.add(key_q3)
        key_q5 = types.InlineKeyboardButton(text='Q5', callback_data='q5gen')
        audikeyboard.add(key_q5)
        key_q7 = types.InlineKeyboardButton(text='Q7', callback_data='q7gen')
        audikeyboard.add(key_q7)
        key_q8 = types.InlineKeyboardButton(text='Q8', callback_data='q8gen')
        audikeyboard.add(key_q8)
        key_etron = types.InlineKeyboardButton(text='E-TRON', callback_data='etrongen')
        audikeyboard.add(key_etron)
        key_tt = types.InlineKeyboardButton(text='TT', callback_data='ttgen')
        audikeyboard.add(key_tt)
        key_r8 = types.InlineKeyboardButton(text='R8', callback_data='r8gen')
        audikeyboard.add(key_r8)
        bot.send_message( message.from_user.id, text='Выберите модель',reply_markup=audikeyboard)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Чтобы запустить бота, напишите Go.\nЧтобы узнать информацию о боте и его создателе, напишите /about.")
    else:
        bot.send_message(message.from_user.id, "Не понимаю вас. Напишите /help.")
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "80gen":
        eightykeyboard = types.InlineKeyboardMarkup()
        key_80b1 = types.InlineKeyboardButton(text='B1 (1972-1978)', callback_data='80b1gen')
        eightykeyboard.add(key_80b1)
        key_80b2 = types.InlineKeyboardButton(text='B2 (1978-1986)', callback_data='80b2gen')
        eightykeyboard.add(key_80b2)
        key_80b3 = types.InlineKeyboardButton(text='B3 (1986-1992)', callback_data='80b3gen')
        eightykeyboard.add(key_80b3)
        key_80b4 = types.InlineKeyboardButton(text='B4 (1991-1996)', callback_data='80b4gen')
        eightykeyboard.add(key_80b4)
        bot.send_message(call.message.chat.id, text='Выберите поколение',reply_markup=eightykeyboard)
    if call.data == "80b1gen":
        audieigtybonephoto = open ('D:/TelegramBots/Project photos/Audi 80 B1.jpg', 'rb')
        audibone = types.InlineKeyboardMarkup()
        bone=types.InlineKeyboardButton("Auto.ru", url='https://auto.ru/moskva/cars/audi/80/9346976/all/')
        audibone.add(bone)
        bonetext = 'Дизайн и конструкция\nТип кузова:\n2‑дв. седан\n4‑дв. седан\n5‑дв. универсал\nДвигатель:\n1,3 л. I4 (55-60 л.с.)\n1,5 л. I4 (75-85 л.с.)\n1,6 л. I4 (75-110 л.с.)\nТрансмиссия:\n4-ступ МКПП\n3-ступ АКПП\nМассово-габаритные характеристики:\nДлина	4175 мм\nШирина	1600 мм\nВысота	1362 мм\nКолёсная база	2470 мм\nМасса	835–880 кг'
        bot.send_photo(call.message.chat.id, audieigtybonephoto, caption = 'Audi 80 II (B1)(1972-1978) - седан D-класса, передний привод. Механика и автомат. Бензиновые двигатели мощностью от 55 до 110 лошадиных сил.')
        bot.send_message(call.message.chat.id,text=bonetext, reply_markup=audibone)
    if call.data == "80b2gen":
        audieightybtwophoto = open ('D:/TelegramBots/Project photos/Audi 80 B2.jpg', 'rb')
        audibtwo = types.InlineKeyboardMarkup()
        btwo=types.InlineKeyboardButton("Auto.tu", url='https://auto.ru/moskva/cars/audi/80/7896111/all/')
        audibtwo.add(btwo)
        btwotext = 'Дизайн и конструкция\nТип кузова:\n2‑дв. седан\n4‑дв. седан\n3‑дв. купе (Audi Coupé)\nДвигатель:1,3 л. I4 (55-60 л.с)\n1,6 л. I4 (73-85 л.с)\n1,6 л. I4 турбодизель (54 л.с.)\n1,8 л. I4 (88-90 л.с.)\n1,9 л. I5\n 2,0 л. I5\n2,1 л. I5\n2,2 л. I5\n1,6 л. I4 дизель/турбодизель\nМассово-габаритные характеристики:\nДлина	4383 мм\nШирина	1682 мм\nВысота	1365 мм\nКолёсная база	2540 мм\nМасса	930–1190 кг\nСвязанные модели:\nAudi Coupe GT\nAudi Quattro\nAudi 5+5\nДизайнер:\nДжорджетто Джуджаро'
        bot.send_photo(call.message.chat.id, audieightybtwophoto, caption = 'Audi 80 III (B2)(1978-1986) – седан D-класса, передний и полный привод. Механика и автомат. Бензиновые и дизельные двигатели мощностью от 54 до 136 лошадиных сил.')
        bot.send_message(call.message.chat.id,text=btwotext, reply_markup=audibtwo)
    if call.data == "80b3gen":
        audieightybthreephoto = open ('D:/TelegramBots/Project photos/Audi 80 B3.jpg', 'rb')
        audibthree = types.InlineKeyboardMarkup()
        bthree=types.InlineKeyboardButton("Auto.tu", url='https://auto.ru/moskva/cars/audi/80/7892649/all/')
        audibthree.add(bthree)
        bthreetext = 'Дизайн и конструкция\nТип кузова:\n4‑дв. седан\n3‑дв. купе (Audi Coupé)\nДвигатель:\n80:\n1,4 л. I4\n1,6 л. I4\n1,8 л. I4\n2,0 л. I4\n2,0 л. I4 16 клапанов\n1,6 л. I4 Дизельный\n1,6 л. I4 Турбодизельный\n1,9 л. I4 Дизельный\n90:\n2,0 л. I5\n2,2 л. I5\n2,3 л. I5\n2,3 л. I5 20 клапанов\n1,6 л. I4 Турбодизельный\nТрансмиссия:\n4-ступ МКПП\n5-ступ МКПП\n3-ступ АКПП\nМассово-габаритные характеристики:\nДлина	4392 мм\nШирина	1695 мм\nВысота	1397 мм\nКолёсная база	2540 мм'
        bot.send_photo(call.message.chat.id, audieightybthreephoto, caption = 'Audi 80 IV (B3)(1986-1992) – седан D-класса, передний и полный привод. Автомат и механика. Дизельные и бензиновые двигатели мощностью от 54 до 137 лошадиных сил.')
        bot.send_message(call.message.chat.id,text=bthreetext, reply_markup=audibthree)
    if call.data == "80b4gen":
        audieightybfourphoto = open ('D:/TelegramBots/Project photos/Audi 80 B4.jpg', 'rb')
        audibfour = types.InlineKeyboardMarkup()
        bfour=types.InlineKeyboardButton("Auto.tu", url='https://auto.ru/moskva/cars/audi/80/7878108/all/')
        audibfour.add(bfour)
        bfourtext = 'Дизайн и конструкция\nТип кузова:\n3‑дв. купе\n2‑дв. кабриолет\n4‑дв. седан\n5‑дв. универсал Avant\nДвигатель:\nБензиновые:\n1,6 л. I4\n2,0 л. I4\n2,3 л. I5\n2,6 л. V6\n2,8 л. V6\nДизельные:\n1,9 л. I4\nТрансмиссия:\n5-ступ МКПП\n4-ступ АКПП\nМассово-габаритные характеристики:\nДлина	Седан: 4580 мм\nКупе: 4470 мм\nШирина	Седан: 1694 мм\nКупе: 1717 мм\nВысота	1992-1994 Седан: 1379 мм\n1995-1996 Седан: 1397 мм\nКупе: 1379 мм\nquattro: 1389 мм\nКолёсная база\nСедан: 2611 мм\nКупе: 2555 мм\nquattro: 2596 м\nМасса	1190–1430 кг\nСвязанные модели:\nAudi RS2 Avant'
        bot.send_photo(call.message.chat.id, audieightybfourphoto, caption = 'Audi 80 V (B4)(1991-1996) - седан D-класса, передний и полный привод. Механика и автомат. Бензиновые и дизельные двигатели мощностью от 71 до 174 лошадиных сил.')
        bot.send_message(call.message.chat.id,text=bfourtext, reply_markup=audibfour)
    if call.data == "100gen":
        hundredkeyboard = types.InlineKeyboardMarkup()
        key_100c1 = types.InlineKeyboardButton(text='C1 (1968-1976)', callback_data='100c1gen')
        hundredkeyboard.add(key_100c1)
        key_100c2 = types.InlineKeyboardButton(text='C2 (1976-1983)', callback_data='100c2gen')
        hundredkeyboard.add(key_100c2)
        key_100c3 = types.InlineKeyboardButton(text='C3 (1982-1988)', callback_data='100c3gen')
        hundredkeyboard.add(key_100c3)
        key_100c3plus = types.InlineKeyboardButton(text='C3 рестайлинг (1988-1991)', callback_data='100c3plusgen')
        hundredkeyboard.add(key_100c3plus)
        key_100c4 = types.InlineKeyboardButton(text='C4 (1990-1994)', callback_data='100c4gen')
        hundredkeyboard.add(key_100c4)
        bot.send_message(call.message.chat.id, text='Выберите поколение',reply_markup=hundredkeyboard)
    if call.data == "100c1gen":
        audihundredconephoto = open ('D:/TelegramBots/Project photos/Audi 100 C1.jpg', 'rb')
        audicone = types.InlineKeyboardMarkup()
        cone=types.InlineKeyboardButton("Auto.tu", url='https://auto.ru/moskovskaya_oblast/cars/audi/100/9347459/used/')
        audicone.add(cone)
        conetext = 'Body and chassis\nBody style:\n2/4-door saloon/sedan\n2-door coupé\nLayout:\nFF layout\nPlatform:\nVolkswagen Group C1 platform\nPowertrain:\nEngine:	\n1588 cc OHC I4\n1760 cc OHV I4\n1782 cc OHV I4 (Swiss 100 LS only)\n1871 cc OHV I4\nTransmission:\n4-speed manual all-synchromesh[4]\nautomatic optional[4]\nDimensions:\nWheelbase:\n105.3 in (2,675 mm)[4] (coupé)\nLength:\n182.6 in (4,638 mm) (sedan)[5]\n173.2 in (4,399 mm)[4] (coupé)\nWidth: 68 in (1,727 mm)[4]\nHeight: 55.8 in (1,417 mm)[4]\nCurb weight:\n2,600–2,689 lb (1,179–1,220 kg) (sedan)\n2,401 lb (1,089 kg)[4] (coupé)'
        bot.send_photo(call.message.chat.id, audihundredconephoto, caption = 'Audi 100 I (C1)(1968-1976) – седан E-класса, передний привод. Механика. Бензиновые двигатели мощностью от 80 до 112 лошадиных сил.')
        bot.send_message(call.message.chat.id,text=conetext, reply_markup=audicone)
    if call.data == "100c2gen":
        audihundredctwophoto = open ('D:/TelegramBots/Project photos/Audi 100 C2.jpg', 'rb')
        audictwo = types.InlineKeyboardMarkup()
        ctwo=types.InlineKeyboardButton("Auto.tu", url='https://auto.ru/moskovskaya_oblast/cars/audi/100/9347460/all/')
        audictwo.add(ctwo)
        ctwotext = 'Body and chassis\nBody style:\n2-door saloon/sedan\n4-door saloon/sedan\n5-door hatchback\nLayout:\nFront engine, front-wheel drive\nPlatform:\nVolkswagen Group C2 platform\nPowertrain:\nEngine:	\n1.6 L I4\n1.9 L I5\n2.0 L I4\n2.1 L I5\n2.1 L turbo I5\n2.0 L diesel I5\n2.0 L turbo diesel I5 (US only)\nTransmission:\n3-speed automatic\n5-speed manual\nDimensions:\nWheelbase:\n105.4 in (2,677 mm)[18]\nLength: 184.3 in (4,681 mm)[18]\nWidth: 69.6 in (1,768 mm)[18]\nHeight: 54.8 in (1,392 mm)[18]\nCurb weight: 2,532 lb (1,148 kg)[18]'
        bot.send_photo(call.message.chat.id, audihundredctwophoto, caption = 'Audi 100 II (C2)(1976-1983)– седан E-класса, передний привод. Механика и автомат. Бензиновые и дизельные двигатели мощностью от 70 до 136 лошадиных сил.')
        bot.send_message(call.message.chat.id,text=ctwotext, reply_markup=audictwo)
    if call.data == "100c3gen":
        audihundredcthreephoto = open ('D:/TelegramBots/Project photos/Audi 100 C3.jpg', 'rb')
        audicthree = types.InlineKeyboardMarkup()
        cthree=types.InlineKeyboardButton("Auto.tu", url='https://auto.ru/moskovskaya_oblast/cars/audi/100/7892647/all/')
        audicthree.add(cthree)
        cthreetext = 'Body and chassis\nBody style:\n4-door saloon/sedan\n5-door estate/wagon\nLayout:\nFront engine, front-wheel drive / quattro permanent four-wheel drive[31]\nPlatform:\nVolkswagen Group C3 platform\nPowertrain:\nEngine:	\nPetrol:\n1.8 L I4\n1.9 L I5\n2.0 L I5\n2.1 L I5\n2.2 L I5\n2.3 L I5\nDiesel:\n2.0 L I5\n2.0 L turbo I5\n2.4 L I5\n2.5 L TDI I5\nTransmission:\n4/5-speed manual\n3/4-speed automatic\nDimensions:\nWheelbase:\n105.6 in (2,682 mm\n(1988–1991 FWD & 200)\n105.9 in (2,690 mm)\n(1988–1990 AWD & Wagons)\n105.8 in (2,687 mm) (Pre-1988)\nLength:\n188.7 in (4,793 mm) (global)\n192.7 in (4,895 mm) (USA)\nWidth:\n71.4 in (1,814 mm)\nHeight:\n55.9 in (1,420 mm)\n55.7 in (1,415 mm) (S)\nCurb weight:\n2,259–3,500 lb (1,025–1,588 kg)\nSuccessor:\nAudi V8 (Audi 200)'
        bot.send_photo(call.message.chat.id, audihundredcthreephoto, caption = 'Audi 100 III (C3)(1982-1988)– седан E-класса, передний и полный привод. Механика и автомат. Бензиновые и дизельные двигатели мощностью от 69 до 165 лошадиных сил.')
        bot.send_message(call.message.chat.id,text=cthreetext, reply_markup=audicthree)
    if call.data == "100c3plusgen":
        audihundredcthreeplusphoto = open ('D:/TelegramBots/Project photos/Audi 100 C3plus.jpg', 'rb')
        audicthreeplus = types.InlineKeyboardMarkup()
        cthreeplus=types.InlineKeyboardButton("Auto.tu", url='https://auto.ru/moskovskaya_oblast/cars/audi/100/7893785/all/')
        audicthreeplus.add(cthreeplus)
        cthreeplustext = 'Body and chassis\nBody style:\n4-door saloon/sedan\n5-door estate/wagon\nLayout:\nFront engine, front-wheel drive / quattro permanent four-wheel drive[31]\nPlatform:\nVolkswagen Group C3 platform\nPowertrain:\nEngine:	\nPetrol:\n1.8 L I4\n1.9 L I5\n2.0 L I5\n2.1 L I5\n2.2 L I5\n2.3 L I5\nDiesel:\n2.0 L I5\n2.0 L turbo I5\n2.4 L I5\n2.5 L TDI I5\nTransmission:\n4/5-speed manual\n3/4-speed automatic\nDimensions:\nWheelbase:\n105.6 in (2,682 mm\n(1988–1991 FWD & 200)\n105.9 in (2,690 mm)\n(1988–1990 AWD & Wagons)\n105.8 in (2,687 mm) (Pre-1988)\nLength:\n188.7 in (4,793 mm) (global)\n192.7 in (4,895 mm) (USA)\nWidth:\n71.4 in (1,814 mm)\nHeight:\n55.9 in (1,420 mm)\n55.7 in (1,415 mm) (S)\nCurb weight:\n2,259–3,500 lb (1,025–1,588 kg)\nSuccessor:\nAudi V8 (Audi 200)'
        bot.send_photo(call.message.chat.id, audihundredcthreeplusphoto, caption = 'Audi 100 III (C3) Рестайлинг (1988-1991) – седан E-класса, передний и полный привод. Механика и автомат. Бензиновые и дизельные двигатели мощностью от 82 до 165 лошадиных сил.')
        bot.send_message(call.message.chat.id,text=cthreeplustext, reply_markup=audicthreeplus)
    if call.data == "100c4gen":
        audihundredcfourphoto = open ('D:/TelegramBots/Project photos/Audi 100 C4.jpg', 'rb')
        audicfour = types.InlineKeyboardMarkup()
        cfour=types.InlineKeyboardButton("Auto.tu", url='https://auto.ru/moskovskaya_oblast/cars/audi/100/7879464/all/')
        audicfour.add(cfour)
        cfourtext = 'Body and chassis:\nBody style:\n4-door saloon/sedan\n5-door estate/wagon\nLayout:\nFront engine,front-wheel drive / quattro permanent four-wheel drive\nPlatform:\nVolkswagen Group C4 platform\nPowertrain:\nEngine\nPetrol:\n2.0 L I4\n2.0 L 16V I4\n2.2 L turbo 20V I5 (S4)\n2.3 L I5\n2.6 L V6\n2.8 L V6\n4.2 L V8 (S4)\nDiesel:\n2.4 L I5\n2.5 L TDI I5\nTransmission:\n4-speed automatic\n5-speed manual\n6-speed manual\nDimensions\nWheelbase:\n105.8 in (2,687 mm) (FWD)\n106 in (2,692 mm) (4WD)\nLength: 192.6 in (4,892 mm)\nWidth: 70 in (1,778 mm)\nHeight:\n56.3 in (1,430 mm)\n56.6 in (1,438 mm) (FWD saloon)\n57 in (1,448 mm) (FWD Avant)\nCurb weight:\n2,689–4,189 lb (1,220–1,900 kg)'
        bot.send_photo(call.message.chat.id, audihundredcfourphoto, caption = ' Audi 100 IV (C4)(1990-1994) – седан E-класса, передний и полный привод. Механика и автомат. Бензиновые и дизельные двигатели мощностью от 82 до 290 лошадиных сил.')
        bot.send_message(call.message.chat.id,text=cfourtext, reply_markup=audicfour)
    if call.data == "a1gen":
        aonekeyboard = types.InlineKeyboardMarkup()
        key_a18x = types.InlineKeyboardButton(text='I(8X) (2010-2015)', callback_data='a18xgen')
        aonekeyboard.add(key_a18x)
        key_a18xplus = types.InlineKeyboardButton(text='I(8X)Рестайлинг (2014-2018)', callback_data='a18xplusgen')
        aonekeyboard.add(key_a18xplus)
        key_a1gb = types.InlineKeyboardButton(text='II(GB) (2018-н.в.)', callback_data='a1gbgen')
        aonekeyboard.add(key_a1gb)
        bot.send_message(call.message.chat.id, text='Выберите поколение',reply_markup=aonekeyboard)
    if call.data == "a18xgen":
        audiaoneeightxphoto = open ('D:/TelegramBots/Project photos/Audi A1 8X.jpg', 'rb')
        audieightx = types.InlineKeyboardMarkup()
        eightx=types.InlineKeyboardButton("Auto.tu", url='https://auto.ru/moskva/cars/audi/a1/6248007/all/')
        audieightx.add(eightx)
        eightxtext='Body and chassis:\nBody style:\n3-door hatchback\n5-door hatchback\nLayout:\nFront-engine, front-wheel-drive\nPlatform:\nVolkswagen Group PQ25\nPowertrain\nEngine:\nPetrol:\n1.2 L TFSI I4\n1.4 L TFSI I4\n2.0 L TFSI I4\nDiesel:\n1.6 L TDI I4\n2.0 L TDI I4[13]\nTransmission\n5-speed manual\n6-speed manual\n7-speed S tronic\n1-speed (A1 e-tron)\nDimensions\nWheelbase: 2,469 mm (97.2 in)[14]\nLength: 3,954 mm (155.7 in)[14]\nWidth: 1,740 mm (68.5 in)[14]\nHeight: 1,416 mm (55.7 in)[14]\nKerb weight: 1,040–1,140 kg (2,290–2,510 lb)'
        bot.send_photo(call.message.chat.id, audiaoneeightxphoto, caption = 'Audi A1 I (8X)(2010-2015) – хэтчбек 5 дв. B-класса, передний привод. Механика и робот. Бензиновые и дизельные двигатели мощностью от 86 до 185 лошадиных сил.')
        bot.send_message(call.message.chat.id,text=eightxtext, reply_markup=audieightx)
    if call.data == "a18xplusgen":
        audiaoneeightxplusphoto = open ('D:/TelegramBots/Project photos/Audi A1 8Xplus.jpg', 'rb')
        audieightxplus = types.InlineKeyboardMarkup()
        eightxplus=types.InlineKeyboardButton("Auto.tu", url='https://auto.ru/moskva/cars/audi/a1/20331105/all/')
        audieightxplus.add(eightxplus)
        eightxplustext='Body and chassis:\nBody style:\n3-door hatchback\n5-door hatchback\nLayout:\nFront-engine, front-wheel-drive\nPlatform:\nVolkswagen Group PQ25\nPowertrain\nEngine:\nPetrol:\n1.2 L TFSI I4\n1.4 L TFSI I4\n2.0 L TFSI I4\nDiesel:\n1.6 L TDI I4\n2.0 L TDI I4[13]\nTransmission\n5-speed manual\n6-speed manual\n7-speed S tronic\n1-speed (A1 e-tron)\nDimensions\nWheelbase: 2,469 mm (97.2 in)[14]\nLength: 3,954 mm (155.7 in)[14]\nWidth: 1,740 mm (68.5 in)[14]\nHeight: 1,416 mm (55.7 in)[14]\nKerb weight: 1,040–1,140 kg (2,290–2,510 lb)'
        bot.send_photo(call.message.chat.id, audiaoneeightxplusphoto, caption = 'Audi A1 I (8X)Рестайлинг (2014-2018) – хэтчбек 5 дв. B-класса, передний привод. Механика и робот. Бензиновые и дизельные двигатели мощностью от 86 до 185 лошадиных сил.')
        bot.send_message(call.message.chat.id,text=eightxplustext, reply_markup=audieightxplus)
    if call.data == "a1gbgen":
        audiaonegbphoto = open ('D:/TelegramBots/Project photos/Audi A1 GB.jpg', 'rb')
        audigb = types.InlineKeyboardMarkup()
        gb=types.InlineKeyboardButton("Auto.tu", url='https://auto.ru/moskva/cars/audi/a1/21428669/all/')
        audigb.add(gb)
        gbtext='Body and chassis:\nBody style: 5-door hatchback\nLayout: Front-engine, front-wheel-drive\nPlatform: Volkswagen Group MQB A0[123][122]\nPowertrain\nEngine\nPetrol:\n1.0 L EA211/EA211 DHSB TFSI I3\n1.5 L EA211 EVO series TFSI I4\n2.0 L EA888 TFSI I4\nTransmission:\n5-speed manual\n6-speed manual\n6-speed S tronic\n7-speed S tronic\nDimensions\nWheelbase: 2,563 mm (100.9 in)[124]\nLength: 4,029 mm (158.6 in)[124]\nWidth: 1,740 mm (68.5 in)[125]\nHeight: 1,409 mm (55.5 in)[125]\nKerb weight: 1,165–1,335 kg (2,568–2,943 lb)'
        bot.send_photo(call.message.chat.id, audiaonegbphoto, caption = 'Audi A1 II (GB)(2018 - н.в.)– хэтчбек 5 дв. B-класса, передний привод. Механика и робот. Бензиновые двигатели мощностью от 95 до 207 лошадиных сил.')
        bot.send_message(call.message.chat.id,text=gbtext, reply_markup=audigb)
    if call.data == "a3gen":
        athreekeyboard = types.InlineKeyboardMarkup()
        key_a38l = types.InlineKeyboardButton(text='I(8L) (1996-2000)', callback_data='a38lgen')
        athreekeyboard.add(key_a38l)
        key_a38lplus = types.InlineKeyboardButton(text='I(8L)Рестайлинг (2000-2003)', callback_data='a38lplusgen')
        athreekeyboard.add(key_a38lplus)
        key_a38p = types.InlineKeyboardButton(text='II(8P) (2003-2005)', callback_data='a38pgen')
        athreekeyboard.add(key_a38p)
        key_a38pplus = types.InlineKeyboardButton(text='II(8P)Рестайлинг 1 (2004-2008)', callback_data='a38pplusgen')
        athreekeyboard.add(key_a38pplus)
        key_a38pplustwo = types.InlineKeyboardButton(text='II(8P)Рестайлинг 2 (2008-2013)', callback_data='a38pplustwogen')
        athreekeyboard.add(key_a38pplustwo)
        key_a38v = types.InlineKeyboardButton(text='III(8V) (2012-2016)', callback_data='a38vgen')
        athreekeyboard.add(key_a38v)
        key_a38vplus = types.InlineKeyboardButton(text='III(8V)Рестайлинг (2016-2020)', callback_data='a38vplusgen')
        athreekeyboard.add(key_a38vplus)
        key_a38y = types.InlineKeyboardButton(text='IV(8Y) (2020-н.в.)', callback_data='a38ygen')
        athreekeyboard.add(key_a38y)
        bot.send_message(call.message.chat.id, text='Выберите поколение',reply_markup=athreekeyboard)
    if call.data == "a38lgen":
        audiathreeeightlphoto = open ('D:/TelegramBots/Project photos/Audi A3 8L.jpg', 'rb')
        audieightl = types.InlineKeyboardMarkup()
        eightl=types.InlineKeyboardButton("Auto.tu", url='https://auto.ru/moskva/cars/audi/a3/3473199/all/')
        audieightl.add(eightl)
        eightltext='Body and chassis:\nBody style:\n3-door hatchback\n5-door hatchback\nPlatform: Volkswagen Group A4 (PQ34)\nPowertrain\nEngine\nPetrol engine:\n1.6 L\n1.8 L 20v\n1.8 L 20v Turbo\nDiesel engine:\n1.9 L TDI\nTransmission	\nManual transmission:\n5-speed Manual\n6-speed Manual\nAutomatic transmission:\n4-speed Automatic\n5-speed Automatic\nDimensions\nWheelbase:\nA3 2,513 mm (98.9 in)\nquattro & S3: 2,519 mm (99.2 in)\nLength:\nA3 4,152 mm (163.5 in)\nS3 4,159 mm (163.7 in)\nWidth:\nA3 1,735 mm (68.3 in)\nS3 1,763 mm (69.4 in)\nHeight:\nA3 1,423 mm (56.0 in)\nS3 1,415 mm (55.7 in)'
        bot.send_photo(call.message.chat.id, audiathreeeightlphoto, caption = 'Audi A3 I (8L)(1996-2000) – хэтчбек 5 дв. C-класса, передний и полный привод. Механика и автомат. Бензиновые и дизельные двигатели мощностью от 90 до 180 лошадиных сил.')
        bot.send_message(call.message.chat.id,text=eightltext, reply_markup=audieightl)
    if call.data == "a38lplusgen":
        audiathreeeightlplusphoto = open ('D:/TelegramBots/Project photos/Audi A3 8Lplus.jpg', 'rb')
        audieightlplus = types.InlineKeyboardMarkup()
        eightlplus=types.InlineKeyboardButton("Auto.tu", url='https://auto.ru/moskva/cars/audi/a3/4927403/all/')
        audieightlplus.add(eightlplus)
        eightlplustext='Body and chassis:\nBody style:\n3-door hatchback\n5-door hatchback\nPlatform: Volkswagen Group A4 (PQ34)\nPowertrain\nEngine\nPetrol engine:\n1.6 L\n1.8 L 20v\n1.8 L 20v Turbo\nDiesel engine:\n1.9 L TDI\nTransmission	\nManual transmission:\n5-speed Manual\n6-speed Manual\nAutomatic transmission:\n4-speed Automatic\n5-speed Automatic\nDimensions\nWheelbase:\nA3 2,513 mm (98.9 in)\nquattro & S3: 2,519 mm (99.2 in)\nLength:\nA3 4,152 mm (163.5 in)\nS3 4,159 mm (163.7 in)\nWidth:\nA3 1,735 mm (68.3 in)\nS3 1,763 mm (69.4 in)\nHeight:\nA3 1,423 mm (56.0 in)\nS3 1,415 mm (55.7 in)'
        bot.send_photo(call.message.chat.id, audiathreeeightlplusphoto, caption = 'Audi A3 I (8L) Рестайлинг (2000-2003)– хэтчбек 5 дв. C-класса, передний и полный привод. Автомат и механика. Бензиновые и дизельные двигатели мощностью от 90 до 180 лошадиных сил.')
        bot.send_message(call.message.chat.id,text=eightlplustext, reply_markup=audieightlplus)    
    if call.data == "a38pgen":
        audiathreeeightpphoto = open ('D:/TelegramBots/Project photos/Audi A3 8P.jpg', 'rb')
        audieightp = types.InlineKeyboardMarkup()
        eightp=types.InlineKeyboardButton("Auto.tu", url='https://auto.ru/moskva/cars/audi/a3/4720892/all/')
        audieightp.add(eightp)
        eightptext='Body and chassis:\nBody style:\n3-door hatchback\n5-door Sportback (hatchback)\n2-door convertible\nPlatform: Volkswagen Group A5 (PQ35)\nPowertrain\nEngine	\nInline-four petrol engine:\n1.2 L I4 Turbo FSI (TFSI)\n1.4 L I4 Turbo FSI (TFSI)\n1.6 L I4\n1.6 L I4 FSI\n1.8 L I4 TFSI\n2.0 L I4 FSI\n2.0 L I4 TFSI\nStraight-five petrol engine:\n2.5 L I5 TFSI\nVR6 engine:\n3.2 L VR6 (petrol)\nInline-four diesel engine:\n1.6 L I4 TDI\n1.9 L I4 TDI\n2.0 L I4 TDI\nTransmission	\nManual transmission:\n5-speed manual\n6-speed manual\nAutomatic transmission:\n6-speed automatic\nDual-clutch automatic transmission:\n6-speed S-Tronic\n7-speed S-Tronic\nDimensions\nWheelbase: 2,578 mm (101.5 in)\nLength:\n3-door: 4,215 mm (165.9 in)\n5-door: 4,285 mm (168.7 in)\nWidth:	1,765 mm (69.5 in)\nHeight:	1,420 mm (55.9 in)'
        bot.send_photo(call.message.chat.id, audiathreeeightpphoto, caption = 'Audi A3 II (8P)(2003-2005) – хэтчбек 3 дв./5 дв. C-класса, передний и полный привод. Механика, автомат и робот. Бензиновые и дизельные двигатели мощностью от 102 до 250 лошадиных сил.')
        bot.send_message(call.message.chat.id,text=eightptext, reply_markup=audieightp)
    if call.data == "a38pplusgen":
        audiathreeeightpplusphoto = open ('D:/TelegramBots/Project photos/Audi A3 8Pplus.jpg', 'rb')
        audieightpplus = types.InlineKeyboardMarkup()
        eightpplus=types.InlineKeyboardButton("Auto.tu", url='https://auto.ru/moskva/cars/audi/a3/6295465/all/')
        audieightpplus.add(eightpplus)
        eightpplustext='Body and chassis:\nBody style:\n3-door hatchback\n5-door Sportback (hatchback)\n2-door convertible\nPlatform: Volkswagen Group A5 (PQ35)\nPowertrain\nEngine	\nInline-four petrol engine:\n1.2 L I4 Turbo FSI (TFSI)\n1.4 L I4 Turbo FSI (TFSI)\n1.6 L I4\n1.6 L I4 FSI\n1.8 L I4 TFSI\n2.0 L I4 FSI\n2.0 L I4 TFSI\nStraight-five petrol engine:\n2.5 L I5 TFSI\nVR6 engine:\n3.2 L VR6 (petrol)\nInline-four diesel engine:\n1.6 L I4 TDI\n1.9 L I4 TDI\n2.0 L I4 TDI\nTransmission	\nManual transmission:\n5-speed manual\n6-speed manual\nAutomatic transmission:\n6-speed automatic\nDual-clutch automatic transmission:\n6-speed S-Tronic\n7-speed S-Tronic\nDimensions\nWheelbase: 2,578 mm (101.5 in)\nLength:\n3-door: 4,215 mm (165.9 in)\n5-door: 4,285 mm (168.7 in)\nWidth:	1,765 mm (69.5 in)\nHeight:	1,420 mm (55.9 in)'
        bot.send_photo(call.message.chat.id, audiathreeeightpplusphoto, caption = 'Audi A3 II (8P)Рестайлинг 1 (2004-2008) – хэтчбек 3 дв./5 дв. C-класса, передний и полный привод. Механика, автомат и робот. Бензиновые и дизельные двигатели мощностью от 102 до 250 лошадиных сил.')
        bot.send_message(call.message.chat.id,text=eightpplustext, reply_markup=audieightpplus)
    if call.data == "a38pplustwogen":
        audiathreeeightpplustwophoto = open ('D:/TelegramBots/Project photos/Audi A3 8Pplustwo.jpg', 'rb')
        audieightpplustwo = types.InlineKeyboardMarkup()
        eightpplustwo=types.InlineKeyboardButton("Auto.tu", url='https://auto.ru/moskva/cars/audi/a3/2305282/all/')
        audieightpplustwo.add(eightpplustwo)
        eightpplustwotext='Body and chassis:\nBody style:\n3-door hatchback\n5-door Sportback (hatchback)\n2-door convertible\nPlatform: Volkswagen Group A5 (PQ35)\nPowertrain\nEngine	\nInline-four petrol engine:\n1.2 L I4 Turbo FSI (TFSI)\n1.4 L I4 Turbo FSI (TFSI)\n1.6 L I4\n1.6 L I4 FSI\n1.8 L I4 TFSI\n2.0 L I4 FSI\n2.0 L I4 TFSI\nStraight-five petrol engine:\n2.5 L I5 TFSI\nVR6 engine:\n3.2 L VR6 (petrol)\nInline-four diesel engine:\n1.6 L I4 TDI\n1.9 L I4 TDI\n2.0 L I4 TDI\nTransmission	\nManual transmission:\n5-speed manual\n6-speed manual\nAutomatic transmission:\n6-speed automatic\nDual-clutch automatic transmission:\n6-speed S-Tronic\n7-speed S-Tronic\nDimensions\nWheelbase: 2,578 mm (101.5 in)\nLength:\n3-door: 4,215 mm (165.9 in)\n5-door: 4,285 mm (168.7 in)\nWidth:	1,765 mm (69.5 in)\nHeight:	1,420 mm (55.9 in)'
        bot.send_photo(call.message.chat.id, audiathreeeightpplustwophoto, caption = 'Audi A3 II (8P)Рестайлинг 2 (2008-2013) – хэтчбек 3 дв./5 дв. C-класса, передний и полный привод. Механика, автомат и робот. Бензиновые и дизельные двигатели мощностью от 90 до 250 лошадиных сил.')
        bot.send_message(call.message.chat.id,text=eightpplustwotext, reply_markup=audieightpplustwo)
    if call.data == "a38vgen":
        audiathreeeightvphoto = open ('D:/TelegramBots/Project photos/Audi A3 8V.jpg', 'rb')
        audieightv = types.InlineKeyboardMarkup()
        eightv=types.InlineKeyboardButton("Auto.tu", url='https://auto.ru/moskva/cars/audi/a3/7979586/used/')
        audieightv.add(eightv)
        eightvtext='Body and chassis:\nBody style:\n2-door convertible\n3-door hatchback\n4-door sedan\n5-door hatchback\nPlatform: Volkswagen Group MQB platform\nPowertrain\nEngine	\nInline-three petrol engine:\n1.0 L I3 TFSi\nInline-four petrol engine:\n1.2 L I4 TFSi\n1.4 L I4 TFSi\n1.4 L I4 TFSi ACDT\n1.4 L I4 TFSi ACDT PHEV System\n1.8 L I4 TFSi\n2.0 L I4 TFSi\nInline-four Bi-Fuel (Petrol/CNG) engine:\n1.4 L TGi I4 ACDT (A3 g-tron)\nStraight-five engine:\n2.5 L I5 TFSi\nInline-four diesel engine:\n1.6 L I4 TDi\n2.0 L I4 TDi\nTransmission:	\n6-speed manual\n6-speed (S-Tronic) automatic\n7-speed (S-Tronic) automatic\nDimensions\nWheelbase:	\n2-door convertible: 2,595 mm (102.2 in)[30]\n3-door: 2,601 mm (102.4 in)\n4-door: 2,636 mm (103.8 in)\n5-door: 2,636 mm (103.8 in)[31]\nLength:	\n2-door convertible: 4,423 mm (174.1 in)[30]\n3-door: 4,237 mm (166.8 in)\n4-door: 4,456 mm (175.4 in)\n5-door: 4,310 mm (169.7 in)[31]\nWidth:	\n2-door convertible: 1,793 mm (70.6 in)[30]\n3-door: 1,777 mm (70.0 in)\n4-door: 1,796 mm (70.7 in)\n5-door: 1,785 mm (70.3 in)[31]\nHeight:	\n2-door convertible: 1,409 mm (55.5 in)[30]\n3-door: 1,421 mm (55.9 in)\n4-door: 1,416 mm (55.7 in)\n5-door: 1,421 mm (55.9 in)[31]\nKerb weight:\n1,150–1,520 kg\n(2,535–3,351 lb)'
        bot.send_photo(call.message.chat.id, audiathreeeightvphoto, caption = 'Audi A3 III (8V) (2012-2016) – автомобиль C-класса, передний и полный привод. Механика и робот. Бензиновые и дизельные двигатели мощностью от 105 до 220 лошадиных сил.')
        bot.send_message(call.message.chat.id,text=eightvtext, reply_markup=audieightv)
    if call.data == "a38vplusgen":
        audiathreeeightvplusphoto = open ('D:/TelegramBots/Project photos/Audi A3 8Vplus.jpg', 'rb')
        audieightvplus = types.InlineKeyboardMarkup()
        eightvplus=types.InlineKeyboardButton("Auto.tu", url='https://auto.ru/moskva/cars/audi/a3/20785010/used/')
        audieightvplus.add(eightvplus)
        eightvplustext='Body and chassis:\nBody style:\n2-door convertible\n3-door hatchback\n4-door sedan\n5-door hatchback\nPlatform: Volkswagen Group MQB platform\nPowertrain\nEngine	\nInline-three petrol engine:\n1.0 L I3 TFSi\nInline-four petrol engine:\n1.2 L I4 TFSi\n1.4 L I4 TFSi\n1.4 L I4 TFSi ACDT\n1.4 L I4 TFSi ACDT PHEV System\n1.8 L I4 TFSi\n2.0 L I4 TFSi\nInline-four Bi-Fuel (Petrol/CNG) engine:\n1.4 L TGi I4 ACDT (A3 g-tron)\nStraight-five engine:\n2.5 L I5 TFSi\nInline-four diesel engine:\n1.6 L I4 TDi\n2.0 L I4 TDi\nTransmission:	\n6-speed manual\n6-speed (S-Tronic) automatic\n7-speed (S-Tronic) automatic\nDimensions\nWheelbase:	\n2-door convertible: 2,595 mm (102.2 in)[30]\n3-door: 2,601 mm (102.4 in)\n4-door: 2,636 mm (103.8 in)\n5-door: 2,636 mm (103.8 in)[31]\nLength:	\n2-door convertible: 4,423 mm (174.1 in)[30]\n3-door: 4,237 mm (166.8 in)\n4-door: 4,456 mm (175.4 in)\n5-door: 4,310 mm (169.7 in)[31]\nWidth:	\n2-door convertible: 1,793 mm (70.6 in)[30]\n3-door: 1,777 mm (70.0 in)\n4-door: 1,796 mm (70.7 in)\n5-door: 1,785 mm (70.3 in)[31]\nHeight:	\n2-door convertible: 1,409 mm (55.5 in)[30]\n3-door: 1,421 mm (55.9 in)\n4-door: 1,416 mm (55.7 in)\n5-door: 1,421 mm (55.9 in)[31]\nKerb weight:\n1,150–1,520 kg\n(2,535–3,351 lb)'
        bot.send_photo(call.message.chat.id, audiathreeeightvplusphoto, caption = 'Audi A3 III (8V)Рестайлинг (2016-2020) – автомобиль C-класса, передний и полный привод. Механика и робот. Бензиновые и дизельные двигатели мощностью от 105 до 220 лошадиных сил.')
        bot.send_message(call.message.chat.id,text=eightvplustext, reply_markup=audieightvplus)
    if call.data == "a38ygen":
        audiathreeeightyphoto = open ('D:/TelegramBots/Project photos/Audi A3 8Y.jpg', 'rb')
        audieighty = types.InlineKeyboardMarkup()
        eighty=types.InlineKeyboardButton("Auto.tu", url='https://auto.ru/moskva/cars/audi/a3/21837610/used/')
        audieighty.add(eighty)
        eightytext='Body and chassis:\nBody style:\n5-door hatchback (Sportback)\n4-door sedan\nPlatform: Volkswagen Group MQB Evo\nPowertrain\nEngine:	\nInline-three petrol engine:\n1.0 L EA211 CHYB turbo\nInline-four petrol hybrid engine:\n1.4 L EA211 I4 t/c ACDT PHEV System\n1.5 L EA211 Evo turbo I4 (mild hybrid)\n2.0 L EA888 evo 2 turbo I4 (S3)\nInline-four Bi-Fuel (Petrol/CNG) engine:\n1.5 L EA211 TGI Evo turbo I4 (30 g-tron)\nStraight-five engine:\n2.5 L I5 TFSI\nInline-four diesel engine:\n2.0 L EA288 evo 4 TDI\nElectric motor:	\n48 Volt belt-drive alternator starter (MHEV)\n81 kW (110 PS; 109 hp) – 85 kW (116 PS; 114 hp) Permanent magnet AC synchronous motor\nTransmission;	\n6-speed manual\n7-speed S-tronic\nHybrid drivetrain;	\nMHEV\nPHEV\nBattery: 13 kWh Li-ion\nDimensions\nWheelbase:\n2,640 mm (103.9 in) (sportback)\n2,636 mm (103.8 in) (sedan)\n2,680 mm (105.5 in) (A3L)\nLength:\n4,337 mm (170.7 in) (sportback)\n4,495 mm (177.0 in) (sedan)\n4,548 mm (179.1 in) (A3L)\nWidth: 1,816 mm (71.5 in)\nHeight: 1,425 mm (56.1 in)'
        bot.send_photo(call.message.chat.id, audiathreeeightyphoto, caption = 'Audi A3 IV (8Y)(2020-н.в.) – автомобиль C-класса, передний и полный привод. Автомат, механика и робот. Бензиновые и дизельные двигатели мощностью от 110 до 200 лошадиных сил.')
        bot.send_message(call.message.chat.id,text=eightytext, reply_markup=audieighty)
    if call.data == "a4gen":
        afourkeyboard = types.InlineKeyboardMarkup()
        key_a4b5 = types.InlineKeyboardButton(text='I(B5) (1994-1999)', callback_data='a4b5gen')
        afourkeyboard.add(key_a4b5)
        key_a4b5plus = types.InlineKeyboardButton(text='I(B5)Рестайлинг (1999-2001)', callback_data='a4b5plusgen')
        afourkeyboard.add(key_a4b5plus)
        key_a4b6 = types.InlineKeyboardButton(text='II(B6) (2000-2006)', callback_data='a4b6gen')
        afourkeyboard.add(key_a4b6)
        key_a4b7 = types.InlineKeyboardButton(text='III(B7) (2004-2007)', callback_data='a4b7gen')
        afourkeyboard.add(key_a4b7)
        key_a4b8 = types.InlineKeyboardButton(text='IV(B8) (2007-2012)', callback_data='a4b8gen')
        afourkeyboard.add(key_a4b8)
        key_a4b8plus = types.InlineKeyboardButton(text='IV(B8)Рестайлинг (2011-2015)', callback_data='a4b8plusgen')
        afourkeyboard.add(key_a4b8plus)
        key_a4b9 = types.InlineKeyboardButton(text='V(B9) (2015-2020)', callback_data='a4b9gen')
        afourkeyboard.add(key_a4b9)
        key_a4b9plus = types.InlineKeyboardButton(text='V(B9)Рестайлинг (2015-2020)', callback_data='a4b9plusgen')
        afourkeyboard.add(key_a4b9plus)
        bot.send_message(call.message.chat.id, text='Выберите поколение',reply_markup=afourkeyboard)
    if call.data == "a4b5gen":
        audiafourbfivephoto = open ('D:/TelegramBots/Project photos/Audi A4 B5.jfif', 'rb')
        audibfive = types.InlineKeyboardMarkup()
        bfive=types.InlineKeyboardButton("Auto.tu", url='https://auto.ru/moskva/cars/audi/a4/3473215/all/')
        audibfive.add(bfive)
        bfivetext='Body and chassis\nBody style:\n4 door saloon/sedan,\n5-door Avant (estate/wagon)\nPlatform: Volkswagen Group B5 (PL45) platform\nPowertrain\nEngine:	\nInline-four petrol engine:\n1.6 L I4\n1.8 L I4 20v\n1.8 L I4 20v Turbo\nV6 petrol engine:\n2.4 L V6 12v\n2.4 L V6 30v\n2.6 L V6\n2.7 L V6 Biturbo2.8 L V6 12v2.8 L V6 30vInline-four diesel engine:1.9 L I4 DI1.9 L I4 TDIV6 diesel engine:2.5 L V6 24v TDITransmission:	Manual transmission:5-speed manual6-speed manualAutomatic transmission:4-speed automatic5-speed ZF 5HP19 automaticDimensions:Wheelbase: 2,615 mm (103.0 in)Length :4,520 mm (178.0 in);Avant: 4,488 mm (176.7 in)Width: 1,733 mm (68.2 in)Height: 1,415 mm (55.7 in);Avant: 1,440 mm (56.7 in)'
        bot.send_photo(call.message.chat.id, audiafourbfivephoto, caption = 'Audi A4 I (B5)(1994-1999) – автомобиль D-класса, передний и полный привод. Механика и автомат. Бензиновые и дизельные двигатели мощностью от 75 до 193 лошадиных сил.')
        bot.send_message(call.message.chat.id,text=bfivetext, reply_markup=audibfive)
    if call.data == "a4b5plusgen":
        audiafourbfiveplusphoto = open ('D:/TelegramBots/Project photos/Audi A4 B5plus.jpg', 'rb')
        audibfiveplus = types.InlineKeyboardMarkup()
        bfiveplus = types.InlineKeyboardButton("Auto.tu", url='https://auto.ru/moskva/cars/audi/a4/6297920/all/')
        audibfiveplus.add(bfiveplus)
        bfiveplustext='Body and chassis\nBody style:\n4 door saloon/sedan,\n5-door Avant (estate/wagon)\nPlatform: Volkswagen Group B5 (PL45) platform\nPowertrain\nEngine:	\nInline-four petrol engine:\n1.6 L I4\n1.8 L I4 20v\n1.8 L I4 20v Turbo\nV6 petrol engine:\n2.4 L V6 12v\n2.4 L V6 30v\n2.6 L V6\n2.7 L V6 Biturbo2.8 L V6 12v2.8 L V6 30vInline-four diesel engine:1.9 L I4 DI1.9 L I4 TDIV6 diesel engine:2.5 L V6 24v TDITransmission:	Manual transmission:5-speed manual6-speed manualAutomatic transmission:4-speed automatic5-speed ZF 5HP19 automaticDimensions:Wheelbase: 2,615 mm (103.0 in)Length :4,520 mm (178.0 in);Avant: 4,488 mm (176.7 in)Width: 1,733 mm (68.2 in)Height: 1,415 mm (55.7 in);Avant: 1,440 mm (56.7 in)'
        bot.send_photo(call.message.chat.id, audiafourbfiveplusphoto, caption = 'Audi A4 I Рестайлинг (B5)(1999-2001) – автомобиль D-класса, передний и полный привод. Механика и автомат. Бензиновые и дизельные двигатели мощностью от 75 до 193 лошадиных сил.')
        bot.send_message(call.message.chat.id,text=bfiveplustext, reply_markup=audibfiveplus)
    if call.data == "a4b6gen":
        audiafourbsixphoto = open ('D:/TelegramBots/Project photos/Audi A4 B6.jpg', 'rb')
        audibsix = types.InlineKeyboardMarkup()
        bsix=types.InlineKeyboardButton("Auto.tu", url='https://auto.ru/moskva/cars/audi/a4/3473225/all/')
        audibsix.add(bsix)
        bsixtext='Body and chassis\nBody style:\n4-door saloon/sedan\n5-door Avant (estate/wagon)\n2-door Cabriolet\nPlatform: Volkswagen Group B6 (PL46) platform\nPowertrain\nEngine:	\nInline-four petrol engine:\n1.6L I4\n1.8L I4 20v Turbo\n2.0L I4 20v\n2.0L I4 FSI 16v\nV6 petrol engine:\n2.4L V6 30v\n3.0L V6 30v\nV8 petrol engine:\n4.2L V8 40v\nInline-four diesel engine:\n1.9L I4 TDI\nV6 diesel engine:\n2.5L V6 TDI\nTransmission	\nManual Transmission:\n5-speed Manual\n6-speed Manual\nAutomatic Transmission:\n5-speed Automatic\n6-speed Automatic\nDimensions\nWheelbase:\n2,650 mm (104.3 in),\nCabriolet: 2,654 mm (104.5 in)\nLength:\n4,547 mm (179.0 in),\nAvant: 4,544 mm (178.9 in); Cabriolet: 4,573 mm (180.0 in)\nWidth:\n1,766 mm (69.5 in),\nCabriolet: 1,777 mm (70.0 in)\nHeight:\n1,428 mm (56.2 in),\nCabriolet: 1,391 mm (54.8 in)'
        bot.send_photo(call.message.chat.id, audiafourbsixphoto, caption = 'Audi A4 II (B6)(2000-2006) – автомобиль D-класса, передний и полный привод. Механика, вариатор и автомат. Бензиновые и дизельные двигатели мощностью от 100 до 220 лошадиных сил.')
        bot.send_message(call.message.chat.id,text=bsixtext, reply_markup=audibsix)
    if call.data == "a4b7gen":
        audiafourbsevenphoto = open ('D:/TelegramBots/Project photos/Audi A4 B7.jfif', 'rb')
        audibseven = types.InlineKeyboardMarkup()
        bseven=types.InlineKeyboardButton("Auto.tu", url='https://auto.ru/moskva/cars/audi/a4/2305334/all/')
        audibseven.add(bseven)
        bseventext='Body and chassis\nBody style:\n4-door saloon/sedan,\n5-door Avant (estate/wagon),\n2-door Cabriolet\nPlatform: Volkswagen Group B7 (PL46) platform\nPowertrain\nEngine	\nInline-four petrol engine:\n1.6L I4\n1.8L I4 20v Turbo\n2.0L I4 20v\n2.0L I4 16v TFSI\nV6 petrol engine:\n3.2L V6 24v FSI\nV8 petrol engine:\n4.2L V8 32v FSI\nInline-four diesel engine:\n1.9L I4 TDI\n2.0L I4 TDI\nV6 diesel engine:\n2.5L V6 TDI\n2.7L V6 TDI\n3.0L V6 TDI\nTransmission	\nManual Transmission:\n5-speed Manual\n6-speed Manual\nAutomatic Transmission:\n6-speed ZF 6 hp Tiptronic\nContinuously Variable Transmission:\n7-speed Multitronic\nDimensions:\nWheelbase: 2,648 mm (104.3 in)\nLength:\n4,586 mm (180.6 in),\nCabriolet: 4,573 mm (180.0 in)\nWidth:\n1,772 mm (69.8 in),\nCabriolet: 1,777 mm (70.0 in)\nHeight:\n1,427 mm (56.2 in),\nCabriolet: 1,518 mm (59.8 in)'
        bot.send_photo(call.message.chat.id, audiafourbsevenphoto, caption = 'Audi A4 III (B7)(2004-2009) – автомобиль D-класса, передний и полный привод. Механика, вариатор и автомат. Бензиновые и дизельные двигатели мощностью от 102 до 255 лошадиных сил.')
        bot.send_message(call.message.chat.id,text=bseventext, reply_markup=audibseven)        
    if call.data == "a4b8gen":
        audiafourbeightphoto = open ('D:/TelegramBots/Project photos/Audi A4 B8.jfif', 'rb')
        audibeight = types.InlineKeyboardMarkup()
        beight=types.InlineKeyboardButton("Auto.tu", url='https://auto.ru/moskva/cars/audi/a4/2323576/all/')
        audibeight.add(beight)
        beighttext='Body and chassis\nBody style:\n4-door saloon/sedan,\n5-door Avant (estate/wagon)\nPlatform: Volkswagen Group MLB platform\nPowertrain\nEngine	\nInline-four petrol engine:\n1.8L TFSI I4\n2.0L TFSI I4\nV6 petrol engine:\n3.0L V6 TFSI\n3.2L V6 FSI\nV8 petrol engine:\n4.2L V8 FSI\nInline-four diesel engine:\n2.0L TDI I4\nV6 diesel engine:\n2.7L V6 TDI\n3.0L V6 TDI\nTransmission	\nManual Transmission:\n6-speed Manual\nAutomatic Transmission:\n6-speed Tiptronic\n8-speed automatic\nDual-clutch Transmission:\n7-speed S tronic\nContinuously Variable Transmission:\n8-speed Multitronic\nDimensions\nWheelbase:\n2,808 mm (110.6 in)\nallroad: 2,805 mm (110.4 in)\nLWB: 2,869 mm (113.0 in)\nLength:\n4,703 mm (185.2 in\nallroad: 4,721 mm (185.9 in)\nLWB: 4,763 mm (187.5 in)\nWidth:\n1,826 mm (71.9 in)\nallroad: 1,841 mm (72.5 in)\nHeight:\n1,427 mm (56.2 in)\nAvant: 1,436 mm (56.5 in)\nallroad: 1,495 mm (58.9 in)\nLWB: 1,426 mm (56.1 in)'
        bot.send_photo(call.message.chat.id, audiafourbeightphoto, caption = 'Audi A4 IV (B8)(2007-2012) – автомобиль D-класса, передний и полный привод. Механика, вариатор, робот и автомат. Бензиновые и дизельные двигатели мощностью от 120 до 265 лошадиных сил.')
        bot.send_message(call.message.chat.id,text=beighttext, reply_markup=audibeight)
    if call.data == "a4b8plusgen":
        audiafourbeightplusphoto = open ('D:/TelegramBots/Project photos/Audi A4 B8plus.jfif', 'rb')
        audibeightplus = types.InlineKeyboardMarkup()
        beightplus=types.InlineKeyboardButton("Auto.tu", url='https://auto.ru/moskva/cars/audi/a4/7754683/all/')
        audibeightplus.add(beightplus)
        beightplustext='Body and chassis\nBody style:\n4-door saloon/sedan,\n5-door Avant (estate/wagon)\nPlatform: Volkswagen Group MLB platform\nPowertrain\nEngine	\nInline-four petrol engine:\n1.8L TFSI I4\n2.0L TFSI I4\nV6 petrol engine:\n3.0L V6 TFSI\n3.2L V6 FSI\nV8 petrol engine:\n4.2L V8 FSI\nInline-four diesel engine:\n2.0L TDI I4\nV6 diesel engine:\n2.7L V6 TDI\n3.0L V6 TDI\nTransmission	\nManual Transmission:\n6-speed Manual\nAutomatic Transmission:\n6-speed Tiptronic\n8-speed automatic\nDual-clutch Transmission:\n7-speed S tronic\nContinuously Variable Transmission:\n8-speed Multitronic\nDimensions\nWheelbase:\n2,808 mm (110.6 in)\nallroad: 2,805 mm (110.4 in)\nLWB: 2,869 mm (113.0 in)\nLength:\n4,703 mm (185.2 in\nallroad: 4,721 mm (185.9 in)\nLWB: 4,763 mm (187.5 in)\nWidth:\n1,826 mm (71.9 in)\nallroad: 1,841 mm (72.5 in)\nHeight:\n1,427 mm (56.2 in)\nAvant: 1,436 mm (56.5 in)\nallroad: 1,495 mm (58.9 in)\nLWB: 1,426 mm (56.1 in)'
        bot.send_photo(call.message.chat.id, audiafourbeightplusphoto, caption = 'Audi A4 IV (B8)Рестайлинг (2011-2015) – автомобиль D-класса, передний и полный привод. Механика, вариатор, робот и автомат. Бензиновые и дизельные двигатели мощностью от 120 до 265 лошадиных сил.')
        bot.send_message(call.message.chat.id,text=beightplustext, reply_markup=audibeightplus)        
    if call.data == "a4b9gen":
        audiafourbninephoto = open ('D:/TelegramBots/Project photos/Audi A4 B9.jpg', 'rb')
        audibnine = types.InlineKeyboardMarkup()
        bnine=types.InlineKeyboardButton("Auto.tu", url='https://auto.ru/moskva/cars/audi/a4/20637504/all/')
        audibnine.add(bnine)
        bninetext='Body and chassis\nBody style:\n4-door saloon/sedan,\n5-door Avant (estate/wagon)\nPlatform: Volkswagen Group MLB Evo platform\nPowertrain\nEngine	\nInline-four petrol engine:\n1.4L TFSI I4\n2.0L TFSI I4\nV6 petrol engine:\n3.0L V6 TFSI\n2.9L V6 TFSI\nInline-four diesel engine:\n2.0L TDI I4\nV6 diesel engine:\n3.0L V6 TDI\nTransmission:\n6-speed manual\n7-speed S-tronic\n8-speed Tiptronic ZF 8HP\nDimensions\nWheelbase: 2,820 mm (111.0 in)\nLength: 4,726–4,762 mm (186.1–187.5 in)\nWidth: 1,842–1,847 mm (72.5–72.7 in)\nHeight: 1,427 mm (56.2 in)'
        bot.send_photo(call.message.chat.id, audiafourbninephoto, caption = 'Audi A4 V (B9)(2015-2020) – автомобиль D-класса, передний и полный привод. Робот, механика и автомат. Бензиновые и дизельные двигатели мощностью от 122 до 272 лошадиных сил.')
        bot.send_message(call.message.chat.id,text=bninetext, reply_markup=audibnine)
    if call.data == "a4b9plusgen":
        audiafourbnineplusphoto = open ('D:/TelegramBots/Project photos/Audi A4 B9plus.jpg', 'rb')
        audibnineplus = types.InlineKeyboardMarkup()
        bnineplus=types.InlineKeyboardButton("Auto.tu", url='https://auto.ru/moskva/cars/audi/a4/21460328/all/')
        audibnineplus.add(bnineplus)
        bnineplustext='Body and chassis\nBody style:\n4-door saloon/sedan,\n5-door Avant (estate/wagon)\nPlatform: Volkswagen Group MLB Evo platform\nPowertrain\nEngine	\nInline-four petrol engine:\n1.4L TFSI I4\n2.0L TFSI I4\nV6 petrol engine:\n3.0L V6 TFSI\n2.9L V6 TFSI\nInline-four diesel engine:\n2.0L TDI I4\nV6 diesel engine:\n3.0L V6 TDI\nTransmission:\n6-speed manual\n7-speed S-tronic\n8-speed Tiptronic ZF 8HP\nDimensions\nWheelbase: 2,820 mm (111.0 in)\nLength: 4,726–4,762 mm (186.1–187.5 in)\nWidth: 1,842–1,847 mm (72.5–72.7 in)\nHeight: 1,427 mm (56.2 in)'
        bot.send_photo(call.message.chat.id, audiafourbnineplusphoto, caption = 'Audi A4 V (B9)Рестайлинг (2019-н.в.)– автомобиль D-класса, передний и полный привод. Робот, механика и автомат. Бензиновые и дизельные двигатели мощностью от 122 до 286 лошадиных сил.')
        bot.send_message(call.message.chat.id,text=bnineplustext, reply_markup=audibnineplus)   
    if call.data == "a5gen":
        afivekeyboard = types.InlineKeyboardMarkup()
        key_a58t = types.InlineKeyboardButton(text='I(8T) (2007-2011)', callback_data='a58tgen')
        afivekeyboard.add(key_a58t)
        key_a58tplus = types.InlineKeyboardButton(text='I(8T)Рестайлинг (2011-2016)', callback_data='a58tplusgen')
        afivekeyboard.add(key_a58tplus)
        key_a5f5 = types.InlineKeyboardButton(text='II(F5) (2016-2020)', callback_data='a5f5gen')
        afivekeyboard.add(key_a5f5)
        key_a5f5plus = types.InlineKeyboardButton(text='II(F5)Рестайлинг (2020-н.в.)', callback_data='a5f5plusgen')
        afivekeyboard.add(key_a5f5plus)
        bot.send_message(call.message.chat.id, text='Выберите поколение',reply_markup=afivekeyboard)
    if call.data == "a58tgen":
        audiafiveeighttphoto = open ('D:/TelegramBots/Project photos/Audi A5 8T.jfif', 'rb')
        audieightt = types.InlineKeyboardMarkup()
        eightt=types.InlineKeyboardButton("Auto.tu", url='https://auto.ru/moskva/cars/audi/a5/2305408/all/')
        audieightt.add(eightt)
        eightttext='Body and chassis\nPlatform: Volkswagen Group MLB platform\nPowertrain\nEngine\nPetrol:\n1.8 L TFSI I4\n2.0 L TFSI I4\n3.2 L FSI V6\n3.0 L TFSI V6\n4.2 L FSI V8\nDiesel:\n2.0 L TDI I4\n2.7 L TDI V6\n3.0 L TDI V6\nTransmission\n6-speed manual,\n6-speed Tiptronic automatic\n7-speed S tronic dual-clutch automatic\n8-speed Tiptronic Automatic\nMultitronic CVT\nDimensions\nWheelbase:\nCoupé & Cabriolet: 2,751 mm (108.3 in)\nSportback: 2,811 mm (110.7 in)\nLength:\nCoupé & Cabriolet: 4,626 mm (182.1 in)\nSportback: 4,712 mm (185.5 in)\nWidth: 1,854 mm (73.0 in)\nHeight:\nCoupé: 1,372 mm (54.0 in)\nCabriolet: 1,383 mm (54.4 in)\nSportback: 1,391 mm (54.8 in)\nKerb weight:\nCoupé: 1,500 kg (3,307 lb)\nCabriolet: 1,695 kg (3,737 lb)\nSportback: 1,565 kg (3,450 lb)\nChronology\nPredecessor	\nAudi Coupé (B3) (A5 Coupe)\nAudi A4 Cabriolet (8H) (A5 Cabriolet)'
        bot.send_photo(call.message.chat.id, audiafiveeighttphoto, caption = 'Audi A5 I (8T)(2007-2011) – автомобиль D-класса, передний и полный привод. Механика, вариатор, робот и автомат. Бензиновые и дизельные двигатели мощностью от 160 до 265 лошадиных сил.')
        bot.send_message(call.message.chat.id,text=eightttext, reply_markup=audieightt)
    if call.data == "a58tplusgen":
        audiafiveeighttplusphoto = open ('D:/TelegramBots/Project photos/Audi A5 8Tplus.jfif', 'rb')
        audieighttplus = types.InlineKeyboardMarkup()
        eighttplus=types.InlineKeyboardButton("Auto.tu", url='https://auto.ru/moskva/cars/audi/a5/7721546/all/')
        audieighttplus.add(eighttplus)
        eighttplustext='Body and chassis\nPlatform: Volkswagen Group MLB platform\nPowertrain\nEngine\nPetrol:\n1.8 L TFSI I4\n2.0 L TFSI I4\n3.2 L FSI V6\n3.0 L TFSI V6\n4.2 L FSI V8\nDiesel:\n2.0 L TDI I4\n2.7 L TDI V6\n3.0 L TDI V6\nTransmission\n6-speed manual,\n6-speed Tiptronic automatic\n7-speed S tronic dual-clutch automatic\n8-speed Tiptronic Automatic\nMultitronic CVT\nDimensions\nWheelbase:\nCoupé & Cabriolet: 2,751 mm (108.3 in)\nSportback: 2,811 mm (110.7 in)\nLength:\nCoupé & Cabriolet: 4,626 mm (182.1 in)\nSportback: 4,712 mm (185.5 in)\nWidth: 1,854 mm (73.0 in)\nHeight:\nCoupé: 1,372 mm (54.0 in)\nCabriolet: 1,383 mm (54.4 in)\nSportback: 1,391 mm (54.8 in)\nKerb weight:\nCoupé: 1,500 kg (3,307 lb)\nCabriolet: 1,695 kg (3,737 lb)\nSportback: 1,565 kg (3,450 lb)\nChronology\nPredecessor	\nAudi Coupé (B3) (A5 Coupe)\nAudi A4 Cabriolet (8H) (A5 Cabriolet)'
        bot.send_photo(call.message.chat.id, audiafiveeighttplusphoto, caption = 'Audi A5 I (8T)Рестайлинг(2011-2016) – автомобиль D-класса, передний и полный привод. Механика, вариатор, робот и автомат. Бензиновые и дизельные двигатели мощностью от 163 до 272 лошадиных сил.')
        bot.send_message(call.message.chat.id,text=eighttplustext, reply_markup=audieighttplus)
    if call.data == "a5f5gen":
        audiafiveffivephoto = open ('D:/TelegramBots/Project photos/Audi A5 F5.jfif', 'rb')
        audiffive = types.InlineKeyboardMarkup()
        ffive=types.InlineKeyboardButton("Auto.tu", url='https://auto.ru/moskva/cars/audi/a5/20795592/all/')
        audiffive.add(ffive)
        ffivetext='Body and chassis\nPlatform: Volkswagen Group MLBevo platform\nPowertrain\nEngine\nPetrol:\n1.4 L EA211 TFSI I4 16V 152 (35 TFSI)\n2.0 L EA888 TFSI I4 + Mild Hybrid 48V 190 (40 TFSI / 40 TFSI S-Line)\n2.0L TFSI + CNG I4 170 (g-Tron)\n2.0 L EA888 CDLA TFSI I4 + Mild Hybrid 48V 252 (45 TFSI/45 TFSI Quattro)\n2.9 L BiTurbo TFSI V6 450 (RS5)\n3.0 L TFSI V6 355 (S5)\nDiesel:\n2.0 L TDI I4 190\n3.0 L V6 TDI 220\n3.0 L V6 TDI 290\nTransmission\n6-speed manual\n7-speed S-Tronic dual-clutch automatic\n8-speed tiptronic automatic (A5 3.0 TDI & S5 & RS5)\nDimensions\nWheelbase\nA5 Coupé & Cabriolet: 2,764 mm (108.8 in)\nS5 Coupé: 2,765 mm (108.9 in)\nA5 Sportback: 2,824 mm (111.2 in)\nS5 Sportback: 2,825 mm (111.2 in)\nLength\nA5 Coupé & Cabriolet: 4,673–4,697 mm (184.0–184.9 in)\nS5 Coupé: 4,673–4,697 mm (184.0–184.9 in)\nA5 Sportback: 4,733 mm (186.3 in)\nS5 Sportback: 4,752 mm (187.1 in)\nWidth\nA5 & S5 Coupé: 1,846 mm (72.7 in)\nA5 & S5 Sportback: 1,843 mm (72.6 in)\nHeight\nA5 Coupé: 1,371 mm (54.0 in)\nS5 Coupé: 1,368 mm (53.9 in)\nA5 Sportback: 1,386 mm (54.6 in)\nS5 Sportback: 1,384 mm (54.5 in)'
        bot.send_photo(call.message.chat.id, audiafiveffivephoto, caption = 'Audi A5 II (F5)(2016-2020) – автомобиль D-класса, полный и передний привод. Робот, механика и автомат. Дизельные и бензиновые двигатели мощностью от 150 до 272 лошадиных сил.')
        bot.send_message(call.message.chat.id,text=ffivetext, reply_markup=audiffive)
    if call.data == "a5f5plusgen":
        audiafiveffiveplusphoto = open ('D:/TelegramBots/Project photos/Audi A5 F5plus.jfif', 'rb')
        audiffiveplus = types.InlineKeyboardMarkup()
        ffiveplus  =types.InlineKeyboardButton("Auto.tu", url='https://auto.ru/moskva/cars/audi/a5/21745628/all/')
        audiffiveplus.add(ffiveplus)
        ffiveplustext='Body and chassis\nPlatform: Volkswagen Group MLBevo platform\nPowertrain\nEngine\nPetrol:\n1.4 L EA211 TFSI I4 16V 152 (35 TFSI)\n2.0 L EA888 TFSI I4 + Mild Hybrid 48V 190 (40 TFSI / 40 TFSI S-Line)\n2.0L TFSI + CNG I4 170 (g-Tron)\n2.0 L EA888 CDLA TFSI I4 + Mild Hybrid 48V 252 (45 TFSI/45 TFSI Quattro)\n2.9 L BiTurbo TFSI V6 450 (RS5)\n3.0 L TFSI V6 355 (S5)\nDiesel:\n2.0 L TDI I4 190\n3.0 L V6 TDI 220\n3.0 L V6 TDI 290\nTransmission\n6-speed manual\n7-speed S-Tronic dual-clutch automatic\n8-speed tiptronic automatic (A5 3.0 TDI & S5 & RS5)\nDimensions\nWheelbase\nA5 Coupé & Cabriolet: 2,764 mm (108.8 in)\nS5 Coupé: 2,765 mm (108.9 in)\nA5 Sportback: 2,824 mm (111.2 in)\nS5 Sportback: 2,825 mm (111.2 in)\nLength\nA5 Coupé & Cabriolet: 4,673–4,697 mm (184.0–184.9 in)\nS5 Coupé: 4,673–4,697 mm (184.0–184.9 in)\nA5 Sportback: 4,733 mm (186.3 in)\nS5 Sportback: 4,752 mm (187.1 in)\nWidth\nA5 & S5 Coupé: 1,846 mm (72.7 in)\nA5 & S5 Sportback: 1,843 mm (72.6 in)\nHeight\nA5 Coupé: 1,371 mm (54.0 in)\nS5 Coupé: 1,368 mm (53.9 in)\nA5 Sportback: 1,386 mm (54.6 in)\nS5 Sportback: 1,384 mm (54.5 in)'
        bot.send_photo(call.message.chat.id, audiafiveffiveplusphoto, caption = 'Audi A5 II (F5)Рестайлинг (2020-н.в.) – автомобиль D-класса, полный и передний привод. Робот, механика и автомат. Дизельные и бензиновые двигатели мощностью от 150 до 286 лошадиных сил.')
        bot.send_message(call.message.chat.id,text=ffiveplustext, reply_markup=audiffiveplus)
    if call.data == "q2gen":
        qtwokeyboard = types.InlineKeyboardMarkup()
        key_q2q2 = types.InlineKeyboardButton(text='I (2016-2020)', callback_data='q2q2gen')
        qtwokeyboard.add(key_q2q2)
        key_q2q2plus = types.InlineKeyboardButton(text='I Рестайлинг (2020-н.в.)', callback_data='q2q2plusgen')
        qtwokeyboard.add(key_q2q2plus)
        bot.send_message(call.message.chat.id, text='Выберите поколение',reply_markup=qtwokeyboard)
    if call.data == "q2q2gen":
        audiqtwoqtwophoto = open ('D:/TelegramBots/Project photos/Audi Q2.jfif', 'rb')
        audiqtwo = types.InlineKeyboardMarkup()
        qtwo=types.InlineKeyboardButton("Auto.tu", url='https://auto.ru/moskovskaya_oblast/cars/audi/q2/20765802/all/')
        audiqtwo.add(qtwo)
        qtwotext='Body and chassis\nClass: Subcompact luxury crossover SUV\nBody style: 5-door SUV\nLayout:\nFront-engine, front-wheel-drive or all-wheel-drive\nFront-motor, front-wheel-drive (Q2L 30 e-tron)\nPlatform: Volkswagen Group MQB A1\nPowertrain\nEngine	\nPetrol:\n1.0 TFSI I3 turbo\n1.4 TFSI COD I4 turbo\n2.0 TFSI I4 turbo\nDiesel:\n1.6 TDI I4 turbo\n2.0 TDI I4 turbo\nElectric motor:\n100 kW (140 PS; 130 hp) AC asynchronous motor (Q2L e-Tron)\nTransmission	\n6-speed manual\n7-speed S tronic automatic\n8-speed Tiptronic automatic\nSingle-speed Fixed gear (Q2L e-Tron)\nBattery: 38 kWh Li-ion (Q2L e-Tron)\nDimensions\nWheelbase:\n2,601 mm (102.4 in)\n2,628 mm (103.5 in) (Q2L)\nLength:\n4,191 mm (165.0 in)\n4,229 mm (166.5 in) (Q2L)\nWidth: 1,794 mm (70.6 in)\nHeight: 1,508 mm (59.4 in)\nCurb weight: 1,205 kg (2,657 lb)'
        bot.send_photo(call.message.chat.id, audiqtwoqtwophoto, caption = 'Audi Q2 I (2016-2020)– внедорожник 5 дв. J-класса, передний и полный привод. Механика и робот. Бензиновые и дизельные двигатели мощностью от 116 до 190 лошадиных сил.')
        bot.send_message(call.message.chat.id,text=qtwotext, reply_markup=audiqtwo)
    if call.data == "q2q2plusgen":
        audiqtwoqtwoplusphoto = open ('D:/TelegramBots/Project photos/Audi Q2plus.jfif', 'rb')
        audiqtwoplus = types.InlineKeyboardMarkup()
        qtwoplus=types.InlineKeyboardButton("Auto.tu", url='https://auto.ru/moskovskaya_oblast/cars/audi/q2/22523394/all/')
        audiqtwoplus.add(qtwoplus)
        qtwoplustext='Body and chassis\nClass: Subcompact luxury crossover SUV\nBody style: 5-door SUV\nLayout:\nFront-engine, front-wheel-drive or all-wheel-drive\nFront-motor, front-wheel-drive (Q2L 30 e-tron)\nPlatform: Volkswagen Group MQB A1\nPowertrain\nEngine	\nPetrol:\n1.0 TFSI I3 turbo\n1.4 TFSI COD I4 turbo\n2.0 TFSI I4 turbo\nDiesel:\n1.6 TDI I4 turbo\n2.0 TDI I4 turbo\nElectric motor:\n100 kW (140 PS; 130 hp) AC asynchronous motor (Q2L e-Tron)\nTransmission	\n6-speed manual\n7-speed S tronic automatic\n8-speed Tiptronic automatic\nSingle-speed Fixed gear (Q2L e-Tron)\nBattery: 38 kWh Li-ion (Q2L e-Tron)\nDimensions\nWheelbase:\n2,601 mm (102.4 in)\n2,628 mm (103.5 in) (Q2L)\nLength:\n4,191 mm (165.0 in)\n4,229 mm (166.5 in) (Q2L)\nWidth: 1,794 mm (70.6 in)\nHeight: 1,508 mm (59.4 in)\nCurb weight: 1,205 kg (2,657 lb)'
        bot.send_photo(call.message.chat.id, audiqtwoqtwoplusphoto, caption = 'Audi Q2 I Рестайлинг (2020-н.в.)– внедорожник 5 дв. J-класса, передний и полный привод. Механика и робот. Бензиновые и дизельные двигатели мощностью от 110 до 190 лошадиных сил.')
        bot.send_message(call.message.chat.id,text=qtwoplustext, reply_markup=audiqtwoplus)
    if call.data == "q3gen":
        qthreekeyboard = types.InlineKeyboardMarkup()
        key_q38u = types.InlineKeyboardButton(text='I (8U)(2011-2014)', callback_data='q38ugen')
        qthreekeyboard.add(key_q38u)
        key_q38uplus = types.InlineKeyboardButton(text='I Рестайлинг (8U)(2014-2018)', callback_data='q38uplusgen')
        qthreekeyboard.add(key_q38uplus)
        key_q3f3 = types.InlineKeyboardButton(text='II (F3)(2018-н.в.)', callback_data='q3f3gen')
        qthreekeyboard.add(key_q3f3)
        bot.send_message(call.message.chat.id, text='Выберите поколение',reply_markup=qthreekeyboard)
    if call.data == "q38ugen":
        audiqthreeeightuphoto = open ('D:/TelegramBots/Project photos/Audi Q3 8U.jfif', 'rb')
        audieightu = types.InlineKeyboardMarkup()
        eightu=types.InlineKeyboardButton("Auto.tu", url='https://auto.ru/moskovskaya_oblast/cars/audi/q3/7341708/all/')
        audieightu.add(eightu)
        eightutext='Body and chassis\nBody style: 5-door SUV[3]\nLayout: Front-engine, front-wheel drive / all-wheel drive\nPlatform: Volkswagen Group A5 (PQ35)\nPowertrain\nEngine:\n1.4L Volkswagen EA211 TFSI I4\n2.0L Volkswagen EA888 TFSI I4\n2.0L Volkswagen EA189 CFGC TDI diesel I4\n2.5L Volkswagen EA855 TFSI I5\nTransmission:\n6-speed manual\n6-speed automatic (North America)\n6-speed S-Tronic (1.4 TFSI)\n7-speed S-Tronic\nDimensions\nWheelbase: 2,603 mm (102.5 in)\nLength: 4,385 mm (172.6 in)\nWidth: 1,831 mm (72.1 in)\nHeight: 1,608 mm (63.3 in)'
        bot.send_photo(call.message.chat.id, audiqthreeeightuphoto, caption = 'Audi Q3 I (8U)(2011-2014) – внедорожник 5 дв. J-класса, передний и полный привод. Механика и робот. Бензиновые и дизельные двигатели мощностью от 140 до 211 лошадиных сил.')
        bot.send_message(call.message.chat.id,text=eightutext, reply_markup=audieightu)
    if call.data == "q38uplusgen":
        audiqthreeeightuplusphoto = open ('D:/TelegramBots/Project photos/Audi Q3 8Uplus.jfif', 'rb')
        audieightuplus= types.InlineKeyboardMarkup()
        eightuplus=types.InlineKeyboardButton("Auto.tu", url='https://auto.ru/moskovskaya_oblast/cars/audi/q3/20293979/all/')
        audieightuplus.add(eightuplus)
        eightuplustext='Body and chassis\nBody style: 5-door SUV[3]\nLayout: Front-engine, front-wheel drive / all-wheel drive\nPlatform: Volkswagen Group A5 (PQ35)\nPowertrain\nEngine:\n1.4L Volkswagen EA211 TFSI I4\n2.0L Volkswagen EA888 TFSI I4\n2.0L Volkswagen EA189 CFGC TDI diesel I4\n2.5L Volkswagen EA855 TFSI I5\nTransmission:\n6-speed manual\n6-speed automatic (North America)\n6-speed S-Tronic (1.4 TFSI)\n7-speed S-Tronic\nDimensions\nWheelbase: 2,603 mm (102.5 in)\nLength: 4,385 mm (172.6 in)\nWidth: 1,831 mm (72.1 in)\nHeight: 1,608 mm (63.3 in)'
        bot.send_photo(call.message.chat.id, audiqthreeeightuplusphoto, caption = 'Audi Q3 I Рестайлинг (8U)(2014-2018) – внедорожник 5 дв. J-класса, передний и полный привод. Механика и робот. Бензиновые и дизельные двигатели мощностью от 120 до 220 лошадиных сил.')
        bot.send_message(call.message.chat.id,text=eightuplustext, reply_markup=audieightuplus)
    if call.data == "q3f3gen":
        audiqthreefthreephoto = open ('D:/TelegramBots/Project photos/Audi Q3 F3.jfif', 'rb')
        audifthree = types.InlineKeyboardMarkup()
        fthree=types.InlineKeyboardButton("Auto.tu", url='https://auto.ru/moskovskaya_oblast/cars/audi/q3/21356775/all/')
        audifthree.add(fthree)
        fthreetext='Body and chassis\nBody style:\n5-door SUV\n5-door coupé SUV (Sportback)\nPlatform: Volkswagen Group MQB A2\nPowertrain\nEngine	\nPetrol:\n1.4 L EA211 (BWK/CAVA) TFSI I4\n1.4 L EA211 (CZDA) TFSI I4\n1.5 L EA211 EVO (DADA) TFSI I4\n2.0 L EA888 TFSI I4\n2.5 L DNWA TFSI I5 (RS Q3)\nDiesel:\n2.0 L CRBC TDI I4\nTransmission	\n6-speed Manual\n6-speed dual clutch S-tronic\n7-speed dual clutch S-tronic\nDimensions\nWheelbase: 2,680 mm (105.5 in)\nLength: 4,485 mm (176.6 in)\nWidth: 1,856 mm (73.1 in)\nHeight:\n1,585 mm (62.4 in)\n1,557 mm (61.3 in) (Sportback)'
        bot.send_photo(call.message.chat.id, audiqthreefthreephoto, caption = 'Audi Q3 II (F3)(2018-н.в.)– внедорожник 5 дв. J-класса, полный и передний привод. Робот, механика и автомат. Дизельные, бензиновые и гибридные двигатели мощностью от 150 до 245 лошадиных сил.')
        bot.send_message(call.message.chat.id,text=fthreetext, reply_markup=audifthree)
    if call.data == "q5gen":
        qfivekeyboard = types.InlineKeyboardMarkup()
        key_q58r = types.InlineKeyboardButton(text='I (8R)(2008-2012)', callback_data='q58rgen')
        qfivekeyboard.add(key_q58r)
        key_q58rplus = types.InlineKeyboardButton(text='I Рестайлинг(8R)(2012-2017)', callback_data='q58rplusgen')
        qfivekeyboard.add(key_q58rplus)
        key_q5fy = types.InlineKeyboardButton(text='II (FY)(2017-2020)', callback_data='q5fygen')
        qfivekeyboard.add(key_q5fy)
        key_q5fyplus = types.InlineKeyboardButton(text='II Рестайлинг(FY)(2017-2020)', callback_data='q5fyplusgen')
        qfivekeyboard.add(key_q5fyplus)
        bot.send_message(call.message.chat.id, text='Выберите поколение',reply_markup=qfivekeyboard)
    if call.data == "q58rgen":
        audiqfiveeightrphoto = open ('D:/TelegramBots/Project photos/Audi Q5 8R.jfif', 'rb')
        audieightr = types.InlineKeyboardMarkup()
        eightr=types.InlineKeyboardButton("Auto.tu", url='https://auto.ru/moskovskaya_oblast/cars/audi/q5/3784280/all/')
        audieightr.add(eightr)
        eightrtext='Body and chassis\nBody style: 5-door SUV\nLayout: Front-engine, four-wheel-drive (quattro)\nPlatform: MLB\nPowertrain\nEngine:\n2.0 L TFSI I4\n2.0 L TDI diesel I4\n3.0 L TDI diesel V6\n3.2 L V6 FSI\nTransmission:\n6-speed Manual\n6-speed Tiptronic\n8-speed Tiptronic ZF 8HP\n7-speed S Tronic\nDimensions\nWheelbase: 2,807 mm (110.5 in)\nLength: 4,639 mm (182.6 in)\nWidth: 1,880 mm (74.0 in)\nHeight: 1,650 mm (65.0 in)\nKerb weight: 1,850 kg (4,080 lb)'
        bot.send_photo(call.message.chat.id, audiqfiveeightrphoto, caption = 'Audi Q5 I (8R)(2008-2012) – внедорожник 5 дв. J-класса, полный и передний привод. Механика, робот и автомат. Бензиновые, дизельные и гибридные двигатели мощностью от 143 до 271 лошадиных сил.')
        bot.send_message(call.message.chat.id,text=eightrtext, reply_markup=audieightr)
    if call.data == "q58rplusgen":
        audiqfiveeightrplusphoto = open ('D:/TelegramBots/Project photos/Audi Q5 8Rplus.jfif', 'rb')
        audieightrplus = types.InlineKeyboardMarkup()
        eightrplus=types.InlineKeyboardButton("Auto.tu", url='https://auto.ru/moskovskaya_oblast/cars/audi/q5/8351293/all/')
        audieightrplus.add(eightrplus)
        eightrplustext='Body and chassis\nBody style: 5-door SUV\nLayout: Front-engine, four-wheel-drive (quattro)\nPlatform: MLB\nPowertrain\nEngine:\n2.0 L TFSI I4\n2.0 L TDI diesel I4\n3.0 L TDI diesel V6\n3.2 L V6 FSI\nTransmission:\n6-speed Manual\n6-speed Tiptronic\n8-speed Tiptronic ZF 8HP\n7-speed S Tronic\nDimensions\nWheelbase: 2,807 mm (110.5 in)\nLength: 4,639 mm (182.6 in)\nWidth: 1,880 mm (74.0 in)\nHeight: 1,650 mm (65.0 in)\nKerb weight: 1,850 kg (4,080 lb)'
        bot.send_photo(call.message.chat.id, audiqfiveeightrplusphoto, caption = 'Audi Q5 I Рестайлинг (8R)(2012-2017) – внедорожник 5 дв. J-класса, полный и передний привод. Механика, робот и автомат. Бензиновые, дизельные и гибридные двигатели мощностью от 150 до 272 лошадиных сил.')
        bot.send_message(call.message.chat.id,text=eightrplustext, reply_markup=audieightrplus)
    if call.data == "q5fygen":
        audiqfivefyphoto = open ('D:/TelegramBots/Project photos/Audi Q5 FY.jfif', 'rb')
        audify = types.InlineKeyboardMarkup()
        fy=types.InlineKeyboardButton("Auto.tu", url='https://auto.ru/moskovskaya_oblast/cars/audi/q5/20849216/all/')
        audify.add(fy)
        fytext='Body and chassis\nBody style:\n5-door SUV\n5-door coupé SUV (Sportback)\nLayout: Front-engine, four-wheel-drive (quattro)\nPlatform: MLB evo\nPowertrain\nEngine:\n2.0L TFSI I4 (252hp & 273lb-ft) (gasoline)\n2.0L TFSI I4 (249hp & 273lb-ft) (MHEV, gasoline) (Q5 45 TFSI quattro)\n2.0L TFSI I4 (CDL) (367hp & 369lb.-ft.) (PHEV, gasoline) (Q5 55 TFSIe)\n2.0L TDI I4 (163hp–190hp & 295lb-ft) (diesel)\n2.0L TDI I4 (EA189) (204PS & 400Nm.) (MHEV, diesel) (Q5 40 TDI Quattro)\n3.0L TDI V6 (231hp & 368lb-ft) (diesel) (45 TDI)\n3.0L TDI V6 (282hp & 457lb-ft) (diesel) (50 TDI)\n3.0L TDI V6 (341 hp & 516lb-ft) (diesel) (SQ5, Europe)\n3.0L TFSI V6 (349 hp & 369 lb-ft) (gasoline) (SQ5, outside Europe)\nElectric motor:\n48-volt main electrical system (MHEV)\nPermanent-magnet electric motor (PHEV)\nTransmission:\n7-speed DSG (4-cylinder variants)\n8-speed ZF 8HP automatic (SQ5 & 3.0 TDI models)\nHybrid drivetrain:\nMild Hybrid 48V (Q5 45 TFSI quattro / 40 TDI Quattro)\nPHEV (Q5 55 TFSIe)\nBattery: lithium-ion\nDimensions\nWheelbase:\n2,819 mm (111.0 in)\n2,907 mm (114.4 in) (Q5L)\nLength:\n4,682 mm (184.3 in)\n4,751 mm (187.0 in) (Q5L)\nWidth: 1,893 mm (74.5 in)\nHeight: 1,662 mm (65.4 in)'
        bot.send_photo(call.message.chat.id, audiqfivefyphoto, caption = 'Audi Q5 II (FY)(2017-2020) – внедорожник 5 дв. J-класса, полный и передний привод. Робот, автомат и механика. Бензиновые, дизельные и гибридные двигатели мощностью от 136 до 367 лошадиных сил.')
        bot.send_message(call.message.chat.id,text=fytext, reply_markup=audify)
    if call.data == "q5fyplusgen":
        audiqfivefyplusphoto = open ('D:/TelegramBots/Project photos/Audi Q5 FYplus.jfif', 'rb')
        audifyplus = types.InlineKeyboardMarkup()
        fyplus=types.InlineKeyboardButton("Auto.tu", url='https://auto.ru/moskovskaya_oblast/cars/audi/q5/22408434/all/')
        audifyplus.add(fyplus)
        fyplustext='Body and chassis\nBody style:\n5-door SUV\n5-door coupé SUV (Sportback)\nLayout: Front-engine, four-wheel-drive (quattro)\nPlatform: MLB evo\nPowertrain\nEngine:\n2.0L TFSI I4 (252hp & 273lb-ft) (gasoline)\n2.0L TFSI I4 (249hp & 273lb-ft) (MHEV, gasoline) (Q5 45 TFSI quattro)\n2.0L TFSI I4 (CDL) (367hp & 369lb.-ft.) (PHEV, gasoline) (Q5 55 TFSIe)\n2.0L TDI I4 (163hp–190hp & 295lb-ft) (diesel)\n2.0L TDI I4 (EA189) (204PS & 400Nm.) (MHEV, diesel) (Q5 40 TDI Quattro)\n3.0L TDI V6 (231hp & 368lb-ft) (diesel) (45 TDI)\n3.0L TDI V6 (282hp & 457lb-ft) (diesel) (50 TDI)\n3.0L TDI V6 (341 hp & 516lb-ft) (diesel) (SQ5, Europe)\n3.0L TFSI V6 (349 hp & 369 lb-ft) (gasoline) (SQ5, outside Europe)\nElectric motor:\n48-volt main electrical system (MHEV)\nPermanent-magnet electric motor (PHEV)\nTransmission:\n7-speed DSG (4-cylinder variants)\n8-speed ZF 8HP automatic (SQ5 & 3.0 TDI models)\nHybrid drivetrain:\nMild Hybrid 48V (Q5 45 TFSI quattro / 40 TDI Quattro)\nPHEV (Q5 55 TFSIe)\nBattery: lithium-ion\nDimensions\nWheelbase:\n2,819 mm (111.0 in)\n2,907 mm (114.4 in) (Q5L)\nLength:\n4,682 mm (184.3 in)\n4,751 mm (187.0 in) (Q5L)\nWidth: 1,893 mm (74.5 in)\nHeight: 1,662 mm (65.4 in)'
        bot.send_photo(call.message.chat.id, audiqfivefyplusphoto, caption = 'Audi Q5 II Рестайлинг (FY)(2020-н.в.) – внедорожник 5 дв. J-класса, полный и передний привод. Робот, автомат и механика. Бензиновые, дизельные и гибридные двигатели мощностью от 163 до 367 лошадиных сил.')
        bot.send_message(call.message.chat.id,text=fyplustext, reply_markup=audifyplus)
    if call.data == "q8gen":
        qeightkeyboard = types.InlineKeyboardMarkup()
        key_q8q8 = types.InlineKeyboardButton(text='I (2018-н.в.)', callback_data='q8qeightgen')
        qeightkeyboard.add(key_q8q8)
        bot.send_message(call.message.chat.id, text='Выберите поколение',reply_markup=qeightkeyboard)
    if call.data == "q8qeightgen":
        audiqeightqeightphoto = open ('D:/TelegramBots/Project photos/Audi Q8.jfif', 'rb')
        audiqeight = types.InlineKeyboardMarkup()
        qeight=types.InlineKeyboardButton("Auto.tu", url='https://auto.ru/moskovskaya_oblast/cars/audi/q8/21315288/all/')
        audiqeight.add(qeight)
        qeighttext='Body and chassis\nClass: Mid-size luxury crossover SUV\nBody style: 5-door SUV\nLayout: Front-engine, four-wheel-drive[1]\nPlatform: Volkswagen Group MLB Evo\nPowertrain\nEngine	\nPetrol:\n3.0 L TFSI V6\n4.0 L TFSI twin-turbo V8\nPetrol plug-in hybrid:\n3.0 L TFSI V6 PHEV\nDiesel:\n3.0 L TDI V6[1]\n4.0 L TDI V8\nElectric motor:	\n48-volt system Belt alternator starter (BAS): MHEV\n100 kW (134 hp; 136 PS) AC induction motor: PHEV\nTransmission:\n8-speed Tiptronic automatic[1] (ZF 8HP90)\nHybrid drivetrain: PHEV (Q8 55/60 TFSIe)\nBattery: 17.3 kWh lithium-ion (PHEV)\nElectric range; 17 mi (27 km) (60 TFSI e)\nDimensions\nWheelbase: 2,995 mm (117.9 in)\nLength: 4,986 mm (196.3 in)[2]\nWidth: 1,995 mm (78.5 in)\nHeight: 1,705 mm (67.1 in)\nCurb weight: 2,145 kg (4,729 lb)'
        bot.send_photo(call.message.chat.id, audiqeightqeightphoto, caption = 'Audi Q8 I (2018-н.в.) – внедорожник 5 дв. J-класса, полный привод. Автомат. Дизельные и бензиновые двигатели мощностью от 231 до 340 лошадиных сил.')
        bot.send_message(call.message.chat.id,text=qeighttext, reply_markup=audiqeight)
    if call.data == "etrongen":
        etronkeyboard = types.InlineKeyboardMarkup()
        key_etronge = types.InlineKeyboardButton(text='I (2018-н.в.)', callback_data='etrongegen')
        etronkeyboard.add(key_etronge)
        bot.send_message(call.message.chat.id, text='Выберите поколение',reply_markup=etronkeyboard)
    if call.data == "etrongegen":
        audietrongephoto = open ('D:/TelegramBots/Project photos/Audi Etron.jfif', 'rb')
        audige = types.InlineKeyboardMarkup()
        ge=types.InlineKeyboardButton("Auto.tu", url='https://auto.ru/moskovskaya_oblast/cars/audi/e_tron/21447469/all/')
        audige.add(ge)
        getext='Дизайн и конструкция\nТип кузова: 5‑дв. SUV (5‑мест.)\nПлатформа: MLB evo\nКолёсная формула: 4 × 4\nДвигатель:\n2 электромотора 408 л.с.\nМассово-габаритные характеристики\nДлина: 4901 мм\nШирина: 1935 мм\nВысота: 1616 мм\nКолёсная база: 2928 мм\nКолея задняя: 1652 мм\nКолея передняя: 1655 мм\nМасса: 2555 кг\nДинамические характеристики:\nРазгон до 100 км/ч: 5.5 сек.\nМаксимальная скорость: 200 км/ч\nСегмент: J-сегмент\nГрузоподъёмность: 575кг.'
        bot.send_photo(call.message.chat.id, audietrongephoto, caption = 'Audi e-tron I (2018-н.в.) – внедорожник 5 дв. J-класса, полный привод. Автомат. Электро двигатели мощностью от 313 до 408 лошадиных сил.')
        bot.send_message(call.message.chat.id,text=getext, reply_markup=audige)
    if call.data == "a7gen":
        asevenkeyboard = types.InlineKeyboardMarkup()
        key_a74g = types.InlineKeyboardButton(text='I (4G)(2010-2014)', callback_data='a74ggen')
        asevenkeyboard.add(key_a74g)
        key_a74gplus = types.InlineKeyboardButton(text='I Рестайлинг (4G)(2014-2018)', callback_data='a74gplusgen')
        asevenkeyboard.add(key_a74gplus)
        key_a74k = types.InlineKeyboardButton(text='II (4K)(2018-н.в.)', callback_data='a74kgen')
        asevenkeyboard.add(key_a74k)
        bot.send_message(call.message.chat.id, text='Выберите поколение',reply_markup=asevenkeyboard)
    if call.data == "a74ggen":
        audiasevenfourgphoto = open ('D:/TelegramBots/Project photos/Audi A7 4G.jfif', 'rb')
        audifourg = types.InlineKeyboardMarkup()
        fourg=types.InlineKeyboardButton("Auto.tu", url='https://auto.ru/moskovskaya_oblast/cars/audi/a7/6457121/all/')
        audifourg.add(fourg)
        fourgtext='Body and chassis\nBody style: 5-door liftback\nPlatform: Volkswagen MLB platform\nPowertrain\nEngine	\nPetrol:\n1.8 L I4 T FSI\n2.0 L I4 T FSI\n2.5 L V6 FSI (China)\n2.8 L V6 FSI\n3.0 L V6 T FSI\n4.0 L V8 T FSI\nDiesel:\n3.0 L V6 TDI\nTransmission	\n7-speed dual clutch S tronic multitronic CVT\n8-speed ZF 8HP automatic (North American model)\nDimensions\nWheelbase: 2,914 mm (114.7 in)\nLength: 4,974 mm (195.8 in)\nWidth: 1,910 mm (75 in)\nHeight: 1,420 mm (56 in)\nCurb weight: 1,910 kg (4,210 lb)'
        bot.send_photo(call.message.chat.id, audiasevenfourgphoto, caption = 'Audi A7 I (4G)(2010-2014) – лифтбек E-класса, передний и полный привод. Вариатор, робот и автомат. Бензиновые и дизельные двигатели мощностью от 204 до 313 лошадиных сил.')
        bot.send_message(call.message.chat.id,text=fourgtext, reply_markup=audifourg)
    if call.data == "a74gplusgen":
        audiasevenfourgplusphoto = open ('D:/TelegramBots/Project photos/Audi A7 4Gplus.jfif', 'rb')
        audifourgplus = types.InlineKeyboardMarkup()
        fourgplus=types.InlineKeyboardButton("Auto.tu", url='https://auto.ru/moskovskaya_oblast/cars/audi/a7/20183736/all/')
        audifourgplus.add(fourgplus)
        fourgplustext='Body and chassis\nBody style: 5-door liftback\nPlatform: Volkswagen MLB platform\nPowertrain\nEngine	\nPetrol:\n1.8 L I4 T FSI\n2.0 L I4 T FSI\n2.5 L V6 FSI (China)\n2.8 L V6 FSI\n3.0 L V6 T FSI\n4.0 L V8 T FSI\nDiesel:\n3.0 L V6 TDI\nTransmission	\n7-speed dual clutch S tronic multitronic CVT\n8-speed ZF 8HP automatic (North American model)\nDimensions\nWheelbase: 2,914 mm (114.7 in)\nLength: 4,974 mm (195.8 in)\nWidth: 1,910 mm (75 in)\nHeight: 1,420 mm (56 in)\nCurb weight: 1,910 kg (4,210 lb)'
        bot.send_photo(call.message.chat.id, audiasevenfourgplusphoto, caption = 'Audi A7 I Рестайлинг (4G)(2014-2018) – лифтбек E-класса, передний и полный привод. Вариатор, робот и автомат. Бензиновые и дизельные двигатели мощностью от 218 до 338 лошадиных сил.')
        bot.send_message(call.message.chat.id,text=fourgplustext, reply_markup=audifourgplus)
    if call.data == "a74kgen":
        audiasevenfourkphoto = open ('D:/TelegramBots/Project photos/Audi A7 4K.jfif', 'rb')
        audifourk = types.InlineKeyboardMarkup()
        fourk=types.InlineKeyboardButton("Auto.tu", url='https://auto.ru/moskovskaya_oblast/cars/audi/a7/21134030/all/')
        audifourk.add(fourk)
        fourktext='Body and chassis\nBody style:\n5-door liftback\n4-door sedan (A7L, China)\nPlatform: Volkswagen MLBevo platform\nPowertrain\nEngine	\nPetrol:\n2.0 L I4 T FSI (45 TFSI)\n3.0 L V6 T FSI (55 TFSI)\n3.0 L V6 T FSI MHEV system\n2.9 L V6 TT FSI (S7)[41]\n4.0 L V8 TT FSI (RS7)\nDiesel:\n2.0 L TDI I4 (40 TDI)\n3.0 L TDI V6 (50 TDI)\nPHEV:\n2.0 L T FSI I4 (55 TFSIe)\nElectric motor: AC synchronous electric motor (55 TFSIe)\nTransmission	\n7-speed dual clutch S tronic\n8-speed automatic tiptronic\nHybrid drivetrain:\nMHEV (55 TFSI / S7 TFSI / RS7 TFSI)\nPHEV (50 TFSI e / 55 TFSI e)\nDimensions\nWheelbase:\n2,926 mm (115.2 in)\n3,024 mm (119.1 in) (A7L)[42]\nLength:\n4,969 mm (195.6 in)\n5,095 mm (200.6 in) (A7L)\nWidth: 1,926 mm (75.8 in)\nHeight: 1,422 mm (56.0 in)\nCurb weight: 1,890 kg (4,170 lb)'
        bot.send_photo(call.message.chat.id, audiasevenfourkphoto, caption = 'Audi A7 II (4K)(2018-н.в.) – лифтбек E-класса, полный и передний привод. Робот и автомат. Бензиновые, дизельные и гибридные двигатели мощностью от 204 до 367 лошадиных сил.')
        bot.send_message(call.message.chat.id,text=fourktext, reply_markup=audifourk)
    if call.data == "q7gen":
        qsevenkeyboard = types.InlineKeyboardMarkup()
        key_q74l = types.InlineKeyboardButton(text='I (4L)(2005-2009)', callback_data='q74lgen')
        qsevenkeyboard.add(key_q74l)
        key_q74lplus = types.InlineKeyboardButton(text='I Рестайлинг (4L)(2009-2015)', callback_data='q74lplusgen')
        qsevenkeyboard.add(key_q74lplus)
        key_q74m = types.InlineKeyboardButton(text='II (4M)(2015-2019)', callback_data='q74mgen')
        qsevenkeyboard.add(key_q74m)
        key_q74mplus = types.InlineKeyboardButton(text='II Рестайлинг (4M)(2019-2022)', callback_data='q74mplusgen')
        qsevenkeyboard.add(key_q74mplus)
        bot.send_message(call.message.chat.id, text='Выберите поколение',reply_markup=qsevenkeyboard)
    if call.data == "q74lgen":
        audiqsevenfourlphoto = open ('D:/TelegramBots/Project photos/Audi Q7 4L.jfif', 'rb')
        audifourl = types.InlineKeyboardMarkup()
        fourl=types.InlineKeyboardButton("Auto.tu", url='https://auto.ru/moskovskaya_oblast/cars/audi/q7/2305494/all/')
        audifourl.add(fourl)
        fourltext='Body and chassis\nPlatform: Volkswagen Group PL71 platform\nPowertrain\nEngine\nPetrol:\n3.0L V6 T FSI\n3.6L VR6 FSI\n4.2L V8 FSI\nDiesel:\n3.0L V6 TDI\n4.2L V8 TDI\n6.0L V12 TDI\nTransmission:\n6-speed manual\n6-speed automatic\n8-speed Aisin automatic\nDimensions\nWheelbase: 3,002 mm (118.2 in)\nLength: 5,085 mm (200.2 in)\nWidth: 1,984 mm (78.1 in)\nHeight: 1,737 mm (68.4 in)[7]\nKerb weight: 2,205–2,605 kg (4,861–5,743 lb)'
        bot.send_photo(call.message.chat.id, audiqsevenfourlphoto, caption = 'Audi Q7 I (4L)(2005-2009) – внедорожник 5 дв. J-класса, полный привод. Автомат и механика. Бензиновые и дизельные двигатели мощностью от 211 до 500 лошадиных сил.')
        bot.send_message(call.message.chat.id,text=fourltext, reply_markup=audifourl)
    if call.data == "q74lplusgen":
        audiqsevenfourlplusphoto = open ('D:/TelegramBots/Project photos/Audi Q7 4Lplus.jfif', 'rb')
        audifourlplus = types.InlineKeyboardMarkup()
        fourlplus=types.InlineKeyboardButton("Auto.tu", url='https://auto.ru/moskovskaya_oblast/cars/audi/q7/6468119/all/')
        audifourlplus.add(fourlplus)
        fourlplustext='Body and chassis\nPlatform: Volkswagen Group PL71 platform\nPowertrain\nEngine\nPetrol:\n3.0L V6 T FSI\n3.6L VR6 FSI\n4.2L V8 FSI\nDiesel:\n3.0L V6 TDI\n4.2L V8 TDI\n6.0L V12 TDI\nTransmission:\n6-speed manual\n6-speed automatic\n8-speed Aisin automatic\nDimensions\nWheelbase: 3,002 mm (118.2 in)\nLength: 5,085 mm (200.2 in)\nWidth: 1,984 mm (78.1 in)\nHeight: 1,737 mm (68.4 in)[7]\nKerb weight: 2,205–2,605 kg (4,861–5,743 lb)'
        bot.send_photo(call.message.chat.id, audiqsevenfourlplusphoto, caption = 'Audi Q7 I Рестайлинг(4L)(2009-2015) – внедорожник 5 дв. J-класса, полный привод. Автомат и механика. Бензиновые и дизельные двигатели мощностью от 204 до 500 лошадиных сил.')
        bot.send_message(call.message.chat.id,text=fourlplustext, reply_markup=audifourlplus)
    if call.data == "q74mgen":
        audiqsevenfourmphoto = open ('D:/TelegramBots/Project photos/Audi Q7 4M.jfif', 'rb')
        audifourm = types.InlineKeyboardMarkup()
        fourm=types.InlineKeyboardButton("Auto.tu", url='https://auto.ru/moskovskaya_oblast/cars/audi/q7/20368749/all/')
        audifourm.add(fourm)
        fourmtext='Body and chassis\nBody style: 4-door SUV\nPlatform: Volkswagen Group MLB Evo\nPowertrain\nEngine	\nPetrol:\n2.0 L TFSI I4\n2.0 L TFSI I4 PHEV\n3.0 L Supercharged V6\n3.0 L TFSI V6\n3.0 L TFSI V6 PHEV\n4.0L TFSI V8\nDiesel:\n3.0L TDI V6\n3.0L TDI V6 PHEV\n4.0L TDI V8\nTransmission:\n6-speed automatic\n8-speed ZF 8HP Automatic\nDimensions\nWheelbase: 2,994 mm (117.9 in)\nLength: 5,052 mm (198.9 in)\nWidth: 1,968 mm (77.5 in)\nHeight: 1,741 mm (68.5 in)\nCurb weight: 1,910–2,445 kg (4,210–5,390 lb)'
        bot.send_photo(call.message.chat.id, audiqsevenfourmphoto, caption = 'Audi Q7 II (4M)(2015-2019) – внедорожник 5 дв. J-класса, полный привод. Автомат. Бензиновые и дизельные двигатели мощностью от 218 до 333 лошадиных сил.')
        bot.send_message(call.message.chat.id,text=fourmtext, reply_markup=audifourm)
    if call.data == "q74mplusgen":
        audiqsevenfourmplusphoto = open ('D:/TelegramBots/Project photos/Audi Q7 4Mplus.jfif', 'rb')
        audifourmplus = types.InlineKeyboardMarkup()
        fourmplus=types.InlineKeyboardButton("Auto.tu", url='https://auto.ru/moskovskaya_oblast/cars/audi/q7/21646875/all/')
        audifourmplus.add(fourmplus)
        fourmplustext='Body and chassis\nBody style: 4-door SUV\nPlatform: Volkswagen Group MLB Evo\nPowertrain\nEngine	\nPetrol:\n2.0 L TFSI I4\n2.0 L TFSI I4 PHEV\n3.0 L Supercharged V6\n3.0 L TFSI V6\n3.0 L TFSI V6 PHEV\n4.0L TFSI V8\nDiesel:\n3.0L TDI V6\n3.0L TDI V6 PHEV\n4.0L TDI V8\nTransmission:\n6-speed automatic\n8-speed ZF 8HP Automatic\nDimensions\nWheelbase: 2,994 mm (117.9 in)\nLength: 5,052 mm (198.9 in)\nWidth: 1,968 mm (77.5 in)\nHeight: 1,741 mm (68.5 in)\nCurb weight: 1,910–2,445 kg (4,210–5,390 lb)'
        bot.send_photo(call.message.chat.id, audiqsevenfourmplusphoto, caption = 'Audi Q7 II Рестайлинг (4M)(2019-н.в.) – внедорожник 5 дв. J-класса, полный привод. Автомат. Бензиновые и дизельные двигатели мощностью от 231 до 462 лошадиных сил.')
        bot.send_message(call.message.chat.id,text=fourmplustext, reply_markup=audifourmplus)
    if call.data == "r8gen":
        reightkeyboard = types.InlineKeyboardMarkup()
        key_r842 = types.InlineKeyboardButton(text='I (Typ 42)(2007-2012)', callback_data='r842gen')
        reightkeyboard.add(key_r842)
        key_r842plus = types.InlineKeyboardButton(text='I Рестайлинг (Typ 42)(2012-2015)', callback_data='r842plusgen')
        reightkeyboard.add(key_r842plus)
        key_r84s = types.InlineKeyboardButton(text='II (4S)(2015-2018)', callback_data='r84sgen')
        reightkeyboard.add(key_r84s)
        key_r84splus = types.InlineKeyboardButton(text='II Рестайлинг(4S)(2019-н.в.)', callback_data='r84splusgen')
        reightkeyboard.add(key_r84splus)
        bot.send_message(call.message.chat.id, text='Выберите поколение',reply_markup=reightkeyboard)
    if call.data == "r842gen":
        audireightfortytwophoto = open ('D:/TelegramBots/Project photos/Audi R8 42.jfif', 'rb')
        audifourtytwo = types.InlineKeyboardMarkup()
        fourtytwo=types.InlineKeyboardButton("Auto.tu", url='https://auto.ru/moskva/cars/audi/r8/2305489/all/')
        audifourtytwo.add(fourtytwo)
        fourtytwotext='Двигатель:\n4.2 FSI V8, 2×DOHC (420 л.с.)\n5.2 FSI V10, 2×DOHC (525 л.с.)\nТрансмиссия:\n6-ступ. МКПП\n6-ступ. R-Tronic (V8)\n7-ступ. S-Tronic (V10)\nМассово-габаритные характеристики:\nДлина:\nV8 Coupé: 4,431 мм\nV10 Coupé: 4,435 мм\nV10 Spyder: 4,434 мм\nШирина:\nV8 Coupé: 1,904 мм\nV10 Spyder: 1,904 мм\nV10 Coupé: 1,930 мм\nВысота:\nV8 Coupé: 1,249 мм\nV10 Coupé: 1,252 мм\nV10 Spyder: 1,244 мм\nКлиренс: 104 мм\nКолёсная база: 2650 мм\nМасса:\nV8 Coupé: 1,560–1,565 кг\nV10 Coupé: 1,620–1,625\nV10 Spyder: 1,720–1,725 кг\nОбъём бака:\n75 л. (V8)\n90 л. (V10)\nДизайнер: Вальтер де Сильва (по прототипу Audi Le Mans quattro)\nМодификации:\nR8 V8 FSI\nR8 V10 FSI\nR8 V10 GT\nR8 V10 Plus\nR8 V8/V10/GT Spyder'
        bot.send_photo(call.message.chat.id, audireightfortytwophoto, caption = 'Audi R8 I (Typ 42)(2007-2012)– купе S-класса, полный привод. Механика и робот. Бензиновые двигатели мощностью от 420 до 525 лошадиных сил.')
        bot.send_message(call.message.chat.id,text=fourtytwotext, reply_markup=audifourtytwo)
    if call.data == "r842plusgen":
        audireightfourtytwoplusphoto = open ('D:/TelegramBots/Project photos/Audi R8 42plus.jfif', 'rb')
        audifourtytwoplus = types.InlineKeyboardMarkup()
        fourtytwoplus=types.InlineKeyboardButton("Auto.tu", url='https://auto.ru/moskva/cars/audi/r8/8465939/all/')
        audifourtytwoplus.add(fourtytwoplus)
        fourtytwoplustext='Двигатель:\n4.2 FSI V8, 2×DOHC (420 л.с.)\n5.2 FSI V10, 2×DOHC (525 л.с.)\nТрансмиссия:\n6-ступ. МКПП\n6-ступ. R-Tronic (V8)\n7-ступ. S-Tronic (V10)\nМассово-габаритные характеристики:\nДлина:\nV8 Coupé: 4,431 мм\nV10 Coupé: 4,435 мм\nV10 Spyder: 4,434 мм\nШирина:\nV8 Coupé: 1,904 мм\nV10 Spyder: 1,904 мм\nV10 Coupé: 1,930 мм\nВысота:\nV8 Coupé: 1,249 мм\nV10 Coupé: 1,252 мм\nV10 Spyder: 1,244 мм\nКлиренс: 104 мм\nКолёсная база: 2650 мм\nМасса:\nV8 Coupé: 1,560–1,565 кг\nV10 Coupé: 1,620–1,625\nV10 Spyder: 1,720–1,725 кг\nОбъём бака:\n75 л. (V8)\n90 л. (V10)\nДизайнер: Вальтер де Сильва (по прототипу Audi Le Mans quattro)\nМодификации:\nR8 V8 FSI\nR8 V10 FSI\nR8 V10 GT\nR8 V10 Plus\nR8 V8/V10/GT Spyder'
        bot.send_photo(call.message.chat.id, audireightfourtytwoplusphoto, caption = 'Audi R8 I Рестайлинг(Typ 42)(2012-2015)– купе S-класса, полный привод. Механика и робот. Бензиновые двигатели мощностью от 430 до 570 лошадиных сил.')
        bot.send_message(call.message.chat.id,text=fourtytwoplustext, reply_markup=audifourtytwoplus)
    if call.data == "r84sgen":
        audireightfoursphoto = open ('D:/TelegramBots/Project photos/Audi R8 4S.jfif', 'rb')
        audifours = types.InlineKeyboardMarkup()
        fours =types.InlineKeyboardButton("Auto.tu", url='https://auto.ru/moskva/cars/audi/r8/20489751/all/')
        audifours.add(fours)
        fourstext='Двигатель:\n5.2 л. V10 540 л.с. (610 л.с Plus)\nТрансмиссия:\n7-ступ. S-Tronic\nМассово-габаритные характеристики:\nДлина: 4426 мм\nШирина: 1940 мм\nВысота: 1240 мм\nКлиренс: 105 мм\nКолёсная база: 2650 мм\nМасса: 1,555 – 1,720 кг\nОбъём бака: 83 л (V10)\nМодификации:\nR8 V10\nR8 V10 Plus\nR8 V10 RWS'
        bot.send_photo(call.message.chat.id, audireightfoursphoto, caption = 'Audi R8 II (4S)(2015-2018) – купе S-класса, полный и задний привод. Робот. Бензиновые двигатели мощностью от 540 до 610 лошадиных сил.')
        bot.send_message(call.message.chat.id,text=fourstext, reply_markup=audifours)
    if call.data == "r84splusgen":
        audireightfoursplusphoto = open ('D:/TelegramBots/Project photos/Audi R8 4Splus.jfif', 'rb')
        audifoursplus = types.InlineKeyboardMarkup()
        foursplus =types.InlineKeyboardButton("Auto.tu", url='https://auto.ru/moskva/cars/audi/r8/21549085/all/')
        audifoursplus.add(foursplus)
        foursplustext='Двигатель:\n5.2 л. V10 540 л.с. (610 л.с Plus)\nТрансмиссия:\n7-ступ. S-Tronic\nМассово-габаритные характеристики:\nДлина: 4426 мм\nШирина: 1940 мм\nВысота: 1240 мм\nКлиренс: 105 мм\nКолёсная база: 2650 мм\nМасса: 1,555 – 1,720 кг\nОбъём бака: 83 л (V10)\nМодификации:\nR8 V10\nR8 V10 Plus\nR8 V10 RWS'
        bot.send_photo(call.message.chat.id, audireightfoursplusphoto, caption = 'Audi R8 II Рестайлинг (4S)(2019-н.в.) – купе S-класса, полный и задний привод. Робот. Бензиновые двигатели мощностью от 540 до 620 лошадиных сил.')
        bot.send_message(call.message.chat.id,text=foursplustext, reply_markup=audifoursplus)
    if call.data == "ttgen":
        ttkeyboard = types.InlineKeyboardMarkup()
        key_tt8n = types.InlineKeyboardButton(text='I (8N)(1998-2003)', callback_data='tt8ngen')
        ttkeyboard.add(key_tt8n)
        key_tt8nplus = types.InlineKeyboardButton(text='I Рестайлинг (8N)(2003-2006)', callback_data='tt8nplusgen')
        ttkeyboard.add(key_tt8nplus)
        key_tt8j = types.InlineKeyboardButton(text='II (8J)(2006-2010)', callback_data='tt8jgen')
        ttkeyboard.add(key_tt8j)
        key_tt8jplus = types.InlineKeyboardButton(text='II Рестайлинг (8J)(2010-2014)', callback_data='tt8jplusgen')
        ttkeyboard.add(key_tt8jplus)
        key_tt8s = types.InlineKeyboardButton(text='III (8S)(2014-2019)', callback_data='tt8sgen')
        ttkeyboard.add(key_tt8s)
        key_tt8splus = types.InlineKeyboardButton(text='III Рестайлинг (8S)(2018-н.в.)', callback_data='tt8splusgen')
        ttkeyboard.add(key_tt8splus)
        bot.send_message(call.message.chat.id, text='Выберите поколение',reply_markup=ttkeyboard)
    if call.data == "tt8ngen":
        auditteightnphoto = open ('D:/TelegramBots/Project photos/Audi TT 8N.jfif', 'rb')
        audieightn = types.InlineKeyboardMarkup()
        eightn =types.InlineKeyboardButton("Auto.tu", url='https://auto.ru/moskovskaya_oblast/cars/audi/tt/4601115/all/')
        audieightn.add(eightn)
        eightntext='Body and chassis\nPlatform: Volkswagen Group A4 (PQ34)\nPowertrain\nEngine:\n1.8 L 20v turbocharged I4\n3.2 L 24v VR6\nTransmission:	\n5-speed manual 02J (all models 180 PS)\n6-speed manual 02M (all models 225 PS)\n6-speed Tiptronic 09G\n6-speed DSG (3.2 L Quattro only)\nDimensions\nWheelbase:\n2,422 mm (95.4 in)\nQuattro: 2,428 mm (95.6 in)\nLength: 4,041 mm (159.1 in)\nWidth: 1,764 mm (69.4 in)\nHeight: 1,346 mm (53.0 in)'
        bot.send_photo(call.message.chat.id, auditteightnphoto, caption = 'Audi TT I (8N)(1999-2003) – автомобиль S-класса, передний и полный привод. Механика и автомат. Бензиновые двигатели мощностью от 150 до 225 лошадиных сил.')
        bot.send_message(call.message.chat.id,text=eightntext, reply_markup=audieightn)
    if call.data == "tt8nplusgen":
        auditteightnplusphoto = open ('D:/TelegramBots/Project photos/Audi TT 8Nplus.jfif', 'rb')
        audieightnplus = types.InlineKeyboardMarkup()
        eightnplus =types.InlineKeyboardButton("Auto.tu", url='https://auto.ru/moskovskaya_oblast/cars/audi/tt/20264265/all/')
        audieightnplus.add(eightnplus)
        eightnplustext='Body and chassis\nPlatform: Volkswagen Group A4 (PQ34)\nPowertrain\nEngine:\n1.8 L 20v turbocharged I4\n3.2 L 24v VR6\nTransmission:	\n5-speed manual 02J (all models 180 PS)\n6-speed manual 02M (all models 225 PS)\n6-speed Tiptronic 09G\n6-speed DSG (3.2 L Quattro only)\nDimensions\nWheelbase:\n2,422 mm (95.4 in)\nQuattro: 2,428 mm (95.6 in)\nLength: 4,041 mm (159.1 in)\nWidth: 1,764 mm (69.4 in)\nHeight: 1,346 mm (53.0 in)'
        bot.send_photo(call.message.chat.id, auditteightnplusphoto, caption = 'Audi TT I Рестайлинг (8N)(2003-2006) – автомобиль S-класса, передний и полный привод. Механика и автомат. Бензиновые двигатели мощностью от 150 до 250 лошадиных сил.')
        bot.send_message(call.message.chat.id,text=eightnplustext, reply_markup=audieightnplus)
    if call.data == "tt8jgen":
        auditteightjphoto = open ('D:/TelegramBots/Project photos/Audi TT 8J.jfif', 'rb')
        audieightj = types.InlineKeyboardMarkup()
        eightj =types.InlineKeyboardButton("Auto.tu", url='https://auto.ru/moskovskaya_oblast/cars/audi/tt/2305317/all/')
        audieightj.add(eightj)
        eightjtext='Body and chassis\nPlatform: Volkswagen Group A5 (PQ35)\nPowertrain\nEngine:	\n1.8 L turbocharged FSI I4\n2.0 L TFSI I4\n2.5 L TFSI I5 (TT RS only)\n3.2 L VR6\n2.0 L TDI CR diesel I4\nTransmission:\n6-speed manual\n6-speed S tronic\nDimensions:\nWheelbase: 2,468 mm (97.2 in)\nLength:\n4,178 mm (164.5 in)\nTTS & TT RS: 4,198 mm (165.3 in)\nWidth: 1,842 mm (72.5 in)\nHeight:	\n1,352 mm (53.2 in)\nTTS: 1,345 mm (53.0 in)\nTT RS: 1,342 mm (52.8 in)\nS Convertible: 53.5 in (1,359 mm)\nConvertible: 53.5 in (1,359 mm)\nKerb weight: 1,260–1,490 kg (2,778–3,285 lb)'
        bot.send_photo(call.message.chat.id, auditteightjphoto, caption = 'Audi TT II (8J)(2006-2010) – автомобиль S-класса, передний и полный привод. Механика и робот. Бензиновые и дизельные двигатели мощностью от 160 до 250 лошадиных сил.')
        bot.send_message(call.message.chat.id,text=eightjtext, reply_markup=audieightj)
    if call.data == "tt8jplusgen":
        auditteightjplusphoto = open ('D:/TelegramBots/Project photos/Audi TT 8Jplus.jfif', 'rb')
        audieightjplus = types.InlineKeyboardMarkup()
        eightjplus =types.InlineKeyboardButton("Auto.tu", url='https://auto.ru/moskovskaya_oblast/cars/audi/tt/6846663/all/')
        audieightjplus.add(eightjplus)
        eightjplustext='Body and chassis\nPlatform: Volkswagen Group A5 (PQ35)\nPowertrain\nEngine:	\n1.8 L turbocharged FSI I4\n2.0 L TFSI I4\n2.5 L TFSI I5 (TT RS only)\n3.2 L VR6\n2.0 L TDI CR diesel I4\nTransmission:\n6-speed manual\n6-speed S tronic\nDimensions:\nWheelbase: 2,468 mm (97.2 in)\nLength:\n4,178 mm (164.5 in)\nTTS & TT RS: 4,198 mm (165.3 in)\nWidth: 1,842 mm (72.5 in)\nHeight:	\n1,352 mm (53.2 in)\nTTS: 1,345 mm (53.0 in)\nTT RS: 1,342 mm (52.8 in)\nS Convertible: 53.5 in (1,359 mm)\nConvertible: 53.5 in (1,359 mm)\nKerb weight: 1,260–1,490 kg (2,778–3,285 lb)'
        bot.send_photo(call.message.chat.id, auditteightjplusphoto, caption = 'Audi TT II Рестайлинг (8J)(2010-2014) – автомобиль S-класса, передний и полный привод. Механика и робот. Бензиновые и дизельные двигатели мощностью от 160 до 211 лошадиных сил.')
        bot.send_message(call.message.chat.id,text=eightjplustext, reply_markup=audieightjplus)
    if call.data == "tt8sgen":
        auditteightsphoto = open ('D:/TelegramBots/Project photos/Audi TT 8S.jfif', 'rb')
        audieights = types.InlineKeyboardMarkup()
        eights =types.InlineKeyboardButton("Auto.tu", url='https://auto.ru/moskovskaya_oblast/cars/audi/tt/20176878/all/')
        audieights.add(eights)
        eightstext='Body and chassis\nPlatform: Volkswagen Group MQB\nPowertrain\nEngine:\n1.8 L CJSA (EA888-Gen3) turbocharged FSI I4\n2.0 L EA888 turbocharged FSI I4\n2.0 L CUPA (EA288) TDI I4\n2.5 L LEV3-ULEV125 turbocharged FSI I5 (TT RS)\nTransmission:	\n6-speed manual\n6-speed S tronic\n7-speed S tronic (RS only)\nDimensions\nWheelbase: 2,505 mm (98.6 in)\nLength:	\nCoupe:4,191 mm (165.0 in)\nRoadster: 4,177 mm (164.4 in)\nWidth: 1,832 mm (72.1 in)\nHeight:	\nCoupe:1,343 mm (52.9 in)\nRoadster: 1,355 mm (53.3 in)\nKerb weight: 1,230–1,425 kg (2,712–3,142 lb)'
        bot.send_photo(call.message.chat.id, auditteightsphoto, caption = 'Audi TT III (8S)(2014-2019) – автомобиль S-класса, передний и полный привод. Робот и механика. Бензиновые и дизельные двигатели мощностью от 180 до 230 лошадиных сил.')
        bot.send_message(call.message.chat.id,text=eightstext, reply_markup=audieights)
    if call.data == "tt8splusgen":
        auditteightsplusphoto = open ('D:/TelegramBots/Project photos/Audi TT 8Splus.jfif', 'rb')
        audieightsplus = types.InlineKeyboardMarkup()
        eightsplus =types.InlineKeyboardButton("Auto.tu", url='https://auto.ru/moskovskaya_oblast/cars/audi/tt/21464559/all/')
        audieightsplus.add(eightsplus)
        eightsplustext='Body and chassis\nPlatform: Volkswagen Group MQB\nPowertrain\nEngine:\n1.8 L CJSA (EA888-Gen3) turbocharged FSI I4\n2.0 L EA888 turbocharged FSI I4\n2.0 L CUPA (EA288) TDI I4\n2.5 L LEV3-ULEV125 turbocharged FSI I5 (TT RS)\nTransmission:	\n6-speed manual\n6-speed S tronic\n7-speed S tronic (RS only)\nDimensions\nWheelbase: 2,505 mm (98.6 in)\nLength:	\nCoupe:4,191 mm (165.0 in)\nRoadster: 4,177 mm (164.4 in)\nWidth: 1,832 mm (72.1 in)\nHeight:	\nCoupe:1,343 mm (52.9 in)\nRoadster: 1,355 mm (53.3 in)\nKerb weight: 1,230–1,425 kg (2,712–3,142 lb)'
        bot.send_photo(call.message.chat.id, auditteightsplusphoto, caption = 'Audi TT III Рестайлинг(8S)(2018-н.в.) – автомобиль S-класса, передний и полный привод. Робот и механика. Бензиновые и дизельные двигатели мощностью от 197 до 245 лошадиных сил.')
        bot.send_message(call.message.chat.id,text=eightsplustext, reply_markup=audieightsplus)
    if call.data == "a6gen":
        asixkeyboard = types.InlineKeyboardMarkup()
        key_a6c4 = types.InlineKeyboardButton(text='I (C4)(1994-1997)', callback_data='a6c4gen')
        asixkeyboard.add(key_a6c4)
        key_a6c5 = types.InlineKeyboardButton(text='II (C5)(1997-2001)', callback_data='a6c5gen')
        asixkeyboard.add(key_a6c5)
        key_a6c5plus = types.InlineKeyboardButton(text='II Рестайлинг (C5)(2001-2005)', callback_data='a6c5plusgen')
        asixkeyboard.add(key_a6c5plus)
        key_a6c6 = types.InlineKeyboardButton(text='III (C6)(2005-2008)', callback_data='a6c6gen')
        asixkeyboard.add(key_a6c6)
        key_a6c6plus = types.InlineKeyboardButton(text='III Рестайлинг (C6)(2008-2011)', callback_data='a6c6plusgen')
        asixkeyboard.add(key_a6c6plus)
        key_a6c7 = types.InlineKeyboardButton(text='IV (C7)(2011-2014)', callback_data='a6c7gen')
        asixkeyboard.add(key_a6c7)
        key_a6c7plus = types.InlineKeyboardButton(text='IV Рестайлинг (C7)(2014-2018)', callback_data='a6c7plusgen')
        asixkeyboard.add(key_a6c7plus)
        key_a6c8 = types.InlineKeyboardButton(text='V (C8)(2018-н.в.)', callback_data='a6c8gen')
        asixkeyboard.add(key_a6c8)
        bot.send_message(call.message.chat.id, text='Выберите поколение',reply_markup=asixkeyboard)
    if call.data == "a6c4gen":
        audiasixcfourphoto = open ('D:/TelegramBots/Project photos/Audi A6 C4.jfif', 'rb')
        audicfourplus= types.InlineKeyboardMarkup()
        cfourplus =types.InlineKeyboardButton("Auto.tu", url='https://auto.ru/moskovskaya_oblast/cars/audi/a6/3473231/all/')
        audicfourplus.add(cfourplus)
        cfourplustext='Body and chassis\nPlatform: Volkswagen Group C4\nPowertrain\nEngine:\n1.8 L I4\n2.0 L I4\n2.6 L V6\n2.8 L V6\n1.9 L I4 TDI\n2.5 L I5 TDI\nTransmission:\n5-speed manual\n6-speed manual\n4-speed automatic\nDimensions\nWheelbase:\n2,687 mm (105.8 in) (FWD)\n2,692 mm (106.0 in) (AWD)\nLength: 4,797 mm (188.9 in)\nWidth: 1,783 mm (70.2 in)\nHeight: 1,430 mm (56.3 in)'
        bot.send_photo(call.message.chat.id, audiasixcfourphoto, caption = 'Audi A6 I (C4)(1994-1997) – автомобиль E-класса, передний и полный привод. Автомат и механика. Бензиновые и дизельные двигатели мощностью от 90 до 193 лошадиных сил.')
        bot.send_message(call.message.chat.id,text=cfourplustext, reply_markup=audicfourplus)
    if call.data == "a6c5gen":
        audiasixcfivephoto = open ('D:/TelegramBots/Project photos/Audi A6 C5.jfif', 'rb')
        audicfive= types.InlineKeyboardMarkup()
        cfive =types.InlineKeyboardButton("Auto.tu", url='https://auto.ru/moskovskaya_oblast/cars/audi/a6/3473237/all/')
        audicfive.add(cfive)
        cfivetext='Body and chassis\nPlatform: Volkswagen Group C5\nPowertrain\nEngine\nPetrol:\n1.8 L 20v I4\n1.8 L turbo 20v I4\n2.0 L 20v I4\n2.4 L 30v V6\n2.4 L 30v BDV V6\n2.7 L turbo 30v V6\n2.8 L 30v V6\n3.0 L 30v V6\n4.2 L 40v V8\n4.2 L turbo 40v V8\nDiesel:\n1.9 L TDI I4\n2.5 L 24v V6 TDI\nTransmission:\n5-speed manual\n6-speed manual\n5-speed automatic\nmultitronic CVT\n5-speed automatic with tiptronic\nDimensions\nWheelbase: 2,760 mm (108.7 in)\nLength: 4,805 mm (189.2 in)\nWidth: 1,810 mm (71.3 in)\nHeight:\nSaloon: 1,453 mm (57.2 in)\nAvant: 1,479 mm (58.2 in)\nKerb weight: 1,480 kg (3,262.8 lb)'
        bot.send_photo(call.message.chat.id, audiasixcfivephoto, caption = 'Audi A6 II (C5)(1997-2001) – автомобиль E-класса, передний и полный привод. Механика, автомат и вариатор. Бензиновые и дизельные двигатели мощностью от 110 до 300 лошадиных сил.')
        bot.send_message(call.message.chat.id,text=cfivetext, reply_markup=audicfive)
    if call.data == "a6c5plusgen":
        audiasixcfiveplusphoto = open ('D:/TelegramBots/Project photos/Audi A6 C5plus.jfif', 'rb')
        audicfiveplus= types.InlineKeyboardMarkup()
        cfiveplus =types.InlineKeyboardButton("Auto.tu", url='https://auto.ru/moskovskaya_oblast/cars/audi/a6/6297437/all/')
        audicfiveplus.add(cfiveplus)
        cfiveplustext='Body and chassis\nPlatform: Volkswagen Group C5\nPowertrain\nEngine\nPetrol:\n1.8 L 20v I4\n1.8 L turbo 20v I4\n2.0 L 20v I4\n2.4 L 30v V6\n2.4 L 30v BDV V6\n2.7 L turbo 30v V6\n2.8 L 30v V6\n3.0 L 30v V6\n4.2 L 40v V8\n4.2 L turbo 40v V8\nDiesel:\n1.9 L TDI I4\n2.5 L 24v V6 TDI\nTransmission:\n5-speed manual\n6-speed manual\n5-speed automatic\nmultitronic CVT\n5-speed automatic with tiptronic\nDimensions\nWheelbase: 2,760 mm (108.7 in)\nLength: 4,805 mm (189.2 in)\nWidth: 1,810 mm (71.3 in)\nHeight:\nSaloon: 1,453 mm (57.2 in)\nAvant: 1,479 mm (58.2 in)\nKerb weight: 1,480 kg (3,262.8 lb)'
        bot.send_photo(call.message.chat.id, audiasixcfiveplusphoto, caption = 'Audi A6 II Рестайлинг (C5)(2001-2005) – автомобиль E-класса, передний и полный привод. Механика, автомат и вариатор. Бензиновые и дизельные двигатели мощностью от 130 до 300 лошадиных сил.')
        bot.send_message(call.message.chat.id,text=cfiveplustext, reply_markup=audicfiveplus)
    if call.data == "a6c6gen":
        audiasixcsixphoto = open ('D:/TelegramBots/Project photos/Audi A6 C6.jfif', 'rb')
        audicsix= types.InlineKeyboardMarkup()
        csix =types.InlineKeyboardButton("Auto.tu", url='https://auto.ru/moskovskaya_oblast/cars/audi/a6/4601089/all/')
        audicsix.add(csix)
        csixtext='Body and chassis\nPlatform: Volkswagen Group C6 platform\nPowertrain\nEngine:\n2.0 L I4 Turbo\n2.4 L V6\n2.8 L V6 FSI\n3.0 L V6 (China)\n3.0 L V6 Supercharged\n3.2 L V6 FSI\n4.2 L V8\n5.0 L V10 biturbo\n5.2 L V10\n2.0 L I4 TDI\n2.7 L V6 TDI\n3.0 L V6 TDI\nTransmission:\n6-speed manual\n6-speed tiptronic automatic\nmultitronic CVT\nDimensions\nWheelbase:\n2,843 mm (111.9 in)\nLWB: 2,945 mm (115.9 in)\nLength:\n4,927 mm (194.0 in)\nLWB: 5,035 mm (198.2 in)\nWidth: 1,855 mm (73.0 in)\nHeight:\nSaloon: 1,459 mm (57.4 in)\nAvant: 1,463 mm (57.6 in)\nLWB: 1,485 mm (58.5 in)\nKerb weight: 1,520–1,845 kg (3,351.0–4,067.5 lb)'
        bot.send_photo(call.message.chat.id, audiasixcsixphoto, caption = 'Audi A6 III (C6)(2005-2008) – автомобиль E-класса, передний и полный привод. Механика, вариатор и автомат. Дизельные и бензиновые двигатели мощностью от 140 до 350 лошадиных сил.')
        bot.send_message(call.message.chat.id,text=csixtext, reply_markup=audicsix)
    if call.data == "a6c6plusgen":
        audiasixcsixplusphoto = open ('D:/TelegramBots/Project photos/Audi A6 C6plus.jfif', 'rb')
        audicsixplus = types.InlineKeyboardMarkup()
        csixplus = types.InlineKeyboardButton("Auto.tu", url='https://auto.ru/moskovskaya_oblast/cars/audi/a6/2305417/all/')
        audicsixplus.add(csixplus)
        csixplustext='Body and chassis\nPlatform: Volkswagen Group C6 platform\nPowertrain\nEngine:\n2.0 L I4 Turbo\n2.4 L V6\n2.8 L V6 FSI\n3.0 L V6 (China)\n3.0 L V6 Supercharged\n3.2 L V6 FSI\n4.2 L V8\n5.0 L V10 biturbo\n5.2 L V10\n2.0 L I4 TDI\n2.7 L V6 TDI\n3.0 L V6 TDI\nTransmission:\n6-speed manual\n6-speed tiptronic automatic\nmultitronic CVT\nDimensions\nWheelbase:\n2,843 mm (111.9 in)\nLWB: 2,945 mm (115.9 in)\nLength:\n4,927 mm (194.0 in)\nLWB: 5,035 mm (198.2 in)\nWidth: 1,855 mm (73.0 in)\nHeight:\nSaloon: 1,459 mm (57.4 in)\nAvant: 1,463 mm (57.6 in)\nLWB: 1,485 mm (58.5 in)\nKerb weight: 1,520–1,845 kg (3,351.0–4,067.5 lb)'
        bot.send_photo(call.message.chat.id, audiasixcsixplusphoto, caption = 'Audi A6 III Рестайлинг (C6)(2008-2011) – автомобиль E-класса, передний и полный привод. Механика, вариатор и автомат. Дизельные и бензиновые двигатели мощностью от 136 до 350 лошадиных сил.')
        bot.send_message(call.message.chat.id,text=csixplustext, reply_markup=audicsixplus)
    if call.data == "a6c7gen":
        audiasixcsevenphoto = open ('D:/TelegramBots/Project photos/Audi A6 C7.jfif', 'rb')
        audicseven = types.InlineKeyboardMarkup()
        cseven =types.InlineKeyboardButton("Auto.tu", url='https://auto.ru/moskovskaya_oblast/cars/audi/a6/6937659/all/')
        audicseven.add(cseven)
        cseventext='Body and chassis\nBody style:\n4-door sedan\n5-door station wagon\nPlatform: Volkswagen Group MLB platform\nPowertrain\nEngine:\n1.8 L TFSI I4 (China)\n2.0 L TFSI I4\n2.5 L FSI V6 (China)\n2.8 L FSI V6\n3.0 L Supercharged V6\n2.0 L I4 Diesel\n3.0 L V6 Diesel\nTransmission:\n6-speed manual\n8-speed Tiptronic ZF 8HP automatic\nMultitronic CVT\n7-speed S Tronic DCT\nDimensions\nWheelbase:\n2,912 mm (114.6 in)\n3,008 mm (118.4 in) (LWB)\nLength: 4,933 mm (194.2 in)\nWidth: 1,874 mm (73.8 in)\nHeight: 1,455 mm (57.3 in)\nCurb weight: 3,726–4,178 lb (1,690.1–1,895.1 kg)'
        bot.send_photo(call.message.chat.id, audiasixcsevenphoto, caption = 'Audi A6 IV (C7)(2011-2014)– автомобиль E-класса, передний и полный привод. Механика, вариатор, робот и автомат. Бензиновые, дизельные и гибридные двигатели мощностью от 136 до 313 лошадиных сил.')
        bot.send_message(call.message.chat.id,text=cseventext, reply_markup=audicseven)
    if call.data == "a6c7plusgen":
        audiasixcsevenplusphoto = open ('D:/TelegramBots/Project photos/Audi A6 C7plus.jfif', 'rb')
        audicsevenplus = types.InlineKeyboardMarkup()
        csevenplus = types.InlineKeyboardButton("Auto.tu", url='https://auto.ru/moskovskaya_oblast/cars/audi/a6/20246005/all/')
        audicsevenplus.add(csevenplus)
        csevenplustext='Body and chassis\nBody style:\n4-door sedan\n5-door station wagon\nPlatform: Volkswagen Group MLB platform\nPowertrain\nEngine:\n1.8 L TFSI I4 (China)\n2.0 L TFSI I4\n2.5 L FSI V6 (China)\n2.8 L FSI V6\n3.0 L Supercharged V6\n2.0 L I4 Diesel\n3.0 L V6 Diesel\nTransmission:\n6-speed manual\n8-speed Tiptronic ZF 8HP automatic\nMultitronic CVT\n7-speed S Tronic DCT\nDimensions\nWheelbase:\n2,912 mm (114.6 in)\n3,008 mm (118.4 in) (LWB)\nLength: 4,933 mm (194.2 in)\nWidth: 1,874 mm (73.8 in)\nHeight: 1,455 mm (57.3 in)\nCurb weight: 3,726–4,178 lb (1,690.1–1,895.1 kg)'
        bot.send_photo(call.message.chat.id, audiasixcsevenplusphoto, caption = 'Audi A6 IV Рестайлинг (C7)(2014-2018)– автомобиль E-класса, передний и полный привод. Механика, вариатор, робот и автомат. Бензиновые, дизельные и гибридные двигатели мощностью от 159 до 333 лошадиных сил.')
        bot.send_message(call.message.chat.id,text=csevenplustext, reply_markup=audicsevenplus)
    if call.data == "a6c8gen":
        audiasixceightphoto = open ('D:/TelegramBots/Project photos/Audi A6 C8.jfif', 'rb')
        audiceight = types.InlineKeyboardMarkup()
        ceight = types.InlineKeyboardButton("Auto.tu", url='https://auto.ru/moskovskaya_oblast/cars/audi/a6/21210593/all/')
        audiceight.add(ceight)
        ceighttext='Body and chassis\nPlatform: Volkswagen Group MLB Evo platform\nPowertrain\nEngine\nPetrol:\n2.0 litre I4 TFSI 185 kW\n2.0 litre I4 TFSI 190 PS Mild Hybrid (MHEV)\n3.0 litre Twin-scroll T V6 TFSI 250 kW\n2.9 litre TT V6 TFSI 336 kW (S6)\n4.0 litre TT V8 TFSI 441 kW (RS6)\nDiesel:\n2.0 litre I4 TDI 150kW\n3.0 litre V6 TDI 172 & 210 kW Mild Hybrid (MHEV; 45 & 50 TDI)\nPHEV engine:\n2.0 litre I4 TFSI 185 kW with an electric motor (A6 50 TFSI e quattro/ A6 55 TFSI e quattro)\nElectric motor:\n48V mild-hybrid system (MHEV)\nAC synchronous electric motor (50 / 55 TFSIe)\nTransmission:\n7-speed dual clutch S tronic\n8-speed automatic tiptronic\nHybrid drivetrain:\nMHEV (55 TFSI / S6 TFSI / RS6 TFSI / 45 TDI / 50 TDI)\nPHEV (55 TFSI e)\nDimensions\nWheelbase:\n2,924 mm (115.1 in)\n3,024 mm (119.1 in) (LWB)\nLength:\n4,939 mm (194.4 i\n5,050 mm (198.8 in) (LWB)\nWidth: 1,886 mm (74.3 in)\nHeight:\n1,457 mm (57.4 in)\nAvant: 1,467 mm (57.8 in)'
        bot.send_photo(call.message.chat.id, audiasixceightphoto, caption = 'Audi A6 V (C8)(2018-н.в.) – универсал 5 дв. E-класса, передний и полный привод. Робот и автомат. Дизельные, бензиновые и гибридные двигатели мощностью от 163 до 367 лошадиных сил.')
        bot.send_message(call.message.chat.id,text=ceighttext, reply_markup=audiceight)             
    if call.data == "a8gen":
        aeightkeyboard = types.InlineKeyboardMarkup()
        key_a8d2 = types.InlineKeyboardButton(text='I (D2)(1994-1999)', callback_data='a8d2gen')
        aeightkeyboard.add(key_a8d2)
        key_a8d2plus = types.InlineKeyboardButton(text='I Рестайлинг (D2)(1999-2002)', callback_data='a8d2plusgen')
        aeightkeyboard.add(key_a8d2plus)
        key_a8d3 = types.InlineKeyboardButton(text='II (D3)(2002-2005)', callback_data='a8d3gen')
        aeightkeyboard.add(key_a8d3)
        key_a8d3plus = types.InlineKeyboardButton(text='II Рестайлинг (D3)(2005-2007)', callback_data='a8d3plusgen')
        aeightkeyboard.add(key_a8d3plus)
        key_a8d3plustwo = types.InlineKeyboardButton(text='II Рестайлинг 2 (D3)(2007-2010)', callback_data='a8d3plustwogen')
        aeightkeyboard.add(key_a8d3plustwo)
        key_a8d4 = types.InlineKeyboardButton(text='III (D4)(2009-2014)', callback_data='a8d4gen')
        aeightkeyboard.add(key_a8d4)
        key_a8d4plus = types.InlineKeyboardButton(text='III Рестайлинг (D4)(2013-2017)', callback_data='a8d4plusgen')
        aeightkeyboard.add(key_a8d4plus)
        key_a8d5 = types.InlineKeyboardButton(text='IV (D4)(2017-2022)', callback_data='a8d5gen')
        aeightkeyboard.add(key_a8d5)
        key_a8d5plus = types.InlineKeyboardButton(text='IV Рестайлинг (D4)(2021-н.в.)', callback_data='a8d5plusgen')
        aeightkeyboard.add(key_a8d5plus)
        bot.send_message(call.message.chat.id, text='Выберите поколение',reply_markup=aeightkeyboard)
    if call.data == "a8d2gen":
        audiaeightdtwophoto = open ('D:/TelegramBots/Project photos/Audi A8 D2.jfif', 'rb')
        audidtwo = types.InlineKeyboardMarkup()
        dtwo = types.InlineKeyboardButton("Auto.tu", url='https://auto.ru/moskva/cars/audi/a8/6015759/all/')
        audidtwo.add(dtwo)
        dtwotext='Powertrain\nEngine\nPetrol engines:\n2.8 L AAH SOHC V6\n2.8 L ALG/AMX 30v V6\n3.7 L AEW V8\n4.2 L ABZ/AHC V8\n6.0 L W12\nDiesel engines:\n2.5 L TDI V6\n3.3 L TDI V8\nTransmission	\nManual transmission:\n5-speed manual\n6-speed manual (S8)\nAutomatic transmission:\n4-speed ZF 4HP24 automatic\n5-speed ZF 5HP19 automatic\n5-speed ZF 5HP24 automatic\nDimensions\nWheelbase:\nSWB: 2,882 mm (113.5 in)\nLWB: 3,010 mm (118.5 in)\nLength:\nSWB: 5,034 mm (198.2 in)\nLWB: 5,164 mm (203.3 in)\nWidth: 1,880 mm (74.0 in)\nHeight: 1,438 mm (56.6 in)\nKerb weight:\n2.5: 1,630 kg (3,590 lb) (TDI)\n2.5: 1,735 kg (3,825 lb) (TDI AWD)\n3.3: 1,860 kg (4,100 lb) (TDI AWD)\n2.8: 1,540 kg (3,400 lb)\n3.7: 1,645 kg (3,627 lb)\n3.7: 1,725 kg (3,803 lb) (AWD)\n4.2: 1,750 kg (3,860 lb) (AWD)\n4.2: 1,845 kg (4,068 lb) (US)\n4.2: 1,790 kg (3,950 lb) (AWD A8L)\n4.2: 1,885 kg (4,156 lb) (US)\n6.0: 1,950 kg (4,300 lb)\n6.0: 1,980 kg (4,370 lb) (AWD A8L)\nS8: 1,730 kg (3,810 lb\nS8: 1,845 kg (4,068 lb) (US)'
        bot.send_photo(call.message.chat.id, audiaeightdtwophoto, caption = 'Audi A8 I (D2)(1994-1999) – седан F-класса, передний и полный привод. Механика и автомат. Дизельные и бензиновые двигатели мощностью от 150 до 300 лошадиных сил.')
        bot.send_message(call.message.chat.id,text=dtwotext, reply_markup=audidtwo)
    if call.data == "a8d2plusgen":
        audiaeightdtwoplusphoto = open ('D:/TelegramBots/Project photos/Audi A8 D2plus.jfif', 'rb')
        audidtwoplus = types.InlineKeyboardMarkup()
        dtwoplus = types.InlineKeyboardButton("Auto.tu", url='https://auto.ru/moskva/cars/audi/a8/4927429/all/')
        audidtwoplus.add(dtwoplus)
        dtwoplustext='Powertrain\nEngine\nPetrol engines:\n2.8 L AAH SOHC V6\n2.8 L ALG/AMX 30v V6\n3.7 L AEW V8\n4.2 L ABZ/AHC V8\n6.0 L W12\nDiesel engines:\n2.5 L TDI V6\n3.3 L TDI V8\nTransmission	\nManual transmission:\n5-speed manual\n6-speed manual (S8)\nAutomatic transmission:\n4-speed ZF 4HP24 automatic\n5-speed ZF 5HP19 automatic\n5-speed ZF 5HP24 automatic\nDimensions\nWheelbase:\nSWB: 2,882 mm (113.5 in)\nLWB: 3,010 mm (118.5 in)\nLength:\nSWB: 5,034 mm (198.2 in)\nLWB: 5,164 mm (203.3 in)\nWidth: 1,880 mm (74.0 in)\nHeight: 1,438 mm (56.6 in)\nKerb weight:\n2.5: 1,630 kg (3,590 lb) (TDI)\n2.5: 1,735 kg (3,825 lb) (TDI AWD)\n3.3: 1,860 kg (4,100 lb) (TDI AWD)\n2.8: 1,540 kg (3,400 lb)\n3.7: 1,645 kg (3,627 lb)\n3.7: 1,725 kg (3,803 lb) (AWD)\n4.2: 1,750 kg (3,860 lb) (AWD)\n4.2: 1,845 kg (4,068 lb) (US)\n4.2: 1,790 kg (3,950 lb) (AWD A8L)\n4.2: 1,885 kg (4,156 lb) (US)\n6.0: 1,950 kg (4,300 lb)\n6.0: 1,980 kg (4,370 lb) (AWD A8L)\nS8: 1,730 kg (3,810 lb\nS8: 1,845 kg (4,068 lb) (US)'
        bot.send_photo(call.message.chat.id, audiaeightdtwoplusphoto, caption = 'Audi A8 I Рестайлинг (D2)(1999-2002) – седан F-класса, передний и полный привод. Механика и автомат. Дизельные и бензиновые двигатели мощностью от 150 до 310 лошадиных сил.')
        bot.send_message(call.message.chat.id,text=dtwoplustext, reply_markup=audidtwoplus)
    if call.data == "a8d3gen":
        audiaeightdthreephoto = open ('D:/TelegramBots/Project photos/Audi A8 D3.jfif', 'rb')
        audidthree = types.InlineKeyboardMarkup()
        dthree = types.InlineKeyboardButton("Auto.tu", url='https://auto.ru/moskva/cars/audi/a8/4720908/all/')
        audidthree.add(dthree)
        dthreetext='Body and chassis\nPlatform: Volkswagen Group D3\nPowertrain\nEngine:\nV6 petrol engine:\n2.8 L V6\n3.0 L V6\n3.2 L V6 FSI\nV8 petrol engine:\n3.7 L V8\n4.2 L V8\nV10 petrol engine:\n5.2 L V10 FSI\nW12 engine:\n6.0 L W12\nV6 diesel engine:\n3.0 L V6 TDI\nV8 diesel engine:\n4.0 L V8 TDI\n4.1 L V8 TDI\nTransmission:	\nAutomatic transmission:\n6-speed ZF 6HP26 tiptronic automatic\nContinuously variable transmission:\nLuK multitronic CVT'
        bot.send_photo(call.message.chat.id, audiaeightdthreephoto, caption = 'Audi A8 II (D3)(2002-2005) – седан F-класса, полный и передний привод. Автомат и вариатор. Дизельные и бензиновые двигатели мощностью от 220 до 450 лошадиных сил.')
        bot.send_message(call.message.chat.id,text=dthreetext, reply_markup=audidthree)
    if call.data == "a8d3plusgen":
        audiaeightdthreeplusphoto = open ('D:/TelegramBots/Project photos/Audi A8 D3plus.jfif', 'rb')
        audidthreeplus = types.InlineKeyboardMarkup()
        dthreeplus = types.InlineKeyboardButton("Auto.tu", url='https://auto.ru/moskva/cars/audi/a8/4601131/all/')
        audidthreeplus.add(dthreeplus)
        dthreeplustext='Body and chassis\nPlatform: Volkswagen Group D3\nPowertrain\nEngine:\nV6 petrol engine:\n2.8 L V6\n3.0 L V6\n3.2 L V6 FSI\nV8 petrol engine:\n3.7 L V8\n4.2 L V8\nV10 petrol engine:\n5.2 L V10 FSI\nW12 engine:\n6.0 L W12\nV6 diesel engine:\n3.0 L V6 TDI\nV8 diesel engine:\n4.0 L V8 TDI\n4.1 L V8 TDI\nTransmission:	\nAutomatic transmission:\n6-speed ZF 6HP26 tiptronic automatic\nContinuously variable transmission:\nLuK multitronic CVT'
        bot.send_photo(call.message.chat.id, audiaeightdthreeplusphoto, caption = 'Audi A8 II Рестайлинг (D3)(2005-2007) – седан F-класса, полный и передний привод. Автомат и вариатор. Дизельные и бензиновые двигатели мощностью от 220 до 450 лошадиных сил.')
        bot.send_message(call.message.chat.id,text=dthreeplustext, reply_markup=audidthreeplus)
    if call.data == "a8d3plustwogen":
        audiaeightdthreeplustwophoto = open ('D:/TelegramBots/Project photos/Audi A8 D3plustwo.jfif', 'rb')
        audidthreeplustwo= types.InlineKeyboardMarkup()
        dthreeplustwo = types.InlineKeyboardButton("Auto.tu", url='https://auto.ru/moskva/cars/audi/a8/2305474/all/')
        audidthreeplustwo.add(dthreeplustwo)
        dthreeplustwotext='Body and chassis\nPlatform: Volkswagen Group D3\nPowertrain\nEngine:\nV6 petrol engine:\n2.8 L V6\n3.0 L V6\n3.2 L V6 FSI\nV8 petrol engine:\n3.7 L V8\n4.2 L V8\nV10 petrol engine:\n5.2 L V10 FSI\nW12 engine:\n6.0 L W12\nV6 diesel engine:\n3.0 L V6 TDI\nV8 diesel engine:\n4.0 L V8 TDI\n4.1 L V8 TDI\nTransmission:	\nAutomatic transmission:\n6-speed ZF 6HP26 tiptronic automatic\nContinuously variable transmission:\nLuK multitronic CVT'
        bot.send_photo(call.message.chat.id, audiaeightdthreeplustwophoto, caption = 'Audi A8 II Рестайлинг 2 (D3)(2007-2010) – седан F-класса, полный и передний привод. Автомат и вариатор. Дизельные и бензиновые двигатели мощностью от 210 до 450 лошадиных сил.')
        bot.send_message(call.message.chat.id,text=dthreeplustwotext, reply_markup=audidthreeplustwo)
    if call.data == "a8d4gen":
        audiaeightdfourphoto = open ('D:/TelegramBots/Project photos/Audi A8 D4.jfif', 'rb')
        audidfour = types.InlineKeyboardMarkup()
        dfour = types.InlineKeyboardButton("Auto.tu", url='https://auto.ru/moskva/cars/audi/a8/6155077/all/')
        audidfour.add(dfour)
        dfourtext='Body and chassis\nPlatform: Volkswagen MLB\nPowertrain\nEngine:\nInline-four petrol engine:\n2.0 I4 TFSI\n2.0 I4 TFSI Hybrid\nV6 petrol engine:\n2.5 V6 FSI (China)\n3.0 V6 TFSI\nV8 petrol engine:\n4.0 V8 TFSI\n4.2 V8 FSI\nW12 engine:\n6.3 W12 CEJA FSI\nV6 diesel engine:\n3.0 V6 TDI\nV8 diesel engine:\n4.2 V8 TDI\nElectric motor:\n54 PS (40 kW; 53 hp) Disc-shaped electric motor\nTransmission:	\nAutomatic transmission\nHybrid drivetrain:\nFHEV (A8 Hybrid)\nBattery: 1.3 kWh Li-ion\nDimensions\nWheelbase:\n2,992 mm (117.8 in)\n3,122 mm (122.9 in) (LWB)\nLength:\n5,131 mm (202.0 in)\n5,267 mm (207.4 in) (LWB)Width	1,948 mm (76.7 in)\nHeight:\n1,461 mm (57.5 in)\n1,471 mm (57.9 in) (LWB)\nKerb weight:\n1,977 kg (4,358.5 lb) A8L 3.0TL\n2,000 kg (4,409.2 lb) A8 4.2L\n2,020 kg (4,453.3 lb) A8 L 4.2L\n2,165 kg (4,773.0 lb) A8 L 6.3L'
        bot.send_photo(call.message.chat.id, audiaeightdfourphoto, caption = 'Audi A8 III (D4)(2009-2014) – седан F-класса, передний и полный привод. Автомат. Гибридные, дизельные и бензиновые двигатели мощностью от 204 до 420 лошадиных сил.')
        bot.send_message(call.message.chat.id,text=dfourtext, reply_markup=audidfour)
    if call.data == "a8d4plusgen":
        audiaeightdfourplusphoto = open ('D:/TelegramBots/Project photos/Audi A8 D4plus.jfif', 'rb')
        audidfourplus = types.InlineKeyboardMarkup()
        dfourplus = types.InlineKeyboardButton("Auto.tu", url='https://auto.ru/moskva/cars/audi/a8/20071435/all/')
        audidfourplus.add(dfourplus)
        dfourplustext='Body and chassis\nPlatform: Volkswagen MLB\nPowertrain\nEngine:\nInline-four petrol engine:\n2.0 I4 TFSI\n2.0 I4 TFSI Hybrid\nV6 petrol engine:\n2.5 V6 FSI (China)\n3.0 V6 TFSI\nV8 petrol engine:\n4.0 V8 TFSI\n4.2 V8 FSI\nW12 engine:\n6.3 W12 CEJA FSI\nV6 diesel engine:\n3.0 V6 TDI\nV8 diesel engine:\n4.2 V8 TDI\nElectric motor:\n54 PS (40 kW; 53 hp) Disc-shaped electric motor\nTransmission:	\nAutomatic transmission\nHybrid drivetrain:\nFHEV (A8 Hybrid)\nBattery: 1.3 kWh Li-ion\nDimensions\nWheelbase:\n2,992 mm (117.8 in)\n3,122 mm (122.9 in) (LWB)\nLength:\n5,131 mm (202.0 in)\n5,267 mm (207.4 in) (LWB)Width	1,948 mm (76.7 in)\nHeight:\n1,461 mm (57.5 in)\n1,471 mm (57.9 in) (LWB)\nKerb weight:\n1,977 kg (4,358.5 lb) A8L 3.0TL\n2,000 kg (4,409.2 lb) A8 4.2L\n2,020 kg (4,453.3 lb) A8 L 4.2L\n2,165 kg (4,773.0 lb) A8 L 6.3L'
        bot.send_photo(call.message.chat.id, audiaeightdfourplusphoto, caption = 'Audi A8 III Рестайлинг (D4)(2013-2017) – седан F-класса, передний и полный привод. Автомат. Гибридные, дизельные и бензиновые двигатели мощностью от 245 до 435 лошадиных сил.')
        bot.send_message(call.message.chat.id,text=dfourplustext, reply_markup=audidfourplus)
    if call.data == "a8d5gen":
        audiaeightdfivephoto = open ('D:/TelegramBots/Project photos/Audi A8 D5.jfif', 'rb')
        audidfive = types.InlineKeyboardMarkup()
        dfive = types.InlineKeyboardButton("Auto.tu", url='https://auto.ru/moskva/cars/audi/a8/21040120/all/')
        audidfive.add(dfive)
        dfivetext='Body and chassis\nPlatform: MLB Evo\nPowertrain\nEngine:\nPetrol engines:\n3.0 L biturbo FSI V6\n3.0 L biturbo FSI V6 MHEV\n3.0 L biturbo FSI V6 PHEV\n4.0 L biturbo FSI V8 MHEV\nDiesel engines:\n3.0 L biturbo V6\n4.0 L biturbo V8\nElectric motor:\n48-volt system Belt alternator starter (BAS): MHEV\n108 hp (81 kW; 109 PS) AC induction motor: PHEV\nTransmission:\n8-speed Tiptronic automatic\n8 Speed Plug-In Hybrid ZF 8HP90 Tiptronic automatic\nHybrid drivetrain:\nMHEV (60 TFSI / S8 TFSI)\nPHEV (60 TFSI e)\nBattery: 14.1 kWh lithium-ion (PHEV)\nElectric range: 17 mi (27 km) (60 TFSI e)\nDimensions:\nWheelbase:\n2,998 mm (118.0 in)\n3,128 mm (123.1 in) (LWB)\n3,258 mm (128.3 in) (Horch)\nLength:\n5,172 mm (203.6 in)\n5,302 mm (208.7 in) (LWB)\n5,422 mm (213.5 in) (Horch)\nWidth: 1,945 mm (76.6 in)\nHeight: 1,485 mm (58.5 in)'
        bot.send_photo(call.message.chat.id, audiaeightdfivephoto, caption = 'Audi A8 IV (D5)(2017-2022) – седан F-класса, полный привод. Автомат. Дизельные, бензиновые и гибридные двигатели мощностью от 249 до 460 лошадиных сил.')
        bot.send_message(call.message.chat.id,text=dfivetext, reply_markup=audidfive)
    if call.data == "a8d5plusgen":
        audiaeightdfiveplusphoto = open ('D:/TelegramBots/Project photos/Audi A8 D5plus.jfif', 'rb')
        audidfiveplus = types.InlineKeyboardMarkup()
        dfiveplus = types.InlineKeyboardButton("Auto.tu", url='https://auto.ru/moskva/cars/audi/a8/23141438/all/')
        audidfiveplus.add(dfiveplus)
        dfiveplustext='Body and chassis\nPlatform: MLB Evo\nPowertrain\nEngine:\nPetrol engines:\n3.0 L biturbo FSI V6\n3.0 L biturbo FSI V6 MHEV\n3.0 L biturbo FSI V6 PHEV\n4.0 L biturbo FSI V8 MHEV\nDiesel engines:\n3.0 L biturbo V6\n4.0 L biturbo V8\nElectric motor:\n48-volt system Belt alternator starter (BAS): MHEV\n108 hp (81 kW; 109 PS) AC induction motor: PHEV\nTransmission:\n8-speed Tiptronic automatic\n8 Speed Plug-In Hybrid ZF 8HP90 Tiptronic automatic\nHybrid drivetrain:\nMHEV (60 TFSI / S8 TFSI)\nPHEV (60 TFSI e)\nBattery: 14.1 kWh lithium-ion (PHEV)\nElectric range: 17 mi (27 km) (60 TFSI e)\nDimensions:\nWheelbase:\n2,998 mm (118.0 in)\n3,128 mm (123.1 in) (LWB)\n3,258 mm (128.3 in) (Horch)\nLength:\n5,172 mm (203.6 in)\n5,302 mm (208.7 in) (LWB)\n5,422 mm (213.5 in) (Horch)\nWidth: 1,945 mm (76.6 in)\nHeight: 1,485 mm (58.5 in)'
        bot.send_photo(call.message.chat.id, audiaeightdfiveplusphoto, caption = 'Audi A8 IV Рестайлинг (D5)(2022-н.в. – седан F-класса, полный привод. Автомат. Бензиновые, дизельные и гибридные двигатели мощностью от 286 до 462 лошадиных сил.')
        bot.send_message(call.message.chat.id,text=dfiveplustext, reply_markup=audidfiveplus)
bot.polling(none_stop=True, interval=0)
