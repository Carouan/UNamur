
## Exo 7

## Définition des varibales de prix et de dates

Prix = float(input('Prix du ticket  :'))
## da = date d'achat
da = float(input('date d''achat du ticket (un nombre)  :'))

## dv = date du vol
dv = float(input('date du vol (un nombre)  : '))

## Vérif si dv > da

## dd = différence entre date du vol et date d'achat

dd = dv-da

##-------

# Fonction de calcul du prix

def get_ticket_price(Prix,dd):

    if (dd >= 100) :
        Prix= Prix *0.5
    elif (dd < 3) :
        Prix = Prix + (dd*15)+100
    elif (dd <= 30) :
        Prix = Prix + (dd*15)
    else :
        return Prix
    return Prix



print (get_ticket_price(Prix,dd))

##print("Le prix de votre ticket sera de : "Prix"")
