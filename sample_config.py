#----------------------------------- https://github.com/m4mallu/clonebot --------------------------------------------#
import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


class Config(object):

    # Get a bot token from botfather
    os.environ['TG_BOT_TOKEN'] = '1881650702:AAGD11iz1FDjmOtCRbNH0UZPIpfitALAKtA'
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

    # Get from my.telegram.org
    os.environ['APP_ID'] = "12808892"
    APP_ID = int(os.environ.get("APP_ID", ""))

    # Get from my.telegram.org
    os.environ['API_HASH'] = "08b32a58f27b680f7a8cb4ab7e5a0fd0"
    API_HASH = os.environ.get("API_HASH", "")

    # Authorized users to use this bot
    # os.environ['AUTH_USERS'] = [631305005]
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())

    # Generate a user session string
    TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "")

    # Database URI
    os.environ['DATABASE_URL'] = "postgres://trgkmtlx:A2oleA8ffp1j1fOyQSLH3hMhyIWn-pYm@chunee.db.elephantsql.com/trgkmtlx"
    print(os.environ['DATABASE_URL'])
    DB_URI = os.environ.get("DATABASE_URL", "")


config = Config()


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
