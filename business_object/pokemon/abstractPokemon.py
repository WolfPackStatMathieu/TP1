from abc import ABC, abstractmethod
from statistique import Statistique

class AbstractPokemon(ABC):
    """_summary_

    Args:
        ABC (_type_): _description_
    """
    def __init__(self, current_stat, _level, _name):
        self._current_stat: Statistique = current_stat
        self._level = _level
        self._name = _name

    @abstractmethod
    def get_pokemon_attack_coef(self):
        pass
    
    def level_up(self):
        pass
