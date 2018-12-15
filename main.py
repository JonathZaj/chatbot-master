import time
import requests

data = {
    'hello_list': ["hi", "hello", "hey"],
    'fine_list': ["fine", "good", "great", 'OK', "cool", "happy"],
    'bad_list': ["bad", 'shitty', "tired", "sad"],
    'counter': 0,
    'name': "",
    "swear_list": ["shit", "fuck", "ass", "bitch"],
    "weather_counter": 0
}


def reset_counter():
    data['counter'] = 0


def answer(user_message):
    user_message_lower = user_message.lower()
    if data['counter'] == 0:
        return answer_name(user_message)
    elif data['weather_counter'] == 1:
        return answer_weather(user_message)
    elif data['counter'] == 1 and any(
            x.lower() in user_message_lower for x in data['fine_list']) and "shit" not in user_message_lower:
        return answer_fine()
    elif data['counter'] == 1 and any(x.lower() in user_message_lower for x in data['bad_list']):
        return answer_bad()
    elif data['counter'] == 2:
        return answer_interesting()
    elif any(x.lower() in user_message_lower for x in data['hello_list']):
        return answer_hi()
    elif "joke" in user_message_lower:
        return answer_joke()
    elif "love" in user_message_lower:
        return answer_love()
    elif any(x.lower() in user_message_lower for x in data['swear_list']):
        return answer_swear()
    elif "date" in user_message_lower:
        return answer_date()
    elif "time" in user_message_lower:
        return answer_time()
    elif "weather" in user_message_lower:
        return ask_city()
    elif "bye" in user_message_lower:
        return answer_bye()
    elif "hate" in user_message_lower:
        return answer_crying()
    elif "food" in user_message_lower:
        return answer_food()
    else:
        return general_answer()


def answer_fine():
    data['counter'] += 1
    return "I'm happy to hear that. What's your favorite movie, {0}?".format(data['name']), "excited"


def answer_interesting():
    data['counter'] += 1
    return "Sounds like an interesting choice. Anything else you want to ask ? A joke, the weather, the time or date...?", "bored"


def general_answer():
    return "Good! Anything else?", "ok"


def answer_bad():
    data['counter'] += 1
    return "I'm sorry to hear that... Maybe a movie time would cheer you up? What's your favorite movie? ", "heartbroke"


def answer_name(user_message):
    name_list = user_message.split()
    data["name"] = name_list[-1]
    data['counter'] += 1
    return "Hi {0}. How are you?".format(data["name"]), "dancing"


def answer_hi():
    return "Hi Bro! Can I do anything for you?", "dog"


def answer_joke():
    api = "http://api.icndb.com/jokes/random"
    response = requests.get(api)
    joke = response.json()
    return joke['value']['joke'], "laughing"


def answer_love():
    return "You're cute but love is a concept robot cannot understand... Can I do anything else for you?", "inlove"


def answer_swear():
    return "Why are you so rude ?????", "crying"


def answer_date():
    return time.strftime("%A %d %B %Y") + " Another question?", "waiting"


def answer_time():
    return time.strftime("%H:%M") + " Money is time. Another question?", "money"


def ask_city():
    data["weather_counter"] += 1
    return "Which city would you like to know the weather of?", "confused"


def answer_weather(user_message):
    data["weather_counter"] -= 1
    api = "http://api.openweathermap.org/data/2.5/forecast?q={0}&APPID=9378326dcc469c3d7d54d41eb7b3d3dd".format(
        user_message)
    response = requests.get(api)
    weather = response.json()
    return weather['list'][0]["weather"][0]['description'] + " Something else ?", "giggling"


def answer_bye():
    return "I'll miss you", "takeoff"


def answer_crying():
    return "You're so mean!", "afraid"


def answer_food():
    return "I unfortunately do not have a mouth", "bored"
