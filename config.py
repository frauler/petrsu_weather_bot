BOT_API_TOKEN = '6254111144:AAFf_z6Hthud9k7y7fC9Yxmb_sYvx057-iA' # токен бота
WEATHER_API_KEY = '30a7e6edf867fe90da9ad113abf2dac5' # токен

# запрос текущей погоды
CURRENT_WEATHER_API_CALL = (
        'https://api.openweathermap.org/data/2.5/weather?'
        'lat={latitude}&lon={longitude}&lang=ru&'
        'appid=' + WEATHER_API_KEY + '&units=metric'
)