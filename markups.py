from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnBack = KeyboardButton("↩️ Назад")

# --- Погода ---
btnWeather = KeyboardButton("🌤 Погода")
btnWind = KeyboardButton("💨 Ветер")
btnSunTime = KeyboardButton("🌓 Восход и закат")
weatherMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnWeather, btnWind, btnSunTime, btnBack)