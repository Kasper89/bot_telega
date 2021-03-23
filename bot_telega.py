import nltk
import random

BOT_CONFIG = {
    'intents': {
        'hello': {
            'examples': ['Привет!', 'Здравсвуйте!))', 'Хай!!'],
            'responses': ['Прив!', 'Хеллоу', 'Как жизнь?']
        },
        'bye': {
            'examples': ['Пока!', 'До свиданья!', 'Увидимся!!', 'выход', 'выключайся'],
            'responses': ['Чао!', 'Будь здоров', 'Сайонара']
        },
        'pizza': {
            'pizza_meat': {
                'examples': ['С мясом', 'мясная', 'пепперони', 'салями', 'моцарелла'],
                'responses': ['Есть мясная', 'Есть суппер мясная', 'Есть с салями и пепперони']
            },
            'pizza_vegan': {
                'examples': ['брокколи', 'веган', 'без мяса', 'грибы', 'вегетарианская'],
                'responses': ['Есть грибы и сыр', 'Есть с брокколи', 'Есть пицца веган']
            }
        },
        'hamburger': {
            'hamburger_pig': {
                'examples': ['свинина', 'Гамбургер со свининой', 'свинная котлета'],
                'responses': ['Есть гамбургер с беконом', 'Есть гамбургер со свинной котлетой и сыром', 'Есть королевский гамбургер со свинной котлетой']
            },
            'hamburger_chicken': {
                'examples': ['курица', 'Гамбургер с курицей', 'куриная котлета'],
                'responses': ['Есть гамбургер с беконом и куриной катлетой', 'Есть гамбургер с куриной котлетой и сыром', 'Есть гамбургер King Chicken']
            },
            'hamburger_beef': {
                'examples': ['говядина', 'Гамбургер с говядиной', 'говяжья котлета'],
                'responses': ['Есть гамбургер с беконом и говяжьей котлетой', 'Есть гамбургер с говяжьей котлетой и сыром', 'Есть гамбургер King Beef']
            }
        }
    },
    'default_answers': ['Извините, я тупой', 'Переформулируйте, меня еще не обучили']
} # "знания" бота

def cleaner(text): # функция очистки текста
    cleaned_text = ''
    for ch in text.lower():
        if ch in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя ':
            cleaned_text = cleaned_text + ch
    return cleaned_text

def match(text, example): # гибкая функция сравнения текстов
    return nltk.edit_distance(text, example) / len(example) < 0.4

def get_intent(text): # функция определения интента текста
    for intent in BOT_CONFIG['intents']:
        if intent in ['pizza','hamburger']:
            for example in BOT_CONFIG['intents'][intent]:
                for food in BOT_CONFIG['intents'][intent][example]['examples']:
                    if match(cleaner(text), cleaner(food)):
                          return intent,example
        else:
            for example in BOT_CONFIG['intents'][intent]['examples']:
                 if match(cleaner(text), cleaner(example)):
                      return intent

def bot(text): # функция бота

    intent = get_intent(text)  # 1. попытаться понять намерение
    if intent is not None:
        if intent[0] in ['pizza', 'hamburger']:
            return random.choice(BOT_CONFIG['intents'][intent[0]][intent[1]]['responses'])
        else:
            return random.choice(BOT_CONFIG['intents'][intent]['responses']) # 2. если удалось, ответить в соответствии намерением
    else:
        return random.choice(BOT_CONFIG['default_answers']) # 3. если не удалось, ответить заглушкой


question = ''
while question not in ['выход', 'выключайся']:

    question = input()
    answer = bot(question)
    print(answer)