import os

class Config:
    PROJECT_NAME = os.getenv('PROJECT_NAME', 'StockPaper')
    API_V1_PREFIX = '/api/v1'
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')
    CORS_ALLOW_ORIGINS = os.getenv('CORS_ALLOW_ORIGINS', '*')
    DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///./test.db')
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'info')

config = Config()