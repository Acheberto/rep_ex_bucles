lnombreporducto = ['pan','manzana', 'pera', 'platano']
lprecioporducto = ['1','2', '4', '7']

x = 0
while True :
    try:
        if float (lprecioporducto[x]) > 3:
            print("El producto {} con el precio {} es caro".format(lnombreporducto[x],lprecioporducto[x]))

        else :
            print("El producto {} con el precio {} es barato".format(lnombreporducto[x],lprecioporducto[x]))

        x +=1
    except:
        break