import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    
    # Azure Blob Storage Configuration
    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT')
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY')
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER')
    BLOB_SAS_TOKEN = os.environ.get('BLOB_SAS_TOKEN')
    BLOB_SAS_URL = os.environ.get('BLOB_SAS_URL')

    # Azure SQL Database Configuration
    SQL_SERVER = os.environ.get('SQL_SERVER')
    SQL_DATABASE = os.environ.get('SQL_DATABASE')
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME')
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD')

    # SQLAlchemy Database URI
    SQLALCHEMY_DATABASE_URI = (
        f"mssql+pyodbc://{SQL_USER_NAME}:{SQL_PASSWORD}@{SQL_SERVER}:1433/{SQL_DATABASE}"
        "?driver=ODBC+Driver+18+for+SQL+Server"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Microsoft Authentication
    CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
    CLIENT_ID = os.environ.get('CLIENT_ID')
    AUTHORITY = os.environ.get('AUTHORITY')
    REDIRECT_PATH = os.environ.get('REDIRECT_PATH')
    SCOPE = ["User.Read"]
    
    # Session Configuration
    SESSION_TYPE = os.environ.get('SESSION_TYPE')
