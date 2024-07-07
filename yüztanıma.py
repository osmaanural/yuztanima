import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image,ImageTk  ## Gray formatına çevirmek için

###Fonksiyon Üret

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        img=cv2.imread("ata.jpeg")  ## dosya yolu var ise dosyayı okur.
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) ## Resmi griye çevirir.
        faces=face_cascade.detectMultiScale(gray,scaleFactor=1.05,minNeighbors=5,minSize=(30,30))  ## Fotoğraftaki yüzleri arar. Scale Factor ile yüzleri küçültür.

        for (x,y,w,h) in faces:  ## x yapay çizgiyi y dikey çizgiyi ifade eder. 2 genişliği h yüksekliği ifade eder.
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)   ##255,0,0 renk kodlarıdır , 2 ise kalınlıktır.
            cv2.putText(img,"insan",(x,y+h+20),cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,0,0),2)
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB) ##resmi tekrar renkliye dönüştürürüz.
        img=Image.fromarray(img)
        img=img.resize((600,400),Image.LANCZOS)
        img=ImageTk.PhotoImage(img)


        canvas.img=img
        canvas.create_image(0,0,anchor=tk.NW,image=img)  #tk.nw ile resim tekrar yüklenince önceki silinir.
        ## Crate ile resmi oluşturuurz. 0,0 noktasında oluşruur.Yeni resim ekleneceği zaman canvas alanına sıfırlanır. img'nin yüklenmesini isteriz.


face_cascade=cv2.CascadeClassifier('C:/Users/osmaa/AppData/Local/Programs/Python/Python310/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')



root=tk.Tk()

root.title("Yüz Algılama")
canvas=tk.Canvas(root,width=600,height=400)
canvas.pack()
open_button=tk.Button(root,text="Dosya Seç",command=open_file)
open_button.pack()




root.mainloop()


