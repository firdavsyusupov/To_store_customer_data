<<<<<<< HEAD
# import logging
# from sql_query import Database
# # from main import Registration
# from aiogram import Bot, Dispatcher, executor, types
# import logging
# import markups as mr
# from aiogram.contrib.fsm_storage.memory import MemoryStorage
# from aiogram.dispatcher import FSMContext
# from aiogram.dispatcher.filters import Text
# from aiogram.dispatcher.filters.state import State, StatesGroup
# from aiogram.contrib.fsm_storage.memory import MemoryStorage
#
#
# # API_TOKEN = '5537289338:AAEwSGOvbS8XlA98MYG1TX87gqT-EkKOVjk'   # AbuBakr
# API_TOKEN = '5366807852:AAERuJaIYQcn5RbsX1kNEKHOLgrouupjh3w'     # Islom
# logging.basicConfig(level=logging.INFO)
#
# # Initialize bot and dispatcher
# bot = Bot(token=API_TOKEN)
# storage = MemoryStorage()
# dp = Dispatcher(bot)

# from sql_query import Database
# db = Database('client.db')
#
#
#
#
# # Initialize bot and dispatcher
# @dp.message_handler(commands=['start'])
# async def register(message: types.Message):
#     # await message.answer(f'Admin Panelga Xush kelibsiz!')
#     await bot.send_message(message.from_user.id, "Aссалому алеком\n Озингизга керакли болимни танланг",reply_markup=mr.main_menu)
#
#
# @dp.callback_query_handler(text='back')
# async def back(message: types.CallbackQuery):
#     await bot.send_message(message.from_user.id, "Aссалому алеком\n Озингизга керакли болимни танланг",
#                            reply_markup=mr.main_menu)
#     """
# #     This handler will be called when user sends `/start` or `/help` command
# #     """
# # @dp.message_handler(state=Registration.viloyat)
# # async def village_viloyat(message: types.Message, state: FSMContext):
# #     answer = message.text
# #
# #     await state.update_data(viloyat=answer)
# #     await bot.send_message(message.from_user.id, "Докон эгасини отини киритинг!")
# #     await Registration.market.set()
# #
# # @dp.message_handler(state=Registration.market)
# # async def owner_viloyat(message: types.Message, state: FSMContext):
# #     answer = message.text.lower()
# #
# #     await state.update_data(qwasar_user=answer)
# #     await bot.send_message(message.from_user.id, "Телефон номерни йозинг!")
# #     await Registration.phone.set()
# #
# # @dp.message_handler(state=Registration.phone)
# # async def owner_phone(message: types.Message, state: FSMContext):
# #     answer = message.text
# #
# #     await state.update_data(phone=answer)
# #     await bot.send_message(message.from_user.id, "Доконнинг локациясини ташланг!")
# #     await Registration.location.set()
# ############################## KLIENT QO'SHISH ###############################################
#
# # @dp.message_handler(state=Registration.location)
# # async def state_season(message: types.Message, state: FSMContext):
# #     answer = message.text
#
#
# @dp.message_handler(content_types=['text'])
# async def other_message(message: types.Message):
#     if message.chat.type == 'private':
#         if message.text == 'Клиент кошиш':
#             await bot.send_message(message.from_user.id, 'Bosh Menu 🗃', reply_markup=types.ReplyKeyboardRemove())
#             await bot.send_message(message.from_user.id, "Вилоятни танланг",reply_markup=mr.add_malumot)
#         if message.text == 'Клиент очириш':
#             await bot.send_message(message.from_user.id, 'Bosh Menu 🗃', reply_markup=types.ReplyKeyboardRemove())
#             await bot.send_message(message.from_user.id, "Вилоятни танланг",reply_markup=mr.remove_malumot)
#         if message.text == 'Клиент хакида малумот':
#             await bot.send_message(message.from_user.id, 'Bosh Menu 🗃', reply_markup=types.ReplyKeyboardRemove())
#             await bot.send_message(message.from_user.id, "Вилоятни танланг",reply_markup=mr.info_malumot)
#         # if message.text == 'Турган жойингизни локатсиясини критинг':
#         #     await bot.send_message(message.from_user.id, "Вилоятни танланг",reply_markup=mr.info_malumot)
#         if message.text == 'Клиент малумотини озгартириш':
#             await bot.send_message(message.from_user.id, 'Bosh Menu 🗃', reply_markup=types.ReplyKeyboardRemove())
#             await bot.send_message(message.from_user.id, "Вилоятни танланг",reply_markup=mr.remake_malumot)
#
#     # await state.update_data(season=answer)
#     # await bot.send_message(message.from_user.id, "Qaysi xonada otirasiz?")
#     # await Registration.stay.set()
#
# if __viloyat__ == '__main__':
#     executor.start_polling(dp, skip_updates=True)


=======
from aiogram.types import Location
>>>>>>> c38241ec8885e12dca1917219b6bddd5e9ec1efb

import logging

import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode
from aiogram.utils import executor
import markups as mr


<<<<<<< HEAD
API_TOKEN = '5366807852:AAERuJaIYQcn5RbsX1kNEKHOLgrouupjh3w'     # Islom

