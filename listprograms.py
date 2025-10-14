foodlist = ['apple','ice cream','cereal','grape']

print ("First item", foodlist[0])
print ("Last item", foodlist[3])

def replaceitem():
    foodlist[1] = 'banana'
    print(foodlist)
    print ("replaced ice cream with banana")
def slice():
    print(foodlist[1:3])

replaceitem()
slice()
