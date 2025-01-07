"""
Requirements
------------
    pip install sqlalchemy
    pip install mysql-connector-python

db URL general template:
<dialect>+<driver>://<username>:<password>@<host>:<port>/<database>
---------------
    MySql
    mysql_db_url = 'mysql://<username>:<password>@<hostname>:<port>/<database>'
    mysql_db_url = 'mysql+mysqlconnector://<username>:<password>@<hostname>:<port>/<database>'

    PostgreSQL
    postgresql_db_url = 'postgresql://<username>:<password>@<hostname>:<port>/<database>'
    "postgresql+psycopg2://<username>:<password>@<hostname>:<port>/<database>"

Get username and port from SQL server
----------------
    CREATE DATABASE test_docker;
    USE test_docker;

    SHOW VARIABLES WHERE Variable_name = 'port';
    SELECT user();
"""

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base #trebuie importata dupa ce cream engine
from sqlalchemy.orm import sessionmaker

mysql_db_url = 'mysql+mysqlconnector://root:Omniasig22#@localhost:3306/test_users'

engine = create_engine(mysql_db_url)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class User(Base):
    __tablename__ = 'users' #vom folosi ORM- tabelul din baza de date
    #cream coloanele din baza de date
    id = Column(Integer, primary_key=True)
    first_name = Column(String(20))
    last_name = Column(String(20))
    email = Column(String(40))
    age = Column(Integer)

Base.metadata.create_all(engine)
