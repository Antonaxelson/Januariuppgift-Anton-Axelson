import csv
# gör det lättare att joba med csv

from csv import writer
# Import writer class from csv module för att göra det enkelt att skriva till csv

import matplotlib.pyplot as plt
#libery av där man kan printa värden på graf och liknande




def visatomkarta():
    im = plt.imread('köpenhamn.png')
    implot = plt.imshow(im)

    plt.xlabel('')
    plt.ylabel('')
    plt.title('karta av minor', fontsize = 20)
    plt.grid()
    plt.legend()
    plt.show()    
    # tilllägg på kartan




def inpuEn():
    x = input("skriv x kordinat innom gränserna av kartan")
    y = input("skriv y kordinat innom gränserna av kartan")

    List=[x,y]
    #listan fylls av inputen
    with open('kordinat.csv', 'a') as f_object:
  
    # Pass this file object to csv.writer()
    # and get a writer object
        writer_object = writer(f_object)
  
    # Pass the list as an argument into
    # the writerow()
        writer_object.writerow(List)
  
    #Close the file object
        f_object.close()

    

def printa(): 
    x = []
    y = []
# tomma listor som sedan fylls av värdena från csv filen
    im = plt.imread('köpenhamn.png')
    implot = plt.imshow(im)
    #bakrundsbilden på köpenhamn


 

    with open('kordinat.csv','r') as csvfile:
        lines = csv.reader(csvfile, delimiter=',')
        for row in lines:
            x.append(int(row[0]))
            y.append(int(row[1]))
            # lägger x från csv där x ska vara och samma med y
            
    plt.scatter(x, y, color = 'g', linestyle = 'dashed',marker = 'o',label = "Weather Data")
    #lägger ut det på kartan
  

    plt.xlabel('')
    plt.ylabel('')
    plt.title('karta av minor', fontsize = 20)
    plt.grid()
    plt.legend()
    plt.show()



vad_ska_göras = input("om du vill skriva in kordinat skriv kordinat\nOM du vill kolla på kartan skriv blank karta\nOm du vill se kartan med minorna skriv något bara: ")
if vad_ska_göras == str("kordinat"):
    inpuEn()
    print("nu har värdena skrivits ner")
elif vad_ska_göras == str("blank karta"):
    visatomkarta()

else:
    printa()
       


