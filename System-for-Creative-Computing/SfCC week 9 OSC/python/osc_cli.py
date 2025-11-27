# osc_cli.py
# Interactive OSC controller for SuperCollider "gun" Synth.

from pythonosc.udp_client import SimpleUDPClient

SC_IP, SC_PORT = "127.0.0.1", 57120
sc = SimpleUDPClient(SC_IP, SC_PORT)

def send(path, value=None):
    if value is None:
        sc.send_message(path, [])
    else:
        sc.send_message(path, [value])
    print(f"Sent {path} {'' if value is None else value}")

HELP = """Commands:
  gun            -> trigger sample
  vol <0..1>     -> set volume (e.g., vol 0.6)
  speed <float>  -> set playback speed (e.g., speed 1.2)
  help           -> show this help
  quit           -> exit
"""

print("SuperCollider OSC CLI ready. Type 'help' for commands.")
while True:
    try:
        line = input("> ").strip()
    except (EOFError, KeyboardInterrupt):
        print("\nExiting.")
        break

    if not line:
        continue

    if line == "quit":
        break
    if line == "help":
        print(HELP)
        continue
    if line == "amen":
        send("/amen")
        continue
    if line.startswith("vol "):
        try:
            v = float(line.split()[1])
            send("/volume", v)
        except Exception:
            print("Usage: vol 0.0..1.0")
        continue
    if line.startswith("speed "):
        try:
            s = float(line.split()[1])
            send("/speed", s)
        except Exception:
            print("Usage: speed <float>")
        continue

    print("Unknown command. Type 'help'.")
