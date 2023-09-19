import pyaudio
import wave

# Set the parameters for audio input and output
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5  # Adjust this to set the recording duration

# Initialize PyAudio
p = pyaudio.PyAudio()

# Create an audio stream for input
stream_in = p.open(format=FORMAT,
                   channels=CHANNELS,
                   rate=RATE,
                   input=True,
                   frames_per_buffer=CHUNK)

# Create an audio stream for output
stream_out = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    output=True)

print("Speak and I'll repeat. Press Ctrl+C to stop.")

try:
    while True:
        # Read audio data from the microphone
        data = stream_in.read(CHUNK)

        # Play the audio data
        stream_out.write(data)
except KeyboardInterrupt:
    print("Stopped by the user.")

# Close the audio streams and terminate PyAudio
stream_in.stop_stream()
stream_out.stop_stream()
stream_in.close()
stream_out.close()
p.terminate()
