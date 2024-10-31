from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QFileDialog, QTableWidget, QTableWidgetItem
from mainWindowUI import Ui_MainWindow
from PyQt6.QtGui import QPixmap, QIcon, QMovie

from gif import Gif
import controller
from fileHandler import readAppPath

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) ->  None:
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.gifs:list[Gif] = []
        self.current = 0
        
        self.btnPrev.clicked.connect(lambda:self.prevGif())
        self.btnNext.clicked.connect(lambda:self.nextGif())

        self.tblMetadata.itemChanged.connect(lambda:self.editGif())

        if not controller.getGifs():
            self.chooseDir()
        self.setGifs(controller.getGifs())

        self.actionAgregar_ruta.triggered.connect(lambda:self.chooseDir())
        self.actionAgregar_ruta.triggered.connect(lambda:self.setGifs(controller.getGifs()))

        self.actionLimpiar_cache.triggered.connect(lambda:controller.clearHistory())
        self.actionLimpiar_cache.triggered.connect(lambda:self.chooseDir())
        self.actionLimpiar_cache.triggered.connect(lambda:self.gifs.clear())
        self.actionLimpiar_cache.triggered.connect(lambda:self.setGifs(controller.getGifs()))


    def setGifs(self, gifs:list[Gif]):
        if not gifs or len(gifs) == 0:
            self.lblGif.setText("No hay gifs en la ubicación seleccionada")
            self.btnNext.setEnabled(False)
            self.btnPrev.setEnabled(False)
            self.tblMetadata.clearContents()
            return
        self.btnNext.setEnabled(True)
        self.btnPrev.setEnabled(True)
        self.gifs = gifs
        self.current = 0
        self.displayGif(self.gifs[self.current])
    
    def chooseDir(self):
        controller.setDir(QFileDialog.getExistingDirectory(self, "Seleccionar carpeta").replace("/", "\\"))

    def displayGif(self, gifToDisplay:Gif):
        tbl = self.tblMetadata
        tbl.clearContents()
        tbl.setColumnCount(2)
        tbl.setHorizontalHeaderLabels(["",""])

        tags = ["Ruta", "Version", "Tamaño", "# Colores", "Tipo de compresión", "Formato numerico", "Fondo", "# Imagenes", "Fecha de creacion", "Fecha de modificacion", "Comentarios"]
        tbl.setRowCount(len(tags))
        tbl.itemChanged.disconnect()
        for i in range(len(tags)):
            tag =  tags[i]
            tbl.setItem(i, 0, QTableWidgetItem(tag))
        if gifToDisplay:

            gifVals = str(gifToDisplay).split(",")
            for i in range(len(gifVals)):
                tbl.setItem(i, 1, QTableWidgetItem(gifVals[i]))
        tbl.itemChanged.connect(lambda:self.editGif())
#        tbl.setItem(0, 1, gifToDisplay.path)

        tbl.resizeColumnsToContents()
        self.lblGif.clear()
        animation = QMovie(gifToDisplay.path)
        animation.setFormat(b"gif")
        animation.setScaledSize(self.lblGif.size())
        animation.start()
        self.lblGif.setMovie(animation)

    def editGif(self):
        if self.gifs  and len(self.gifs) > 0:
            path = self.tblMetadata.item(0, 1).text()
            info = []
            for i in range(1, 11):
                info.append(self.tblMetadata.item(i, 1).text())
            self.gifs[self.current] = Gif(path, info)
    

    def nextGif(self):
        if self.current < len(self.gifs) - 1:
            self.current += 1
        else:
            self.current = 0
        self.displayGif(self.gifs[self.current])
    
    def prevGif(self):
        if self.current > 0:
            self.current -= 1
        else:
            self.current = len(self.gifs) - 1
        self.displayGif(self.gifs[self.current])

    def closeEvent(self, event):
        controller.saveGifs(self.gifs)
        event.accept()


def run():
    analizer = QApplication([])
    window = MainWindow()
    window.show()

    analizer.exec()
    return window

if __name__ == "__main__":
    run()