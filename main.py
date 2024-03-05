import os
def rename_dir_files(dir_path: str, seperation_place: str): # dir_path = directory path e.g "music", seperation_place = What's supposed to be removed; clear example below
  list_of_songs = os.listdir(dir_path)
  stripped_list_of_songs = [item.split(seperation_place) for item in list_of_songs]
  removed_songs_text = [item.pop(-1) for item in stripped_list_of_songs]

  for i in range(len(removed_songs_text)):
    if list_of_songs[i] != removed_songs_text[i]:
      os.rename("music/" + list_of_songs[i], "music/" + removed_songs_text[i])
      
# Example use: -> Directory with sound snippets with an unnecessary info e.g Sound effect - Email.mp3, Sound effect - Swoosh.mp3
rename_dir_files("music", "- ") # -> Removes *Sound effect - * --> new file is now Email.mp3