from pythonosc.udp_client import SimpleUDPClient
import time

SC_IP, SC_PORT = "127.0.0.1", 57120
sc = SimpleUDPClient(SC_IP, SC_PORT)

def trigger_amen():
    sc.send_message("/amen", [])
    print("Triggered amen loop")
# 
# def set_volume(vol: float):
#     sc.send_message("/volume", [float(vol)])
#     print(f"Set volume -> {vol:.2f}")
# 
# def set_speed(speed: float):
#     sc.send_message("/speed", [float(speed)])
#     print(f"Set speed -> {speed:.2f}")

if __name__ == "__main__":
    # Trigger once
    trigger_amen()
#     time.sleep(0.5)

#     # Update parameters without retriggering
#     for speed in [0.8, 1.0, 1.2]:
#         set_speed(speed)
#         set_volume(0.4 + 0.1 * (speed - 0.8))
#         time.sleep(0.8)
