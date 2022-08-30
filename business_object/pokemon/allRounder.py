from abstractPokemon import AbstractPokemon


class AllRounder(AbstractPokemon):
    def __init__(self, _current_stat, _level, _name):
        super().__init__(_current_stat, _level, _name)
    
    def get_pokemon_attack_coef(self):
        return 1 + (self._current_stat.__spe_atk + self._current_stat.__spe_def)
        