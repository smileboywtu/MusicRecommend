#!/usr/bin/env python2

"""

	this script use python3 and work period to get the
	recommend music from netease.

"""

import time
import sqlite3
from netease import NetEase


# config
USERNAME = 'your username'
PASSWORD = 'your password'
DATABASE_URL = 'recommend.db'

UPDATE_PERIOD = 6 * 60 * 60



def period(seconds):
    """ use this to sleep the program."""
    def schedule(func, *args):
        while True:
            func(*args)
            time.sleep(seconds)
    return schedule


def get_song_list():
    instance = NetEase()
    login_info = instance.login(USERNAME, PASSWORD)
    playlist = instance.recommend_playlist()
    songs = instance.dig_info(playlist, 'songs')
    # get ten most ones
    collection = []
    for index, song in enumerate(songs):
        if index == 10: break
        item = {}
        item['artist'] = song['artist']
        item['song_name'] = song['song_name']
        collection.append(item)
    return collection


@period(UPDATE_PERIOD)
def start():
    songs = get_song_list()
    with sqlite3.connect(DATABASE_URL) as db:
        cursor = db.cursor()
        cursor.execute('delete from music_recommend')
        for song in songs:
            cursor.execute("insert into music_recommend(name, singer) values(?, ?)",
                (song['song_name'], song['artist']))
        db.commit()


if __name__ == '__main__':
    start()
