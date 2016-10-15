import os
import sys

from youtube_dl import YoutubeDL

DEBUG=True

def main():
    try:
        if len(sys.argv) == 3:
            install_vlc(DEBUG)
            download(sys.argv[
        else:
            print("Usage: get_swifty [YoutubeURL] [VideoTitle]")
            sys.exit(1)
    except Exception as e:
        if DEBUG:
            print("Encountered exception in main")
            print(e)
        sys.exit(2)

def install_vlc(debug=False):
    try:
        debian  ="apt-get install -y vlc"
        redhat  ="yum install -y vlc"
        arch    ="pacman -Syu --noconfirm vlc"
        bsd     ="pkg install -y vlc"
        OR = "||"

        retval = os.system(debian+OR+redhat+OR+arch+OR+bsd)
        if debug:
            print("Attempt to install vlc, exit status = {}".format(retval))

    except Exception as e:
        if debug:
            print("Encountered error installing vlc")
            print(e)
        sys.exit(3)

def download(url, title, ydl_opts, debug=False):
    try:
        ydl_opts['outtmpl'] = title
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except Exception as e:
        if debug:
            print("Encountered error downloading video")
            print(e)
        sys.exit(4)

if __name__ == "__main__":
    main()
