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
<h4>Continuum(entity,sample_rate=44100)</h3>
   It is the simulated reality. It represents a 4D unreality and functions associated with them. 
   
 - <code>entity </code> is size of the continuum. It contains 4 elements. They stands for **(duration, x_points, y_points, z_points)**. **duration** signifies how many seconds of time period measured, and others signifies how many points exist per dimension. 
 - <code>sample_rate</code> represents how many samples per second.
 <h5> monotonicSpeaker(location, time_interval, amplitude, frequency, phase=1.5*pi)</h5>
    Creates a virtual oscillator that creates monotonic audio.
 - <code>location</code>:Location of the speaker. It is a tuple with 3 elements
 - <code>time_interval</code>: Signifies which time periods tone will be played. It is a tuple with 2 elements
 - <code>amplitude</code>: Indicates amplitude of the tone
 - <code>frequency </code>:Indicates frequency of the tone
 - <code>phase </code>:Indicates phase of the tone
