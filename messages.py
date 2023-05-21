from api_service import get_weather

def weather(lat, lon) -> str:
    """Возвращает сообщение с указанием температуры и описанием погоды"""
    wthr = get_weather(lat, lon)
    return f'{wthr.location}, {wthr.description}\n' \
           f'Текущая температура {int(round(wthr.temperature, 0))}°C, ощущается как {int(round(wthr.temperature_feeling, 0))}°C'


def wind(lat, lon) -> str:
    """Возвращает сообщение о направлении ветра и его скорости"""
    wthr = get_weather(lat, lon)
    return f'Направление ветра: {wthr.wind_direction}\nCкорость ветра: {wthr.wind_speed} м/с'


def sun_time(lat, lon) -> str:
    """Возвращает сообщение о времени заката и рассвета"""
    wthr = get_weather(lat, lon)
    return f'Восход: {wthr.sunrise.strftime("%H:%M")}\n' \
           f'Закат: {wthr.sunset.strftime("%H:%M")}\n'