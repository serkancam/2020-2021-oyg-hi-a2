import cv2
import numpy as np
import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5 import uic
from PyQt5.QtGui import QImage, QPixmap
import time,threading

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
        self.win.closeEvent = self.closeEvent
    def closeEvent(self, event):
        self.kamera_durumu=False
        print("program kapanıyor")

    def kamera_ac_kapa(self):       
        self.kamera_durumu = not self.kamera_durumu
        print("Kamera durumu:",self.kamera_durumu)  
        if self.kamera_durumu:
            self.kamera_thread = threading.Thread(target=self.kamera)
            self.kamera_thread.start()
        # threading.Thread(target=self.kamera,args=()).start() 
        # if not x.is_alive():
        #     print("Kamera açıldı")
        #     self.x.start()
        # print("test")
       
        
          
          
       
    def kamera(self):
      
        haar_path=os.path.join(self.cd,"opencv","haarcascade_frontalface_alt.xml")
        face_cascade = cv2.CascadeClassifier(haar_path)
        cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)# ilk kamera 0 sonrası 1 ....
        

        while self.kamera_durumu:
           
            ret,frame = cam.read()          
            gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray,1.3,5)
            face_s=0
            for (x,y,w,h) in faces:
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
                face_s+=1
            # print("yuz sayısı=",face_s)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.resize(frame, None, fx=0.6, fy=0.6,interpolation=cv2.INTER_AREA)
            height, width, channel = frame.shape
            step = channel*width
            qImg = QImage(frame.data, width, height,step, QImage.Format_RGB888)            
            self.win.lblCam.setPixmap(QPixmap.fromImage(qImg))
            cv2.waitKey(50)           
            if not(self.kamera_durumu):                        
                break
        cam.release()
        cv2.destroyAllWindows()
        self.win.lblCam.clear()     
        print("thread kapatıldı")
        
      
       
        
    
       




if __name__ == "__main__":
    app = QApplication(sys.argv)
    uygulama = App()
    sys.exit(app.exec_())