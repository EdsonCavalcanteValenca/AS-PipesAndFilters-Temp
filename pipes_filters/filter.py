"""Contrato unico do sistema.

Todo filtro implementa esta interface. O Pipe conhece SOMENTE ela --
nunca as implementacoes concretas. E isso que permite adicionar filtros
novos sem alterar uma linha do Pipe.
"""

from abc import ABC, abstractmethod


class Filter(ABC):
    """Um filtro recebe um dado, transforma e devolve. Nada mais."""

    @abstractmethod
    def execute(self, data):
        """Processa o dado e retorna o resultado da transformacao."""
        raise NotImplementedError

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}>"
