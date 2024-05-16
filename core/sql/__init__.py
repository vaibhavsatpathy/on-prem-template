from sql.database.database_manager import DatabaseManager
from commons.logger import logger
from sqlalchemy.sql import text

database_manager = DatabaseManager.sharedInstance()
Base = database_manager.Base
from sql.database.context_manager import session

with session() as transaction_session:
    transaction_session.execute(text("CREATE EXTENSION IF NOT EXISTS vector"))
    transaction_session.commit()

from sql.orm_models import *

Base.metadata.create_all(bind=database_manager.engine)
from commons.load_config import load_configuration

config = load_configuration()
