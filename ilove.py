from gtts import gTTS


x = input("Who do you miss?\n")


while True:
  lang = int(input("Choose the accent\n(1)=American\n(2)=British\n(3)=Irish\n(4)=Australian\n(5)=Canadian\n(6)=Indian\n(7)=African\n"))
  if lang not in{1, 2, 3, 4, 5, 6, 7}:
    print("That's not an accent!")
  else:
    break


langlist = ["us", "co.uk", "ie", "com.au", "ca", "co.in", "co.za"]
accent = langlist[lang-1]


lyrics = f"""
I miss the old {x}, straight from the 'Go {x}
Chop up the soul {x}, set on his goals {x} 
I hate the new {x}, the bad mood {x} 
The always rude {x}, spaz in the news {x} 
I miss the sweet {x}, chop up the beats {x} 
I gotta to say at that time I'd like to meet {x} 
See I invented {x}, it wasn't any {x}s 
And now I look and look around and there's so many {x}s 
I used to love {x}, I used to love {x} 
I even had the pink polo, I thought I was {x} 
What if {x} made a song about {x} 
Called 'I Miss The Old {x}', man that would be so {x} 
That's all it was {x}, we still love {x} 
And I love you like {x} loves {x}
"""


tts = gTTS(lyrics, lang = 'en', tld = accent)
tts.save(f"I Love " + x)
print(lyrics)
