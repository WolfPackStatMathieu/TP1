from abstractPokemon import AbstractPokemon

class Attacker(AbstractPokemon):
    def __init__(self, _current_stat, _level, _name):
        super().__init__(_current_stat, _level, _name)
        