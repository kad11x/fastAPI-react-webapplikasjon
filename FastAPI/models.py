#her skal vi ha modelen vår for databsen

from sqlalchemy import Column, Integer, String, Boolean, Text, Float
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from database import Base

#her lager vi tabellen: veldig grei oppsett som kan refereser tilbake til mysqlworkbench
class Guid(Base):
    __tablename__ = "guids"

    id = Column(Integer, primary_key= True,autoincrement=True, nullable= False)
    pris = Column(Float)
    title = Column(String(255), nullable= False)
    content = Column(Text, nullable=False)
    sted = Column(String(255), nullable=False)
    #created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    user_id = Column(Integer)



class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key= True,autoincrement=True, nullable= False)
    fNavn = Column(String(255), nullable=False)
    eNavn = Column(String(255), nullable= False)
    fodselsnummer = Column(Integer, nullable=False)