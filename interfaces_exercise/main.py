from model.Pato import Pato
from model.Aguila import Aguila
from model.Delfin import Delfin
from model.Tiburon import Tiburon
from model.Gaviota import Gaviota
from model.Murcielago import Murcielago

def main():
    pato = Pato()
    aguila = Aguila()
    delfin = Delfin()
    tiburon = Tiburon()
    gaviota = Gaviota()
    murcielago = Murcielago()

    pato.volar()
    pato.nadar()
    pato.hacer_sonido()
    pato.migrar()

    aguila.volar()
    aguila.hacer_sonido()

    delfin.nadar()
    delfin.hacer_sonido()

    tiburon.nadar()

    gaviota.volar()
    gaviota.hacer_sonido()
    gaviota.migrar()

    murcielago.volar()
    murcielago.hacer_sonido()

main()