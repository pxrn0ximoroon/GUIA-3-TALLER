import math


class cuenta:
    def __init__(self,nombre,saldo):
        self.nombre=nombre
        self.saldo=saldo

    def Depositar(self,valor):
        if valor > 0:
            self.saldo=self.saldo+valor
            print("Deposito realizado")
        else:
            print("Valor invalido")

    def retirar(self,valor):
        if valor <= self.saldo and valor > 0:
            self.saldo=self.saldo-valor
            print("Retiro realizado")
        else:
            print("No es posible realizar el retiro")


def transferir(origen,destino,valor):
    if valor > 0 and valor <= origen.saldo:
        origen.saldo=origen.saldo-valor
        destino.saldo=destino.saldo+valor
        print("Transferencia realizada")
    else:
        print("No es posible realizar la transferencia")


def mostrarCuenta(c):
    print("Titular:",c.nombre)
    print("Saldo:",c.saldo)


def main():
    cuenta1=cuenta("Ana",1000)
    cuenta2=cuenta("Carlos",500)

    print("=== CUENTAS INICIALES ===")
    mostrarCuenta(cuenta1)
    mostrarCuenta(cuenta2)

    cuenta1.Depositar(500)
    cuenta1.retirar(200)
    transferir(cuenta1,cuenta2,300)

    print("\n=== CUENTAS FINALES ===")
    mostrarCuenta(cuenta1)
    mostrarCuenta(cuenta2)


if __name__=="__main__":
    main()
