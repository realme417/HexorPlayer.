from callsmusic.callsmusic import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User
from config import BOT_USERNAME

@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,"ššš²šæš² šššš¶ššš®š»š°š² š¢š³ @{BOT_USERNAME}\nāØš§šµš¶š šš¼š šš²šš²š¹š¼š½š²š± šš @ššÆš¼šššš²šš¼šæ\nššš¼š»š š¦š½š®šŗ šš²šæš²")
  return                        
