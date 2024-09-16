notas = [100,50,20,10]
def caixa(saldo):
    if saldo in notas:
        return {saldo: 1}
    if saldo == 30:
        return {20: 1, 10:1} 
    return None