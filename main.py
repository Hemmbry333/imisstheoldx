from gtts import gTTS

x = input("Who do you miss?\n")

lyrics = (f"I miss the old {x}, straight from the 'Go {x} \nChop up the soul {x}, set on his goals {x} \nI hate the new {x}, the bad mood {x} \nThe always rude {x}, spaz in the news {x} \nI miss the sweet {x}, chop up the beats {x} \nI gotta to say at that time I'd like to meet {x} \nSee I invented {x}, it wasn't any {x}s \nAnd now I look and look around and there's so many {x}s \nI used to love {x}, I used to love {x} \nI even had the pink polo, I thought I was {x} \nWhat if {x} made a song about {x} \nCalled 'I Miss The Old {x}', man that would be so {x} \nThat's all it was {x}, we still love {x} \nAnd I love you like {x} loves {x}")

tts = gTTS(lyrics, lang = 'en', tld = 'co.uk')
tts.save(f"I Love {x}")
print(lyrics)