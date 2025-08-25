import random

print("Mietin numeroa väliltä 1-100. Pystytkö  arvaamaan sen?🎰")


def pelaa_numeropeli():
    numero = random.randint(1, 100)
    arvaukset = 0
    while True:
        try:
            arvaus = int(input("Syötä arvauksesi: "))
            arvaukset += 1
            if arvaus < numero:
                print("Numero on isompi.☹️ Yritä uudelleen!")
            elif arvaus > numero:
                print("Numero on pienempi.☹️ Yritä uudelleen!")
            else:
                print(f"Oikein!✅ Arvasit oikein! Numero oli {numero}. Arvasit tämän {arvaukset}. yrityksellä!")
                break
        except ValueError:
            print("Syötä vain kokonaislukuja!⚠️")


def main():    
    while True:
        pelaa_numeropeli()

        uusipeli = input("Pelataanko uudelleen? (k/e):").strip().lower()
        if uusipeli != "k":
            print("Kiitos näkemiin! 👋")
            break
if __name__ == "__main__":
    main()