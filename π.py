p=0

for i in range (1,2000):
 if ( i % 2 == 0):
   p = p - (4.0 / (2 * i - 1));

 else:
   p = p + (4.0 / (2 * i - 1));	

print"The value of p is %.2f "%(p)
