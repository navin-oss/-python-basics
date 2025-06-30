set1={'Ram','shyam','Om'}
set2={'Om','soham','ojas'}
set3={'anuj','Pran','atul'}
print(set1.difference(set2))#Gives item in set 1 which are not in set 2.
#print(set1 - set2)
#print(set1.difference(set2,set3))#Gives item in set 1 which are not in set 2 and in set 3.
set2.difference_update(set1)
print(set1)
print(set2)
#symmeteic difference = not written common terms remaining all are written. 
print(set1.symmetric_difference(set2))#symmetric difference not allowed in multiple sets.
print(set1 ^ set2)
set2.symmetric_difference_update(set1)#same as above.
print(set2)
print(set1.isdisjoint(set2))
print(set1.issubset(set2))
