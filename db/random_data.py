
#!/bin/python3

import random 
import sqlite3

def insert_product(ReferencePro, DesignationPro, PrixPro, QuantiteStock):
    conn = sqlite3.connect('app.db')
    c = conn.cursor()
    c.execute(""" INSERT INTO Produit (ReferencePro, DesignationPro, PrixPro, QuantiteStock) VALUES (?,?,?,?) """,
                (ReferencePro, DesignationPro, PrixPro, QuantiteStock))
                
    conn.commit()
    conn.close()
    print(f"Product inserted {ReferencePro}, {DesignationPro}, {PrixPro}, {QuantiteStock}")


if __name__ == "__main__":
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for i in range(130):
        ReferencePro = ''.join(random.choice(chars) for i in range(5))
        DesignationPro = ''.join(random.choice(chars) for i in range(10))
        PrixPro = random.randint(1, 100)
        QuantiteStock = random.randint(1, 100)

        insert_product(ReferencePro, DesignationPro, PrixPro, QuantiteStock)
