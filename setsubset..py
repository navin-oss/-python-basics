set1={'Ram','shyam','Om'}
set2={'Om','soham','ojas'}
set3={'Ram','shyam','Om'}
print(set1.isdisjoint(set2))
print(set1.issubset(set2))
print(set1 <= set3)#Its nothing but subset 
print(set1.issuperset(set2))
print(set1>=set3)
del set2 #This delete items as well as set so we cant print set 2 now.