=======
<<<<<<< HEAD
API_TOKEN = '5500425634:AAHqo9K3FeFgRg25UFytX_oszZbscJ_e6j4'   # AbuBakr
# API_TOKEN = '5366807852:AAERuJaIYQcn5RbsX1kNEKHOLgrouupjh3w'     # Islom
# logging.basicConfig(level=logging.INFO)
=======
# API_TOKEN = '5537289338:AAEwSGOvbS8XlA98MYG1TX87gqT-EkKOVjk'   # AbuBakr
# API_TOKEN = '5366807852:AAERuJaIYQcn5RbsX1kNEKHOLgrouupjh3w'     # Islom
API_TOKEN = "5111585539:AAGcIPBKJiTM6DKbyhRbfjdLMDPVQOXesng"    # Islom kril-lotin
>>>>>>> c38241ec8885e12dca1917219b6bddd5e9ec1efb

logging.basicConfig(level=logging.INFO)
>>>>>>> 2364c4fcf5b5cb93c486646a5c793035d9ce0118


bot = Bot(token=API_TOKEN)

# For example use simple MemoryStorage for Dispatcher.
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


# States
class Klientqoshish(StatesGroup):
    viloyat = State()  # Will be represented in storage as 'Klientqoshish: viloyat'
    Dokon_egasi_name = State()  # Will be represented in storDokon_egasi_name as 'Klientqoshish: Dokon_egasi_name'
    dokon_tel_raqam = State()  # Will be represented in storage as 'Klientqoshish: dokon_tel_raqam'


# @dp.message_handler(commands='start')
# async def cmd_start(message: types.Message):
#     """
#     Conversation's entry point
#     """
#     # Set state
#     await Klientqoshish.viloyat.set()
#     await message.reply("Iltimos viloyatni tanlang!", reply_markup=mr.add2_malumot)

# # Initialize bot and dispatcher
@dp.message_handler(commands=['start'])
async def register(message: types.Message ):
    # await message.answer(f'Admin Panelga Xush kelibsiz!')
<<<<<<< HEAD
    await bot.send_message(message.from_user.id, "Aссалому алеком\n Озингизга керакли болимни танланг",reply_markup=mr.markup)


@dp.message_handler(content_types='location')
async def file_1(msg: types.Message):
=======
    await bot.send_message(message.from_user.id, "Aссалому алеком\n Озингизга керакли болимни танланг",reply_markup=mr.location)


<<<<<<< HEAD

# You can use state '*' if you need to handle all states
@dp.message_handler(state='*', commands='cancel')
@dp.message_handler(Text(equals='cancel', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    """
    Allow user to cancel any action
    """
    current_state = await state.get_state()
    if current_state is None:
        return

    logging.info('Cancelling state %r', current_state)
    # Cancel state and inKlientqoshish user about it
    await state.finish()
    # And remove keyboard (just in case)
    await message.reply('Cancelled.', reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(state=Klientqoshish.viloyat)
async def process_viloyat(message: types.Message, state: FSMContext):
    """
    Process user viloyat
=======
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
>>>>>>> c38241ec8885e12dca1917219b6bddd5e9ec1efb
    """
    async with state.proxy() as data:
        data['viloyat'] = message.text

    await Klientqoshish.next()
    await message.reply("Докон эгасини йозинг")
    test = message.text
    print(test)


# Check age. age gotta be digit
# @dp.message_handler(lambda message: not message.text.isdigit(), state=Klientqoshish.Dokon_egasi_name)
# async def process_age_invalid(message: types.Message):
#     """
<<<<<<< HEAD
#     If age is invalid
#     """
#     return await message.reply("age gotta be a number.\nHow old are you? (digits only)")


@dp.message_handler(lambda message: message.text.isdigit(), state=Klientqoshish.Dokon_egasi_name)
async def process_age(message: types.Message, state: FSMContext):
    # Update state and data
    await Klientqoshish.next()
    await state.update_data(Dokon_egasi_name=int(message.text))
    await message.reply("Докон номерини киритинг")
    nomercha = message.text
    print(nomercha)


@dp.message_handler(lambda message: message.text not in ["Male", "Female", "Other"], state=Klientqoshish.dokon_tel_raqam)
async def process_gender_invalid(message: types.Message):
    """
    In this example gender has to be one of: Male, Female, Other.
    """
    return await message.reply("Bad gender viloyat. Choose your gender from the keyboard.")


@dp.message_handler(state=Klientqoshish.dokon_tel_raqam)
async def process_gender(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['dokon_tel_raqam'] = message.text

        # Remove keyboard
        markup = types.ReplyKeyboardRemove()

        # And send message
        await bot.send_message(
            message.chat.id,
            md.text(
                md.text('Hi! Nice to meet you,', md.bold(data['viloyat'])),
                md.text('Dokon egasini ismi:', md.code(data['Dokon_egasi_name'])),
                md.text('Dokon telefon raqami:', data['dokon_tel_raqam']),
                sep='\n',
            ),
            reply_markup=markup,
            parse_mode=ParseMode.MARKDOWN,
        )

    # Finish conversation
    await state.finish()
=======
############################## KLIENT QO'SHISH ###############################################
>>>>>>> c38241ec8885e12dca1917219b6bddd5e9ec1efb


async def other_message(message: types.Message):
    if message.chat.type == 'private':
        if message.text == 'Клиент кошиш':
            await Klientqoshish.viloyat.set()
            await message.reply("Iltimos viloyatni tanlang!", reply_markup=mr.add2_malumot)

            # DATABASE VILOYAT
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


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)