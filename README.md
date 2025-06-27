# MongoDB Atlas, FastAPI i HTML-JS
Anem crear una aplicació web per enviar, llistar i esborrar comentaris utilitzant HTML, FastAPI i MongoDB Atlas. 
## Què és MongoDB Atlas?
MongoDB Atlas és una plataforma de base de dades com a servei (DBaaS) que ofereix MongoDB  al núvol. És el servei oficial gestionat pel mateix equip que desenvolupa MongoDB, i permet utilitzar MongoDB sense haver de gestionar la infraestructura o la configuració del servidor. Oferix seguretat I té pla gratuït

El projecte té dues parts: 

        ◦ Frontend: HTML + JavaScript. 
        ◦ Backend: FastAPI + MongoDB Atlas
## Frontend: HTML i JavaScript

* Formulari amb dos camps: Nom i Comentari.
* Botó per enviar i un altre per llistar comentaris.
* Missatge de confirmació (Comentari enviat OK!).
* Llista on es mostraran els comentaris.
• Anem a fer ús de la DB d’exemple de MongoDB Atlas anomenada Sample_mflix
* JavaScript

## Backend: FastAPI i MongoDB
#### Què és  FastAPI?
És un framework web modern i altament eficient per a construir APIs amb Python. Està pensat per ser ràpid, fàcil d'utilitzar i molt potent, especialment per crear serveis web tipus RESTful APIs. Una RESTful API (Application Programming Interface) és un conjunt de regles per dissenyar serveis web simples, escalables i fàcils d’utilitzar.

## Connexió a MongoDB Atlas
Tenim  les rutes de l’API (o endpoints)

• POST /comments: insereix un comentari nou.
• GET /comments: retorna tots els comentaris.
• DELETE /comments/{id}: esborra un comentari pel seu ID.

## CORS
Val a dir què s’afegeix CORSMiddleware per a permetre connexions des del frontend.
