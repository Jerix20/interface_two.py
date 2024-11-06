from model.interfaces.SonidoAble import SonidoAble
from model.interfaces.VoladorAble import VoladorAble


class Aguila(VoladorAble, SonidoAble):
    def volar(self):
        print("El águila vuela a gran altura")

    def hacer_sonido(self):
        print("El águila emite un grito agudo")
