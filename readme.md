This is a discord bot written in Python, made to be used in the Sora Society server. It counts how many times we use certain emotes.

This bot was hosted in Heroku. "Procfile" and "requirements.txt" are files used by Heroku to run the bot.

The bot requires a file named "token.txt" placed in the same folder, containing the bot token in the first line.

The bot will store the counters to a binary file named "countstore.bin". Due to a limitation in Heroku, this file is useless. I'm working on a fix.

The bot was tested and works with Python 3.8.5 and discord.py version 1.4.1.

My discord: linkips#8609
