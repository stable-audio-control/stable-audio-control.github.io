<div style="text-align: center"> 

<h1> Editing Music with Melody and Text: <br> Using ControlNet for Diffusion Transformer </h1>
Siyuan Hou<sup>1,2</sup>, Shansong Liu<sup>2</sup>, Ruibin Yuan<sup>3</sup>, Wei Xue<sup>3</sup>, Ying Shan<sup>2</sup>, Mangsuo Zhao<sup>1</sup>, Chao Zhang<sup>1</sup>  <br>
<sup>1</sup>Tsinghua University <br>
<sup>2</sup>ARC Lab, Tencent PCG <br>
<sup>3</sup>Hong Kong University of Science and Technology<br>

<p>
Supporting webpage for ICASSP 2025.<br>
<a href="https://arxiv.org/abs/2410.05151">[Paper on ArXiv]</a> 
<!-- Code is available <a href="https://github.com/NilsDem/control-transfer-diffusion/">here</a> -->
</p>

</div>


<div style="text-align: justify"> 

<h2>Abstract</h2>

Despite the significant progress in controllable music generation and editing, challenges remain in the quality and length of generated music due to the use of Mel-spectrogram representations and UNet-based model structures. To address these limitations, we propose a novel approach using a Diffusion Transformer (DiT) augmented with an additional control branch using ControlNet. This allows for long-form and variable-length music generation and editing controlled by text and melody prompts.
For more precise and fine-grained melody control, we introduce a novel top-k constant-Q Transform representation as the melody prompt, reducing ambiguity compared to previous representations (e.g., chroma), particularly for music with multiple tracks or a wide range of pitch values. To effectively balance the control signals from text and melody prompts, we adopt a curriculum learning strategy that progressively masks the melody prompt, resulting in a more stable training process.
Experiments have been performed on text-to-music generation and music-style transfer tasks using open-source instrumental recording data. The results demonstrate that by extending StableAudio, a pre-trained text-controlled DiT model, our approach enables superior melody-controlled editing while retaining good text-to-music generation performance. These results outperform a strong MusicGen baseline in terms of both text-based generation and melody preservation for editing.

</div>
<p align="center">
<img src="method.png">
</p>


# [Update: Music Editing Examples]

