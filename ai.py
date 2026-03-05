"""
matrizes e tensores
redes neurais
backpropagation
otimizador
salvamento
inferencia
"""




def create_matrix(nums , length , width ):
    if len(nums) != length*width:
        return "erro de tamanho"
    
    counter_line = 0
    counter_column = 0
    num = 0
    matrix = list()

    while(counter_line <width ):
        new_line = list()
        counter_column = 0
        while (counter_column <length):
            new_line.append(nums[num])
            num+=1
            counter_column+=1

        matrix.append(new_line)
        counter_line +=1
    return matrix


def redefine_matrix(matrix , length , width):
    nums = list()
    for line in matrix:
        for num in line:
            nums.append(num)
    if len(nums) != length*width:
        return "erro de tamanho"
    
    matrix = create_matrix(nums=nums , length=length , width=width)
    return matrix

def num_columns(matrix):
    return len(matrix[0])

def num_lines(matrix):
    return len(matrix)

def multiply_matrixes(matrix1 , matrix2):
    new_matrix = list()
    if (num_columns(matrix1) != num_lines(matrix2)):
        return "Formato invalido de ultiplicaçao"
    
    for row in matrix1:
        new_line = list()
        for column in range(num_columns(matrix2)):
            sum = 0
            for i in range(num_lines(matrix2)):
                sum += row[i]*matrix2[i][column]
            new_line.append(sum)
        new_matrix.append(new_line)


    return new_matrix

def add_matrix(matrix1 , matrix2):
    if num_lines(matrix1)!=num_lines(matrix2) or num_columns(matrix1) != num_columns(matrix2):
        return "formato invalido"
    new_matrix = list()
    for row in range(num_lines(matrix1)):
        new_line = list()
        for column in range(num_columns(matrix1)):
            new_line.append(matrix1[row][column]+matrix2[row][column])
        new_matrix.append(new_line)

    return new_matrix

def sub_matrix(matrix1 , matrix2):
    if num_lines(matrix1)!=num_lines(matrix2) or num_columns(matrix1) != num_columns(matrix2):
        return "formato invalido"
    new_matrix = list()
    for row in range(num_lines(matrix1)):
        new_line = list()
        for column in range(num_columns(matrix1)):
            new_line.append(matrix1[row][column]-matrix2[row][column])
        new_matrix.append(new_line)

def sqaure_matrix(nums , order):
    if len(nums) != order**2:
        return "erro de formataçao"
    new_matrix = list();
    counter =0;
    for i in range(order):
        new_line = list()
        for l in range(order):
            new_line.append(nums[counter])
            counter+=1
        new_matrix.append(new_line)


    return new_matrix

def det_matrix(matrix):
    if (num_columns(matrix) != num_lines(matrix)):
        return "erro de formato"
    det = 0
    if num_lines(matrix) ==2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    

    slice_matrix1 = matrix[0]
    slice_matrix2 = matrix[1:]
    while num_columns(slice_matrix2) !=3:
        det_matrix(slice_matrix2)

    return matrix[0][0]*(matrix[1][1]*matrix[2][2] - matrix[1][2]*matrix[2][1]) - matrix[0][1]*(matrix[1][0]*matrix[2][2] - matrix[1][2]*matrix[2][0]) + matrix[0][2]*(matrix[1][0]*matrix[2][1] - matrix[1][1]*matrix[2][0])
    

    

[1,2,3,4,5]
[6,7,8,9,10]
[1,3,4,5,7]
[0,9,7,6,5]
[3,4,5,6,7]




matrix1 = create_matrix(nums=[47, 892, 15, 603, 274, 981, 36, 710, 58, 429, 166, 847, 92, 301, 654, 9, 777, 214, 590, 38], length=4 , width=5)
matrix2 = create_matrix(nums=[83, 417, 29, 906, 512, 64, 738, 201, 945, 37, 684, 158, 799, 22, 560, 311, 874, 90, 447, 6, 721, 259, 998, 134], length=6 , width=4)

#new_matrix = redefine_matrix(matrix = matrix1 , width = 3 , length=5)

multiply_matrix = multiply_matrixes(matrix1 , matrix2)

for row in matrix1:
    print(row)

print("\n")
for row in matrix2:
    print(row)

print("\n")
for row in multiply_matrix:
    print(row)

print("\n")
for row in add_matrix(matrix1,matrix2):
    print(row)

print("\n")

for row in sqaure_matrix([2,3,4,5,6,7,8,9,2],3):
    print(row)


    
            
