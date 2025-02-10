#  app.py
import os
from PyQt5.QtWidgets import (
        QApplication, QWidget, QListWidget,
        QHBoxLayout, QVBoxLayout,
        QPushButton,QFileDialog,QLabel)

from qss import QSS

from PyQt5.QtCore import Qt # потрібна константа Qt.KeepAspectRatio для зміни розмірів із збереженням пропорцій
from PyQt5.QtGui import QPixmap # оптимізована для показу на екрані картинка
from PIL import Image,ImageFilter

app = QApplication([])
win = QWidget()

win.resize(1000, 800)
win.setObjectName("mainWindow")
win.setWindowTitle('chicken_file')
win.setStyleSheet(QSS)

lb_image = QLabel("Картинка")
btn_dir = QPushButton("Папка")
lw_files = QListWidget()


btn_left = QPushButton("Уліво")
btn_right = QPushButton("Управо")
btn_flip = QPushButton("Дзеркало")
btn_sharp = QPushButton("Різкість")
btn_bw = QPushButton("Ч/Б")
btn_custom = QPushButton('будь-яка')

row = QHBoxLayout()          # Основний рядок
col1 = QVBoxLayout()         # ділиться на два стовпці
col2 = QVBoxLayout()
col1.addWidget(btn_dir)      # у першому – кнопка вибору директорії
col1.addWidget(lw_files)     # та список файлів
col2.addWidget(lb_image, 95) # у другому - картинка
row_tools = QHBoxLayout()    # та рядок кнопок
row_tools.addWidget(btn_left)
row_tools.addWidget(btn_right)
row_tools.addWidget(btn_flip)
row_tools.addWidget(btn_sharp)
row_tools.addWidget(btn_bw)
row_tools.addWidget(btn_custom)
col2.addLayout(row_tools)

row.addLayout(col1, 30)
row.addLayout(col2, 70)
win.setLayout(row)

win.show()

workdir = ""

def filter(files, extensions):
   result = []
   for filename in files:
       for ext in extensions:
           if filename.endswith(ext):
               result.append(filename)
   return result


def chooseWorkdir():
   global workdir
   workdir = QFileDialog.getExistingDirectory()


def showFilenamesList():
   extensions = [".jpg",".jpeg", ".png", ".gif", ".bmp"]
   chooseWorkdir()
   filenames = filter(os.listdir(workdir), extensions)
   lw_files.clear()
   for filename in filenames:
       lw_files.addItem(filename)
class Image_processor:

    def __init__(self):
        self.image = None
        self.dir = None
        self.image_name = None
        self.save_dir = 'Dumbledore/'
    def LoadImage(self,dir,image_name):
        self.dir = dir
        self.image_name = image_name
        image_path = os.path.join(dir,image_name)
        self.image = Image.open(image_path)

    def saveImage(self):
        ''' зберігає копію файлу у підпапці '''
        path = os.path.join(self.dir, self.save_dir)
        if not (os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        image_path = os.path.join(path, self.image_name)
        self.image.save(image_path)

    def showImage(self, path):
        lb_image.hide()  # Ховає елемент `lb_image`, щоб під час зміни зображення користувач не бачив проміжного стану.
        pixmapimage = QPixmap(path)  # Завантажує зображення з вказаного шляху (`path`) у об'єкт `QPixmap`.
        w, h = lb_image.width(), lb_image.height()  # Зберігає поточну ширину (`w`) і висоту (`h`) віджета `lb_image`.
        pixmapimage = pixmapimage.scaled(w, h,Qt.KeepAspectRatio)  # Масштабує зображення, щоб воно відповідало розмірам `lb_image`, зберігаючи пропорції.
        lb_image.setPixmap(pixmapimage)  # Встановлює масштабоване зображення в якості вмісту для віджета `lb_image`.
        lb_image.show()
    def Do_BW(self):
        self.image = self.image.convert("L")
        self.saveImage()
        image_path = os.path.join(self.dir,self.save_dir,self.image_name)
        self.showImage(image_path)

    def left (self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.saveImage()
        image_path = os.path.join(self.dir,self.save_dir,self.image_name)
        self.showImage(image_path)


    def right (self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.saveImage()
        image_path = os.path.join(self.dir,self.save_dir,self.image_name)
        self.showImage(image_path)


    def mirrror (self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.saveImage()
        image_path = os.path.join(self.dir,self.save_dir,self.image_name)
        self.showImage(image_path)

    def sharping (self):
        self.image = self.image.filter(ImageFilter.SHARPEN)
        self.saveImage()
        image_path = os.path.join(self.dir,self.save_dir,self.image_name)
        self.showImage(image_path)


    def add_frame(self):
        texture = Image.open("wizard_frame.png")
        width, height = self.image.size
        texture = texture.resize((width, height))
        self.image.paste(texture, (0, 0), texture)

        self.saveImage()
        image_path = os.path.join(workdir,
                                  self.save_dir, self.image_name)
        self.showImage(image_path)




def showChosenImage():
    if lw_files.currentRow() >= 0:
        image_name = lw_files.currentItem().text()
        workimage.LoadImage(workdir,image_name)
        image_path = os.path.join(workimage.dir,workimage.image_name)  # Створює повний шлях до зображення, поєднуючи директорію та ім'я файлу.
        workimage.showImage(image_path)




btn_dir.clicked.connect(showFilenamesList)

workimage = Image_processor() #поточне робоче зображення для роботи

lw_files.currentRowChanged.connect(showChosenImage)
btn_bw.clicked.connect(workimage.Do_BW)
btn_left.clicked.connect(workimage.left)
btn_right.clicked.connect(workimage.right)
btn_flip.clicked.connect(workimage.mirrror)
btn_sharp.clicked.connect(workimage.sharping)
btn_custom.clicked.connect(workimage.add_frame)
app.exec()








