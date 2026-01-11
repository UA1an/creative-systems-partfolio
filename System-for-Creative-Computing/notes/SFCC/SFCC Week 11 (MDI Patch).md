## Overview
For this task, I created **a Pure Data (Pd)** patch that generates random MIDI notes. The purpose of the patch is to demonstrate how MIDI data can be generated and sent from Pure Data, without the need for an external analogue synthesiser or sound output.

The patch focuses on MIDI logic rather than audio synthesis, which aligns with the task requirements.

## Patch Description
The patch consists of a simple generative system that continuously produces MIDI note values at a fixed time interval.

A toggle object is used to start and stop the system. When activated, it triggers a metro object that sends regular timing pulses. These pulses are then used to generate random MIDI note values.

## Explanation of Key Objects
 
* ### Toggle (`tgl`)
  The toggle is used to control the patch. When switched on, it activates the metro object and starts the generation of MIDI notes. When switched off, the patch stops sending data.
![[Toggle.png]]
---
* ### Metro (`metro 500`)
  The metro object sends a bang every 500 milliseconds. This controls the rhythm and timing of the MIDI note generation.
![[Metro.png]]
---
* ### Random (`random 60`)
  The random object generates random numbers between 0 and 59. These values represent raw MIDI note offsets.
![[Random.png]]
---
* ### Addition (`+ 30`)
  This object shifts the generated values into a more musical MIDI note range (approximately notes 30–89), avoiding extremely low or high pitches.
![[Addition.png]]
---
* ### Number Box
  A number box is connected to the note generation chain to visually display the changing MIDI note values. This confirms that the patch is actively generating notes, even if no sound is produced.
![[NumberBox.png]]
---
* ### MakeNote (`makenote 100 300`)
  The makenote object converts the MIDI note numbers into proper MIDI note on and note off messages. It also defines the velocity and duration of each note.
![[MakeNote.png]]
---

* ### NoteOut (`noteout`)
  The noteout object sends the generated MIDI data to the selected MIDI output device.
![[NoteOut.png]]


## MIDI Output and Visibility

No external synthesiser or MIDI instrument was connected during testing. As a result, no audible sound or visible MIDI notes were produced outside of Pure Data.

However, the changing values in the number box confirm that MIDI note data is being generated correctly. The task specifically required the creation of a Pd patch that outputs MIDI notes, not the use of a physical or virtual synthesiser.

## Reflection

This task helped me understand how Pure Data can be used for generative MIDI systems rather than audio synthesis alone. I learned how timing, randomness, and MIDI message construction work together in a simple patch.

I can see how this approach could be expanded by connecting the MIDI output to external software instruments, hardware synthesisers, or more complex generative systems in future projects.

## Result

![[Result11.png]]