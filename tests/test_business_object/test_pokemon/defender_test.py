from unittest import TestCase

from pokemon_unite_lite.business_object.pokemon.defender import Defender
from business_object.statistique import Statistique


class TestDefenderPokemon(TestCase):
    
    def test_get_coef_damage_type(self):
        # GIVEN
        attack = 1
        defense = 1
        snorlax = Defender(_current_stat=Statistique(15, attaque=attack, defense=defense, spe_atk= 4, spe_def=6, vitesse= 8)
                            , _level=1, _name="mon_Defender")
        #WHEN
        multiplier = snorlax.get_pokemon_attack_coef()
        #THEN
        self.assert_(3, multiplier)
        