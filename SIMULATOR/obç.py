from tkinter import *
import time

pencere = Tk()
pencere.title("Simulasyon")
pencere.geometry("200x200+350+150")
pencere.config(bg = "black")
pencere.resizable(FALSE,FALSE)

#//pencere olusturduk
isim = Label(pencere,bg="green",fg="white",font="Calibri 15 italic",text="Onur Başar ÇINAR")
isim.pack(expand=YES)
#//isim etiketi oluşturduk ve adını yazdırdık

no = Label(pencere,bg="green",fg="white",font="Calibri 12 italic",text="9-A/124")
no.pack(expand=YES)
#//numara etiketi oluşturduk ve okul numarasını yazdık

def start():

    pencere2 = Tk()
    pencere2.title("Simulasyon")
    pencere2.geometry("300x300+400+200")
    pencere.destroy()
    pencere2.resizable(FALSE,FALSE)
    pencere2.config(bg="black")

    #//içeride bir pencere oluşturduk
    
    hiz11 = Label(pencere2,bg="blue",fg="white",text="İlk Hız: ")
    hiz11.grid(column=1,row=1)
    #//hiz1 etiketi oluşturduk

    hiz12 = Entry(pencere2)
    hiz12.grid(column=2,row=1)

    #//hiz1 girişi oluşturduk

    hiz21 = Label(pencere2,bg="blue",fg="white",text="İkinci Hız: ")
    hiz21.grid(column=1,row=2)
    
    #//hiz2 etiketi oluşturduk
    
    hiz22 = Entry(pencere2)
    hiz22.grid(column=2,row=2)
    
    #//hiz2 girişi oluşturduk

    timing11 = Label(pencere2,bg="blue",fg="white",text="Geçen Süre: ")
    timing11.grid(column=1,row=3)

    #//timing1 etiketi oluşturduk

    timing12 = Entry(pencere2)
    timing12.grid(column=2,row=3)

    #//timing1 girişi oluşturduk

    def hesap1():
        
        ivmeilk = float(hiz22.get())-float(hiz12.get())

        #//ivmenin ilk parçasını aldık
        
        ivme2 = float(ivmeilk)/float(timing12.get())

        #//ivmenin ikinci bölümünü aldık ve sonucu elde ettik

        ivmebildir = Label(pencere2,bg="blue",fg="white",text="İvme: "+str(ivme2)) 
        ivmebildir.grid(column=2,row=5)
        ivmebildir.config(height=3,width=18)

        #//bulduğumuz ivmeyi  yazdirdik

        if hiz12.get() < hiz22.get():
        #//cismin hızlanma-yavaşlama durumuna baktık
            hizlan = Label(pencere2,bg="blue",fg="white",text="Cisim hızlandı.")
            hizlan.grid(column=2,row=6)
            hizlan.config(height=3,width=18)
        else:
            yavasla = Label(pencere2,bg="blue",fg="white",text="Cisim yavaşladı.")
            yavasla.grid(column=2,row=6)
            yavasla.config(height=3,width=18)


        def grafiksel():

            grafik = Tk()
            grafik.title("Grafiksel İşlem")
            grafik.resizable(FALSE,FALSE)
            grafik.geometry("500x500+450+250")
            pencere2.destroy()

            logo = PhotoImage(file="logo.gif")

            logo2 = Label(grafik,image=logo)
            logo2.grid(column=1,row=1)

        graphical = Button(pencere2,bg="magenta",fg="white",text="Grafiksel Görünüm",command=grafiksel)
        graphical.config(height=3,width=18)
        graphical.grid(column=2,row=7)
        
        

        

        
        

    ivmebut = Button(pencere2,bg="white",fg="blue",text="İvme Hesapla",command=hesap1)
    ivmebut.grid(column=2,row=4)
    ivmebut.config(width=18,height=2)

    #//ivme hesaplama butonu oluşturduk

    

    

    
#//bir değişken tanımladık bunun üzerinden işlem yapacağız

    
	
	
	
basla = Button(pencere,bg="white",fg="green",font="Times 14 bold",text="BAŞLA",command=start)
basla.pack(expand=YES)
 
#//değişkeni aktive eden butonu oluşturduk



pencere.mainloop()
