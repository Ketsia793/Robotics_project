from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from robotics import robotics

app = Flask(__name__)
CORS(app)
# api = robotics('list')
@app.route('/', methods=['GET'])
def add_robots():
     return robotics

if __name__=="__main__":
     robot1 = robotics('KUKA', 'Reeducation')
     # créer une boucle puis ajouter une condition pour les spécialités n'ayant pas de robots
     #boucle for 
          #condition si condition vraie
               # robot1 = robotics('KUKA', 'Reeducation')
               # add robot à liste
     print(f"voici mon robot1: {robot1.nom} spécialisé dans la {robot1.fonctionnalite}")
     app.run(debug=True, port=5000, host='0.0.0.0')
