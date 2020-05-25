import sqlalchemy as alchemy
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session
import sqlalchemy.ext.declarative as declarative


SqlAlchemyBase = declarative.declarative_base()

__factory = None


def global_init(db_file):
    global __factory

    if __factory:
        return

    if not db_file.strip():
        raise Exception('Укажите файл базы данных!')

    connection_path = f'sqlite:///{db_file.strip()}?check_same_thread=False'

    engine = alchemy.create_engine(connection_path, echo=False)
    __factory = orm.sessionmaker(bind=engine)

    from . import __all_models
    SqlAlchemyBase.metadata.create_all(engine)


def create_session() -> Session:
    global __factory
    return __factory()