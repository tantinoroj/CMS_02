import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    SECRET_KEY = '2971343e-c5d9-4bce-a664-56e7d292b42e'
    
    # Azure Blob Storage Configuration
    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT')
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY')
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER')
    # BLOB_SAS_TOKEN = os.environ.get('BLOB_SAS_TOKEN')
    # BLOB_SAS_URL = os.environ.get('BLOB_SAS_URL')

    # Azure SQL Database Configuration
    SQL_SERVER = os.environ.get('SQL_SERVER')
    SQL_DATABASE = os.environ.get('SQL_DATABASE')
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME')
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD')

    # SQLAlchemy Database URI
    # SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE  + '?driver=ODBC+Driver+17+for+SQL+Server'
    
    SQLALCHEMY_DATABASE_URI = (
        f"mssql+pyodbc://{SQL_USER_NAME}@{SQL_PASSWORD}@{SQL_SERVER}:1433/{SQL_DATABASE}"
        "?driver=ODBC+Driver+17+for+SQL+Server"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Microsoft Authentication
    CLIENT_SECRET = '5038Q~N~2KCnaRV3gov~STzRepw6hcINpKXh4b9z'
    CLIENT_ID = '416d6f76-eb16-48ac-a864-59b8326309a1'
    AUTHORITY = "https://login.microsoftonline.com/ff873fe8-6631-416d-9262-bdbd56117dae"
    REDIRECT_PATH = "/getAToken"
    SCOPE = ["User.Read"]
    
    # Session Configuration
    SESSION_TYPE = "filesystem"
