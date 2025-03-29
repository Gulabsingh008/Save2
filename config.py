from os import getenv


API_ID = int(getenv("API_ID", "26494161"))
API_HASH = getenv("API_HASH", "55da841f877d16a3a806169f3c5153d3")
BOT_TOKEN = getenv("BOT_TOKEN", "8152839871:AAFq4rA-s3bH4iLMxYTYretkpnzmjfUaSxQ")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7170452349").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://kkrishna1444:valnxGUtnpZvPN6E@cluster0.gbuk8.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002394679447"))
PREMIUM_LOGS = int(getenv("PREMIUM_LOGS", "-1002213359277"))


