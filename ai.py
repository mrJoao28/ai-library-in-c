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
    
    for line in matrix1:
        new_line = list()
        for row in range(num_lines(matrix1)):
            soma = 0
            for i in range(num_columns(matrix1)):
                soma+=line[i]*matrix2[i][row]
            new_line.append(soma)
        
        new_matrix.append(new_line)

    return new_matrix






matrix1 = create_matrix(nums=[1,2,100,4,5,6,7,2], length=2 , width=4)
matrix2 = create_matrix(nums=[4,3,2,1], length=2 , width=2)

new_matrix = redefine_matrix(matrix = matrix1 , width = 3 , length=5)

multiply_matrix = multiply_matrixes(matrix1 , matrix2)

for row in matrix1:
    print(row)

print("\n")
for row in matrix2:
    print(row)

print("\n")
for row in multiply_matrix:
    print(row)



    
            
