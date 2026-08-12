"""Filtro de exemplo: converte o texto para maiusculas."""

from pipes_filters.filter import Filter


class UppercaseFilter(Filter):
    """Converte toda a entrada para letras maiusculas."""

    def execute(self, data: str) -> str:
        return data.upper()
