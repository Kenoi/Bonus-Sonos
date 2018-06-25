from soco import SoCo
import time
Sonos = SoCo("192.168.0.21")
#IP Adress of the desired speaker.
while True:
    CurrentState = Sonos.get_current_transport_info()["current_transport_state"]
    if CurrentState == "PAUSED_PLAYBACK":
        time.sleep(300)
        #Time before the status is checked again.
        CurrentState = Sonos.get_current_transport_info()["current_transport_state"]
        if CurrentState == "PAUSED_PLAYBACK":
            Sonos.play_uri("x-rincon-mp3radio://bbcmedia.ic.llnwd.net/stream/bbcmedia_radio2_mf_q?s=1527663981&e=1527678381&h=dc603413da37642fe5f6914969d4c548", title="Radio 2")
            #URI for radio stream. Replace http with x-rincon-mp3radio:// The title tag can be changed to suit the radio station.
            Sonos.pause()
            #Pauses the audio before it can start playing.
    time.sleep(300)
    #Time before status is checked again.
