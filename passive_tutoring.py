import logging
import time
import wave
import random
import configparser
import simpleaudio as sa
from datetime import datetime
from os import listdir, getcwd
from os.path import isfile, join

config = configparser.ConfigParser()
config.read('/etc/systemd/system/passive_tutoring.service')

SONG_DIR = config['config']['song_directory']
INTERVAL_LIST = config['config']['tutoring_intervals'].replace(" ", "").split(",")
LOG_LEVEL = config['config']['log_level'].upper()

logging.basicConfig(level=LOG_LEVEL)

logging.info("using songs from directory: " + SONG_DIR)

start_list = []
stop_list = []

for time_interval in INTERVAL_LIST:
    start_list.append(time_interval.split("-")[0])
    stop_list.append(time_interval.split("-")[1])

all_songs_list = [item for item in listdir(SONG_DIR) if isfile(join(SONG_DIR, item))]

def loop_songs():
    # function that loops through all_songs_list and plays one at random
    random_song = random.choice(all_songs_list)
    logging.info("playing song: " + str(random_song))
    
    song_path = join(SONG_DIR, random_song)
    wave_read = wave.open(song_path, 'rb')
    wave_obj = sa.WaveObject.from_wave_read(wave_read)
    play_obj = wave_obj.play()
    play_obj.wait_done()

    # this variable sets a random wait time between 15 and 30 seconds
    wait_time = random.randint(15,30)
    logging.info("waiting: ", wait_time, " seconds")
    time.sleep(wait_time)

def loop_songs_intervals():
    while True:
        current_time = datetime.now().time()
        for i in range(len(start_list)):
            start_time = start_list[i]
            end_time = stop_list[i]
            if current_time >= datetime.strptime(start_time+':00', '%H:%M:%S').time() and current_time <= datetime.strptime(end_time+':00', '%H:%M:%S').time():
                loop_songs()
        
        time.sleep(1)

if __name__ == "__main__":
    loop_songs_intervals()
