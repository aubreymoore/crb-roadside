import crb_roadside as crb

def test_say_hello():
    assert crb.say_hello() == 'Hello'

def test_say_goodbye():
    assert crb.say_goodbye() == 'Goodbye'