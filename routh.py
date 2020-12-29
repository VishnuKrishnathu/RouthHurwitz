from pandas import DataFrame
def zero_func(array, length):
    if len(array)!= length:
        for i in range(len(array), length):
            array.append(0)
    return array

print("\n\n######################################### Routh's Criteria #########################################\n\n")
order = input("Enter the order of the system: ")
equation = []
for i in range(int(order), -1, -1):
    equation.append(int(input("Enter the coefficietnt of s^" + str(i) + ": ")))
table = []
layer1 = []
for i in range(0, len(equation),2):
    layer1.append(equation[i])
table.append(layer1)
layer2 = []
for i in range(1, len(equation),2):
    layer2.append(equation[i])
layer2 = zero_func(layer2, len(layer1))
table.append(layer2)
for i in range(2, len(equation)):
    layers = []
    for j in range(0, len(layer1)-1):
        layers.append(round((table[i-1][0]*table[i-2][j+1] - table[i-2][0]*table[i-1][j+1])/table[i-1][0], 2))
    layers = zero_func(layers, len(layer1))
    table.append(layers)
print(DataFrame(table))