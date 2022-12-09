from sqlalchemy import create_engine

SQLALCHEMY_DATABASE_URL = 'sqlite:///./datakantinburjo'

db_engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args = {"check_same_thread": False},
    echo=True
)