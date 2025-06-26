from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from pymongo import MongoClient
from bson import ObjectId
from fastapi.middleware.cors import CORSMiddleware

# Model de dades
class Comentari(BaseModel):
    name: str
    text: str

class ComentariDB(Comentari):
    id: str

app = FastAPI()

# Permetre CORS per localhost (frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Connectar a MongoDB Atlas
client = MongoClient("mongodb+srv://iesbiseguretat:becerola@cluster0.dsfllf6.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.sample_mflix
comments_col = db.comments

# Helper per convertir ObjectId a str
def comentaridict(comentari):
    return {
        "id": str(comentari["_id"]),
        "name": comentari["name"],
        "text": comentari["text"]
    }

@app.post("/comments", response_model=ComentariDB)
def inserir_comentari(comentari: Comentari):
    result = comments_col.insert_one(comentari.dict())
    comentari_inserit = comments_col.find_one({"_id": result.inserted_id})
    return comentaridict(comentari_inserit)

@app.get("/comments", response_model=List[ComentariDB])
def llistar_comentaris():
    comentaris = comments_col.find()
    return [comentaridict(c) for c in comentaris]

@app.delete("/comments/{comentari_id}")
def eliminar_comentari(comentari_id: str):
    result = comments_col.delete_one({"_id": ObjectId(comentari_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Comentari no trobat")
    return {"message": "Comentari eliminat"}
