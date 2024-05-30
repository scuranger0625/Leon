import os
from pydub import AudioSegment

def convert_to_mp3(directory):
    for filename in os.listdir(directory):
        if filename.endswith((".wav", ".m4a", ".flac", ".ogg")):
            filepath = os.path.join(directory, filename)
            sound = AudioSegment.from_file(filepath)
            mp3_filename = os.path.splitext(filename)[0] + ".mp3"
            mp3_filepath = os.path.join(directory, mp3_filename)
            sound.export(mp3_filepath, format="mp3")
            print(f"Converted {filename} to {mp3_filename}")

# 指定你想要轉換的資料夾路徑
directory = r"C:\Users\Leon\Desktop\python\YTdownloadandAIGC\musicdatatrain"

# 執行轉換
convert_to_mp3(directory)

