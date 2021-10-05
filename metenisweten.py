input ('Verzoek')

a = input ('Vul een heel getal in ')
print ('')

b = input ('Vul een heel getal in ')
print ('')

max = int(a)
min = int(b)

if max > min:
    print('a is het grootste getal: ' + str(max))

elif max < min : 
    print('a is het kleinste getal: ' + str(min))

else:
        print('a en b zijn even groot')