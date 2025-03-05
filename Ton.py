async def withdraw(update: Update, context: ContextTypes.DEFAULT_TYPE):
       user_id = update.effective_user.id
       address = context.args[0]  # User-provided crypto address
       amount = int(context.args[1])
       if user_balances[user_id] >= amount:
           # Integrate with a blockchain API (e.g., TON, Ethereum)
           user_balances[user_id] -= amount
           await update.message.reply_text(f"Withdrew {amount} tokens to {address}")
       else:
           await update.message.reply_text("Insufficient balance!")
