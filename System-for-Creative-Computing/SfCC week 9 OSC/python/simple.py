from pythonosc.udp_client import SimpleUDPClient
sc = SimpleUDPClient("127.0.0.1", 57120)

sc.send_message("/amen", [])
sc.send_message("/volume", [0.5])
sc.send_message("/speed", [1.2])
