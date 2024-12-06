import numpy as np

def get_input(equations, variables):
    final_variables = np.array(np.zeros((variables, 1)))
    final_results = np.array(np.zeros((equations,1)))
    final_numbers = np.array(np.zeros((variables,equations)))
    for i in range(0,equations):
        final_results[i,0] = float(input(f"Enter result for equation {i+1}: "))
        for x in range(0, variables):
            final_numbers[i,x] = float(input(f"Enter number for equation {i+1} variable {x+1}: "))


    return final_variables, final_results, final_numbers
            



def gauss_jordan(equations, variables):
    final_variables, final_results, final_numbers = get_input(equations, variables)
    
    n = len(final_results)
    m = n - 1
    
    final_concate = np.concatenate((final_numbers, final_results), axis=1, dtype = float)

    for i in range(len(final_results-1)):
            for j in range(i+1, len(final_results)):
                if final_concate[i,i] != 0:
                    final_concate[j,:] = final_concate[j,:] - (final_concate[j,i] / final_concate[i,i]) * final_concate[i,:]

    final_variables[m] = final_concate[m][n] / final_concate[m][m]

    for k in range(n - 2, -1, -1):
        final_variables[k] = final_concate[k][n]
        for l in range(k + 1, n):
            final_variables[k] = final_variables[k] - final_concate[k][l] * final_variables[l]
        final_variables[k] = final_variables[k] / final_concate[k][k]
        
    print("Final result",final_variables)
  
                               
    """print("Final variables",final_variables)
    print("Final results",final_results)
    print("Final numbers",final_numbers)

    final_contcate = np.concatenate((final_numbers, final_results), axis=1, dtype = float)

    print("Final contcate",final_contcate)

    for i in range(len(final_results-1)):
        for j in range(i+1, len(final_results)):
            if final_contcate[i,i] != 0:
                print("=========",final_contcate[i,:],"======= J:",j,"======= I:",i , "=======",final_contcate[j,i])
                
                final_contcate[j,:] = final_contcate[j,:] - (final_contcate[j,i] / final_contcate[i,i]) * final_contcate[i,:]
                #final_contcate[j,i] = 0

    print("Final contcate after step 1",final_contcate)
    size = len(final_results)
    
    final_results[size-1,0] = final_contcate[size-1,size] / final_contcate[size-1,size-1]
    final_contcate[size-1,size] = final_results[size-1,0]
    final_contcate[size-1,size-1] = 1


    for i in range(size-2, -1, -1):
        print("final_results",final_results)
        print("final_contcate",final_contcate)
        
        temp = final_results[i,0]
        for j in range(i+1, size):
            temp = temp - final_contcate[i,j] * final_results[j,0]
        
        final_results[i,0] = temp / final_contcate[i,i]



        
       temp = final_results[i+1,0]
        print("temp",temp)
        subtract = final_contcate[i,size-1] - temp * final_contcate[i,i]
        final_results[i,0] = subtract / final_contcate[i,i]
        final_contcate[i,size-1] = final_results[i,0]"""


    return final_variables
    

def cramer_rule(equations, variables):
    final_variables, final_results, final_numbers = get_input(equations, variables)

    a_det = np.linalg.det(final_numbers)
    n = len(final_results)
    for i in range(0, n):
        tempMatrix = np.copy(final_numbers)
        for j in range(0, n):
            tempMatrix[j][i] = final_results[j]
            final_variables[i] = np.linalg.det(tempMatrix) / a_det

    print("Final result",final_variables)
        
    return final_variables


def main():
    option = int(input("Enter 1.Gauss-Jordan 2.Cramer's Rule: "))
    
    equations = int(input("Enter number of equations: "))
    variables = int(input("Enter number of variables: "))
    
    if option == 1:
        gauss_jordan(equations, variables)
    elif option == 2:
        cramer_rule(equations, variables)
    else:
        print("Invalid option")
    
    
main()