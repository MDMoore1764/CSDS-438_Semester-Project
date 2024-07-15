import os
import numpy as np
from pydub import AudioSegment
from pydub.generators import Sine
from mido import MidiFile
from midi2audio import FluidSynth

relative = "./src2/Data/midis/Super Mario 64 - Medley.mid"
full_path = os.path.abspath(relative)
# Load the MIDI file
midi_file = MidiFile(full_path)

# Print out the MIDI file information
for i, track in enumerate(midi_file.tracks):
    print(f"Track {i}: {track.name}")
    for msg in track:
        print(msg)


import numpy as np
from pydub import AudioSegment
from pydub.generators import Sine
from mido import MidiFile


# Function to convert a MIDI file to WAV using sine waves
def midi_to_wav(
    midi_file_path, wav_file_path, sample_rate=44100, duration_per_note=500
):
    # Load the MIDI file
    midi_file = MidiFile(midi_file_path)

    # Initialize an empty audio segment
    audio_segment = AudioSegment.silent(duration=0, frame_rate=sample_rate)

    # Iterate through each track in the MIDI file
    for track in midi_file.tracks:
        time_elapsed = 0
        for msg in track:
            if msg.type == "note_on" and msg.velocity > 0:
                # Calculate the time at which the note should start
                time_elapsed += msg.time
                note_start_time = time_elapsed * 1000 / midi_file.ticks_per_beat

                # Calculate the frequency of the note
                frequency = 440 * 2 ** ((msg.note - 69) / 12)

                # Generate the sine wave for the note
                sine_wave = Sine(frequency, sample_rate=sample_rate).to_audio_segment(
                    duration=duration_per_note
                )

                # Insert the sine wave at the correct position in the audio segment
                audio_segment = audio_segment.overlay(
                    sine_wave, position=note_start_time
                )

    # Export the final audio segment to a WAV file
    audio_segment.export(wav_file_path, format="wav")


midi_to_wav(full_path, "./out.wav")
