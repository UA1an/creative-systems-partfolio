### What does mean SuperCollider?

**==SuperCollider IDE==** is a new cross-platform coding environment, developed specifically for SuperCollider and introduced in version 3.6.

It is easy to start using, handy to work with, and sprinkled with powerful features for experienced SuperCollider coders. It is also very customizable.

It runs equally well and looks almost the same on macOS, Linux and Windows 7. (Issues with Windows XP remain to be solved.)
# SuperCollider Patterns and Synthesis Basics

Patterns in SuperCollider are used to generate streams of values for musical parameters. They are combined with `Pbind` to create algorithmic sequences.

---

## Basic Pattern Types

### Pseq(list, repeats)

Plays a sequence of values in order, then repeats.

``` bash
Pseq([60, 62, 64, 67].midicps, inf)
```

### Prand(list, repeats)

Chooses random values from a list, without replacement until all are used.

``` bash
Prand([60, 62, 64, 67].midicps, inf)
```

### Pxrand(list, repeats)

Like `Prand`, but ensures no immediate repeats.

``` bash
Pxrand([60, 62, 64, 67].midicps, inf)
```

### Pwhite(lo, hi, repeats)

Generates random values in a range (continuous).

``` bash
Pwhite(40.midicps, 52.midicps, inf)
```

### Pshuf(list, repeats)

Shuffles the list and plays through it.

``` bash
Pshuf([60, 62, 64, 67].midicps, inf)
```

---

## Using Patterns with Pbind

`Pbind` maps pattern values to synth parameters:

``` bash
Pbind(
    \instrument, \bass,
    \freq, Pwhite(40.midicps, 52.midicps, inf),
    \dur, 0.125
).play;
```

Common keys:

- `\instrument`: SynthDef name
- `\freq`: frequency in Hz
- `\dur`: duration of each event

---

## Examples

### Sequential melody

``` bash
Pbind(
    \instrument, \bass,
    \freq, Pseq([60, 62, 64, 67].midicps, inf),
    \dur, 0.25
).play;
```

### Random bassline

``` bash
Pbind(
    \instrument, \bass,
    \freq, Prand([40, 45, 50, 55, 60].midicps, inf),
    \dur, 0.125
).play;
```

### Continuous random pitches

```bash
Pbind(
    \instrument, \bass,
    \freq, Pwhite(40.midicps, 52.midicps, inf),
    \dur, 0.125
).play;
```

---

## Synthesis Basics

### Oscillators

- `SinOsc`: sine wave oscillator.
- `Saw`: sawtooth wave.
- `Pulse`: pulse wave.

Example:
 
``` bash
{ SinOsc.ar(440, 0, 0.2) }.play;
```

### Envelopes

Shape amplitude over time using `Env`:

``` bash
{ SinOsc.ar(220) * Env.perc(0.01, 0.3).ar(doneAction:2) }.play;
```

### SynthDef Structure

Defines reusable instruments:

``` bash
SynthDef(\simpleTone, {
    |freq=440, out=0|
    var sig = SinOsc.ar(freq, 0, 0.2);
    Out.ar(out, sig!2);
}).add;
```

Play it:

``` bash
Synth(\simpleTone);
```

### Kick Drum Example

``` bash
SynthDef(\kick, {
    |out=0|
    var env = Env.perc(0.001, 0.05).kr(2);
    var pitchEnv = Env([100, 40], [0.05]).kr;
    var sig = SinOsc.ar(pitchEnv) * env;
    Out.ar(out, sig!2);
}).add;
```

### Bass Synth Example

``` bash
SynthDef(\bass, {
    |freq=60, on=1, out=0|
    var env = Env.perc(0.01, 0.2).kr(gate:1);
    var sig = Saw.ar(freq, 0.2*on) * env;
    sig = LPF.ar(sig, 800);
    Out.ar(out, sig!2);
}).add;
```

---

## Tips

- Combine multiple `Pbind` patterns for layered rhythms.
- Use envelopes for dynamic shaping.
- Explore filters (`LPF`, `HPF`) for tone control.

---

### Result code
```bash
(
{
	var freq = 90;
	var env = EnvGen.kr(Env.perc(0.001, 0.6));

	SinOsc.ar(freq, 0, 1*env) !2
}.play
)

(
SynthDef(\kick, {
	arg freq = 90;
	var env = EnvGen.kr(Env.perc(0.001, 0.05), doneAction:2);
	var sig = SinOsc.ar(freq, 0, 1*env) !2;

	Out.ar(0, sig)
}).add
)

(
SynthDef(\bass, {
	arg freq = 30, on = 1, rel = 0.5;
	var env = EnvGen.kr(Env.perc(0.001, rel), doneAction:2);
	var sig = Saw.ar(freq, 0.2*env) !2;

	Out.ar(0, sig)
}).add
)

Synth(\bass);

Synth(\kick);

TempoClock.default.tempo = 100/60; //120 BPM

(
Pbind(
	\instrument, \kick,
	\dur, Pseq([1, 1, 1/4, 1/4, 1/4, 1/4], inf),
	\freq, 60
).play;


Pbind(
	\instrument, \bass,
	\freq, Pwhite(50, 100, inf),
	\dur, Prand([0.5, 1], inf),
	\rel, Pwhite(0.1, 0.8, inf),
	\on, Prand([0,1], inf)
).play;

)
```

