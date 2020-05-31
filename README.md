# upstateBot
A simple bot to send telegram notifications if one of my services is down

For debian create a cronjob which executes the script

`$ sudo crontab -e`

`*/10 * * * * python3 /path/to/upstateCheck.py`

Executes script all 10 minutes

# Create a Telegram bot

search `@BotFather` in your favourite telegram client

write commands as chat message

`/newbot`

fill out what's asked

this will provide you a token. enter the bot chatroom and hit start to receive messages.

You can get the chatroom id by open the following url in the browser after sending a message to the bot first

https://api.telegram.org/bot(token)/getUpdates (replace (token) with your generated token)
  
the id is under chat => id

