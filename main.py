#!/usr/bin/env python3

import pytube

def yt_download(url):
    try:
        video_url = url.strip()
        yt = YouTube(video_url)
        video_title = yt.title
        stream = yt.streams.get_highest_resolution()
        stream.download(output_path="./Downloads")
        return f"# Successfully Downloaded >>>>>  {video_title}"
    except YouTubeError as e:
        return "invalid_URL"


def single_video(url):
    print("# Processing Request...")
    operation = yt_download(url)

    if operation == "invalid_URL":
        print("# Enter Valid URL")
    else:
        print(operation)
        print("#")


def multiple_videos(urls):
    if not urls:
        print("# No URLs entered")
        return

    for url in urls:
        single_video(url)

def url_list(path):
    if not path:
        print("# No path entered")
        return

    with open(path, 'r') as url_file:
        for url in url_file:
            single_video(url)

def help():
    print('''
    This script is a YouTube video downloader. It allows you to download single videos, multiple videos, or videos from a text file.

    Available Commands:
        s - Download a single video.
        m - Download multiple videos.
        l - Download videos from a text file.
        h - Get help.
        q - Quit.

    How to Use:
        - To download a single video, enter the video's URL and press Enter.
        - To download multiple videos, enter the videos' URLs, one per line, and enter 'x' when you are finished.
        - To download videos from a text file, enter the path to the text file and press Enter.
        - The text file should contain one video URL per line.

    Help:
        - To get help, press h.

    Exit:
        - To quit, press q.

    Notes:
        - This script only downloads non-age restricted videos.
        - The videos will be downloaded to the ./Downloads directory.
    
    Author:
        - sahanEra [https://sahanera.me]
    
    License:
        - This project is licensed under the MIT License.

    ''')

    
print('''
==========================================
        Youtube Video Downloader
                by SahanEra
========================================== ''')

print('''
Available Commands:
    s      | for download single video
    m      | for download multiple videos 
    l      | for download videos using url list(txt file)
    h      | for get help
    q      | for exit
''')

while True:
    command = input("yt_downloader$ ").lower()

    if (command == "q"):
        print("See You Again!!")
        break

    elif (command == "s"):
        url = input("# Enter URL: ")
        single_video(url)

    elif (command == "m"):
        urls = []
        url = "epty"
        while not((url == "x") or (url == "X")):
            url = input("# Enter URL, or 'x' for exit> ")
            if not((url == "x") or (url == "X")):
                urls.append(url)
        multiple_videos(urls)

    elif (command == "l"):
        url_file = input("# Enter txt file path> ")
        url_list(url_file)

    elif (command == "h"):
        help()

    else:
        print("----- Invalid Input! [for get help, enter 'h'] -----")
