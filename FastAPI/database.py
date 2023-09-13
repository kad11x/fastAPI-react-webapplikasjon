#hvordan koble opp mot database serveren med SQLALCHEMY som bruker ORM og man slipper å kode sql
#ORM står for OBJECTIV REALSION MODELL
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#nøvendig for å koble opp sqlalchemy
DATABASE_URL = "mysql+pymysql://root:Delnia123!@localhost:3306/gruppeoppgave"
engine = create_engine(DATABASE_URL)
sessionLocal = sessionmaker(autocommit=False, autoflush=False,bind=engine)
Base = declarative_base()


#depandancy, kobler opp her
def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()