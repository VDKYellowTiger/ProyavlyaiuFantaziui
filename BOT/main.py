from telebot import TeleBot
from config import BotConfig
from gamerBOT import FishingGame

config = BotConfig()

bot = TeleBot(config.token, parse_mode=config.parse_mode)

game = FishingGame(bot)

if __name__ == '__main__':
    bot.polling()