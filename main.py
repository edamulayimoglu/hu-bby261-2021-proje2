
from tkinter import*
from random import randint
pencere =Tk()
pencere.geometry("300x300+200+200")
pencere.title("Yeni Harry Potter'ı Arıyoruz! ")
pencere.configure(bg="pink")

giris = Label(pencere,text="Seçilmiş Kişisin!",fg="yellow", bg="purple")
giris.pack()
giris.config(font=("Arial", 20))
giris.grid()

def sayisal():
    i = 0
    secilenler = [0,0,0,0,0,0]
    for rastgele in secilenler:
        while i < len(secilenler):
            secilen = randint(1, 49)
            if secilen not in secilenler:
                secilenler[i] = secilen
                i+=1
        siralanan = (sorted(secilenler))
        i=0

        buton = Label(pencere,text=siralanan)
        buton.config(font=("Arial",16 ))
        buton.grid(column=10, row=10)
        buton.grid()

sayılar= Button (pencere, text="Şanslı Sayılarımı Listele" ,fg="black", bg="white", command=sayisal)
sayılar.config(font=("Arial", 14))
sayılar.grid(column=0, row=10)
sayılar.grid()

def bilgi():
    dosya ="Size nasıl yardımcı olabiliriz? bknz: 1. Şanslı Sayılarımı Listele adlı butona her tıklamanızda 6 adet yeni sayı dizisi ile karşılaşacaksınız. 2. Çıkış'a tıkladığınızda sistemden ayrılmış olacaksınız "
    bilgi = Label(pencere, text= dosya)
    bilgi.config(font=("Arial", 23))
    bilgi.grid(column=12, row=14)
    bilgi.grid()

yardım= Button(pencere, text=" Yardım'a mı ihtiyacınız var?", fg="black", bg="white", command= bilgi)
yardım.config(font=("Arial", 14))
yardım.grid()



cikis = Button (pencere, text="Çıkış", command= pencere.quit,fg="white", bg="red")
cikis.config(font=("Arial", 12))
cikis.grid(column=0, row=20)
cikis.grid()
pencere.mainloop()