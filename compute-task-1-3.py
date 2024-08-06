Aliens = ['gunther', 'karzan', 'pip1do', 'jarzk', 'p0ppy', 'garzon', 'marz4']
alien_probabilty ={}
for i in Aliens:
    if i.isalpha():
       if i[0] =='g' and 'arz' in i :
         alien_probabilty[i]=75
       elif 'arz' in i :
          alien_probabilty[i]=50
       elif i[0] == 'g':
           alien_probabilty[i]=25
    else:
         for j in i:
            if j.isdigit():
                alien_probabilty[i]=100

     
        
print( alien_probabilty)
    