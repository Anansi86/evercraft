from evercraft import *

def test_character():
    blodgram = Character('blodgram','good',10,5)
    assert isinstance(blodgram, Character)


def test_char_name():
    blodgram = Character('blodgram','good',10,5)
    assert blodgram.name != 'alex'

def test_char_align():
    blodgram = Character('blodgram','good',10,5)
    assert blodgram.align == 'good'

def test_armor():
    blodgram = Character('blodgram','good',10,5)
    assert blodgram.armorClass != 9

def test_hitPoints():
    blodgram = Character('blodgram','good',10,5)
    assert blodgram.hitPoints == 5

def test_attack():
    blodgram = Character('blodgram','good',10,5)
    assert blodgram.attack(11, 10) == True #hit

def test_damaged():
    blodgram = Character('blodgram','good',10,5)
    mario = Character('mario','bad',11,5)
    assert blodgram.damaged(10,mario.armorClass) == 4


