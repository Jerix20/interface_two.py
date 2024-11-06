from model.interfaces.MigradorAble import MigradorAble
from model.interfaces.NadadorAble import NadadorAble
from model.interfaces.SonidoAble import SonidoAble
from model.interfaces.VoladorAble import VoladorAble


class Pato(VoladorAble, NadadorAble, SonidoAble, MigradorAble):
    def volar(self):
        print("El pato vuela a baja altura")

    def nadar(self):
        print("El pato nada en el lago")

    def hacer_sonido(self):
        print("El pato hace cuac cuac")

    def migrar(self):
        print("El pato migra al sur en invierno")
