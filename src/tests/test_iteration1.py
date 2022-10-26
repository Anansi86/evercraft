from evercraft import *


def test_character():
    blodgram = Character('blodgram', 'good')
    assert isinstance(blodgram, Character)


def test_char_name():
    blodgram = Character('blodgram', 'good')
    assert blodgram.name != 'alex'


def test_char_align():
    blodgram = Character('blodgram', 'good')
    assert blodgram.align == 'good'


def test_armor():
    blodgram = Character('blodgram', 'good')
    assert blodgram.armorClass != 9


def test_hitPoints():
    blodgram = Character('blodgram', 'good')
    assert blodgram.hitPoints == 5

# hit


def test_attack():
    blodgram = Character('blodgram', 'good')
    assert blodgram.attack(11, 10) == True  # hit

# nothit


def test_no_hit():
    blodgram = Character('blodgram', 'good')
    assert blodgram.attack(8, 10) == False


# Critical hit test
def test_critical_hit():
    blodgram = Character('blodgram', 'good')
    assert blodgram.attack(20, 10) == 'Critical Hit'


def test_damaged():
    blodgram = Character('blodgram', 'good')
    mario = Character('mario', 'bad')
    assert blodgram.damaged(10, mario.armorClass) == 4


def test_is_dead():
    blodgram = Character("blodgram", 'good')
    assert blodgram.is_dead != True


def test_is_alive():
    blodgram = Character("blodgram", 'good')
    assert blodgram.is_dead == False


def test_strenth():
    blodgram = Character('Blodgram', 'good')
    assert blodgram.strength == 10


def test_dexterity():
    blodgram = Character('Blodgram', 'good')
    assert blodgram.dexterity == 10


def test_constitution():
    blodgram = Character('Blodgram', 'good')
    assert blodgram.constitution == 10


def test_wisdom():
    blodgram = Character('Blodgram', 'good')
    assert blodgram.wisdom == 10

def test_intelligence():
    blodgram = Character('Blodgram', 'good')
    assert blodgram.intelligence == 10