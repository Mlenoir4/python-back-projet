# ProjectPythonBack

## Installation

## Docker mode
**requirements:** docker and docker-compose installed  
To launch, your terminal must be in the root folder of this repository. Then issue :  
`docker-compose up --build`

## Uvicorn mode
**requirements:** python3.10 or greater installed  
First, install dependencies
`pip install -r requirements.txt`

Then, run the app:  
`uvicorn app.main:app --host 0.0.0.0 --port 80`

## Usage
    - Pour utiliser l'application il suffit de se rendre sur l'adresse suivante : http://localhost:80/docs.
    - Vous n'aurez pas acces au differentes routes si vous n'etes pas connecté. 
      Pour cela, il faut cliquer sur le bouton Authorize en haut à droite de la page.
    - Renter les information de connection d'un utilisateur valide (Voir la section Test pour plus d'information).
    - Une fois connecté vous pourrez selon le role attribuer à votre utilisateur, acceder aux differentes fonctionnalitées de l'application.
    - Pour tester les routes, il suffit de cliquer sur la route souhaitée et de cliquer sur le bouton "Try it out" en bas à droite de la page.
    - Vous pouvez ensuite rentrer les parametres de la requete et cliquer sur le bouton "Execute" pour envoyer la requete. 
      Vous pouvez aussi tester les routes avec un logiciel comme Postman.
    - Pour plus d'information sur les routes, vous pouvez vous rendre sur la page http://localhost:80/redoc.



## Tests

    - Information de connection d'un utilisateur valide :
        - username : mathieu
        - password : azerty

    - Information de connection d'un administrateur valide :
        - username : admin
        - password : azerty

    - Information de connection d'un maintainer valide :
        - username : user
        - password : azerty