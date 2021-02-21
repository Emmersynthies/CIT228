
def make_album(artist, title, tracks=0):
    album_list = {
        'artist': artist.title(),
        'title': title.title(),
        }
    if tracks:
        album_list["tracks"] = tracks
    return album_list
album = make_album('taylor swift', "evermore",tracks=15)
print(album)
album = make_album('ac dc', "power up", tracks=12)
print(album)
album = make_album('mac miller', "circles", tracks=14)
print(album)
album = make_album("post malone", "stoney", tracks=18)
print(album)

title_prompt = "\nWhat album are you thinking of? "
artist_prompt = "Who's the artist? "
track_prompt = "What number in the album?"



print("Enter 'q' at any time to quit.")

while True:
    title = input(title_prompt)
    if title == 'q':
        break
    
    artist = input(artist_prompt)
    if artist == 'q':
        break
    track = input(track_prompt)
    if artist == 'q':
        break

    album = make_album(artist, title)
    print(album)

print("\nThank you for the info!")