These examples are all from the [Song Describer dataset](https://github.com/mulab-mir/song-describer-dataset)<a href="#note1" id="note1ref">[1]</a>. For our model, we use a text prompt and a music prompt as conditions for music editing. The text prompt is derived by randomly sampling from the original dataset and further enriched and refined, 
while the music prompt is the top-4 constant-Q transform (CQT) representation extracted from the input audio. This enables the model to achieve music transformation in terms of style and instrumentation. All audio samples are 47 seconds long, which is the maximum length supported by the model.

Scroll to see all the results if necessary.

<table class="table table-sm text-center" style="vertical-align: middle;">
  <colgroup>
      <col style="width: 300px;">
      <col style="width: 395px;">
      <col style="width: 300px;">
    </colgroup>
  <thead>
    <tr>
      <th style="text-align:center;"><span style="display: inline-block; width:250px">Input Audio</span></th>
      <th style="text-align:center;"><span style="display: inline-block; width:395px">Text Prompt</span></th>
      <th style="text-align:center"><span style="display: inline-block; width:250px">Generated Audio</span></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="3"><audio src="../audios/editing/input/49.wav" controls style="width: 200px"></audio></td>
      <td>A heartfelt, warm acoustic guitar performance, evoking a sense of tenderness and deep emotion, with a melody that truly resonates and touches the heart.</td>
      <td><audio src="../audios/editing/ours/49-1-0.wav" controls style="width: 200px"></audio></td>
    </tr>
      <tr>
      <td>A vibrant MIDI electronic composition with a hopeful and optimistic vibe.</td>
      <td><audio src="../audios/editing/ours/49-3-4.wav" controls style="width: 200px"></audio></td>
    </tr>
      <tr>
      <td>This track composed of electronic instruments gives a sense of opening and clearness.</td>
      <td><audio src="../audios/editing/ours/49-4-0.wav" controls style="width: 200px"></audio></td>
    </tr>
    <tr>
      <td rowspan="3"><audio src="../audios/editing/input/322.wav" controls style="width: 200px"></audio></td>
      <td>This track composed of electronic instruments gives a sense of opening and clearness.</td>
      <td><audio src="../audios/editing/ours/322-1-0.wav" controls style="width: 200px"></audio></td>
    </tr>
      <tr>
      <td>Hopeful instrumental with guitar being the lead and tabla used for percussion in the middle giving a feeling of going somewhere with positive outlook</td>
      <td><audio src="../audios/editing/ours/322_831.wav" controls style="width: 200px"></audio></td>
    </tr>
      <tr>
      <td>A string ensemble opens the track with legato, melancholic melodies. The violins and violas play beautifully, while the cellos and bass provide harmonic support for the moving passages. The overall feel is deeply melancholic, with an emotionally stirring performance that remains harmonious and a sense of clearness.</td>
      <td><audio src="../audios/editing/ours/322-2-0.wav" controls style="width: 200px"></audio></td>
    </tr>
    <tr>
      <td rowspan="2"><audio src="../audios/editing/input/610.wav" controls style="width: 200px"></audio></td>
      <td>An exceptionally harmonious string performance with a lively tempo in the first half, transitioning to a gentle and beautiful melody in the second half. It creates a warm and comforting atmosphere, featuring cellos and bass providing a solid foundation, while violins and violas showcase the main theme, all without any noise, resulting in a cohesive and serene sound.</td>
      <td><audio src="../audios/editing/ours/610-3-2.wav" controls style="width: 200px"></audio></td>
    </tr>
      <tr>
      <td>Pop solo piano instrumental song. Simple harmony and emotional theme. Makes you feel nostalgic and wanting a cup of warm tea sitting on the couch while holding the person you love.</td>
      <td><audio src="../audios/editing/ours/610_361.wav" controls style="width: 200px"></audio></td>
    </tr>
      <tr>
      <td rowspan="2"><audio src="../audios/editing/input/785.wav" controls style="width: 200px"></audio></td>
      <td>A whimsical string arrangement with rich layers, featuring violins as the main melody, accompanied by violas and cellos. The light, playful melody blends harmoniously, creating a sense of clarity.</td>
      <td><audio src="../audios/editing/ours/785-1-1.wav" controls style="width: 200px"></audio></td>
    </tr>
      <tr>
      <td>An instrumental piece primarily featuring acoustic guitar, with a lively and nimble feel. The melody is bright, delivering an overall sense of joy.</td>
      <td><audio src="../audios/editing/ours/785-3-3.wav" controls style="width: 200px"></audio></td>
    </tr>
      <tr>
      <td rowspan="2"><audio src="../audios/editing/input/933.wav" controls style="width: 200px"></audio></td>
      <td>A joyful saxophone performance that is smooth and cohesive, accompanied by cello. The first half features a relaxed tempo, while the second half picks up with an upbeat rhythm, creating a lively and energetic atmosphere. The overall sound is harmonious and clear, evoking feelings of happiness and vitality.</td>
      <td><audio src="../audios/editing/ours/933-1-0.wav" controls style="width: 200px"></audio></td>
    </tr>
      <tr>
      <td>A cheerful piano performance with a smooth and flowing rhythm, evoking feelings of joy and vitality.</td>
      <td><audio src="../audios/editing/ours/933-2-0.wav" controls style="width: 200px"></audio></td>
    </tr>
      <tr>
      <td rowspan="2"><audio src="../audios/editing/input/1069.wav" controls style="width: 200px"></audio></td>
      <td>An instrumental piece primarily featuring piano, with a lively rhythm and cheerful melodies that evoke a sense of joyful childhood playfulness. The melodies are clear and bright.</td>
      <td><audio src="../audios/editing/ours/1069-2-0.wav" controls style="width: 200px"></audio></td>
    </tr>
      <tr>
      <td>fast and fun beat-based indie pop to set a protagonist-gets-good-at-x movie montage to.</td>
      <td><audio src="../audios/editing/ours/1069_712.wav" controls style="width: 200px"></audio></td>
    </tr>
      <tr>
      <td><audio src="../audios/editing/input/57.wav" controls style="width: 200px"></audio></td>
      <td>A lively 70s style British pop song featuring drums, electric guitars, and synth violin. The instruments blend harmoniously, creating a dynamic, clean sound without any noise or clutter.</td>
      <td><audio src="../audios/editing/ours/57-2-3.wav" controls style="width: 200px"></audio></td>
    </tr>
      <tr>
      <td><audio src="../audios/editing/input/703.wav" controls style="width: 200px"></audio></td>
      <td>A soothing acoustic guitar song that evokes nostalgia, featuring intricate fingerpicking. The melody is both sacred and mysterious, with a rich texture.</td>
      <td><audio src="../audios/editing/ours/703-1-1.wav" controls style="width: 200px"></audio></td>
    </tr>
  </tbody>
</table> 


## Music Editing

The examples of music editing task are all from the [Song Describer dataset](https://github.com/mulab-mir/song-describer-dataset)<a href="#note1" id="note1ref">[1]</a>. For our model, we use a text prompt and a music prompt as the conditions for music editing. The text prompt comes from the dataset, while the music prompt is the top-4 constant-Q transform (CQT) representation extracted from the target audio. The table below shows the music prompt, displaying the top-4 CQT representation of the left channel from 0 to 6 seconds. For the baseline model [MusicGEN](https://github.com/facebookresearch/audiocraft/blob/main/docs/MUSICGEN.md)<a href="#note2" id="note2ref">[2]</a>, the same text prompt and Chroma-based melody representation are used as conditional inputs.

Scroll to see all the results if necessary.

<table class="table table-sm text-center" style="vertical-align: middle;">
  <colgroup>
      <col style="width: 300px;">
      <col style="width: 400px;">
      <col style="width: 200px;">
      <col style="width: 200px;">
      <col style="width: 200px;">
  </colgroup>
  <thead>
    <tr>
      <th style="text-align:center;"><span style="display: inline-block; width:300px">text prompt</span></th>
      <th style="text-align:center;"><span style="display: inline-block; width:400px">music prompt</span></th>
      <th style="text-align:center;">Target</th>
      <th style="text-align:center;">MusicGen-melody</th>
      <th style="text-align:center;">MusicGen-melody-large</th>
      <th style="text-align:center;">Ours</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>A twisty nice melody song by a slide electric guitar on top of acoustic chords later accompanied with a ukelele.</td>
      <td><img src="../audios/transfer/source/95.png" controls style="width: 400px"></td>
      <td><audio src="../audios/transfer/target/95.wav" controls style="width: 200px"></audio></td>
      <td><audio src="../audios/transfer/melody/95.wav" controls style="width: 200px"></audio></td>
      <td><audio src="../audios/transfer/melody-large/95.wav" controls style="width: 200px"></audio></td>
      <td><audio src="../audios/transfer/our/95.wav" controls style="width: 200px"></audio></td>
    </tr>
    <tr>
      <td>8-bit melody brings one back to the arcade saloons while keeping the desire to dance.</td>
      <td><img src="../audios/transfer/source/99.png" controls style="width: 400px"></td>
      <td><audio src="../audios/transfer/target/99.wav" controls style="width: 200px"></audio></td>
      <td><audio src="../audios/transfer/melody/99.wav" controls style="width: 200px"></audio></td>
      <td><audio src="../audios/transfer/melody-large/99.wav" controls style="width: 200px"></audio></td>
      <td><audio src="../audios/transfer/our/99.wav" controls style="width: 200px"></audio></td>
    </tr>
    <tr>
      <td>Instrumental piano piece with a slightly classical touch and a nostalgic, bittersweet or blue mood.</td>
      <td><img src="../audios/transfer/source/327.png" controls style="width: 400px"></td>
      <td><audio src="../audios/transfer/target/327.wav" controls style="width: 200px"></audio></td>
      <td><audio src="../audios/transfer/melody/327.wav" controls style="width: 200px"></audio></td>
      <td><audio src="../audios/transfer/melody-large/327.wav" controls style="width: 200px"></audio></td>
      <td><audio src="../audios/transfer/our/327.wav" controls style="width: 200px"></audio></td>
    </tr>
    <tr>
      <td>Positive instrumental pop song with a strong rhythm and brass section.</td>
      <td><img src="../audios/transfer/source/343.png" controls style="width: 400px"></td>
      <td><audio src="../audios/transfer/target/343.wav" controls style="width: 200px"></audio></td>
      <td><audio src="../audios/transfer/melody/343.wav" controls style="width: 200px"></audio></td>
      <td><audio src="../audios/transfer/melody-large/343.wav" controls style="width: 200px"></audio></td>
      <td><audio src="../audios/transfer/our/343.wav" controls style="width: 200px"></audio></td>
    </tr>
    <tr>
      <td>A blues piano track that would be very well suited in a 90s sitcom. The piano occupies the whole track that has a prominent bass line as well, with a general jolly and happy feeling throughout the song.</td>
      <td><img src="../audios/transfer/source/567.png" controls style="width: 400px"></td>
      <td><audio src="../audios/transfer/target/567.wav" controls style="width: 200px"></audio></td>
      <td><audio src="../audios/transfer/melody/567.wav" controls style="width: 200px"></audio></td>
      <td><audio src="../audios/transfer/melody-large/567.wav" controls style="width: 200px"></audio></td>
      <td><audio src="../audios/transfer/our/567.wav" controls style="width: 200px"></audio></td>
    </tr>
    <tr>
      <td>An upbeat pop instrumental track starting with synthesized piano sound, later with guitar added in, and then a saxophone-like melody line.</td>
      <td><img src="../audios/transfer/source/835.png" controls style="width: 400px"></td>
      <td><audio src="../audios/transfer/target/835.wav" controls style="width: 200px"></audio></td>
      <td><audio src="../audios/transfer/melody/835.wav" controls style="width: 200px"></audio></td>
      <td><audio src="../audios/transfer/melody-large/835.wav" controls style="width: 200px"></audio></td>
      <td><audio src="../audios/transfer/our/835.wav" controls style="width: 200px"></audio></td>
    </tr>
    <tr>
      <td>Pop song with a classical chord progression in which all instruments join progressively, building up a richer and richer music.</td>
      <td><img src="../audios/transfer/source/903.png" controls style="width: 400px"></td>
      <td><audio src="../audios/transfer/target/903.wav" controls style="width: 200px"></audio></td>
      <td><audio src="../audios/transfer/melody/903.wav" controls style="width: 200px"></audio></td>
      <td><audio src="../audios/transfer/melody-large/903.wav" controls style="width: 200px"></audio></td>
      <td><audio src="../audios/transfer/our/903.wav" controls style="width: 200px"></audio></td>
    </tr>
    <tr>
      <td>An instrumental world fusion track with prominent reggae elements.</td>
      <td><img src="../audios/transfer/source/959.png" controls style="width: 400px"></td>
      <td><audio src="../audios/transfer/target/959.wav" controls style="width: 200px"></audio></td>
      <td><audio src="../audios/transfer/melody/959.wav" controls style="width: 200px"></audio></td>
      <td><audio src="../audios/transfer/melody-large/959.wav" controls style="width: 200px"></audio></td>
      <td><audio src="../audios/transfer/our/959.wav" controls style="width: 200px"></audio></td>
    </tr>
  </tbody>
</table> 


## Text To Music

The examples for the text-to-music task also come from the [Song Describer dataset](https://github.com/mulab-mir/song-describer-dataset)<a href="#note1" id="note1ref">[1]</a>. For both our model and the baseline model [MusicGEN](https://github.com/facebookresearch/audiocraft/blob/main/docs/MUSICGEN.md)<a href="#note2" id="note2ref">[2]</a>, only the text prompt from the dataset is used as the control condition for music generation. In this case, the music prompt for our model is left empty.

Scroll to see all the results if necessary.


| <span style="display: inline-block; width:120px">text prompt</span> | MusicGen-melody | MusicGen-melody-large | Ours |
| :-: | :-: | :-: | :-: |
| An energetic rock and roll song, accompanied by a nervous electric guitar. |<audio src="../audios/text-to-music/melody/659.wav" controls style="width: 200px"></audio> | <audio src="../audios/text-to-music/melody-large/659.wav" controls style="width: 200px"></audio> | <audio src="../audios/text-to-music/ours/659.wav" controls style="width: 200px"></audio> |
| A deep house track with a very clear build up, very well balanced and smooth kick-snare timbre. The glockenspiel samples seem to be the best option to aid for the smoothness of such a track, which helps 2 minutes to pass like it was nothing.  A very clear and effective contrastive counterpoint structure between the bass and treble registers of keyboards and then the bass drum/snare structure is what makes this song a very good representative of house music. |<audio src="../audios/text-to-music/melody/867.wav" controls style="width: 200px"></audio> | <audio src="../audios/text-to-music/melody-large/867.wav" controls style="width: 200px"></audio> | <audio src="../audios/text-to-music/ours/867.wav" controls style="width: 200px"></audio> |
| A string ensemble starts of the track with legato melancholic playing. After two bars, a more instruments from the ensemble come in. Alti and violins seem to be playing melody while celli, alti and basses underpin the moving melody lines with harmonies and chords. The track feels ominous and melanchonic. Halfway through, alti switch to pizzicato, and then fade out to let the celli and basses come through with somber melodies, leaving the chords to the violins. |<audio src="../audios/text-to-music/melody/58.wav" controls style="width: 200px"></audio> | <audio src="../audios/text-to-music/melody-large/58.wav" controls style="width: 200px"></audio> | <audio src="../audios/text-to-music/ours/58.wav" controls style="width: 200px"></audio> |
| medium tempo ambient sounds to begin with and slow guitar plucking layering followed by an ambient rhythmic beat and then remove the layering in the opposite direction. |<audio src="../audios/text-to-music/melody/452.wav" controls style="width: 200px"></audio> | <audio src="../audios/text-to-music/melody-large/452.wav" controls style="width: 200px"></audio> | <audio src="../audios/text-to-music/ours/452.wav" controls style="width: 200px"></audio> |
| An instrumental surf rock track with a twist. Open charleston beat with strummed guitar and a mellow synth lead. The song is a happy cyberpunk soundtrack. |<audio src="../audios/text-to-music/melody/300.wav" controls style="width: 200px"></audio> | <audio src="../audios/text-to-music/melody-large/300.wav" controls style="width: 200px"></audio> | <audio src="../audios/text-to-music/ours/300.wav" controls style="width: 200px"></audio> |
| Starts like an experimental hip hop beat, transitions into an epic happy and relaxing vibe with the melody and guitar. It is an instrumental track with mostly acoustic instruments. |<audio src="../audios/text-to-music/melody/215.wav" controls style="width: 200px"></audio> | <audio src="../audios/text-to-music/melody-large/215.wav" controls style="width: 200px"></audio> | <audio src="../audios/text-to-music/ours/215.wav" controls style="width: 200px"></audio> |

## References 

<a id="note1" href="#note1ref">[1]</a> I. Manco, B. Weck, S. Doh, M. Won, Y. Zhang, D. Bogdanov, Y. Wu, K. Chen, P. Tovstogan, E. Benetos, E. Quinton, G. Fazekas, and J. Nam, “The Song Describer dataset: A corpus of audio captions for music-and-language evaluation,” in Proc. NeurIPS, New Orleans, 2023.

<a id="note2" href="#note2ref">[2]</a> J. Copet, F. Kreuk, I. Gat, T. Remez, D. Kant, G. Synnaeve, Y. Adi, and A. Defossez, “Simple and controllable music generation,” in Proc. NeurIPS, New Orleans, 2023.
