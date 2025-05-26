import argparse
import os
from pydub import AudioSegment

def convert_mp3_to_wav(mp3_path, wav_path):
    audio = AudioSegment.from_mp3(mp3_path)
    audio.export(wav_path, format="wav")
    print(f"🎧 Saved WAV: {wav_path}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--track", required=True)
    parser.add_argument("--mp3", required=True)
    args = parser.parse_args()

    track = args.track
    mp3_path = args.mp3
    wav_path = mp3_path.replace("/mp3/", "/wav/").replace(".mp3", ".wav")
    os.makedirs(os.path.dirname(wav_path), exist_ok=True)

    convert_mp3_to_wav(mp3_path, wav_path)

    # Add more steps here later...

if __name__ == "__main__":
    main()
