'''
Algoritmo do Professor Rodrigo Cesar Pedrosa Silva
'''
'''
def r0e7(sol,val):
    if len(sol) > 0:
        return sol[0] == 7

    return True

'''

# Conferindo se não há duas rainhas na mesma coluna
def different_column(sol,val):
    return not (val in sol)

# Conferindo se não há duas rainhas na mesma diagonal
def different_diagonal(sol,val):
    
    for i in range(len(sol)):
        deltay = abs(sol[i]-val)
        deltax = abs(i - len(sol))
        if (deltay == deltax):
            return False

    return True

# Função que confere todas as restrições dadas
def check_constraints(sol,val,constraints):

    for c in constraints:
        if not c(sol,val):
            return False

    return True

# BackTracking
def search(domain, constraints, sol=[]):
    #Se o tamanho do domínio for igual ao tamanho da solução, então uma solução foi encontrada
    if len(sol) == len(domain):
        print(sol)
    else:
        #Se não para cada possibilidade de domínio empilhamos uma ramificação para ser testada
        for d in domain[len(sol)]:
            #A solução parcial só é empilhada caso não viole nenhuma solução
            #Isso evita ter que testar todas as soluções possíveis
            if check_constraints(sol, d, constraints):
                sol.append(d)
                search(domain,constraints,sol)
                sol.pop(-1)

if __name__ == '__main__':
    
    n = 8
    domain = [[i for i in range(n)] for j in range(n)]
    constraints = [different_column, different_diagonal]
    
    print(domain)
    search(domain, constraints)