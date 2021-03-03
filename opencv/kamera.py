import cv2
import numpy as np
import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5 import uic
from PyQt5.QtGui import QImage, QPixmap
import time

class App(QMainWindow):
    def __init__(self):
        super(App,self).__init__()
        self.cd = os.getcwd()
        self.ui_path=os.path.join(self.cd,"opencv","kamera.ui")
        self.kamera_durumu=False # kamera durumunuı tutacak        
        self.InitUI()

    def InitUI(self):
        self.win = uic.loadUi(self.ui_path)
        # event 
        self.win.btnCam.clicked.connect(self.kamera_ac_kapa)
        self.win.show()

    def kamera_ac_kapa(self):
        # print("Tıklandı")
        haar_path=os.path.join(self.cd,"opencv","haarcascade_frontalface_alt.xml")
        face_cascade = cv2.CascadeClassifier(haar_path)
        cam = cv2.VideoCapture(0)# ilk kamera 0 sonrası 1 ....
        self.win.lblCam.clear()
        self.kamera_durumu = not self.kamera_durumu
        while self.kamera_durumu:
            ret,frame = cam.read()
            frame = cv2.resize(src=frame,dsize=None,fx=0.7,fy=0.7,interpolation=cv2.INTER_AREA)
            gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray,1.3,5)
            face_s=0
            for (x,y,w,h) in faces:
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
                face_s+=1
            print("yuz sayısı=",face_s)
            h,w,c = frame.shape

            frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            step =w*c # tarama kaç adımda olacak
            lblImg = QImage(frame.data, w, h,step,QImage.Format_RGB888)
            self.win.lblCam.setPixmap(QPixmap.fromImage(lblImg))
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        cam.release()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    uygulama = App()
    sys.exit(app.exec_())