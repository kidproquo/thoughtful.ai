def sort(width, height, length, mass):
  dim_limit = 150
  volume_limit = 1000000
  mass_limit = 20

  volume = width * height * length
  bulky = volume >= volume_limit or width >= dim_limit or height >= dim_limit or length >= dim_limit
  heavy = mass >= mass_limit

  if bulky and heavy:
    return "REJECTED"

  if bulky or heavy:
    return "SPECIAL"

  return "STANDARD"


#TEST CASES
#STANDARD
width = 10
height = 100
length = 100
mass = 10
s = sort(width, height, length, mass)
print('width:', width, 'height:', height, 'length:', length, 'mass:', mass, 'sort:', s)

#SPECIAL
width = 100
height = 100
length = 100
mass = 10
s = sort(width, height, length, mass)
print('width:', width, 'height:', height, 'length:', length, 'mass:', mass, 'sort:', s)

#REJECTED
width = 100
height = 100
length = 100
mass = 100
s = sort(width, height, length, mass)
print('width:', width, 'height:', height, 'length:', length, 'mass:', mass, 'sort:', s)
