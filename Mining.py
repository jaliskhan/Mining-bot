async def invite(update: Update, context: ContextTypes.DEFAULT_TYPE):
       user_id = update.effective_user.id
       referral_link = f"https://t.me/{context.bot.username}?start={user_id}"
       await update.message.reply_text(f"Invite friends: {referral_link}")
