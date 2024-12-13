# programacion tradicional
saldo = 0
tasa_interes = 5
def deposito(catidad):
    global saldo
    saldo += catidad
def retirar(catidad):
    global saldo
    saldo += catidad
def calcular_interes():
    global saldo,tasa_interes
    interes = saldo * tasa_interes
    saldo += interes
deposito(1000)
retirar(500)
calcular_interes()
print("saldo (tradicional) es :",saldo)
#poo
#gestion de  una cuenta bancaria
class cuenta_banco:
    def __init__(self,saldo_inicial = 49, tasa_interes= 5):
        self.saldo = saldo_inicial
        self.tasa_interes = tasa_interes
    def deposito(self,catidad):
        self.saldo += catidad
    def retirar(self,catidad):
        if catidad>=self.saldo:
            self.saldo -= catidad
        else:
            print("el saldo es insuficiente")
    def calcular_interes(self):
        interes = self.saldo * (self.tasa_interes/ 100)  # Convertir tasa a decimal
        self.saldo += interes
# realizar operaciones
saldos = cuenta_banco()
saldos.deposito(100)
saldos.retirar(500)
saldos.calcular_interes()
print("el saldo total de la (cuenta bancaria) es :",saldos.saldo)
