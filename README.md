# The Incus Project
   A headphone is an escape from reality. When you upset, you start to listen a music then you feel relief. When you are in underground train, you seem to be felt scared; however, this not the case. Most of us listen music during the journey and we feel something depending on what is included in the music. Great accompanionship! This implies that hearing impacts out mood and it is very strong sense. The Incus Project renders this fact. It creates real like audio. By this way you would create your own reality and determine what you hear.
## Tree of the Module
<pre>
Continuum(entity,sample_rate=44100)---|
                                      |----monotonicSpeaker(location, time_interval, amplitude, frequency, phase=1.5*pi)
                                      |----hear(location)
                                      |----play_music(path_to_file,location,start_time)
</pre>
## Docs
<h3>Continuum(entity,sample_rate=44100)</h3>
   It is the simulated reality. It represents a 4D unreality and functions associated with them. 
   
 <ul><code>entity </code> is size of the continuum. It contains 4 elements. They stands for **(duration, x_points, y_points, z_points)**. **duration** signifies how many seconds of time period measured, and others signifies how many points exist per dimension. </ul>
 <ul> <code>sample_rate</code> represents how many samples per second.</ul>
 <h4> monotonicSpeaker(location, time_interval, amplitude, frequency, phase=1.5*pi)</h4>
    Creates a virtual oscillator that creates monotonic audio.
 <ul> <code>location</code>:Location of the speaker. It is a tuple with 3 elements</ul>
 <ul> <code>time_interval</code>: Signifies which time periods tone will be played. It is a tuple with 2 elements</ul>
 <ul><code>amplitude</code>: Indicates amplitude of the tone</ul>
 <ul> <code>frequency </code>:Indicates frequency of the tone</ul>
 <ul> <code>phase </code>:Indicates phase of the tone</ul>

<h4>hear(location)</h4>
Renders which sound is heard in given location through the entire time period of the *Continuum*
- <code>location</code>: Indicates location of the virtual microphone. It is a tuple with 3 elements

<h4>play_music(path_to_file,location,start_time)</h4>
Adds a sound file into Continuum

 <ul><code> path_to_file </code>: Indicates location of **.wav** file. **Only .wav files are accepted**.</ul>
  <ul><code>location</code>:Indicates where will file played. It is a tuple with 3 elements.</ul>
  <ul><code>start_time</code>: Signifies when the file is played.</ul>
 
