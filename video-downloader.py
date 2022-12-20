from pytube import YouTube, exceptions
import sys
import argparse

def progressbar(progress, file_size, prefix="", size=60, out=sys.stdout):
    count = file_size

    def show(j):
        x = int(size*j/count)
        print("{}[{}{}] {}/{}".format(prefix, "█"*x, "."*(size-x), j, count), 
                end='\r', file=out, flush=True)

    show(0)
    for i, item in file_size:
        yield item
        show(i+progress)
    print("\n", flush=True, file=out)

def on_progress(vid, chunk, bytes_remaining):
    total_size = vid.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    totalsz = (total_size/1024)/1024
    totalsz = round(totalsz,1)
    remain = (bytes_remaining / 1024) / 1024
    remain = round(remain, 1)
    dwnd = (bytes_downloaded / 1024) / 1024
    dwnd = round(dwnd, 1)
    percentage_of_completion = round(percentage_of_completion,2)

    prefix = "Download Progress: "
    size = 50

    def show(j):
        x = int(size*j/totalsz)
        print("{}[{}{}] {}% - {}/{}MB".format(prefix, "="*x, "-"*(size-x), percentage_of_completion, j, totalsz), 
                end='\r', file=sys.stdout, flush=True)

    show(dwnd)
    if totalsz == dwnd :
        print("", flush=True, file=sys.stdout)
        print("Download completed, enjoy your video!")

def main():
    parser = argparse.ArgumentParser("YouTube video downloader.")
    parser.add_argument("--link", help="The URL of the YouTube video.", type=str, required=True)
    parser.add_argument("--resolution", help="Resolution of video to download, that shold match 2160p, 1440p, 1080p, 720p, 480p, 360p or 240p.", type=str, required=True)
    parser.add_argument("--oauth", help="Set this flag as 'True' if you want to download aged restricted videos", type=bool, default=False)
    args = parser.parse_args()

    link = args.link
    resolution = args.resolution
    oauth = args.oauth

    resolutionList = ["2160p", "1440p", "1080p", "720p", "480p", "360p", "240p"]

    if resolution not in(resolutionList):
        return print('Error: The required resolution is not valid, please enter one of these 2160p, 1440p, 1080p, 720p, 480p, 360p or 240p.')

    try:
        yt = YouTube(link, use_oauth=oauth)
        yt.register_on_progress_callback(on_progress)

        print(f'Title: {yt.title}')
        yt.streams.filter(res=resolution, progressive=False).first().download()
    except exceptions.RegexMatchError as error:
        print(f"Error: The link '{link}' is not valid, please enter a valid one.")

    except exceptions.ExtractError as error:
        print(f"Error: {error}")
    
    except AttributeError as error:
        yt.streams.get_highest_resolution().download()
        print(f"It was not possible to download the video in {resolution}, so we downloaded it at the highest quality as possible.")

    except exceptions.AgeRestrictedError as error:
        print(f"Error: The video have age restriction, if you want to download enter the flag '--oauth' as true.")

    except Exception as error:
        print(f"Error: {error}")

if __name__ == "__main__":
    main()