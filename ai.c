/*
matrizes e tensores
redes neurais
backpropagation
otimizador
salvamento
inferencia
*/

#include <stdio.h>
#include <stdlib.h>


typedef struct Matrix{
    
}Matrix;

float create_matrix(float nums[], int x , int y){
    float *matrix  = malloc(x*sizeof());
    if ((sizeof(nums)/sizeof(nums[0])) != x*y){
        return 1;
    }
    for (int i = 0 ; i <x ; i++){
        float *new_line = malloc(y*sizeof(float));
        for (int l = 0 ; l<y ; l++){
            new_line[l] = nums[]
        }

    }
}