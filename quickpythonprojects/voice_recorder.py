import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv


# Sampling frequency
freq = 44100

# Recording duration
duration = 10



# Start recorder with the given values of 
# duration and sample frequency
recording = sd.rec(int(duration * freq), 
                   samplerate=freq, channels=2)

# Record audio for the given number of seconds
sd.wait()


write("recording0.wav", freq, recording)