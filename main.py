#importare le librerie necessarie per i grafici
import matplotlib.pyplot as plt
import numpy as np


def retta(m,q):
    #procedura per disegnare la retta

    #definire gli assi 
    x_min = -1e2
    x_max = 1e2
    x = np.linspace(x_min, x_max, 1000) #
    y = m * x + q  #ordinate di ogni punto (equazione retta)

    #punti di intersezioni con i due assi
    y_int = q
    x_int = -q / m if m != 0 else np.inf 
    plt.plot(x, y, label=f'y = {m}x + {q}')
    if x_int != np.inf:
        #evidenziare i punti di intersezione
        plt.scatter(x_int, 0, color='red') 
        plt.text(x_int, 0, f'({x_int:.1f}, 0)', fontsize=10, ha='left') 


    #rifiniture grafiche
    plt.scatter(0, y_int, color='blue') 
    plt.text(0, y_int, f'(0, {y_int:.1f})', fontsize=10, ha='right')
    plt.title('Grafico della retta')
    plt.xlabel('Ascisse')
    plt.ylabel('Ordinate')
    plt.grid(True)
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)
    plt.legend()
    plt.show()

def parabola(a,b,c):
    #procedura per disegnare la parabola

    #definire gli assi
    x_min = -1e1
    x_max = 1e1
    x = np.linspace(x_min, x_max, 1000)
    y = a *x*x + b*x + c #ordinate dei punti (equazione parabola)
    y_int = c
    delta = b**2 - 4*a*c #calcolo del delta

    #calcolo delle intersezioni con l'asse x in base al valore del Delta
    if delta > 0:
        intersezioni = [ ]
        xint_1 = (-b + np.sqrt(delta)) / (2*a) 
        xint_2 = (-b - np.sqrt(delta)) / (2*a)
        intersezioni.append(xint_1)
        intersezioni.append(xint_2)
        plt.scatter(0, y_int, color='blue') 
        for i in intersezioni:
            #evidenziare i punti di intersezione
            plt.scatter(i, 0, color='red')
            plt.text(i, 0, f'({i:.1f}, 0)', color = 'red' ,  fontsize=10, ha='left')
    elif delta == 0:
        xint = -b  / (2*a) 
        plt.scatter(xint, 0 , color = 'red')
        plt.text(xint, 0,f'({xint:.1f}, 0)', fontsize=10, ha='left' )
    elif delta < 0:
                plt.text(0, 0, 
                 "Nessuna intersezione con l'asse x.", 
                 fontsize=10, 
                 ha='left')

    #rifiniture grafiche
    plt.plot(x, y)
    plt.title('Grafico della parabola')
    plt.xlabel('Ascisse')
    plt.ylabel('Ordinate')
    plt.xlim(x_min, x_max)
    plt.ylim(np.min(y), np.max(y))
    plt.grid(True)
    plt.axhline(0, color='black',linewidth=1)
    plt.axvline(0, color='black',linewidth=1)
    plt.show()

def circonferenza(xc,yc,r):
    #procedura per disegnare la circonferenza

    #genera l'array di angoli da 0 a 360 gradi
    theta = np.linspace(0, 2*np.pi, 1000)

    #calcola il coseno  e il seno di ogni angolo theta che       
    #verranno moltiplicati per il raggioverranno moltiplicati        per il raggio
    #e sommmati alle coordinate del centro
    x = xc + r * np.cos(theta)
    y = yc + r * np.sin(theta)

    #rifiniture grafiche
    plt.plot(x,y)
    plt.title('Grafico della circonferenza')
    plt.xlabel('Ascisse')
    plt.ylabel('Ordinate')
    plt.grid(True)
    plt.axhline(0, color='black',linewidth=1)
    plt.axvline(0, color='black',linewidth=1)
    plt.show()

def ellisse(a,b):
    #procedura per disegnare l'ellisse

    #genera l'array di angoli da 0 a 360 gradi
    theta = np.linspace(0, 2 * np.pi, 1000)


    #calcola il coseno e il seno per ogni angolo theta e viene 
    #moltiplicato per i due parametri dell'equazione dell'ellisse
    #ottenendo le coordinate dei punti
    x = a * np.cos(theta) 
    y = b * np.sin(theta)
    #ottenendo le coordinate dei punti
    x = a * np.cos(theta) 
    y = b * np.sin(theta)

    #rifiniture grafiche
    plt.plot(x, y,)
    plt.title("Grafico dell Ellisse")
    plt.xlabel('Ascisse')
    plt.ylabel('Ordinate')
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)
    plt.grid(True)
    plt.show()

def main():
    #menu dove l'utente inserisce l'input del luogo geometrico
    while True:
        luogog = int(input("Inserisci il luogo geometrico che vuoi graficare: \n"
                         + "1. Retta \n"
                         + "2. Parabola \n"
                         + "3. Circonferenza \n"
                         + "4. Ellisse \n"
                         + "5. Exit \n"))
        match luogog:
            case 1:
                m = float(input("Inserisci il coefficiente angolare: "))
                q = float(input("Inserisci l'intercetta y: "))
                retta(m,q)
            case 2:
                a = float(input("Inserisci il coefficiente a: "))
                b = float(input("Inserisci il coefficiente b : "))
                c = float(input("Inserisci l'intercetta y (coefficiente c): "))
                parabola(a,b,c)
            case 3:
                xc = float(input("Inserisci la coordinata x del centro: "))
                yc = float(input("Inserisci la coordinata y del centro: "))
                r = float(input("Inserisci il raggio: "))
                circonferenza(xc,yc,r)
            case 4:
                a = float(input("Inserisci il coefficiente a: "))
                b = float(input("Inserisci il coefficiente b: "))
                ellisse(a,b)
            case 5:
                break
if __name__ == "__main__":
    main()            
