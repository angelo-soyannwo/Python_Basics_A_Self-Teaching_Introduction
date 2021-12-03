l1 = [ 3, 6, 1, 8, 5]
l2 = [ 7, 4, 6, 2, 9]
i1 = iter(l1)
i2 = iter(l2)
l3 = sorted( list(i1) + list(i2) )
print( 'List1 - ', l1, '\nList2 - ', l2, '\nSortedCombn - ',
l3 )
