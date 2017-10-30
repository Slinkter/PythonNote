countries = {
'mexico':122,
'colombia':49,
'argentina':43,
'chile':18,
'peru':31
}

while True:
    country= str(input("escribir el nombre de un país : ")).lower()
    try:
        print("la poblacion de {} es : {} millones ".format(country,countries[country]))
    except KeyError:
        print("no existe infomación sobre ese país {} ".format(country))
