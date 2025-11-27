
``` bash
s.boot;


a = Buffer.read(s, thisProcess.nowExecutingPath.dirname +/+ "../audio/amen-short.wav");

(
{
	var mouse = MouseX.kr(-1, 1);

	PlayBuf.ar(
		2,
		a.bufnum,
		BufRateScale.kr(a.bufnum) * mouse,
		loop:1
	)
}.play
)

(
SynthDef(\amen, {
	arg pitch = 1, volume = 0.5;
	var sig = PlayBuf.ar(
		2,
		a.bufnum,
		BufRateScale.kr(a.bufnum) * pitch,
		loop:1
	) * volume;
	Out.ar(0, sig)
}).add
)


(
a = Synth(\amen);
OSCFunc({ |msg| a.set = Synth(\amen) }, '/amen');
OSCFunc({ |msg| a.set(\pitch, msg[1])}, '/speed');
OSCFunc({ |msg| a.set(\volume, msg[1])}, '/volume');

)

```

![[Screenshot 2025-11-27 at 16.53.32.png]]
