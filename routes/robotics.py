import sqlite3

# Connexion à la base de données
con = sqlite3.connect("roboticslist.db")
cursor = con.cursor()

# Vérifier si la table Robots_med_old existe déjà et la supprimer si nécessaire
cursor.execute("""
    SELECT name FROM sqlite_master WHERE type='table' AND name='Robots_med_old';
""")
table_exists = cursor.fetchone()

if table_exists:
    print("La table Robots_med_old existe déjà. Suppression de l'ancienne table.")
    cursor.execute("DROP TABLE Robots_med_old;")

# Renommer l'ancienne table Robots_med
cursor.execute("ALTER TABLE Robots_med RENAME TO Robots_med_old;")

# Créer la nouvelle table avec la structure correcte
cursor.execute("""
CREATE TABLE IF NOT EXISTS Robots_med (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Reeducation TEXT,
    chirurgie TEXT,
    Assistance_med TEXT,
    Diag_spé TEXT
)
""")

# Copier les données de l'ancienne table dans la nouvelle
cursor.execute("""
INSERT INTO Robots_med (Reeducation, chirurgie, Assistance_med, Diag_spé)
SELECT Reeducation, chirurgie, Assistance_med, Diag_spé FROM Robots_med_old;
""")

# Fonction pour ajouter les robots
class robotics:
    "Liste des robots et machines dans le secteur de la santé"
    def __init__(self, nom, fonctionnalite):
        self.nom = nom
        self.fonctionnalite = fonctionnalite
        
def add_robots(cursor, con, robots):
    try:
        # Boucle pour insérer plusieurs robots
        for robot in robots:
            query = "INSERT INTO Robots_med (Reeducation, chirurgie, Assistance_med, Diag_spé) VALUES (?, ?, ?, ?);"
            cursor.execute(query, (robot['Reeducation'], robot['chirurgie'], robot['Assistance_med'], robot['Diag_spé']))
        con.commit()  # Valider les changements
        print("Les robots ont été ajoutés avec succès.")
    except sqlite3.Error as e:
        print(f"Erreur lors de l'ajout des robots : {e}")
        con.rollback()  # Annuler les modifications en cas d'erreur

# Liste des robots à ajouter
robots_to_add = [
    {'Reeducation': 'KUKA', 'chirurgie': 'Robot Da Vinci X', 'Assistance_med': 'TUD', 'Diag_spé': 'Monarch™ Platform'},
    {'Reeducation': 'Armemo Spring', 'chirurgie': 'Robot Mako', 'Assistance_med': 'Aethon TUG', 'Diag_spé': 'Vici™ Robot'},
    {'Reeducation': 'Mirror Image Motion Enabler', 'chirurgie': 'ROSATM', 'Assistance_med': 'EPIONE', 'Diag_spé': None},
    {'Reeducation': 'Reogo', 'chirurgie': 'Robodoc', 'Assistance_med': 'RIBA', 'Diag_spé': None},
    {'Reeducation': 'Haptic Master', 'chirurgie': 'Caspar', 'Assistance_med': 'Robear', 'Diag_spé': None},
    {'Reeducation': 'Amadeo', 'chirurgie': 'AcuSurgical', 'Assistance_med': None, 'Diag_spé': None},
    {'Reeducation': 'ReoGo', 'chirurgie': 'Robot Mako', 'Assistance_med': None, 'Diag_spé': None},
    {'Reeducation': 'Lokomat', 'chirurgie': 'CyberKnife', 'Assistance_med': None, 'Diag_spé': None},
    {'Reeducation': 'HapticMaster', 'chirurgie': 'Versius Surgical System', 'Assistance_med': None, 'Diag_spé': None}
]   

# Appel de la fonction pour ajouter les robots
add_robots(cursor, con, robots_to_add)

# # Supprimer l'ancienne table après l'ajout des robots
# cursor.execute("DROP TABLE Robots_med_old;")
# print("L'ancienne table Robots_med_old a été supprimée.")
# print("La table a été recréée avec succès.")

# Fermer la connexion
con.close()
