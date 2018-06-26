from soco import SoCo
Sonos = SoCo("192.168.0.21")
while True:
    print(Sonos.volume)

