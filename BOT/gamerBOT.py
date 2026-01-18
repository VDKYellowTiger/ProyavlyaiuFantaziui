import random
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

class FishingGame:
    def __init__(self, bot):
        self.bot = bot
        self.user_states = {}

        self.register_handlers()

    # -------- РЕГИСТРАЦИЯ ОБРАБОТЧИКОВ --------

    def register_handlers(self):

        @self.bot.message_handler(commands=['start'])
        def start(message):
            self.start_menu(message.chat.id)

        @self.bot.callback_query_handler(func=lambda c: c.data.startswith('fish'))
        def fish_choice(callback_query):
            self.choose_fish(callback_query)

        @self.bot.callback_query_handler(func=lambda c: c.data == 'restart')
        def restart(callback_query):
            self.start_menu(callback_query.message.chat.id)

        @self.bot.callback_query_handler(func=lambda c: c.data == 'finish')
        def finish(callback_query):
            chat_id = callback_query.message.chat.id
            self.bot.send_message(chat_id,"Хорошо, приходи в следующий раз 🤗")
            # очищаем состояние пользователя
            if chat_id in self.user_states:
                self.user_states.pop(chat_id)

        @self.bot.message_handler(content_types=['text'])
        def text_handler(message):
            self.process_text(message)

    # -------- КРАСИВОЕ ГЛАВНОЕ МЕНЮ --------

    def start_menu(self, chat_id):

        self.user_states[chat_id] = {"stage": "start","inventory": []}

        kb = InlineKeyboardMarkup()

        kb.add(InlineKeyboardButton("Карп", callback_data="fish_карп"),
            InlineKeyboardButton("Лещ", callback_data="fish_лещ"),
            InlineKeyboardButton("Щука", callback_data="fish_щука"))

        self.bot.send_message(chat_id,"🎣 Добро пожаловать на виртуальную рыбалку!\n\n""Выбери, какую рыбу будем ловить:",reply_markup=kb)

    # -------- ВЫБОР РЫБЫ --------

    def choose_fish(self, callback_query):

        chat_id = callback_query.message.chat.id
        fish = callback_query.data.split("_")[1]

        self.user_states[chat_id]["fish"] = fish
        self.user_states[chat_id]["stage"] = "action"

        rkb = ReplyKeyboardMarkup(one_time_keyboard=True)
        rkb.add(KeyboardButton("Будем продолжать"))

        if fish == "карп":
            text = "Бойл был слишком большим, рыба могла испугаться!"
            self.user_states[chat_id]["inventory"].append("огромный бойл")

        elif fish == "лещ":
            text = "Личинки слишком активные могут быстро расползтись!"
            self.user_states[chat_id]["inventory"].append("банка личинок")

        else:
            text = "На живца ловить нужно терпение!"
            self.user_states[chat_id]["inventory"].append("живец")

        self.bot.send_message(chat_id, text, reply_markup=rkb)

    # -------- ОБРАБОТКА ТЕКСТА --------

    def process_text(self, message):

        chat_id = message.chat.id
        text = message.text

        state = self.user_states.get(chat_id)

        if not state:
            self.bot.send_message(chat_id, "Нажмите /start чтобы начать игру!")
            return

        if text == "Будем продолжать":
            self.ask_time(chat_id)
            return

        if state["stage"] == "waiting_time":
            self.check_time(chat_id, text)

    # -------- ВОПРОС ПРО ВРЕМЯ --------

    def ask_time(self, chat_id):

        self.user_states[chat_id]["stage"] = "waiting_time"
        self.bot.send_message(chat_id,"⏱ Сколько минут будете ждать? Введите любое число от 5 до 20.")

    # -------- ПРОВЕРКА УДАЧИ --------

    def check_time(self, chat_id, text):

        try:
            user_number = int(text)
        except ValueError:
            self.bot.send_message(chat_id, "Нужно ввести именно число 🔢")
            return

        lucky = random.randint(5, 20)

        inventory = self.user_states[chat_id]["inventory"]

        if user_number == lucky:
            result = "🐟 Клюнула! Отлично! Тащи!"
            inventory.append("пойманная рыба")
        else:
            result = f"Не клюнула! Надо было ждать {lucky} минут."

        # Показываем инвентарь
        inv_text = "\n".join(inventory) if inventory else "пусто"

        kb = InlineKeyboardMarkup()
        kb.add(InlineKeyboardButton("Начать заново 🔁", callback_data="restart"),InlineKeyboardButton("Всё, я устал(а) 😴", callback_data="finish"))

        self.bot.send_message(chat_id,f"{result}\n\n🎒 Ваш инвентарь:\n{inv_text}",reply_markup=kb)

        # Обнуляем состояние
        self.user_states.pop(chat_id, None)