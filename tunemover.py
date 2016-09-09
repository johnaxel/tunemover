import os
import re
from shutil import copytree, ignore_patterns

music_source = os.environ['MUSIC_SOURCE']
music_dest = os.environ['MUSIC_DESTINATION']

artist_source = os.listdir(music_source)
artist_dest = os.listdir(music_dest)

regex_dot = re.compile(r'^\.')
regex_z = re.compile(r'^z-')

filtered_artist_source = [i for i in artist_source if not regex_dot.match(i)]
filtered_artist_dest = [i for i in artist_dest if not regex_dot.match(i)]

for artist in filtered_artist_source:
    copy_artist_source = '%s/%s' % (music_source, artist)
    copy_artist_dest = '%s/%s' % (music_dest, artist)
    
    if artist not in filtered_artist_dest:
        copytree(
            copy_artist_source, 
            copy_artist_dest, 
            symlinks=False, 
            ignore=ignore_patterns('z-*')
        )
        print "Copying artist %s ..." % artist.upper() 
    else:
        album_source = os.listdir(copy_artist_source)
        album_dest = os.listdir(copy_artist_dest)
        filtered_album_source = [i for i in album_source if not regex_z.match(i)]
        filtered_album_dest = [i for i in album_dest if not regex_z.match(i)]
        
        for album in filtered_album_source:
            copy_album_source = '%s/%s' % (copy_artist_source, album)
            copy_album_dest = '%s/%s' % (copy_artist_dest, album)
            
            if album not in filtered_album_dest:
                copytree(
                    copy_album_source, 
                    copy_album_dest, 
                    symlinks=False, 
                    ignore=None
                ) 
                print "Copying album %s by artist %s ..." % (album.upper(), artist.upper())