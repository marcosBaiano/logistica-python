import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')

    SQLALCHEMY_DATABASE_URI = (
        f"mysql+mysqlconnector://"
        f"{os.getenv('root')}:"
        f"{os.getenv('3512')}@"
        f"{os.getenv('DB_HOST')}/"
        f"{os.getenv('Logistica')}"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False
