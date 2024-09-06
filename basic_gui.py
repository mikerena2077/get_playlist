#python basic_gui.py

from tkinter import * 
import sys
import requests
import urllib.request
import pyperclip
import subprocess
import os
from pytube import Playlist
from pytubefix import YouTube
from pytubefix.cli import on_progress
import threading

#sample url
#https://www.youtube.com/watch?v=nVy4GAtkh7Q

#sample playlist url
#https://www.youtube.com/watch?v=MNMqyrhPrXY&list=PL6ogdCG3tAWjo_2ljw--dgT5N-DU5Ybyc


def newline():
   print("")
   
def CloseIt():
   root.destroy()

def dn():
   x = threading.Thread(target=thread_function_dn, args=(1,))
   x.start()

def thread_function_dn(name):
   url = E2.get()
   url_b = url
   
   if not url_b:
      print("no url entered")
      return -1
      
   os.chdir('C:\\Users\\miker\\OneDrive\\Desktop\\')
   
   yt = YouTube(url, on_progress_callback = on_progress)
   print(yt.title)
   
   tb.insert('end', yt.title + "\n\n")
   tb.insert('end', url_b+ "\n")
   
   ys = yt.streams.get_audio_only()
   ys.download(mp3=True)
   
   newline()
   newline()
   print("done")


def scrape():
   x = threading.Thread(target=thread_function_scrape, args=(1,))
   x.start()

def thread_function_scrape(name):
    

   url = E1.get()
   
   video_url = url
   
   if not video_url:
      print("no url entered")
      return -1
      
      
   # Create a YouTube object
   playlist = Playlist(video_url)

   print(f"Number of videos in the playlist: {len(playlist.video_urls)}")


   #print("Title of the page:", title)
   
   # Retrieve the video URLs
   urls = []
   title_list = []
   link_list = []
   
   for url in playlist:
      urls.append(url)
      
      yt = YouTube(url, on_progress_callback = on_progress)
      #print(yt.title)
      
      title_list.append(yt.title)
      link_list.append(url)
    

   print(urls)
   
   tb.insert('end', playlist.title + "\n\n")
      
      
   for i in range(0, len(title_list)):

      
      tb.insert('end', str(i + 1) + ". " + title_list[i] + "\n\n")
      tb.insert('end', link_list[i] + "\n\n")
      
     
   
   
   # Define the path to the folder
   #folder_path = 'C:\\Users\\miker\\OneDrive\\Desktop\\dn\\'
   folder_path = 'C:\\Users\\miker\\OneDrive\\Desktop\\' 
   folder_path += playlist.title.replace(" ", "_").replace(":", "_") + "\\" #dn\\'

   #playlist.title

   # Check if the folder exists
   if not os.path.exists(folder_path):
      # Create the folder if it doesn't exist
       os.makedirs(folder_path)
       print(f'Folder "{folder_path}" created.')
   else:
      print(f'Folder "{folder_path}" already exists.')

   
   os.chdir(folder_path)
   
   for url in playlist:
      url_b = url
 
      yt = YouTube(url, on_progress_callback = on_progress)
      print(yt.title)
      
      file_name = yt.title.replace("?", "_")
      
      ys = yt.streams.get_audio_only()
      ys.download(mp3=True, filename=file_name)
      
   newline()
   newline()
   print("done")
   
   
root = Tk()
root.geometry("500x550")

root.title("Yt downloader")

tb = Text(
    root,
    height=25,
    width=60
)
tb.grid(row=0, column=0)       

E1 = Entry(root, width = 80)
E1.grid(row=1, column=0)


button1 = Button(root, text="Get Urls", width=7,  command=scrape)
button1.grid(row=2, column=0)

button2 = Button(root, text="Exit", width=5, command=CloseIt)
button2.grid(row=5, column=0)

E2 = Entry(root, width = 80)
E2.grid(row=3, column=0)

button3 = Button(root, text="dn", width=7,  command=dn)
button3.grid(row=4, column=0)


root.mainloop()

