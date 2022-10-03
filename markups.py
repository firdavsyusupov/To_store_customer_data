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


remove_1_viloyat = InlineKeyboardButton("Qoraqalpogʻiston Respublikasi",callback_data= "rv_1")
remove_2_viloyat = InlineKeyboardButton("Buxoro viloyati",callback_data= "rv_2")
remove_3_viloyat = InlineKeyboardButton("Fargʻona  viloyati",callback_data= "rv_3")
remove_4_viloyat = InlineKeyboardButton("Jizzax viloyati",callback_data= "rv_4")
remove_5_viloyat = InlineKeyboardButton("Xorazm viloyati",callback_data= "rv_5")
remove_6_viloyat = InlineKeyboardButton("Namangan viloyati",callback_data= "rv_6")
remove_7_viloyat = InlineKeyboardButton("Navoiy viloyati",callback_data= "rv_7")
remove_8_viloyat = InlineKeyboardButton("Qashqadaryo viloyati",callback_data= "rv_8")
remove_9_viloyat = InlineKeyboardButton("Andijon viloyati",callback_data= "rv_9")
remove_10_viloyat = InlineKeyboardButton("Samarqand viloyati",callback_data= "rv_10")
remove_11_viloyat= InlineKeyboardButton("Sirdaryo viloyati",callback_data= "rv_11")
remove_12_viloyat= InlineKeyboardButton("Surxondaryo viloyati",callback_data= "rv_12")


info_1_viloyat = InlineKeyboardButton("Qoraqalpogʻiston Respublikasi",callback_data= "1v_1")
info_2_viloyat = InlineKeyboardButton("Buxoro viloyati",callback_data= "1v_2")
info_3_viloyat = InlineKeyboardButton("Fargʻona  viloyati",callback_data= "1v_3")
info_4_viloyat = InlineKeyboardButton("Jizzax viloyati",callback_data= "1v_4")
info_5_viloyat = InlineKeyboardButton("Xorazm viloyati",callback_data= "1v_5")
info_6_viloyat = InlineKeyboardButton("Namangan viloyati",callback_data= "1v_6")
info_7_viloyat = InlineKeyboardButton("Navoiy viloyati",callback_data= "1v_7")
info_8_viloyat = InlineKeyboardButton("Qashqadaryo viloyati",callback_data= "1v_8")
info_9_viloyat = InlineKeyboardButton("Andijon viloyati",callback_data= "1v_9")
info_10_viloyat = InlineKeyboardButton("Samarqand viloyati",callback_data= "1v_10")
info_11_viloyat= InlineKeyboardButton("Sirdaryo viloyati",callback_data= "1v_11")
info_12_viloyat= InlineKeyboardButton("Surxondaryo viloyati",callback_data= "1v_12")


remake_1_viloyat = InlineKeyboardButton("Qoraqalpogʻiston Respublikasi",callback_data= "rev_1")
remake_2_viloyat = InlineKeyboardButton("Buxoro viloyati",callback_data= "rev_2")
remake_3_viloyat = InlineKeyboardButton("Fargʻona  viloyati",callback_data= "rev_3")
remake_4_viloyat = InlineKeyboardButton("Jizzax viloyati",callback_data= "rev_4")
remake_5_viloyat = InlineKeyboardButton("Xorazm viloyati",callback_data= "rev_5")
remake_6_viloyat = InlineKeyboardButton("Namangan viloyati",callback_data= "rev_6")
remake_7_viloyat = InlineKeyboardButton("Navoiy viloyati",callback_data= "rev_7")
remake_8_viloyat = InlineKeyboardButton("Qashqadaryo viloyati",callback_data= "rev_8")
remake_9_viloyat = InlineKeyboardButton("Andijon viloyati",callback_data= "rev_9")
remake_10_viloyat = InlineKeyboardButton("Samarqand viloyati",callback_data= "rev_10")
remake_11_viloyat= InlineKeyboardButton("Sirdaryo viloyati",callback_data= "rev_11")
remake_12_viloyat= InlineKeyboardButton("Surxondaryo viloyati",callback_data= "rev_12")

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
remove_malumot.insert(remove_1_viloyat)
remove_malumot.insert(remove_2_viloyat)
remove_malumot.insert(remove_3_viloyat)
remove_malumot.insert(remove_4_viloyat)
remove_malumot.insert(remove_5_viloyat)
remove_malumot.insert(remove_6_viloyat)
remove_malumot.insert(remove_7_viloyat)
remove_malumot.insert(remove_8_viloyat)
remove_malumot.insert(remove_9_viloyat)
remove_malumot.insert(remove_10_viloyat)
remove_malumot.insert(remove_11_viloyat)
remove_malumot.insert(remove_12_viloyat)
remove_malumot.insert(back)



info_malumot = InlineKeyboardMarkup(row_width = 2)
info_malumot.insert(info_1_viloyat)
info_malumot.insert(info_2_viloyat)
info_malumot.insert(info_3_viloyat)
info_malumot.insert(info_4_viloyat)
info_malumot.insert(info_5_viloyat)
info_malumot.insert(info_6_viloyat)
info_malumot.insert(info_7_viloyat)
info_malumot.insert(info_8_viloyat)
info_malumot.insert(info_9_viloyat)
info_malumot.insert(info_10_viloyat)
info_malumot.insert(info_11_viloyat)
info_malumot.insert(info_12_viloyat)
info_malumot.insert(back)


remake_malumot = InlineKeyboardMarkup(row_width = 2)
remake_malumot.insert(remake_1_viloyat)
remake_malumot.insert(remake_2_viloyat)
remake_malumot.insert(remake_4_viloyat)
remake_malumot.insert(remake_5_viloyat)
remake_malumot.insert(remake_6_viloyat)
remake_malumot.insert(remake_7_viloyat)
remake_malumot.insert(remake_8_viloyat)
remake_malumot.insert(remake_9_viloyat)
remake_malumot.insert(remake_10_viloyat)
remake_malumot.insert(remake_11_viloyat)
remake_malumot.insert(remake_12_viloyat)
remake_malumot.insert(back)










