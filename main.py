from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import certifi
from pymongo import MongoClient
from bson import ObjectId


app = FastAPI()

# Servir fitxers estàtics en /static
app.mount("/static", StaticFiles(directory="static"), name="static")

# Ruta principal → carrega l'index.html
@app.get("/")
def root():
    return FileResponse("static/index.html")

# Permetre CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
import certifi
from pymongo import MongoClient
# Connexió a MongoDB Atlas
client = MongoClient(
    "mongodb+srv://iesbiseguretat:123... COMPLETA ...",
    tlsCAFile=certifi.where()
)

db = client.sample_mflix
comments_col = db.comments

# Models de dades
class Comentari(BaseModel):
    name: str
    text: str

class ComentariDB(Comentari):
    id: str

# Convertir ObjectId a string
def comentaridict(c):
    return {
        "id": str(c["_id"]),
        "name": c["name"],
        "text": c["text"]
    }

# Llistar comentaris
@app.get("/comments", response_model=List[ComentariDB])
def llistar_comentaris():
    comentaris = comments_col.find()
    return [comentaridict(c) for c in comentaris]

# Afegir comentari
@app.post("/comments", response_model=ComentariDB)
def inserir_comentari(comentari: Comentari):
    result = comments_col.insert_one(comentari.dict())
    c = comments_col.find_one({"_id": result.inserted_id})
    return comentaridict(c)

# Eliminar comentari
@app.delete("/comments/{comentari_id}")
def eliminar_comentari(comentari_id: str):
    try:
        result = comments_col.delete_one({"_id": ObjectId(comentari_id)})
    except:
        raise HTTPException(status_code=400, detail="ID invàlid")

    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Comentari no trobat")

    return {"message": "Comentari eliminat"}
