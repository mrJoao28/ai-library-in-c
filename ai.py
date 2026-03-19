import math

"""
matrizes e tensores V
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

def div_matrix(matrix , num):
    for r,row in enumerate(matrix):
        for n in range(len(row)):
            matrix[r][n] /= num
    return matrix

def maximum(nums , min):
    result = list()
    for num in nums:
        if num <=0:
            result.append(min)
        else:
            result.append(num)
    return result

def neural_network(nums, weigth1 , weigth2 , acctivate_value ,bias ):
    data = list()
    for num in nums:
        for n in num:
            data.append(n)
    if len(weigth1) != len(data) or len(weigth2) != len(data):
        return "quantidade invalida"

    for i in range(len(data)):
        data[i] = data[i]*weigth1[i] + bias

    data = maximum(data , acctivate_value)

    for i in range(len(data)):
        data[i] = data[i]*weigth2[i] +bias

    data = maximum(data , acctivate_value)

    return data
    
def det_matrix(matrix):
    det = 1
    

    if (num_lines(matrix) != num_columns(matrix)):
        return "formato de matrix invalido"

    if (num_lines(matrix) == 1):
        return matrix[0][0]
    
    elif (num_lines(matrix) ==2):
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]


    for row in matrix:
        counter =0 
        for num in row:
            if num == 0:
                counter +=1
        if counter == num_lines(matrix):
            return 0
        
    if matrix[0][0] == 0 :
        for i,row in enumerate(matrix[1:]):
            new_line = list()
            if row[0] != 0:
                new_line = matrix[0]
                matrix[0] = matrix[i+1]
                matrix[i+1] = new_line
                det  *= -1
    
    first_element = matrix[0][0]

    first_line = matrix[0][1:]
    for i in range(len(first_line)):
        first_line[i] /= first_element

    det /= matrix[0][0]

    matrix = matrix[1:]

    first_column = list()
    
    for i,row in enumerate(matrix):
        first_column.append(row[0])
        del matrix[i][0]



    for r , row in enumerate(matrix):
        for c  in range(len(row)):
            matrix[r][c] =  (matrix[r][c] - first_line[c]*first_column[r])

    for num in range(len(matrix[0])):
        matrix[0][num] /= (det)


    return det_matrix(matrix)
    
def creat_vector(nums):
    vector = list()
    for i in nums:
        vector.append(i)
    return vector

def sum_vector(vector_A , vector_B):
    vector  = list()
    if  len(vector_A)>len(vector_B):
        for i in range(len(vector_B)):
            vector.append(vector_A[i]+vector_B[i])
        for num in vector_A[len(vector_B)+1:]:
            vector.append(num)
    
    elif len(vector_A)<len(vector_B):
        for i in range(len(vector_A)):
            vector.append(vector_A[i]+vector_B[i])
        for num in vector_B[len(vector_A)+1:]:
            vector.append(num)
    
    else:
        for i in range(len(vector_A)):
            vector.append(vector_A[i]+vector_B[i])
    
    return vector
        
def sub_vector(vector_A , vector_B):
    for i in range(len(vector_B)):
        vector_B[i] = -1*vector_B[i]

    return sum_vector(vector_A,vector_B)

def mult_scalar_vector(vector, num):
    for a in range(len(vector)):
        vector[a] = vector[a]*num
    return vector


#supondo que seja uma base ortnormal(simplificando contas)


def module_vector(vector):
    module = 0 
    for num in vector:
        module += num**2
    
    return module**(1/2)

def dot_vector(vector_A,vector_B,degress):
    mod_vector_A = module_vector(vector_A)
    mod_vector_B = module_vector(vector_B)
    
    return mod_vector_A*mod_vector_B*math.sin(degress)

def cross_vector(vector_A , vector_B ):
    vector = list()

    if len(vector_A) !=3 or len(vector_B)!=3:
        return "invlaid format"
    
    for i in range(len(vector_A)):
        if i ==0:
            vector.append(det_matrix(vector_A[i+1:],vector_B[i+1:]))
        elif i==1:
            vector.append(-1*det_matrix([vector_A[i-1],vector_A[i+1]],[vector_B[i-1],vector_B[i+1]]))
        elif i ==2:
            vector.append(det_matrix(vector_A[:i],vector_B[:i]))

    return vector
    
def mist_product(vector_A,vector_B,vector_C,degress):
    if len(vector_A) != 3 or len(vector_B) != 3 or len(vector_C) != 3:
        return "invalid format"

    return dot_vector(cross_vector(vector_A,vector_B,degress),vector_C)








matrix1 = create_matrix(nums=[47, 892, 15, 603, 274, 981, 36, 710, 58, 429, 166, 847, 92, 301, 654, 9, 777, 214, 590, 38], length=4 , width=5)
matrix2 = create_matrix(nums=[83, 417, 29, 906, 512, 64, 738, 201, 945, 37, 684, 158, 799, 22, 560, 311, 874, 90, 447, 6, 721, 259, 998, 134], length=6 , width=4)
matrix3 = sqaure_matrix([1,2,3,4,5,6,7,8,9],3)
#new_matrix = redefine_matrix(matrix = matrix1 , width = 3 , length=5)
matrix3 = div_matrix(matrix3 , 255)

multiply_matrix = multiply_matrixes(matrix1 , matrix2)
matrix_square = sqaure_matrix([100,100,5,4,5,4,7,8,100,34,3,2,3,2,200,45] , 4)

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

print("\n")
for row in matrix_square:
    print(row)



print("\n")
print(neural_network(nums=matrix3 , weigth1=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9] , weigth2=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9] , bias=0.5 , acctivate_value=2) )
print("\n")
print(det_matrix(matrix_square))
