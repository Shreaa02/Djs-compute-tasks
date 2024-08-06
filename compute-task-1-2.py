
register = ["Gunther", "karzan", "pip1do", "amelia", "emma", "jarzk", "P0ppy", "gunther", "Daisy"," Demelza ", "Lisa ", "garzon ", "marz4"]
Humans = []
Aliens = []


def sort_humans(r):
    for k in register:
        i = k.lower()
        flag = 0
        for j in i:
            if j.isdigit():
                flag +=1 
        if i[0] == 'g' or 'arz' in i or flag !=0  :
            if i not in Aliens:
                Aliens.append(i)           
        else:
             Humans.append(i)
    print(f"Humans = {Humans}")
    print(f"Aliens = {Aliens}")

#__main__
sort_humans(register)