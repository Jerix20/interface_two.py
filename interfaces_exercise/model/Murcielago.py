from model.interfaces.SonidoAble import SonidoAble
from model.interfaces.VoladorAble import VoladorAble


class Murcielago(VoladorAble, SonidoAble):
    def volar(self):
        print("El murciélago vuela de noche")

    def hacer_sonido(self):
        print("El murciélago emite sonidos de ultrasonido")
