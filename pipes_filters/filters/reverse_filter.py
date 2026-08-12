"""Segundo filtro de exemplo: inverte o texto.

Existe para que o pipeline tenha mais de uma etapa e o papel do Pipe
fique visivel.
"""

from pipes_filters.filter import Filter


class ReverseFilter(Filter):
    """Inverte a ordem dos caracteres da entrada."""

    def execute(self, data: str) -> str:
        return data[::-1]
