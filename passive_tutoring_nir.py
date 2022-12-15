import time
import wave
import random
from datetime import datetime
import simpleaudio as sa

song_dir = '/home/pi/Desktop/all_songs_for_6_birds/'

all_songs_list = ['bird1song1.wav', 'bird1song2.wav', 'bird1song3.wav', 'bird1song4.wav', 'bird1song5.wav',
'bird2song1.wav', 'bird2song2.wav', 'bird2song3.wav', 'bird2song4.wav', 'bird2song5.wav',
'bird3song1.wav', 'bird3song2.wav', 'bird3song3.wav', 'bird3song4.wav', 'bird3song5.wav',
'bird4song1.wav', 'bird4song2.wav', 'bird4song3.wav', 'bird4song4.wav', 'bird4song5.wav',
'bird5song1.wav', 'bird5song2.wav', 'bird5song3.wav', 'bird5song4.wav', 'bird5song5.wav',
'bird6song1.wav', 'bird6song2.wav', 'bird6song3.wav', 'bird6song4.wav', 'bird6song5.wav']

def loop_songs():
    #function that loops through all_songs_list and plays one at random
    random_song = random.choice(all_songs_list)
    print("playing song: " + str(random_song))
    wave_read = wave.open(song_dir + random_song, 'rb')
    wave_obj = sa.WaveObject.from_wave_read(wave_read)
    play_obj = wave_obj.play()
    play_obj.wait_done()
    # this variable sets a random wait time between 15 and 30 seconds
    wait_time = random.randint(15,30)
    print("waiting: ", wait_time, " seconds")
    time.sleep(wait_time)

def loop_songs_between_08_and_12():
    while True:
        current_time = datetime.now().time()
        if current_time >= datetime.strptime('08:00:00', '%H:%M:%S').time() and current_time <= datetime.strptime('12:00:00', '%H:%M:%S').time():
            loop_songs()
        time.sleep(1)

if __name__ == "__main__":
    loop_songs_between_08_and_12()
