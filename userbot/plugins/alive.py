"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"
RCBOT_IS_ALIVE = ("**I AM STILL ALIVE SIR ✌** \n`🇮🇳BOT Status : ` **AWESOMELY WORKING🥳**\n\n"
                     f"`MY PRO OWNER`: {DEFAULTUSER}\n\n"
                     "`RC Bot Version:` [1.0](https://telegra.ph/RCBOT-07-02)\n`Python:` **3.7.4**\n"
                     "`Database Status:` **ALL WELL AND GOOD🙂**\n\n`ALWAYS WITH YOU AND WORKING FOR U MU MASTER!\n`"
                     "**Bot Creator:** [🇮🇳RUSHI CHOKSI](t.me/Mai_RC)\n"
                     "**Coding helper:** [🇮🇳INDIAN BHAI](t.me/pureindialover)\n"
                     "**Updates helper:** [🇮🇳AKASH](t.me/AKASH_AM1)\n\n"
                     "     [🇮🇳Deploy This RCBot🇮🇳](https://github.com/rushichoksi/IndianBot)") 


#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    chat = await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_message(chat, RCBOT_IS_ALIVE) 
