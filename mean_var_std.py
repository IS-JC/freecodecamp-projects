import numpy as np

#Función del arreglo 3x3
def calculate (*data):
    if len(data) != 9:
        print( "La lista debe contener nueve números")
    arr = np.array(data)
    return arr.reshape(3,3)

# Llamada a la función con 9 números
result = calculate(1,2,3,4,5,6,7,10,9)

# Diccionario que guarda todos los cálculos estadísticos de la matriz
analysis = {
    'mean': [result.mean(axis=0).tolist(),
             result.mean(axis=1).tolist(),
             result.flatten().mean().tolist()],

    'variance': [result.var(axis=0).tolist(),
             result.var(axis=1).tolist(),
             result.flatten().var().tolist()],

    'standard deviation': [result.std(axis=0).tolist(),
             result.std(axis=1).tolist(),
             result.flatten().std().tolist()],

    'max': [result.max(axis=0).tolist(),
             result.max(axis=1).tolist(),
             result.flatten().max().tolist()],

    'min': [result.min(axis=0).tolist(),
             result.min(axis=1).tolist(),
             result.flatten().min().tolist()],

    'sum': [result.sum(axis=0).tolist(),
             result.sum(axis=1).tolist(),
             result.flatten().sum().tolist()]
 }

# Imprime el diccionario con formato legible
print("{") 
for key, value in analysis.items():
    print(f"  '{key}': {value},")
print("}")