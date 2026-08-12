"""O tubo: conduz o dado de um filtro para o proximo."""

from pipes_filters.filter import Filter


class Pipe:
    """Encadeia filtros e executa na ordem em que foram adicionados.

    Exemplo:
        resultado = Pipe().add(UppercaseFilter()).add(ReverseFilter()).run("ola")
    """

    def __init__(self):
        self._filters: list[Filter] = []

    def add(self, filter_: Filter) -> "Pipe":
        """Adiciona um filtro ao final da cadeia e devolve o proprio Pipe."""
        if not isinstance(filter_, Filter):
            raise TypeError(
                f"{filter_!r} nao implementa a interface Filter."
            )
        self._filters.append(filter_)
        return self

    def run(self, data):
        """Faz o dado atravessar todos os filtros, em ordem."""
        for filter_ in self._filters:
            data = filter_.execute(data)
        return data

    @property
    def filters(self) -> list[Filter]:
        return list(self._filters)

    def __len__(self) -> int:
        return len(self._filters)

    def __repr__(self) -> str:
        nomes = " -> ".join(f.__class__.__name__ for f in self._filters)
        return f"Pipe({nomes or 'vazio'})"
