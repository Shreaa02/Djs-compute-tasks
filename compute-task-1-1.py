code_names = ["Orion", "Barracuda", "Amethyst", "Blade", "Wasp", "Nemesis", "Fury", "Cobra", "Tempest", "Leo", "Scythe"]



def codename_generator(cn):
    a = ""
    b =""
    names = []
    for i in range(len(cn)):
        a = code_names[i]
        for j in range(len(cn)):
            n = []
            b = cn[j]
            x = a
            y = b
            l = ( a+" "+b)
            k= (b+" "+a)
            if a!= b and k not in names :
                 names.append(l)
                 print(l)

codename_generator(code_names )