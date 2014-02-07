from pygoogletts import pygoogletts

tts = pygoogletts()

stream = tts.get_sound_stream("hello", language="en", ie="UTF-8")
print str(stream)

