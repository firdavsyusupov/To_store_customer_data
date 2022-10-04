import logging

from sql_query import Database
# from main import Registration
from aiogram import Bot, Dispatcher, executor, types
import logging
import markups as mr

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext


# API_TOKEN = '5537289338:AAEwSGOvbS8XlA98MYG1TX87gqT-EkKOVjk'   # AbuBakr
# API_TOKEN = '5366807852:AAERuJaIYQcn5RbsX1kNEKHOLgrouupjh3w'     # Islom
API_TOKEN = "5111585539:AAGcIPBKJiTM6DKbyhRbfjdLMDPVQOXesng"    # Islom kril-lotin

logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot)

db = Database('client.db')

# Initialize bot and dispatcher


@dp.message_handler(commands=['start'])
async def register(message: types.Message):
    # await message.answer(f'Admin Panelga Xush kelibsiz!')
    await bot.send_message(message.from_user.id, "Aссалому алеком\n Озингизга керакли болимни танланг",reply_markup=mr.location)


@dp.message_handler(content_types=['location'])
async def handle_location(message: types.Message):
    lat = message.location.latitude
    lon = message.location.longitude
    reply = "latitude:  {}\nlongitude: {}".format(lat, lon)
    await message.answer(reply, reply_markup=types.ReplyKeyboardRemove())
    print(lat)
    print(lon)
@dp.callback_query_handler(text='back')
async def back(message: types.CallbackQuery):
    await bot.send_message(message.from_user.id, "Aссалому алеком\n Озингизга керакли болимни танланг",
                           reply_markup=mr.main_menu)
    """
#     This handler will be called when user sends `/start` or `/help` command
#     """
# @dp.message_handler(state=Registration.name)
# async def village_name(message: types.Message, state: FSMContext):
#     answer = message.text
#
#     await state.update_data(name=answer)
#     await bot.send_message(message.from_user.id, "Докон эгасини отини киритинг!")
#     await Registration.market.set()
#
# @dp.message_handler(state=Registration.market)
# async def owner_name(message: types.Message, state: FSMContext):
#     answer = message.text.lower()
#
#     await state.update_data(qwasar_user=answer)
#     await bot.send_message(message.from_user.id, "Телефон номерни йозинг!")
#     await Registration.phone.set()
#
# @dp.message_handler(state=Registration.phone)
# async def owner_phone(message: types.Message, state: FSMContext):
#     answer = message.text
#
#     await state.update_data(phone=answer)
#     await bot.send_message(message.from_user.id, "Доконнинг локациясини ташланг!")
#     await Registration.location.set()
############################## KLIENT QO'SHISH ###############################################

# @dp.message_handler(state=Registration.location)
# async def state_season(message: types.Message, state: FSMContext):
#     answer = message.text

@dp.message_handler(content_types=['text'])
async def other_message(message: types.Message):
    if message.chat.type == 'private':
        if message.text == 'Клиент кошиш':
            await bot.send_message(message.from_user.id, 'Bosh Menu 🗃', reply_markup=types.ReplyKeyboardRemove())
            await bot.send_message(message.from_user.id, "Вилоятни танланг",reply_markup=mr.add_malumot)
        if message.text == 'Клиент очириш':
            await bot.send_message(message.from_user.id, 'Bosh Menu 🗃', reply_markup=types.ReplyKeyboardRemove())
            await bot.send_message(message.from_user.id, "Вилоятни танланг",reply_markup=mr.remove_malumot)
        if message.text == 'Клиент хакида малумот':
            await bot.send_message(message.from_user.id, 'Bosh Menu 🗃', reply_markup=types.ReplyKeyboardRemove())
            await bot.send_message(message.from_user.id, "Вилоятни танланг",reply_markup=mr.info_malumot)
        # if message.text == 'Турган жойингизни локатсиясини критинг':
        #     await bot.send_message(message.from_user.id, "Вилоятни танланг",reply_markup=mr.info_malumot)
        if message.text == 'Клиент малумотини озгартириш':
            await bot.send_message(message.from_user.id, 'Bosh Menu 🗃', reply_markup=types.ReplyKeyboardRemove())
            await bot.send_message(message.from_user.id, "Вилоятни танланг",reply_markup=mr.remake_malumot)







    # await state.update_data(season=answer)
    # await bot.send_message(message.from_user.id, "Qaysi xonada otirasiz?")
    # await Registration.stay.set()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)