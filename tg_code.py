from aiogram.types import Location

from sql_query import Database
# from main import Registration
from aiogram import Bot, Dispatcher, executor, types
import logging
import markups as mr

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext


<<<<<<< HEAD
API_TOKEN = '5500425634:AAHqo9K3FeFgRg25UFytX_oszZbscJ_e6j4'   # AbuBakr
# API_TOKEN = '5366807852:AAERuJaIYQcn5RbsX1kNEKHOLgrouupjh3w'     # Islom
# logging.basicConfig(level=logging.INFO)
=======
# API_TOKEN = '5537289338:AAEwSGOvbS8XlA98MYG1TX87gqT-EkKOVjk'   # AbuBakr
# API_TOKEN = '5366807852:AAERuJaIYQcn5RbsX1kNEKHOLgrouupjh3w'     # Islom
API_TOKEN = "5111585539:AAGcIPBKJiTM6DKbyhRbfjdLMDPVQOXesng"    # Islom kril-lotin

logging.basicConfig(level=logging.INFO)
>>>>>>> 2364c4fcf5b5cb93c486646a5c793035d9ce0118

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot)

db = Database('client.db')

# Initialize bot and dispatcher


@dp.message_handler(commands=['start'])
async def register(message: types.Message ):
    # await message.answer(f'Admin Panelga Xush kelibsiz!')
<<<<<<< HEAD
    await bot.send_message(message.from_user.id, "Aссалому алеком\n Озингизга керакли болимни танланг",reply_markup=mr.markup)


@dp.message_handler(content_types='location')
async def file_1(msg: types.Message):
=======
    await bot.send_message(message.from_user.id, "Aссалому алеком\n Озингизга керакли болимни танланг",reply_markup=mr.location)


@dp.message_handler(content_types=['location'])
async def handle_location(message: types.Message):
    lat = message.location.latitude
    lon = message.location.longitude
    reply = "latitude:  {}\nlongitude: {}".format(lat, lon)
    await message.answer(reply, reply_markup=types.ReplyKeyboardRemove())
    print("latitude:", lat)
    print("longitude:", lon)
>>>>>>> 2364c4fcf5b5cb93c486646a5c793035d9ce0118

    lokatsiya = msg.location
    print(lokatsiya.longitude, lokatsiya.latitude)
@dp.callback_query_handler(text='back')
async def back(message: types.CallbackQuery):
    await bot.send_message(message.from_user.id, "Aссалому алеком\n Озингизга керакли болимни танланг",
                           reply_markup=mr.main_menu)
    """
#     This handler will be called when user sends `/start` or `/help` command
#     """
############################## KLIENT QO'SHISH ###############################################


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

        if message.location:
            print(message.location)







    # await state.update_data(season=answer)
    # await bot.send_message(message.from_user.id, "Qaysi xonada otirasiz?")
    # await Registration.stay.set()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)