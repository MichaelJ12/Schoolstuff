import tkinter as tk
import pygame
import threading
from mutagen.mp3 import MP3
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from mutagen.easyid3 import EasyID3

# Initialize pygame mixer for audio playback
pygame.mixer.init()

# Create the root window for the music player
root = tk.Tk()
root.title("Music Player")
root.geometry("500x400")

# Global variables
playlist = []  # List to store the playlist
current_index = -1  # Current song index
progressbar = None  # Progress bar for the song position

print(playlist)

# Function to load and play a song
def load_play():
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3;*.wav")])
    def _play_audio():
        if file_path:
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.play()
            update_status()
            song_info(file_path=file_path)

    threading.Thread(target=_play_audio, daemon=True).start()

# Function to display song information
def song_info(file_path=None):
    global progressbar

    if file_path:
        audio = MP3(file_path, ID3=EasyID3)
    else:
        audio = MP3(playlist[current_index], ID3=EasyID3)

    title = "Unknown Title"
    artist = "Unknown Artist"

    if 'title' in audio:
        title = audio['title'][0]

    if 'artist' in audio:
        artist = audio['artist'][0]

    duration = audio.info.length  # Duration in seconds

    minutes = int(duration // 60)
    seconds = int(duration % 60)

    # Calculate the duration (in seconds)
    dur = minutes * 60 + seconds

    # Update the labels for song info
    title_label.config(text=f"{title}")
    artist_label.config(text=f"{artist}")
    duration_label.config(text=f"{minutes}:{seconds:02d}")

    print(f"Title: {title}")
    print(f"Artist: {artist}")
    print(f"Duration123: {dur}")
    print(f"Duration: {minutes}:{seconds:02d}")

    # Remove the old progress bar if it exists
    if progressbar:
        progressbar.destroy()

    # Create and update the new progress bar
    bar_progress(dur)  # Pass dur to the progress bar function

# Function to update the progress bar
def bar_progress(dur):
    global progressbar

    progressbar = ttk.Progressbar(root, length=300, mode='determinate', maximum=dur)
    progressbar.pack()

    def update_progress():
        current_pos = pygame.mixer.music.get_pos() / 1000

        progressbar['value'] = current_pos

        if pygame.mixer.music.get_busy() or current_pos <= dur:
            root.after(100, update_progress)
        else:
            progressbar['value'] = progressbar['maximum']
            print("Audio finished.")

    update_progress()

# Function to add a song to the playlist
def add_playlist():
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3;*.wav")])
    playlist.append(file_path)

    def _play_audio():
        if file_path:
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.play()
            update_status()
            song_info(file_path=file_path)

    threading.Thread(target=_play_audio, daemon=True).start()

    for index, songs in enumerate(playlist):
        print(f"Index {index}: {songs}")

# Function to play the next song in the playlist
def next_song():
    global current_index
    if current_index < +len(playlist):
        current_index += 1
        pygame.mixer.music.load(playlist[current_index])
        pygame.mixer.music.play()
        song_info()
        print(current_index)

# Function to play the previous song in the playlist
def previous_song():
    global current_index
    if current_index > -len(playlist):
        current_index -= 1
        pygame.mixer.music.load(playlist[current_index])
        pygame.mixer.music.play()
        song_info()
        print(f"test: {playlist[current_index]}")
        print(current_index)

# Function to update the play/pause status label
def update_status():
    if pygame.mixer.music.get_busy():
        status_label.config(text="Playing")
    else:
        status_label.config(text="Paused")

# Function to toggle play and pause
def play_pause_button():
    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.unpause()
        play_pause_button.config(text="Play")
        update_status()
    else:
        pygame.mixer.music.pause()
        play_pause_button.config(text="Pause")
        update_status()

# Function to update the volume
def update_volume(value):
    volume = float(value) / 100
    pygame.mixer.music.set_volume(float(volume))
    print(scale_widget.get())

# UI Elements
button_frame = tk.Frame(root)
button_frame.pack()

song_label = Label(button_frame, pady=10, text='Songs')
song_label.pack()

load_button = tk.Button(button_frame, command=load_play, padx=10, text="load")
load_button.pack(side=tk.TOP, fill=BOTH)

add_playlist_button = tk.Button(button_frame, command=add_playlist, padx=10, text="add playlist")
add_playlist_button.pack(side=tk.TOP, fill=BOTH)

status_label = tk.Label(button_frame, fg="blue")
status_label.pack()

title_label = tk.Label(button_frame, text=f"")
title_label.pack()

artist_label = tk.Label(button_frame, text=f"")
artist_label.pack()

duration_label = tk.Label(button_frame, text=f"")
duration_label.pack()

next_button1 = tk.Button(button_frame, command=next_song, padx=10, text="Next")
next_button1.pack(side=tk.RIGHT)

play_pause_button = tk.Button(button_frame, command=play_pause_button, padx=10, text="Play")
play_pause_button.pack(side=tk.RIGHT)

previous_button2 = tk.Button(button_frame, command=previous_song, padx=10, text="Previous")
previous_button2.pack(side=tk.RIGHT)

scale_widget = tk.Scale(button_frame, from_=0, to=100, command=update_volume, orient=HORIZONTAL)
scale_widget.set(10)
scale_widget.pack(side=tk.TOP)

root.mainloop()
