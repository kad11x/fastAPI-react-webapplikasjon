from typing import Annotated
from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
#import mysql.connector
import time
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware 
import models
from .database import engine, get_db




#dette er en del av å importere sqlalchemy databse
models.Base.metadata.create_all(bind = engine)



app = FastAPI()

#man kan tenke seg at denne delen er som java. lager en klasse til tabellen vår
class GuidsBase(BaseModel):
    pris: int #--> skal kun hente: title som er string
    title: str #--> skal kun hente: content som er string
    content: str #--> skal kun hente: content som er string
    sted: str #--> kan også ha med bool
    user_id: int   #--> hvis ingen gir info vil den være

#lager tabell nr 2
class UserBase(BaseModel):
    fNavn: str #--> skal kun hente: title som er string
    eNavn: str #--> skal kun hente: content som er string
    userName: str #--> skal kun hente: content som er string
    fødselsnummer: int #--> kan også ha med bool
    


db_dependency = Annotated[Session, Depends(get_db)]


@app.post("/users/", status_code = status.HTTP_201_CREATED)
def create_posts(user: UserBase, db:db_dependency):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()







'''
hvordan koble til mysql:
while True:
     try:
        conn = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Delnia123!",
        database= "webapi")
        cursor = conn.cursor()
        print("\n*Database connection was succesfull!*\n")
        break
   except Exception as error:
        print("connecting to databse failed")
        print("Error: ", error)
        time.sleep(2)
'''


'''
#sending only a http request
@app.get("/") #denne deklerasjonen gjør at vi kan lage funkjsonen og gi meldingen. og det finnes
            # flere  http metoder: get, head, put, post osv... og inne i parantesen er rout adressen

def root(): #navnet er bare et navn, så vi velger selv, root er best
    return {"message": "Welcom to my pi"} # returnerer denne til jason for å vise på siden.

#tester sqlalchemy koden med å lage en test path
@app.get("/sqlalchemy")
def test_post(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return {"data": posts}


@app.get("/posts")
def get_posts():
    cursor.execute("""SELECT * FROM posts""") #gjør SQL spørringen vi ønsker
    posts = cursor.fetchall() # henter ut informasjonnen fra SQL_spørringen.
    return {"data": posts} #returnerer arraylist og ikek dict, vet ikke hvorfor.


#post request is sending data aswell to the API-server

@app.post("/posts", status_code = status.HTTP_201_CREATED)
def create_posts(post: Post):
    cursor.execute(""" INSERT INTO posts(title,content) VALUES(%s,%s) """,
                  (post.title, post.content)) #slikt setter man in 
    
    # må bruke denne metoden for å hente siste laget post pga mysql
    cursor.execute("SELECT LAST_INSERT_ID()")
    new_post_id = cursor.fetchone()[0]
    cursor.execute("SELECT * FROM posts WHERE id = %s", (new_post_id,))
    new_post = cursor.fetchone() 
    
    conn.commit() #gjør at forandringene går igjennom, sånnn at databasen oppdaterer.  
    
    return {"data": new_post}


#hente en spesifikk post
@app.get("/posts/{id}")
def get_post(id: int, response: Response): #Fast API konverterer til til den data typen du ønsker ved å legge det inn, eks her INT
    cursor.execute(""" SELECT * FROM posts WHERE id = %s""", (id,))
    post = cursor.fetchone()
    
    if not post:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                            detail = f"post with id: {id} was not found")
        #response.status_code = status.HTTP_404_NOT_FOUND
        #return {'message': f" post with id: {id} was not found "}
    return {"post_detail": post}


@app.delete("/posts/{id}", status_code= status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    #find the index in the array that gas required ID

    cursor.execute(""" DELETE FROM  posts WHERE id = %s""", (id,))
    deleted_post = cursor.fetchone
    conn.commit()
    if deleted_post == None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail= f"post with {id} does not existest")
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/posts/{id}")
def update_post(id:int, post: Post):
    cursor.execute(""" UPDATE posts SET title = %s, content = %s WHERE id = %s""",
                    (post.title, post.content, id,))
    conn.commit()

    #henter ut posten igjen etterpå med en annen spørring
    cursor.execute("""SELECT * FROM posts WHERE id = %s""", (id,))
    updated_post = cursor.fetchone()
    
    if updated_post == None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail= f"post with {id} does not existest")
    
    
    return {'data': updated_post}
'''




