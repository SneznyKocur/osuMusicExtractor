import os
import music_tag
import shutil
songs_dir = input("Enter the osu songs directory: ")
output_dir = input("Enter the output directory: ")
for songdir in os.listdir(songs_dir):
    os.chdir(os.path.abspath(os.path.join(songs_dir, songdir)))
    for file in os.listdir():
        if file.endswith(".osu"):
            with open(file, "r") as f:
                lines = f.readlines()
                for line in lines:
                    if "AudioFilename" in line:
                        audiofile = line.split(":")[1].strip() 
                    if "Title:" in line:
                        title = line.split(":")[1].strip()
                    if "TitleUnicode:" in line:
                        titleunicode = line.split(":")[1].strip()
                    if "Artist:" in line:
                        artist = line.split(":")[1].strip()
                    if "ArtistUnicode:" in line:
                        artistunicode = line.split(":")[1].strip()
                extension = os.path.splitext(audiofile)[1]
                if "\\" in title or "/" in title:
                    title = title.replace("\\", "")
                    title = title.replace("/", "")    
                if "\\" in artist or "/" in artist:
                    artist = artist.replace("\\", "")
                    artist = artist.replace("/", "")

                
                try:
                    shutil.copyfile(os.path.abspath(audiofile), os.path.abspath(f"{output_dir}/{title} - {artist}.{extension}"))
                except:
                    print(f"Failed to copy {os.path.abspath(audiofile)}")
                    continue
                f = music_tag.load_file(os.path.abspath(f"{output_dir}/{title} - {artist}.{extension}"))
                f['title'] = titleunicode
                f['artist'] = artistunicode
                f.save()
                break
    os.chdir(os.path.join(songs_dir))
