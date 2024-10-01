import os
import librosa
import soundfile as sf

# 音频处理函数：截取前 47 秒并保存
def process_wav_file(input_path, output_path, duration=47):
    # 加载音频文件
    y, sr = librosa.load(input_path, sr=None)
    
    # 计算对应的采样点
    max_samples = int(sr * duration)
    
    # 截取音频
    y_trimmed = y[:max_samples]
    
    # 保存截取后的音频
    sf.write(output_path, y_trimmed, sr)

# 遍历目录下所有的 wav 文件并处理
def process_audio_directory(input_dir, output_dir, duration=47):
    # 确保输出目录存在
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # 遍历输入目录下的所有文件
    for filename in os.listdir(input_dir):
        if filename.endswith(".wav"):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)
            
            print(f"Processing: {input_path}")
            
            # 处理音频文件
            process_wav_file(input_path, output_path, duration)
            print(f"Saved to: {output_path}")

# 主函数调用
input_directory = "audios/transfer/reference"  # 输入目录路径
output_directory = "audios/transfer/target"  # 输出目录路径

os.makedirs(output_directory, exist_ok=True)

process_audio_directory(input_directory, output_directory, duration=47)