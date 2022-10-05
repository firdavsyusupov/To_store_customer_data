from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

add_klient_base = KeyboardButton('Клиент кошиш')
remove_klient_base = KeyboardButton("Клиент очириш")
info_klient_base = KeyboardButton("Клиент хакида малумот")
location_klient_base = KeyboardButton("Турган жойингизни локатсиясини критинг")
remake_klient_base = KeyboardButton("Клиент малумотини озгартириш")

add_viloyat_1 = InlineKeyboardButton("Qoraqalpogʻiston Respublikasi", callback_data= "av_1")
add_viloyat_2 = InlineKeyboardButton("Buxoro viloyati",callback_data= "av_2")
add_viloyat_3 = InlineKeyboardButton("Fargʻona  viloyati",callback_data= "av_3")
add_viloyat_4 = InlineKeyboardButton("Jizzax viloyati",callback_data= "av_4")
add_viloyat_5 = InlineKeyboardButton("Xorazm viloyati",callback_data= "av_5")
add_viloyat_6 = InlineKeyboardButton("Namangan viloyati",callback_data= "av_6")
add_viloyat_7 = InlineKeyboardButton("Navoiy viloyati",callback_data= "av_7")
add_viloyat_8 = InlineKeyboardButton("Qashqadaryo viloyati",callback_data= "av_8")
add_viloyat_9 = InlineKeyboardButton("Andijon viloyati",callback_data= "av_9")
add_viloyat_10 = InlineKeyboardButton("Samarqand viloyati",callback_data= "av_10")
add_viloyat_11= InlineKeyboardButton("Sirdaryo viloyati",callback_data= "av_11")
add_viloyat_12= InlineKeyboardButton("Surxondaryo viloyati",callback_data= "av_12")
back = InlineKeyboardButton('Back', callback_data='back')
markup = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton("Lokatsiya", request_location=True))
########################################## REPLY ##############################################
main_menu = ReplyKeyboardMarkup(resize_keyboard= True)
main_menu.add(add_klient_base)
main_menu.add(remove_klient_base)
main_menu.add(info_klient_base)
main_menu.add(location_klient_base)
main_menu.add(remake_klient_base)

add_malumot = InlineKeyboardMarkup(row_width = 2)
add_malumot.insert(add_viloyat_1)
add_malumot.insert(add_viloyat_2)
add_malumot.insert(add_viloyat_3)
add_malumot.insert(add_viloyat_4)
add_malumot.insert(add_viloyat_5)
add_malumot.insert(add_viloyat_6)
add_malumot.insert(add_viloyat_7)
add_malumot.insert(add_viloyat_8)
add_malumot.insert(add_viloyat_9)
add_malumot.insert(add_viloyat_10)
add_malumot.insert(add_viloyat_11)
add_malumot.insert(add_viloyat_12)
add_malumot.insert(back)


remove_malumot = InlineKeyboardMarkup(row_width = 2)
remove_malumot.insert(add_viloyat_1)
remove_malumot.insert(add_viloyat_2)
remove_malumot.insert(add_viloyat_3)
remove_malumot.insert(add_viloyat_4)
remove_malumot.insert(add_viloyat_5)
remove_malumot.insert(add_viloyat_6)
remove_malumot.insert(add_viloyat_7)
remove_malumot.insert(add_viloyat_8)
remove_malumot.insert(add_viloyat_9)
remove_malumot.insert(add_viloyat_10)
remove_malumot.insert(add_viloyat_11)
remove_malumot.insert(add_viloyat_12)
remove_malumot.insert(back)



info_malumot = InlineKeyboardMarkup(row_width = 2)
info_malumot.insert(add_viloyat_1)
info_malumot.insert(add_viloyat_2)
info_malumot.insert(add_viloyat_3)
info_malumot.insert(add_viloyat_4)
info_malumot.insert(add_viloyat_5)
info_malumot.insert(add_viloyat_6)
info_malumot.insert(add_viloyat_7)
info_malumot.insert(add_viloyat_8)
info_malumot.insert(add_viloyat_9)
info_malumot.insert(add_viloyat_10)
info_malumot.insert(add_viloyat_11)
info_malumot.insert(add_viloyat_12)
info_malumot.insert(back)


remake_malumot = InlineKeyboardMarkup(row_width = 2)
remake_malumot.insert(add_viloyat_1)
remake_malumot.insert(add_viloyat_2)
remake_malumot.insert(add_viloyat_3)
remake_malumot.insert(add_viloyat_4)
remake_malumot.insert(add_viloyat_5)
remake_malumot.insert(add_viloyat_6)
remake_malumot.insert(add_viloyat_7)
remake_malumot.insert(add_viloyat_8)
remake_malumot.insert(add_viloyat_9)
remake_malumot.insert(add_viloyat_10)
remake_malumot.insert(add_viloyat_11)
remake_malumot.insert(add_viloyat_12)
remake_malumot.insert(back)










