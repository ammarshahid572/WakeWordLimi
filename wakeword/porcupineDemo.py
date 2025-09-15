import pvporcupine
import pyaudio
import struct
import os
from dotenv import load_dotenv

load_dotenv()
# Initialize Porcupine with a built-in wake word

ACCESS_KEY = os.getenv("ACCESS_KEY")
porcupine = pvporcupine.create(access_key=ACCESS_KEY, keywords=["picovoice", "computer"])

pa = pyaudio.PyAudio()

stream = pa.open(
    rate=porcupine.sample_rate,
    channels=1,
    format=pyaudio.paInt16,
    input=True,
    frames_per_buffer=porcupine.frame_length
)

print("Listening for wake word...")

try:
    while True:
        pcm = stream.read(porcupine.frame_length, exception_on_overflow=False)
        pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)
        result = porcupine.process(pcm)

        if result >= 0:
            print("Wake word detected!")

except KeyboardInterrupt:
    print("Stopping...")

finally:
    stream.close()
    pa.terminate()
    porcupine.delete()
