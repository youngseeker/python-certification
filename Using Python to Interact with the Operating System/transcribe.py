"""
================================================================================
OFFLINE AUDIO & VIDEO TRANSCRIBER (ENGLISH & YORÙBÁ)
================================================================================
HOW TO USE THIS SCRIPT ANYTIME (NO INTERNET REQUIRED):
1. Make sure VS Code is using Python 3.12 (check the bottom-right corner of VS Code).
2. Click the 'Play' (Run) button in the top-right corner of VS Code.
3. Look at the terminal below: when it asks for a file, either:
   - Right-click your audio/video file in Windows -> "Copy as path" -> Paste it here, OR
   - Drag and drop the file straight from File Explorer into the terminal window.
4. Press Enter and wait for "Transcription saved to: ..." to appear.

SUPPORTED FILES: .mpeg, .mp3, .ogg (WhatsApp), .wav, .m4a, .mp4, .mkv, .mov
OUTPUT LOCATION: Saves automatically as <same_name>.txt in the exact same folder.
================================================================================
"""

from pathlib import Path
from faster_whisper import WhisperModel

# --- STEP 1: GET THE FILE PATH INTERACTIVELY ---
# No need to edit this code anymore! Just paste or drag your file when prompted.
# .strip('"') automatically removes extra quotes added by Windows "Copy as path".
raw_path = input("Paste or drag your audio/video file here, then press Enter: ").strip().strip('"')
input_file = Path(raw_path)

# Safety check: Make sure the file actually exists before loading the heavy AI model
if not input_file.is_file():
    print(f"\nERROR: Could not find file at:\n{input_file}")
    print("Tip: Right-click your file -> 'Copy as path', then paste it into the terminal.")
    raise SystemExit(1)

# --- STEP 2: SET THE OUTPUT FILENAME ---
# Automatically saves <filename>.txt in the same folder as your recording.
# (Handles double extensions like 'recording.mp3.mpeg' -> 'recording.txt' cleanly)
clean_name = Path(input_file.stem).stem if len(input_file.suffixes) > 1 else input_file.stem
output_file = input_file.with_name(f"{clean_name}.txt")

# --- STEP 3: LOAD THE OFFLINE AI MODEL ---
# Uses the 'medium' model already cached on your hard drive (no internet needed).
# NOTE: Do not change "medium" unless you are connected to the internet to download a new size.
print("\nLoading offline transcription model...")
model = WhisperModel("medium", device="cpu", compute_type="int8")

# --- STEP 4: TRANSCRIBE THE AUDIO ---
# CUSTOMIZING FOR NEW SITUATIONS:
# - Mixed English + Yorùbá (Default): Leave 'language=None' and keep the bilingual prompt below.
# - English-only (Faster/Cleaner): Change initial_prompt to "This is an English recording."
# - Yorùbá-only: Add language="yo", right after beam_size=5,
print(f"Transcribing '{input_file.name}'... (Longer files take a few minutes, please wait)")
segments, info = model.transcribe(
    str(input_file),
    beam_size=5,
    initial_prompt="Ẹ káàárọ̀. This is a bilingual conversation mixing English and Yorùbá."
)

print(f"Detected primary language: {info.language}")

# --- STEP 5: SAVE TO .TXT FILE ---
# Writes each spoken phrase on a new line so it is easy to read.
with open(output_file, "w", encoding="utf-8") as f:
    for segment in segments:
        line = segment.text.strip()
        f.write(line + "\n")
        # Prints progress live in the terminal so you know it hasn't frozen
        print(f"  -> {line}")

print(f"\nDONE! Transcription saved to:\n{output_file}")
