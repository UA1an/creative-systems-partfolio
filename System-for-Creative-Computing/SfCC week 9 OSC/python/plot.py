# optional_visual.py
import matplotlib.pyplot as plt

speeds = [0.8, 1.0, 1.2, 1.4]
plt.figure(figsize=(5, 3))
plt.plot(speeds, marker="o")
plt.title("Playback speeds sent")
plt.xlabel("Event index")
plt.ylabel("Speed multiplier")
plt.tight_layout()
plt.show()
