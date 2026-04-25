import logging
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# ТОКЕН ДЛЯ @bex_test_2026_bot
TOKEN = "8747298604:AAHVWLRgmajd_EDGMLVcMzrmiTAkQOins6A"

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [['Меню 📜'], ['Заказ 🛒'], ['Подтверждение ✅']]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        f"Привет, {update.effective_user.first_name}! 👋\nЯ бот кафе Bexultan. Готов принять твой заказ.",
        reply_markup=reply_markup
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "Меню 📜":
        await update.message.reply_text(
            "📜 НАШЕ МЕНЮ:\n\n"
            "☕ Кофе:\n— Капучино (800 ₸)\n— Латте (900 ₸)\n\n"
            "🍰 Десерты:\n— Чизкейк (1200 ₸)\n— Тирамису (1500 ₸)\n\n"
            "Нажмите 'Заказ 🛒', чтобы выбрать блюдо."
        )

    elif text == "Заказ 🛒":
        await update.message.reply_text(
            "🛒 ОФОРМЛЕНИЕ ЗАКАЗА:\n\n"
            "Пожалуйста, напишите название блюда и ваш номер телефона одним сообщением.\n"
            "Например: 'Капучино, 87071234567'"
        )

    elif text == "Подтверждение ✅":
        await update.message.reply_text(
            "✅ ЗАКАЗ ПОДТВЕРЖДЕН!\n\n"
            "Ваш запрос передан администратору. Мы свяжемся с вами в течение 5 минут для уточнения деталей.\n"
            "Спасибо, что выбрали нас!"
        )
    
    else:
        # Если пользователь просто что-то пишет (например, свой заказ с номером)
        print(f"ПОЛУЧЕНЫ ДАННЫЕ ЗАКАЗА: {text}")
        await update.message.reply_text("Принято! Теперь нажмите кнопку 'Подтверждение ✅' для финализации.")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    
    print("--- БОТ ДЛЯ ПРЕЗЕНТАЦИИ ЗАПУЩЕН! ---")
    app.run_polling()