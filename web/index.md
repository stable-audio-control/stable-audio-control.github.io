<div style="text-align: center"> 

<h1> Editing Music with Melody and Text: <br> Using ControlNet for Diffusion Transformer </h1>
Siyuan Hou<sup>1,2</sup>, Shansong Liu<sup>2</sup>, Ruibin Yuan<sup>3</sup>, Wei Xue<sup>3</sup>, Ying Shan<sup>2</sup>, Mangsuo Zhao<sup>1</sup>, Chao Zhang<sup>1</sup>  <br>
<sup>1</sup>Tsinghua University <br>
<sup>2</sup>ARC Lab, Tencent PCG <br>
<sup>3</sup>Hong Kong University of Science and Technology<br>

<p>
Supporting webpage for ICASSP 2025.<br>
<!-- <a href="https://arxiv.org/abs/2301.12503">[Paper on ArXiv]</a> -->
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
