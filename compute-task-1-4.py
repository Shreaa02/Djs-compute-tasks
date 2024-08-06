your_districts = ['I', 'IV', 'V', 'I', 'VI', 'IX', 'X', 'II', 'III', 'I']
their_districts = ['V', 'IV', 'VI', 'XII', 'VII', 'IV', 'VI', 'VIII', 'III']
patrolled_districts = ['I', 'II', 'XII', 'IX', 'XI', 'IV', 'II', 'VI']
meet = set()


def common_districts(your_districts,their_districts):
    yd = set(your_districts)
    td = set(their_districts)
    meet.update(yd.intersection(td))
    return meet
    


common_districts(your_districts,their_districts)
pd =  set(patrolled_districts)
npd = meet.difference(pd)
print(f"Meet Up Districts:{meet}")
print(f"New Meet Up Districts: {npd}")