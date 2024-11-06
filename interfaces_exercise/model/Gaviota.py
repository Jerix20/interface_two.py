from model.interfaces.MigradorAble import MigradorAble
from model.interfaces.SonidoAble import SonidoAble
from model.interfaces.VoladorAble import VoladorAble


class Gaviota(VoladorAble, SonidoAble, MigradorAble):
    def volar(self):
        print("La gaviota vuela sobre el mar")

    def hacer_sonido(self):
        print("La gaviota hace un sonido fuerte")

    def migrar(self):
        print("La gaviota migra a climas más cálidos")
