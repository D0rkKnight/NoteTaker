import os
import whisper


def transcribe(folder_path: str = "artifacts/lectures") -> str:
    model = whisper.load_model("small.en")
    transcriptions = []

    audio_files = [file for file in os.listdir(folder_path)]

    # Iterate over each audio file
    for audio_file in audio_files:
        audio_file_path = os.path.join(folder_path, audio_file)
        print(f"Transcribing: {audio_file_path}")
        result = model.transcribe(audio_file_path, verbose=False)
        transcriptions.append(result["text"])

    return transcriptions
