set1={'Ram','shyam','Om'}
set2={'Om','soham','ojas'}
set3={'anuj','Pran','atul'}
print(set1.union(set2))
#print(set2.union(set1)) this is same as previous
print(set1 | set2)
print(set1.union(set2,set3))
print(set1.union(('om','raj')))
set1.update(['OM','Ram'])
print(set1)

#Intersection
print(set1.intersection(['Mohan','Shova']))
print(set1 & set2)
set1.intersection_update(set2)
print(set1)