# Author : @0xtz 

#!/bin/python3 

from PyQt6 import uic, QtCore, QtWidgets
from PyQt6.QtCore import QDateTime, QDate
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QIcon

import sys, time, os, sqlite3
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%

# load the ui.py file
from mainUI import Ui_MainWindow

# load the ui file
# Ui_MainWindow = uic.loadUiType("./ui/mainUI.ui")[0]

WINDOW_SIZE = 0
CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))


class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        super().setupUi(self)
        self.ui()
        self.buttons_handler()

    def ui(self) -> None:
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)

        # self.label_path.setText(CURRENT_DIR)
        # self.label_path.setStyleSheet("font-size:12pt; font-weight:700; color:#bd93f9;")

        self.label_time.setText(time.strftime("%H:%M"))
        self.label_time.setStyleSheet("font-size:12pt; font-weight:700; color:#bd93f9;")
        # update the label_time every second
        # self.timer = QTimer()
        # self.timer.timeout.connect(self.update_time)
        # self.timer.start(1000)

    
    def mousePressEvent(self, event) -> None:
        self.dragPos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event) -> None:
      self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos )
      self.dragPos = event.globalPosition().toPoint()
      event.accept()

    def restore_or_maximize_window(self) -> None:
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

    # todo button handlers 
    # todo btn_name 
    def buttons_handler(self) -> None:
        self.btn_close.clicked.connect(self.close)
        self.btn_minimize.clicked.connect(self.showMinimized)
        self.btn_maximize.clicked.connect(self.restore_or_maximize_window)
        # self.btn_settings.clicked.connect(self.settings)
        # self.btn_about.clicked.connect(self.about)
        # self.btn_help.clicked.connect(self.help)
        # self.btn_exit.clicked.connect(self.exit)

        # change the stackedWidget index
        self.btn_welcome.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.btn_gestion.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.btn_g_entre.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.btn_g_produit.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        self.btn_ventes.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))
        # TODO add a settings page
        self.btn_settings.clicked.connect(lambda: self.load_csv_to_db())

        self.btn_refrech_table_rupture_stock.clicked.connect(self.table_rupture)
        self.btn_create_p.clicked.connect(self.create_produit)
        self.btn_edite_p.clicked.connect(self.edite_produit)
        self.btn_delete_p.clicked.connect(self.delete_produit)
        self.btn_search_produit.clicked.connect(self.search_produit)
        self.btn_create_entre.clicked.connect(self.create_entres)
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
                                    self.linedit_reference_entre.text(),
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
                                int(self.linedit_quantite_entre.text()),
                                self.linedit_reference_entre.text(),
                                self.linedit_raison_entre.text()
                            ))
            db.commit()
            db.close()

            db = sqlite3.connect("./db/app.db")
            cursor = db.cursor()
            cursor.execute(""" UPDATE Produit SET QuantiteStock = ? WHERE ReferencePro = ? """,
                            (
                                int(fetch_result[0]) + int(self.linedit_quantite_entre.text()),
                                self.linedit_reference_entre.text()
                            ))                            
            db.commit()
            db.close()
            # clear the line edit
            self.linedit_reference_entre.clear()
            self.linedit_quantite_entre.clear()
            self.linedit_raison_entre.clear()
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




# QPushButton#btn_welcome {
# 	border: 2px solid rgb(52, 59, 72);
# 	border-radius: 5px;	
# 	background-color: rgb(52, 59, 72);
# }
# QPushButton#btn_welcome:hover {
# 	background-color: rgb(57, 65, 80);
# 	border: 2px solid rgb(61, 70, 86);
# }
# QPushButton#btn_welcome:pressed {	
# 	background-color: rgb(35, 40, 49);
# 	border: 2px solid rgb(43, 50, 61);
# }
