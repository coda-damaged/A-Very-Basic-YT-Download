from pytubefix import YouTube, Playlist
from pytubefix.cli import on_progress
import webbrowser
import time

# print("""                                               
#                                       .:          
#                                    .:?J7^!PP.     
#                 ^7YPGGGGP5Y?!~^^75B#&#:#BB@J      
#              :JB@@@@@@@@@@@@@@@@@@@@@#P&&BGP~     
#          :!7J#@@@@@@@@@@@@@@@@@@@@@GPYJ^^^!Y5:    
#         ~JG@@@@@@@@5Y#@@@@@@@@@@@@P^:!?P&@@@&P^   
#      7YYJ~ P@@@@@@@BJ!Y&@@@@@@@@@@&#BGP55PG?^75   
#     Y###@@BB@@@@@@@@@#~G@@@@@@@@@@&J:      ..     
#     :....!!~&@@@@@@@@@?G5B@@@@@@@G:               
#   .5#&&BY   :G@@@@@@@5:. !@@@@@@G                 
#   :#P?!77     G@@@@&J     B@B?@@5                 
#   .: ^JY      !@@@@P      ?@G 7&@^                
#     !@@P       !PGGBBBJ    Y#5J!5G5!              
#     .^:             :^:     .^~. .^:              

# """)

print("YouTube Downloader \nBy: TrashOS")
print("-----------------------------------")
# Below is trash
while True:
    try:
        print("\nWhat would you like to do?")

        choice = input(
            "1. Download a video\n"
            "2. Download audio only\n"
            "3. Download playlist audio\n"
            "4. Exit\n> "
        )

        if choice == "1":
            try:
                url = input("Enter the YouTube video URL: ")

                yt = YouTube(url, on_progress_callback=on_progress)

                print(f"Title: {yt.title}")

                ys = yt.streams.get_highest_resolution()

                if ys is None:
                    print("No video stream found.")
                else:
                    print("Downloading...")
                    ys.download()
                    print("Download complete!")

            except Exception as e:
                print(f"Error downloading video: {e}")

        elif choice == "2":
            try:
                url = input("Enter the YouTube video URL: ")

                yt = YouTube(url, on_progress_callback=on_progress)

                print(f"Title: {yt.title}")

                ys = yt.streams.get_audio_only()

                if ys is None:
                    print("No audio stream found.")
                else:
                    print("Downloading audio...")
                    ys.download(filename=f"{yt.title}.mp3")
                    print("Audio download complete!")

            except Exception as e:
                print(f"Error downloading audio: {e}")

        elif choice == "3":
            try:
                url = input("Enter the YouTube playlist URL: ")

                pl = Playlist(url)

                print(f"Playlist title: {pl.title}")

                for video in pl.videos:
                    try:
                        print(f"\nDownloading: {video.title}")

                        ys = video.streams.get_audio_only()

                        if ys is not None:
                            ys.download(filename=f"{yt.title}.mp3")
                            print("Done!")
                        else:
                            print("No audio stream found.")

                    except Exception as e:
                        print(f"Skipped video due to error: {e}")

                print("Playlist download complete!")

            except Exception as e:
                print(f"Error downloading playlist: {e}")

        elif choice == "4":
            print("dont waste my time then.....")
            time.sleep(1)

            try:
                webbrowser.open(
                    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSwHp6XD1TuSNae9dEPiUNv-6HEnpbKb3Zr2Q&s"
                )
            except Exception as e:
                print(f"Browser error: {e}")

            time.sleep(3)
            break

        else:
            print("Invalid option. Please choose 1-4.")

    except KeyboardInterrupt:
        print("\nProgram stopped by user.")
        break

    except Exception as e:
        print(f"Unexpected error: {e}")
# end of trash