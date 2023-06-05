from imeasurepy.main import frequency_intj, frequency_emoji


def test_frequency_interj_zero():
    assert frequency_intj("Isso é bem legal") == 0


def test_frequency_interj_not_zero():
    assert frequency_intj("!!!") == 3
    
    
def test_frequency_emoji_zero():
    assert frequency_emoji("Oi oi oi, tulin") == 0
    
    
def test_frequency_emoji_not_zero():
    assert frequency_emoji("Olá! 👋 Como você está? 😊") == 2
