## exo 8

amount = float(input("Montant a convertir : "))
currency = input("Monnaie de départ : ")
taux = 1.12586
chg = flaot(input("Taux de change : "))



def currency_conversion (amount, currency,chg) :
##        """ Specification de la fonction

##    Paramètres
##    ---------
##    amount : amount to convert (float)
##    currency : currency of amount
##    chg = taux

##      Returns 
##      -------
##      result : converted currency (float)
##
##      Notes
##      ------
##      Use E for Euro or S for dollar
##      1E = 1.12586 S
##
    if (currency =="E") :
        amount = amount*chg
        print("Vous aurez "amount" dollars")
    elif (currency =="S") :
        print("Vous aurez "amount * chg " euro")
    else :
        print("Monnaie inconnue")


currency_conversion()