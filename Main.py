import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Simulated user balances (use a database in production)
user_balances = {}
user_mining_cooldown = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id not in user_balances:
        user_balances[user_id] = 0
    keyboard = [[InlineKeyboardButton("⛏️ Mine Now", callback_data="mine")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Welcome to the Mining Bot!\nClick the button to mine!",
        reply_markup=reply_markup
    )

async def mine(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.callback_query.from_user.id
    if user_id in user_mining_cooldown:
        await update.callback_query.answer("Wait 24 hours before mining again!", show_alert=True)
        return

    # Reward user with 10 tokens
    user_balances[user_id] = user_balances.get(user_id, 0) + 10
    user_mining_cooldown[user_id] = True  # Add cooldown logic (e.g., 24h timer)

    await update.callback_query.answer()
    await update.callback_query.edit_message_text(
        f"⛏️ You mined 10 tokens! Total: {user_balances[user_id]}"
    )

async def balance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    await update.message.reply_text(f"Your balance: {user_balances.get(user_id, 0)} tokens")

if __name__ == "__main__":
    app = Application.builder().token(os.getenv("TELEGRAM_BOT_TOKEN")).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("balance", balance))
    app.add_handler(CallbackQueryHandler(mine, pattern="^mine$"))
    app.run_polling()
