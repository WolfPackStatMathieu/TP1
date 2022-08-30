from ABC import abc

class AbstractPokemon(abc):
    def __init__(self, _current_stat, _level, _name):
        self._current_stat = _current_stat
        self._level = _level
        self._name = name

    @abstractmethod
    def get_pokemon_attack_coef(self):
        pass
    @abstractmethod
    def level_up(self):
        pass
