import logging
from telegram.ext import Updater, CommandHandler

BOT_TOKEN = "8389875803:AAGcCO8bG1mQS2khsUa5S2BqD8J0kfc68Bo"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def start(update, context):
    update.message.reply_html(
        "🎯 <b>ARTBAZAR</b>\n\n"
        "AI для продавцов маркетплейсов\n\n"
        "/help - Помощь\n"
        "/tariff - Тарифы\n"
        "/subscribe - Премиум"
    )

def help_cmd(update, context):
    update.message.reply_html(
        "📖 <b>Помощь</b>\n\n"
        "/start - Меню\n"
        "/tariff - Тарифы\n\n"
        "Контакт: @Artbazar_payment"
    )

def tariff_cmd(update, context):
    update.message.reply_html(
        "💎 <b>Тарифы</b>\n\n"
        "🆓 Базовый - бесплатно\n"
        "⭐️ Премиум - 500 сом/мес"
    )

def subscribe_cmd(update, context):
    update.message.reply_html(
        "💳 <b>Подписка</b>\n\n"
        "O!Деньги: +996707140788\n"
        "Контакт: @Artbazar_payment"
    )

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_cmd))
    dp.add_handler(CommandHandler("tariff", tariff_cmd))
    dp.add_handler(CommandHandler("subscribe", subscribe_cmd))
    
    logger.info("Бот запущен!")
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
  
