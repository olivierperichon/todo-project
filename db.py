import sqlite3 as sql
import os.path

IINTIAL_DATA = [[""     , "rien"           ],
                [""     , "pas grand chose"],
                [""     , "sieste"         ],
                ["denys", "truc"           ],
                ["denys","machin"          ],
                ["denys","chose"           ],
               ]

class DB:

    def __init__(self):
        d = os.path.dirname(__file__)
        p = os.path.join(d, "db.sql")
        if not os.path.exists(p):
            self._create(p)
        else:
            self._open(p)

    def _create(self, p):
        # ouvrir une connection à la base de données
        self._open(p)

        # créer la table
        self._cursor.execute(
            """CREATE TABLE todos (user text, task text)""")

        # insérer les dpnnées initiales
        self._cursor.executemany(
            """INSERT INTO todos VALUES (?,?)""",
            INITIAL_DATA)

        # commiter la transaction
        self._conn.commit()

    def _open(self, p):
        self._conn = sql.connect(p)
        self._cursor = self._conn.cursor()

    def get(self, name):
        if name is None:
            # dans le cas Anonyme
            name = ""

        # obtenir un curseur sur les lignes d'un utilisateur donné
        self._cursor.execute(
            """SELECT * FROM todos WHERE user=?""", (name,))

        # en retourner la liste
        return self._cursor.fetchall()
