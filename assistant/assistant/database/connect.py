from mongoengine import connect
import configparser
from pathlib import Path

variant = "DB-DEV"
file_config = Path(__file__).parent.parent.parent.parent.joinpath('config.ini')
config = configparser.ConfigParser()
config.read(file_config)

user = config.get("DB-DEV", "user")
password = config.get("DB-DEV", "password")
domain = config.get("DB-DEV", "domain")
db_name = config.get("DB-DEV", "db_name")
# port = config.get("DB-DEV", "port")

# url = f"""mongodb+srv://{user}:{password}@{domain}/{db_name}?retryWrites=true&w=majority"""
# connect(host=url, ssl=True)
connect(host="mongodb://localhost:27017")


