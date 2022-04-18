# Author : @0xtz
# version : 0.1.2
# date : 2020-04-24

#!/usr/bin/python3

# TODO " import just the needed components"
from PyQt6 import uic, QtCore, QtWidgets
from PyQt6.QtCore import QDateTime
from PyQt6.QtWidgets import * # QApplication, QWidget, QMainWindow 
from PyQt6.QtGui import QIcon

import sys, time, os
import sqlite3 

# load the ui file
from mainUI import Ui_MainWindow

WINDOW_SIZE = 0

class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        super().setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.buttons_handler()

        
    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
      self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos )
      self.dragPos = event.globalPosition().toPoint()
      event.accept()

    def restore_or_maximize_window(self):
        # Global windows state
        global WINDOW_SIZE 
        win_status = WINDOW_SIZE

        if win_status == 0:
        	# If the window is not maximized
        	WINDOW_SIZE = 1
        	self.showMaximized()
        else:
        	# If the window is on its default size
            WINDOW_SIZE = 0
            self.showNormal()

    def buttons_handler(self):
        # title bar btns
        self.btn_close.clicked.connect(self.close) # close button
        self.btn_minimize.clicked.connect(self.showMinimized) # minimize button
        self.btn_maximize.clicked.connect(self.restore_or_maximize_window) # maximize button

        # # # nav Menu btns

        # change the stackedWidget index
        self.btn_welcome.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.btn_gestion.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.btn_g_entree.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.btn_g_produit.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        self.btn_ventes.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))

        self.btn_refrech_table_rupture_stock.clicked.connect(self.table_rupture)
        self.btn_create_p.clicked.connect(self.create_produit)
        self.btn_edite_p.clicked.connect(self.edite_produit)
        self.btn_delete_p.clicked.connect(self.delete_produit)
        self.btn_search_produit.clicked.connect(self.search_produit)
        self.btn_create_entres.clicked.connect(self.create_entres)
        self.btn_vente.clicked.connect(self.create_ventes)
        self.btn_refrech_ventes.clicked.connect(self.refrech_ventes)

        # TODO load csv filr to the db
        self.btn_create_p_csv.clicked.connect(self.load_csv_to_db)

    ## DB functions 
    def table_rupture(self):
        db = sqlite3.connect("./db/app.db")
        cursor = db.cursor()
        result = cursor.execute(""" SELECT * FROM Produit WHERE QuantiteStock < 10""")

        self.table_rupture_stock.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.table_rupture_stock.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.table_rupture_stock.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        
        db.close()
    
    def create_produit(self):
        db = sqlite3.connect("./db/app.db")
        cursor = db.cursor()
        # check if the product already exist
        cursor.execute(""" SELECT * FROM Produit WHERE ReferencePro = ?""",
                        (self.linedit_reference.text(),)
                        )
        result = cursor.fetchone()
        if result:
            # create an alert box
            self.window_alert("Ce produit existe déjà")
        else:
            cursor.execute(""" INSERT INTO Produit(ReferencePro, DesignationPro, PrixPro) 
                                VALUES(?, ?, ?)
                            """,
                            (self.linedit_reference.text(), 
                            self.linedit_designation.text(),
                            float(self.linedit_prix.text()))
                            )
            db.commit()
            db.close()
            # clear the line edit
            self.linedit_reference.clear()
            self.linedit_designation.clear()
            self.linedit_prix.clear()
    
    def delete_produit(self):
        # create an alert box
        self.window_alert("Voulez-vous vraiment Suprimer ce produit ?")
        
        db = sqlite3.connect("./db/app.db")
        cursor = db.cursor()
        cursor.execute(""" DELETE FROM produit WHERE ReferencePro = ?""",
                        (self.linedit_delete_p.text(),)
                        )
        db.commit()
        db.close()
        # clear the line edit
        self.linedit_delete_p.clear()

    def edite_produit(self):
        # create an alert box
        self.window_alert("Voulez-vous vraiment Modifier ce produit ?")

        # check if the user want to edit the product
        db = sqlite3.connect("./db/app.db")
        cursor = db.cursor()
        cursor.execute(""" UPDATE Produit SET DesignationPro = ?, PrixPro = ? WHERE ReferencePro = ?""",
                        (self.linedit_edit_des.text(),
                        float(self.linedite_edit_prix.text()),
                        self.linedit_edit_reference.text())
                        )
        db.commit()
        db.close()
        # clear the line edit
        self.linedit_reference.clear()
        self.linedit_designation.clear()
        self.linedit_prix.clear()

    def search_produit(self):
        db = sqlite3.connect("./db/app.db")
        cursor = db.cursor()
        result = cursor.execute(""" SELECT * FROM Produit WHERE ReferencePro = ?""",
                                (self.linedit_search_produit.text(),)
                                )
        # clear the table
        self.table_rupture_stock.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.table_rupture_stock.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.table_rupture_stock.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        db.close()
        # clear the line edit
        self.linedit_search_produit.clear()
    
    def load_csv_to_db(self):
        self.window_alert("THIS FUNCTION IS NOT IMPLEMENTED YET")
    
    # # La Gestion des Entrées

    def create_entres(self):
        # check if the product exist in Produit
        db = sqlite3.connect("./db/app.db")
        cursor = db.cursor()
        result = cursor.execute(""" SELECT QuantiteStock FROM Produit WHERE ReferencePro = ?""",
                                (
                                    self.linedit_reference_entres.text(),
                                ))
        fetch_result = cursor.fetchone()
        # if the product exist
        if fetch_result != None:
            datetime = QDateTime.currentDateTime()
            db = sqlite3.connect("./db/app.db")
            cursor = db.cursor()
            cursor.execute(""" INSERT INTO Entrees(DateEntree, Quantite, ReferencePro, RaisonSocialeFournisseur) 
                                VALUES(?, ?, ?, ?)
                        """,
                            (   datetime.toString(),
                                int(self.linedit_quantite_entres.text()),
                                self.linedit_reference_entres.text(),
                                self.linedit_raison_entres.text()
                            ))
            db.commit()
            db.close()

            db = sqlite3.connect("./db/app.db")
            cursor = db.cursor()
            cursor.execute(""" UPDATE Produit SET QuantiteStock = ? WHERE ReferencePro = ? """,
                            (
                                int(fetch_result[0]) + int(self.linedit_quantite_entres.text()),
                                self.linedit_reference_entres.text()
                            ))                            
            db.commit()
            db.close()
            # clear the line edit
            self.linedit_reference_entres.clear()
            self.linedit_quantite_entres.clear()
            self.linedit_raison_entres.clear()
        else:
            # if the product doesn't exist
            self.window_alert("Produit inexistant")

    # # La Gestion des Ventes
    def create_ventes(self):
        db = sqlite3.connect("./db/app.db")
        c = db.cursor()
        # check if the product exist in Produit
        result = c.execute(""" SELECT QuantiteStock From Produit WHERE ReferencePro = ? """,
                            (self.linedit_reference_ventes.text(),)
                        )
        quantite_stock = result.fetchone()
        db.commit()
        db.close()
        # if the product exist
        if quantite_stock != None:
            
            if int(self.linedit_quantite_ventes.text()) <= int(quantite_stock[0]):
                self.insert_produit()

                db = sqlite3.connect("./db/app.db")
                cursor = db.cursor()
                # subtract the quantity from the stock 

                cursor.execute(""" UPDATE Produit SET QuantiteStock = ? WHERE ReferencePro = ? """,
                                (
                                    int(quantite_stock[0]) - int(self.linedit_quantite_ventes.text()),
                                    self.linedit_reference_ventes.text()
                                ))                            
                db.commit()
                db.close()
                
            else:
                self.window_alert("La quantité de stock est insuffisante !")
            
            # clear the line edit
            self.linedit_reference_ventes.clear()
            self.linedit_quantite_ventes.clear()

        else:
            # if the product doesn't exist
            self.window_alert("Ce produit n'existe pas !")
        
    def refrech_ventes(self):
        db = sqlite3.connect("./db/app.db")
        cursor = db.cursor()
        result = cursor.execute(""" SELECT * FROM Ventes """)
        # clear the table
        self.table_ventes.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.table_ventes.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.table_ventes.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        db.close()

    # # # # DB READ WRITE # # # #

    def insert_produit(self):
        datetime = QDateTime.currentDateTime()
        db = sqlite3.connect("./db/app.db")
        cursor = db.cursor()
        cursor.execute(""" INSERT INTO Ventes(DateVente , ReferencePro, QuantiteVendue) VALUES(?, ?, ?)""",
                        (   datetime.toString(),
                            self.linedit_reference_ventes.text(), 
                            self.linedit_quantite_ventes.text()
                        ))
        db.commit()
        db.close()
    
    # # # # UTILS # # # #
    
    def window_alert(self,  alert):
        msg = QMessageBox()
        msg.setText(alert)
        retval = msg.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())


# REFERENCES 
"""
https://www.sqlitetutorial.net/sqlite-python : SQLite Python Tutorial

https://zetcode.com/ : PyQt6 Tutorials

"""

