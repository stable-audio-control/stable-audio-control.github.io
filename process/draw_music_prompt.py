import numpy as np
import matplotlib.pyplot as plt
import json
import librosa
from torchaudio import transforms as T
import torch.nn.functional as F
from tqdm.auto import tqdm
import multiprocessing as mp
import torch
import torchaudio
import copy

num=95
audio_path = f'audios/transfer/reference/{num}.wav'
length = 4096

def compute_music_represent(audio, sr, channel=2):

    # 高通滤波
    filter_y = torchaudio.functional.highpass_biquad(audio, sr, 261.6)

    # 计算CQT, fmin是最低频率，n_bins是bins的数量，bins_per_octave是每个八度的bins数量
    fmin = librosa.midi_to_hz(0)
    CQT_spec = librosa.cqt(y=filter_y.numpy(), fmin=fmin, sr=sr, n_bins=128, bins_per_octave=12, hop_length=512)
    CQT_dB = librosa.amplitude_to_db(np.abs(CQT_spec), ref=np.max)

    return CQT_dB


def load_audio(filename, sr):
    ext = filename.split(".")[-1]

    audio, in_sr = torchaudio.load(filename, format=ext)

    if in_sr != sr:
        resample_tf = T.Resample(in_sr, sr)
        audio = resample_tf(audio)

    return audio


def padding_audio(audio):

    sample_size = 2097152
    n_channels, n_samples = audio.shape

    # 计算需要填充的长度
    if sample_size - n_samples > 0:
        padding_length = sample_size - n_samples
        audio = F.pad(audio, (0, padding_length))

    # 使用np.pad进行填充
    return audio


def stereo(signal):
    signal_shape = signal.shape
    if len(signal_shape) == 1:  # [s] -> [2, s]
        signal = signal.unsqueeze(0).repeat(2, 1)
    elif len(signal_shape) == 2:
        if signal_shape[0] == 1:  # [1, s] -> [2, s]
            signal = signal.repeat(2, 1)
        elif signal_shape[0] > 2:  # [?, s] -> [2, s]
            signal = signal[:2, :]

    return signal


y = load_audio(audio_path, sr=44100)
y = stereo(y)
music = padding_audio(y)
cqt_spec = compute_music_represent(music, sr=44100)
assert cqt_spec.shape == (2, 128, 4096), "ERROR: The shape of cqt spec is not correct. The cqt shape is {}".format(cqt_spec.shape)

argsort_cqt_spec = np.zeros((8, length), dtype=int)
try:
    # 遍历每一个frame
    for i in range(length):
        idx_left = np.argsort(cqt_spec[0, :, i])[-1:-5:-1]
        idx_right = np.argsort(cqt_spec[1, :, i])[-1:-5:-1]

        argsort_cqt_spec[0:8:2, i] = idx_left
        argsort_cqt_spec[1:8:2, i] = idx_right
except Exception as e:
    print("There are something wrong when use np.argsort, the shape of cqt_spec is {}, the ERROR is {}".format(cqt_spec.shape, e))
    exit()

# from 0-127 to 1-128, 0 is mask, every argsort_cqt_spec's shape is [8, 4096]
argsort_cqt_spec = argsort_cqt_spec + 1

# 绘制8条线
plt.figure(figsize=(16, 8))  # 设置图像尺寸，宽度16，高度8

# 绘制每一行数据为一条线，并分别命名
labels = ['top-L0', 'top-L1', 'top-L2', 'top-L3', 'top-R0', 'top-R1', 'top-R2', 'top-R3']
for i in range(8):
    plt.plot(argsort_cqt_spec[i], label=labels[i])

# 添加标题和标签
plt.title("music prompt")
plt.xlabel("Pitch")
plt.ylabel("Frame")

# 显示图例
plt.legend()

# 保存图像到本地
output_path = f"audios/transfer/source/{num}.png"  # 设置保存路径和文件名
plt.savefig(output_path, dpi=300)  # 保存图像，dpi=300 保证高分辨率

# 显示图像
plt.show()
