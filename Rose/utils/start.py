from pyrogram.types import Message
from Rose import *
from Rose.mongo.rulesdb import Rules



async def get_private_rules(_, m: Message, help_option: str):
    chat_id = int(help_option.split("_")[1])
    rules = Rules(chat_id).get_rules()
    if not rules:
        await m.reply_text(
            "The Admins of that group have not setup any rules!",
            quote=True,
        )
        return ""
    await m.reply_text(
        f"""
** Rules are**:

{rules}
""",
        quote=True,
        disable_web_page_preview=True,
    )
    return ""

async def get_learn(_, m: Message, help_option: str):
    await m.reply_text(
        f"""
məndən istifadə etməyin başqa yolu daxili sorğunu özünüz yazmaqdır
 format bu tənzimləmədə olmalıdır

`@DaintySecurityBot your whisper @username`

indi formatı 3 hissəyə bölüb hər bir hissəsini izah edəcəyəm

1- `@DaintySecurityBot`
bu mənim istifadəçi adımdır, daxili sorğunun əvvəlində olmalıdır, ona görə də biləcəyəm ki, başqa botdan deyil, məndən istifadə edirsiniz.

2- `gizli mesak`
it is the whisper that will be sent to the target user, you need to remove your whisper and insert your actual whisper.

3- `@username`
you should replace this with target's username so the bot will know that the user with this username can see your whisper message.

example:- 
`@DaintySecurityBot hello this is a test @Nixhadx`

📎 bot qruplarda işləyir və hədəf istifadəçi sizinlə eyni qrupda olmalıdır
 nəyi gözləyirsən?!
 indi məni sınayın 😉
""",
        quote=True,
        disable_web_page_preview=True,
    )
    return ""


