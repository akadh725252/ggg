import config
import time
import logging
from pyrogram import Client, idle
from pyromod import listen  # type: ignore
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid

logging.basicConfig(
    level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

StartTime = time.time()
app = Client(
    "Anonymous",
    api_id=1747534,
    api_hash="5a2684512006853f2e48aca9652d83ea",
    bot_token="6271198287:AAFluU_3WWZcED4ujHq8dND_GCdESqBUdwI",
    in_memory=True,
    plugins=dict(root="StringGenBot"),
)


if __name__ == "__main__":
    print("Starting the String Generator Bot...")
    try:
        app.start()
    except (ApiIdInvalid, ApiIdPublishedFlood):
        raise Exception("Your API_ID/API_HASH is not valid.")
    except AccessTokenInvalid:
        raise Exception("Your BOT_TOKEN is not valid.")
    uname = app.get_me().username
    print(f"@{uname} started successfully !")
    idle()
    app.stop()
    print("Bot stopped. Bye !")
