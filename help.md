
# miditoyz
here's a full list of all the `miditoyz` command help genrated by 
calling `miditoyz --help` and `miditoyz <command> --help` for each 
command:

```
$ miditoyz --help
                                                                                
 Usage: miditoyz [OPTIONS] COMMAND [ARGS]...                                    
                                                                                
╭─ Options ────────────────────────────────────────────────────────────────────╮
│ --install-completion          Install completion for the current shell.      │
│ --show-completion             Show completion for the current shell, to copy │
│                               it or customize the installation.              │
│ --help                        Show this message and exit.                    │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ───────────────────────────────────────────────────────────────────╮
│ catalog  Memorize a new catalog file for future streaming.                   │
│ devices  List available midi devices.                                        │
│ dump     Dump a MIDI song file in raw text format. See also: "miditoyz raw   │
│          --debug".                                                           │
│ init     Generate a new music collection from a source directory in          │
│          destination directory without duplicate songs.                      │
│ raw      Dump a MIDI song file in raw text format, optionally with           │
│          hexdump-style output. See also: "miditoyz dump --metadata".         │
│ stream   Stream music from a catalog song list, a midi file, or directory    │
│          full of midi files to a midi device with using bank selection and   │
│          program changes based on voice preferences stored in                │
│          "~/.miditoyz/settings.json" and saved automatically each time you   │
│          stream. Catalog song lists are JSON files with the format:          │
│          [{"title": "Autumn Leaves", "song": "hash.mid"}, ...] and can be    │
│          created from your collections "catalog.json". Bookmark values are   │
│          based on the sequential number of the song in the playlist or       │
│          directory song list starting with 1. We do the right thing if you   │
│          specify a bookmark number that's too big or small or your play      │
│          different music than last time. Your command line options are       │
│          remembered between streaming sessions, so subsequent streamings     │
│          pick up from the last song played.                                  │
│ voices   Generate a list of voices for each track in a midi song file.       │
╰──────────────────────────────────────────────────────────────────────────────╯


$ miditoyz catalog --help
                                                                                
 Usage: miditoyz catalog [OPTIONS] CATALOG_FILE                                 
                                                                                
 Memorize a new catalog file for future streaming.                              
                                                                                
╭─ Arguments ──────────────────────────────────────────────────────────────────╮
│ *    catalog_file      TEXT  Catalog file from your miditoyz song            │
│                              collection.                                     │
│                              [default: None]                                 │
│                              [required]                                      │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────╮
│ --help          Show this message and exit.                                  │
╰──────────────────────────────────────────────────────────────────────────────╯


$ miditoyz devices --help
                                                                                
 Usage: miditoyz devices [OPTIONS]                                              
                                                                                
 List available midi devices.                                                   
                                                                                
╭─ Options ────────────────────────────────────────────────────────────────────╮
│ --help          Show this message and exit.                                  │
╰──────────────────────────────────────────────────────────────────────────────╯


$ miditoyz dump --help
                                                                                
 Usage: miditoyz dump [OPTIONS] SONG                                            
                                                                                
 Dump a MIDI song file in raw text format. See also: "miditoyz raw --debug".    
                                                                                
╭─ Arguments ──────────────────────────────────────────────────────────────────╮
│ *    song      TEXT  The path to the MIDI song file to be analyzed.          │
│                      [default: None]                                         │
│                      [required]                                              │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────╮
│ --metadata    --no-metadata      Show only metadata. [default: no-metadata]  │
│ --help                           Show this message and exit.                 │
╰──────────────────────────────────────────────────────────────────────────────╯


$ miditoyz init --help
                                                                                
 Usage: miditoyz init [OPTIONS] SOURCE_DIRECTORY DESTINATION_DIRECTORY          
                                                                                
 Generate a new music collection from a source directory in destination         
 directory without duplicate songs.                                             
                                                                                
╭─ Arguments ──────────────────────────────────────────────────────────────────╮
│ *    source_directory           PATH  Directory full of MIDI songs to clean  │
│                                       up.                                    │
│                                       [default: None]                        │
│                                       [required]                             │
│ *    destination_directory      PATH  Directory for cleaned up MIDI song     │
│                                       collection with duplicates removed and │
│                                       catalog generated.                     │
│                                       [default: None]                        │
│                                       [required]                             │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────╮
│ --help          Show this message and exit.                                  │
╰──────────────────────────────────────────────────────────────────────────────╯


$ miditoyz raw --help
                                                                                
 Usage: miditoyz raw [OPTIONS] MIDI_FILE                                        
                                                                                
 Dump a MIDI song file in raw text format, optionally with hexdump-style        
 output. See also: "miditoyz dump --metadata".                                  
                                                                                
╭─ Arguments ──────────────────────────────────────────────────────────────────╮
│ *    midi_file      TEXT  MIDI file to dump in raw format. [default: None]   │
│                           [required]                                         │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────╮
│ --debug    --no-debug      Enable debug mode. [default: no-debug]            │
│ --help                     Show this message and exit.                       │
╰──────────────────────────────────────────────────────────────────────────────╯


$ miditoyz stream --help
                                                                                
 Usage: miditoyz stream [OPTIONS]                                               
                                                                                
 Stream music from a catalog song list, a midi file, or directory full of midi  
 files to a midi device with using bank selection and program changes based on  
 voice preferences stored in "~/.miditoyz/settings.json" and saved              
 automatically each time you stream. Catalog song lists are JSON files with the 
 format: [{"title": "Autumn Leaves", "song": "hash.mid"}, ...] and can be       
 created from your collections "catalog.json". Bookmark values are based on the 
 sequential number of the song in the playlist or directory song list starting  
 with 1. We do the right thing if you specify a bookmark number that's too big  
 or small or your play different music than last time. Your command line        
 options are remembered between streaming sessions, so subsequent streamings    
 pick up from the last song played.                                             
                                                                                
╭─ Options ────────────────────────────────────────────────────────────────────╮
│ --music           TEXT     MIDI song file, directory full of music, or       │
│                            catalog list to stream. A catalog list is a JSON  │
│                            file containing list of song titles and "hashes"  │
│                            with the format: [{"title": "Autumn Leaves",      │
│                            "song": "hash.mid"}, ...].                        │
│                            [default: /tmp/ronnell.json]                      │
│ --bookmark        INTEGER  Bookmark for last song played assuming you don't  │
│                            pick different music.                             │
│                            [default: 28]                                     │
│ --device          TEXT     MIDI device to stream to (e.g. "Clavinova Port 1" │
│                            for USB, "Network Clavinova for WIFI, etc.))      │
│                            [default: Clavinova Port 1]                       │
│ --help                     Show this message and exit.                       │
╰──────────────────────────────────────────────────────────────────────────────╯


$ miditoyz voices --help
                                                                                
 Usage: miditoyz voices [OPTIONS] MIDI_FILE                                     
                                                                                
 Generate a list of voices for each track in a midi song file.                  
                                                                                
╭─ Arguments ──────────────────────────────────────────────────────────────────╮
│ *    midi_file      TEXT  MIDI file for voice list [default: None]           │
│                           [required]                                         │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────╮
│ --voices                   TEXT  Official Yamaha Clavinova "datalist" of     │
│                                  voices. Check vendor documentation for      │
│                                  other device voicing.                       │
│                                  [default:                                   │
│                                  /Users/dirkleas/.miditoyz/datalist.pickle]  │
│ --detail    --no-detail          Include voice MSB, LSB, PC voice values for │
│                                  searching datalist csv or pdf for voice     │
│                                  names.                                      │
│                                  [default: no-detail]                        │
│ --help                           Show this message and exit.                 │
╰──────────────────────────────────────────────────────────────────────────────╯

```
