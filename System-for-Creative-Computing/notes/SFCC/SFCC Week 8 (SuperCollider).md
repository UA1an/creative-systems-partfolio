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

```
Pseq([60, 62, 64, 67].midicps, inf)
```

### Prand(list, repeats)

Chooses random values from a list, without replacement until all are used.

```
Prand([60, 62, 64, 67].midicps, inf)
```

### Pxrand(list, repeats)

Like `Prand`, but ensures no immediate repeats.

```
Pxrand([60, 62, 64, 67].midicps, inf)
```

### Pwhite(lo, hi, repeats)

Generates random values in a range (continuous).

```
Pwhite(40.midicps, 52.midicps, inf)
```

### Pshuf(list, repeats)

Shuffles the list and plays through it.

```
Pshuf([60, 62, 64, 67].midicps, inf)
```

---

## Using Patterns with Pbind

`Pbind` maps pattern values to synth parameters:

```
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

```
Pbind(
    \instrument, \bass,
    \freq, Pseq([60, 62, 64, 67].midicps, inf),
    \dur, 0.25
).play;
```

### Random bassline

```
Pbind(
    \instrument, \bass,
    \freq, Prand([40, 45, 50, 55, 60].midicps, inf),
    \dur, 0.125
).play;
```

### Continuous random pitches

```
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

```
{ SinOsc.ar(440, 0, 0.2) }.play;
```

### Envelopes

Shape amplitude over time using `Env`:

```
{ SinOsc.ar(220) * Env.perc(0.01, 0.3).ar(doneAction:2) }.play;
```

### SynthDef Structure

Defines reusable instruments:

```
SynthDef(\simpleTone, {
    |freq=440, out=0|
    var sig = SinOsc.ar(freq, 0, 0.2);
    Out.ar(out, sig!2);
}).add;
```

Play it:

```
Synth(\simpleTone);
```

### Kick Drum Example

```
SynthDef(\kick, {
    |out=0|
    var env = Env.perc(0.001, 0.05).kr(2);
    var pitchEnv = Env([100, 40], [0.05]).kr;
    var sig = SinOsc.ar(pitchEnv) * env;
    Out.ar(out, sig!2);
}).add;
```

### Bass Synth Example

```
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

