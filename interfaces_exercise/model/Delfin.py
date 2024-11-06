from model.interfaces.NadadorAble import NadadorAble
from model.interfaces.SonidoAble import SonidoAble


class Delfin(NadadorAble, SonidoAble):
    def nadar(self):
        print("El delfín nada rápidamente en el océano")

    def hacer_sonido(self):
        print("El delfín emite sonidos de chasquido")
