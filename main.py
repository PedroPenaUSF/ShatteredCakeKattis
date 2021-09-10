# Step 1 accept user input which will be width of cake then second input is amount of pieces of cake

width = int(input())
cakePieces = int(input())
areaOfCake = 0

# Step 2 loop to accept line of input. split input by " " and first element * second element is area of that piece

for i in range(cakePieces):
    a = input()
    a = a.split(' ')
    w = int(a[0])
    l1 = int(a[1])
# Step 3 multiply elements and add to area of cake. at end of loop total area of cake should be found.
    areaOfCake = (w * l1) + areaOfCake
# Step 4 A = L X W so L = A/W
length = int(areaOfCake/width)

print(length)
