import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import messages
import config

import markups as nav

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.BOT_API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

# --- Команда /start ---
@dp.message_handler(commands='start')
async def introduction_message(message: types.Message):
    await message.answer(text="Здравствуйте, я погодный ассистент. Используйте команду /gps для получения вашего местоположения")

# --- Команда /gps ---
class location(StatesGroup): # состояние для хранения координат
    get = State()
    selects = State()
    language = State()

def get_keyboard():
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard = True)
    button = types.KeyboardButton("Поделиться местополжением", request_location=True)
    keyboard.add(button)
    return keyboard

@dp.message_handler(commands='gps')
async def cmd_locate_me(message: types.Message):
    await message.answer(text = "Нажмите на кнопку ниже, чтобы поделиться вашим местоположением", reply_markup=get_keyboard())
    await location.get.set()

@dp.message_handler(content_types='location', state = location.get)
async def handle_location(message: types.Message, state: FSMContext):
    lat = message.location.latitude
    lon = message.location.longitude
    locate = []
    locate.append(lat), locate.append(lon)
    await message.answer(text="Какую информацию вы хотите узнать?", reply_markup=nav.weatherMenu)

    async with state.proxy() as data:
        data['location'] = locate
    await location.selects.set()

@dp.message_handler(state = location.selects)
async def bot_messages(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        handle_location = data['location']
    print(handle_location[0], handle_location[1])
    if message.text == "🌤 Погода":
        await message.answer(text=messages.weather(handle_location[0], handle_location[1]), reply_markup=nav.weatherMenu)
    elif message.text == "💨 Ветер":
        await message.answer(text=messages.wind(handle_location[0], handle_location[1]), reply_markup=nav.weatherMenu)
    elif message.text == "🌓 Восход и закат":
        await message.answer(text=messages.sun_time(handle_location[0], handle_location[1]), reply_markup=nav.weatherMenu)
    elif message.text == "↩️ Назад":
        await state.finish()
        await message.answer(text="Возвращение в меню", reply_markup=types.ReplyKeyboardRemove())
    else:
        await message.answer(text="Неверная команда! Используйте кнопки для информации о погоде", reply_markup=nav.weatherMenu)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)