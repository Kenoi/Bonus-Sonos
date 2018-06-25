from soco import SoCo
Sonos = SoCo("192.168.0.21")
LastVolume = Sonos.volume
LastState = Sonos.get_current_transport_info()["current_transport_state"]



while True:
    CurrentVolume = Sonos.volume
    if CurrentVolume != LastVolume:
        print(CurrentVolume)
        LastVolume = CurrentVolume
        CurrentVolume = Sonos.volume
    CurrentState = Sonos.get_current_transport_info()["current_transport_state"]
    if CurrentState != LastState:
        print("Change in state!")
        LastState = CurrentState
