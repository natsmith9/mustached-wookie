__author__ = 'Nathan A. Smith'


bottles = 99

while bottles > 1:
    print(str(bottles) + " bottles of beer on the wall" + str(bottles) + " bottles of beer," \
        " take one down, pass it around " + str(bottles - 1) + " bottles of beer on the wall!\n")
    bottles -= 1

print(str(bottles) + " bottle of beer " + str(bottles) + " bottle of beer," \
      "take one down, pass it around, no more bottles of beer on the wall!")