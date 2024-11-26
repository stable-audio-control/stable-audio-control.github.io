import os
import soundfile as sf
from tqdm.auto import tqdm


def process_wav_file(input_path, output_path, duration=47):
    data, sr = sf.read(input_path)
    max_samples = int(sr * duration)
    data_trimmed = data[:max_samples]
    sf.write(output_path, data_trimmed, sr)


def process_audio_directory(input_dir, output_dir, duration=47):
    for filename in tqdm(os.listdir(input_dir)):
        print(filename)
        if filename.endswith(".mp3"):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)
            process_wav_file(input_path, output_path, duration)


# 主函数调用
input_directory = "../../audios/editing/input"  # 输入目录路径
output_directory = "../../audios/editing/input"  # 输出目录路径

os.makedirs(output_directory, exist_ok=True)
process_audio_directory(input_directory, output_directory, duration=47)
