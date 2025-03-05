# Login
   heroku login

   # Create Heroku app
   heroku create your-bot-name

   # Set environment variables
   heroku config:set TELEGRAM_BOT_TOKEN=your_bot_token_here
   heroku config:set TON_MNEMONIC=your_wallet_phrase  # If using TON

   # Enable worker dyno
   heroku ps:scale worker=1

   # Deploy
   git push heroku main
