"""Ponto de entrada: monta o pipeline e executa.

Este e o UNICO arquivo que muda quando um filtro novo entra no sistema.
Nem o Pipe nem os filtros existentes precisam ser tocados -- essa e a
propriedade que a arquitetura Pipes and Filters entrega.
"""

from pipes_filters.pipe import Pipe
from pipes_filters.filters import UppercaseFilter, ReverseFilter


def main() -> None:
    entrada = "Arquitetura de Software"

    pipeline = (
        Pipe()
        .add(UppercaseFilter())
        .add(ReverseFilter())
    )

    saida = pipeline.run(entrada)

    print("Pipeline montado :", pipeline)
    print("Entrada          :", repr(entrada))
    print("Saida            :", repr(saida))


if __name__ == "__main__":
    main()
