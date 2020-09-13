
def harmonise_fetes_nationales(text):
    if text[0:4]=="les ":
        return ("des" +text[3:])
    elif text[0] in ["a","e","i","o","u","y","A","E","I","O","U","Y","î"]:
        return ("d'"+text)
    elif text[0:3]=="le ":
        return ("du" +text[2:])
    else:
        return ("de "+text)

def text_affiche(tag,text):
    if tag == "fetes_nationales":
        return f"Trinquons pour la fête nationale {harmonise_fetes_nationales(text[0])}!"
    elif tag=="":
        return "Trinquez pour vous même, il n'y a rien de spécial à fêter."
    elif tag== "journee":
        return f"Trinquons pour la {text[0]}!"
    elif tag=="royaute"or tag=="histoire":
        return f"Trinquons pour {text[0]}!"
    else:
        return f"Oups il y a une erreur"
