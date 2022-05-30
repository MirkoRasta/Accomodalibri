from PyPDF2 import PdfFileReader, PdfFileWriter
import tkinter as tk
import tkinter.messagebox
import tkinter.filedialog
 
window = tk.Tk()   #inizializzo finestra
window.geometry("620x280")
window.title("Accomodabooks")
window.resizable(False,False)
window.configure(background='#3D4849')

input_file = 'Seleziona un PDF'

def aggiustalibro():    #Funzione che riordina le pagine ammodo
   global input_file

   if input_file == 'Seleziona un PDF':      #controlla se premo aggiusta prima di selezionare il file
       box_err=tk.messagebox.showinfo(title="No supporto", message="Seleziona un PDF")
       box_err.grid(row=2,column=20)      

   print("Riparato:  " + input_file)     #stampa il nome del file riparato         
   output_file = open(input_file[:(len(input_file)-4)] +'_aggiustato.pdf','wb')   #crea il fine in uscita

   read_pdf = PdfFileReader(input_file)    #legge il file di ingresso
   number_of_pages = read_pdf.getNumPages()

   if number_of_pages % 4 > 0 :     #aggiusta il numero di pagine per avere un file di pagine multiple di 4
      auxpdf=PdfFileWriter()
      auxpdf.appendPagesFromReader(read_pdf)
      for i in range(4- (number_of_pages % 4)):
        auxpdf.addBlankPage()
   else:
      auxpdf=read_pdf               #se è gia un multiplo di 4 va bene così

   number_of_pages = auxpdf.getNumPages()
   writer = PdfFileWriter()

   for i in range(int(number_of_pages/2)): #riordino effettivo
      page=auxpdf.getPage(i)
      writer.addPage(page)
      page=auxpdf.getPage(number_of_pages-1 - i)
      page.rotateClockwise(180)     
      writer.addPage(page)

   writer.write(output_file)   #scrive sul file
   output_file.close()    #chiude il pdf

def caricaPDF():   #tasto caricamento PDF
   global input_file
   input_file=tk.filedialog.askopenfilename(filetypes=(("PDF files","*.pdf"),("All files","*.*")))  #permette di selezionare solo PDF  
   
   per1=tk.Entry(window,font=40,width=35, background='light grey')   #box percorso
   per1.grid(row=1,column=1)
   per1.insert(tk.END, input_file)

text_path = tk.Label(window, text='Accomodalibri di MirkoRasta', font=("Helvetica",12), background="#3D4849",fg='white', width=30)  #titolo
text_path.grid(row=0,column=1,padx=10,pady=2)  

def chiudi_programma():
    ris = tkinter.messagebox.askyesno("Uscita","Sei sicuro di chiudere il programma?")
    if ris == True:
       window.destroy()   

textnome= "PDF selezionato:"     #testo prima
text_path = tk.Label(window, text=textnome, font=("Helvetica",11), fg="white", background="#3D4849")
text_path.grid(row=1,column=0,padx=20,pady=40,sticky='E')

per1=tk.Entry(window,font=40, background='light grey', width=35) #testo casella percorso
per1.grid(row=1,column=1,sticky='W')
per1.insert(tk.END, input_file)

path_button = tk.Button(text="Carica PDF", command=caricaPDF)     #bottone che carica
path_button.grid(row=1,column=2, padx=10, pady=30)

start_button = tk.Button(text="Aggiusta il libro", command=aggiustalibro)    #bottone che aggiusta
start_button.grid(row=2,column=1, padx=20, pady=20, sticky='EW')

close_button = tk.Button(text="Chiudi", command=chiudi_programma)    #bottone che chiude
close_button.grid(row=3,column=1, padx=20, pady=5)

text_path = tk.Label(window, text="Software avanzato per la riparazione di libri \n impaginati male da almeno 3500 anni", font=("Helvetica",10), fg="white",background="#3D4849")
text_path.grid(row=4,column=1) 

if __name__ == "__main__":
   window.mainloop()

