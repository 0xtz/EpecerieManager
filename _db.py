# # # # # # # # 
# WARNING 
# # # # # # # #
# THIS FILE USED TO CREATE THE DATABASE AND THE TABLE : RUN THIS FILE ONLY ONCE
# # # # # # # #

import sqlite3

# create a database
def create_produit():
    conn = sqlite3.connect('./db/app.db')
    c = conn.cursor()
    c.execute(""" 
                CREATE TABLE IF NOT EXISTS Produit (
                    ReferencePro	TEXT,
                    DesignationPro	TEXT,
                    PrixPro     	REAL,
                    QuantiteStock	INTEGER DEFAULT 0
                );
                
                """)

    conn.commit()
    conn.close()

def create_entres():
    conn = sqlite3.connect('./db/app.db')
    c = conn.cursor()
    c.execute(""" 
                CREATE TABLE IF NOT EXISTS Entre (
                    ReferencePro	TEXT,
                    QuantiteEntree	INTEGER,
                    DateEntree	TEXT
                );
                
                """)

    conn.commit()
    conn.close()

def create_ventes():
    conn = sqlite3.connect('./db/app.db')
    c = conn.cursor()
    c.execute(""" 
                CREATE TABLE IF NOT EXISTS Vente (
                    ReferencePro	TEXT,
                    QuantiteVente	INTEGER,
                    DateVente	TEXT
                );
                
                """)

    conn.commit()
    conn.close()