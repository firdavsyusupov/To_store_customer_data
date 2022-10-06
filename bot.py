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
from sql_query import Database

db = Database('client.db')
logging.basicConfig(level=logging.INFO)
API_TOKEN = '5366807852:AAERuJaIYQcn5RbsX1kNEKHOLgrouupjh3w'

bot = Bot(token=API_TOKEN)

# For example use simple MemoryStorage for Dispatcher.
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


# STATES
# CLASS-STATE KLIENT QOSHISH
class KlientQoshish(StatesGroup):
    viloyat = State()  # Will be represented in storage as 'KlientQoshish:viloyat'
    Dokon_egasi = State()  # Will be represented in storage as 'KlientQoshish:Dokon_egasi'
    dokon_number = State()  # Will be represented in storage as 'KlientQoshish:dokon_number'
    dokon_locatsiya = State()  # Will be represented in storage as 'KlientQoshish:dokon_locatsiya'
    gender = State()  # Will be represented in storage as 'KlientQoshish:gender'

# CLASS-STATE KLIENT OCHIRISH
class KlientOchirish(StatesGroup):
    viloyat = State()
    dokon_royhati = State()
    tasdiqlash = State()


@dp.message_handler(commands=['start'])
async def register(message: types.Message):
    await bot.send_message(message.from_user.id, "Aссалому алеком\n Озингизга керакли болимни танланг",
                           reply_markup=mr.main_menu)

# ================================================================================================
# ========================================= KLIENT QOSHISH =======================================
# ================================================================================================


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
    # Cancel state and inKlientQoshish user about it
    await state.finish()
    # And remove keyboard (just in case)
    await message.reply('Cancelled.', reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(state=KlientQoshish.viloyat)
async def process_viloyat(message: types.Message, state: FSMContext):
    """
    Process user viloyat
    """
    async with state.proxy() as data:
        data['viloyat'] = message.text

    await KlientQoshish.next()
    await message.reply("Докон егасини исмини киритинг!")


@dp.message_handler(state=KlientQoshish.Dokon_egasi)
async def process_Dokon_egasi(message: types.Message, state: FSMContext):
    """
    Process user Dokon_egasi

    """
    async with state.proxy() as data:
        data['Dokon_egasi'] = message.text

    await KlientQoshish.next()
    await message.reply("Телефон ракамни киритинг!")


# Check age. dokon_number gotta be digit
@dp.message_handler(lambda message: not message.text.isdigit(), state=KlientQoshish.dokon_number)
async def process_dokon_number(message: types.Message):
    """
    If dokon_number is invalid
    """
    return await message.reply("Илтимос номер юворин! Масалан: 998 90 000 00 00")


@dp.message_handler(lambda message: message.text.isdigit(), state=KlientQoshish.dokon_number)
async def process_age(message: types.Message, state: FSMContext):
    # Update state and data
    await KlientQoshish.next()
    await state.update_data(dokon_number=int(message.text))

    await message.reply("Локациезни юворин!", reply_markup=mr.markup)


@dp.message_handler(content_types='location', state=KlientQoshish.dokon_locatsiya)
async def file_1(msg: types.Message, state: FSMContext):
    lokatsiya = msg.location
    print('Location', lokatsiya.longitude, lokatsiya.latitude)

    locat = [lokatsiya.latitude, lokatsiya.longitude]
    loc1 = lokatsiya.latitude
    loc2 = lokatsiya.longitude

    async with state.proxy() as data:
        data['dokon_locatsiya'] = locat
        data['loc1'] = loc1
        data['loc2'] = loc2

    await KlientQoshish.next()
    # Configure ReplyKeyboardMarkup
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup.add("Малумот олиш")
    print(locat)
    await msg.reply("Малумот йозиб олинди!", reply_markup=markup)


@dp.message_handler(state=KlientQoshish.gender)
async def process_gender(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['gender'] = message.text

        # Remove keyboard
        markup = types.ReplyKeyboardRemove()
        db.create_table(str(data['viloyat']))
        db.add_data(data['viloyat'], data['Dokon_egasi'], data['dokon_number'], data['loc1'], data['loc2'])
        data_sql = get_data(data['viloyat'])

        # And send message
        await bot.send_message(
            message.chat.id,
            md.text(
                md.text('Viloyat: ', md.bold(data['viloyat'])),
                md.text('Dokon egasini ismi: ', md.bold(data['Dokon_egasi'])),
                md.text('Dokon raqami: ', md.code(data['dokon_number'])),
                md.text('Локация:', md.text('QABUL')),
                sep='\n',
            ),
            reply_markup=markup,
            parse_mode=ParseMode.MARKDOWN,
        )
        await bot.send_location(message.chat.id, data['loc1'], data['loc2'])


    # Finish conversation
    await state.finish()


# ================================ **** KLIENT QOSHISH **** ======================================
# ================================================================================================


# ================================================================================================
# ========================================= KLIENT OSHIRISH ======================================
# ================================================================================================

@dp.message_handler(state=KlientOchirish.viloyat)
async def process_viloyat(message: types.Message, state: FSMContext):
    """
    Process user viloyat
    """
    async with state.proxy() as data:
        data['viloyat'] = message.text

    await KlientQoshish.next()
    await message.reply("Докон ройхатини танланг!")


@dp.message_handler(state=KlientOchirish.dokon_royhati)
async def process_viloyat(message: types.Message, state: FSMContext):
    """
    Process user viloyat
    """
    async with state.proxy() as data:
        data['viloyat'] = message.text

    await KlientQoshish.next()
    await message.reply("Докон егасини исмини киритинг!")

# ================================ **** KLIENT OSHIRISH **** =====================================
# ================================================================================================

# ================================================================================================
# ========================================= KLIENT OSHIRISH ======================================
# ================================================================================================



@dp.message_handler(content_types=['text'])
async def other_message(message: types.Message):
    if message.chat.type == 'private':
        if message.text == 'Клиент кошиш':
            await KlientQoshish.viloyat.set()
            await message.reply("Iltimos viloyatni tanlang!", reply_markup=mr.add2_malumot)

            # DATABASE VILOYAT
        if message.text == 'Клиент очириш':
            await KlientOchirish.viloyat.set()
            await message.reply("Iltimos viloyatni tanlang!", reply_markup=mr.add2_malumot)

        if message.text == 'Клиент хакида малумот':
            await bot.send_message(message.from_user.id, 'Bosh Menu 🗃', reply_markup=types.ReplyKeyboardRemove())
            await bot.send_message(message.from_user.id, "Вилоятни танланг", reply_markup=mr.info_malumot)

        # if message.text == 'Турган жойингизни локатсиясини критинг':
        #     await bot.send_message(message.from_user.id, "Вилоятни танланг",reply_markup=mr.info_malumot)

        if message.text == 'Клиент малумотини озгартириш':
            await bot.send_message(message.from_user.id, 'Bosh Menu 🗃', reply_markup=types.ReplyKeyboardRemove())
            await bot.send_message(message.from_user.id, "Вилоятни танланг", reply_markup=mr.add2_malumot)
            # print()
            # db.get_shop(message.reply_markup)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)