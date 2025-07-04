
# miditoyz
here's a full list of all the `miditoyz` command help generated by 
calling `miditoyz --help` and `miditoyz <command> --help` for each 
command:

```
$ miditoyz --help
                                                                                                    
 Usage: miditoyz [OPTIONS] COMMAND [ARGS]...                                                        
                                                                                                    
╭─ Options ────────────────────────────────────────────────────────────────────────────────────────╮
│ --install-completion          Install completion for the current shell.                          │
│ --show-completion             Show completion for the current shell, to copy it or customize the │
│                               installation.                                                      │
│ --help                        Show this message and exit.                                        │
╰──────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ───────────────────────────────────────────────────────────────────────────────────────╮
│ init        Generate a new music collection from a source directory into a destination directory │
│             removing duplicates songs. Duplicates include same song in multiple directory paths, │
│             renamed versions of the same song, etc. that have identical song content "inside"    │
│             the song MIDI file.                                                                  │
│ merge       Merge source JSON catalog into destination JSON catalog, overwriting destination     │
│             catalog songs with source catalog songs if there are any duplicates -- this is only  │
│             merging JSON files, not the catalog database or user metadata.                       │
│ devices     List currently connected midi output devices attached via USB, WIFI, or Bluetooth.   │
│ stream      Stream music from a catalog song list, a midi file, or directory full of midi files  │
│             to a midi device with using bank selection and program changes based on voice        │
│             preferences stored in your home directory on Windows as ".miditoyz\settings.json" or │
│             ".miditoyz/settings.json" on MacOS/Linux. Your last song played and saved            │
│             automatically each time you stream.                                                  │
│ voices      Generate a list of voices for each track in a midi song file.                        │
│ dump        Dump a MIDI song file in raw text format. See also: "miditoyz raw --debug".          │
│ raw         Dump a MIDI song file in alternative raw text format with optionally with            │
│             hexdump-style debug output. See also: "miditoyz dump --metadata".                    │
│ summarize   Summarize MIDI song metadata and voices (e.g. convenience command which runs both    │
│             dump with metadata and voices commands).                                             │
│ verify      Verify MIDI song file can be processed with mido package or that a JSON or CSV file  │
│             is the correct format.                                                               │
│ catalog     Change to a new catalog file for streaming.                                          │
│ voicing     Change to a new instrument name for voicing streams.                                 │
│ info        Show current miditoyz settings, including user metadata tags and genres.             │
│ query       Query a song list from your catalog for streaming or managing user metadata with     │
│             several options to choose from depending on whether you prefer a simple or advanced  │
│             capabilities. Once you see the desired song list, you can save it to a .csv file     │
│             with the --save option.                                                              │
│ metadata    Add user metadata to music to supplement the optional MIDI event metadata embedded   │
│             in your song files. User metadata is stored in your catalog database and is added to │
│             your music by using the query command to identify the specific songs you want to     │
│             specify metadata for. You can also use the --backup and --restore if you wish to     │
│             re-initialize your music collection and restore your metadata later.                 │
│ fields      Show the field names and types from your catalog database tables that you can use    │
│             for advanced queries.                                                                │
│ panic       Send MIDI panic to turn off any hung notes.                                          │
│ db          Analyze music catalog database with duckdb (enter ".quit" to exit when finished).    │
╰──────────────────────────────────────────────────────────────────────────────────────────────────╯


$ miditoyz init --help
                                                                                                    
 Usage: miditoyz init [OPTIONS] SOURCE_DIRECTORY DESTINATION_DIRECTORY                              
                                                                                                    
 Generate a new music collection from a source directory into a destination directory removing      
 duplicates songs. Duplicates include same song in multiple directory paths, renamed versions of    
 the same song, etc. that have identical song content "inside" the song MIDI file.                  
                                                                                                    
╭─ Arguments ──────────────────────────────────────────────────────────────────────────────────────╮
│ *    source_directory           PATH  Directory full of MIDI songs to clean up. [default: None]  │
│                                       [required]                                                 │
│ *    destination_directory      PATH  Directory for cleaned up MIDI song collection with         │
│                                       duplicates removed and catalog generated.                  │
│                                       [default: None]                                            │
│                                       [required]                                                 │
╰──────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────────────────────────╮
│ --voices        TEXT  Official Yamaha Clavinova "datalist" of voices. Check vendor documentation │
│                       for other device voicing.                                                  │
│                       [default: /Users/dirkleas/h4x/miditoyz/datalist.pickle]                    │
│ --help                Show this message and exit.                                                │
╰──────────────────────────────────────────────────────────────────────────────────────────────────╯


$ miditoyz merge --help
                                                                                                    
 Usage: miditoyz merge [OPTIONS] SOURCE DESTINATION                                                 
                                                                                                    
 Merge source JSON catalog into destination JSON catalog, overwriting destination catalog songs     
 with source catalog songs if there are any duplicates -- this is only merging JSON files, not the  
 catalog database or user metadata.                                                                 
                                                                                                    
╭─ Arguments ──────────────────────────────────────────────────────────────────────────────────────╮
│ *    source           TEXT  Source catalog to merge into destination catalog. [default: None]    │
│                             [required]                                                           │
│ *    destination      TEXT  Destination catalog to merge source catalog into, overriding         │
│                             duplicates with source songs.                                        │
│                             [default: None]                                                      │
│                             [required]                                                           │
╰──────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────────────────────────╮
│ --backup    --no-backup      Create destination catalog backup .zip archive before merging.      │
│                              [default: backup]                                                   │
│ --help                       Show this message and exit.                                         │
╰──────────────────────────────────────────────────────────────────────────────────────────────────╯


$ miditoyz devices --help
                                                                                                    
 Usage: miditoyz devices [OPTIONS]                                                                  
                                                                                                    
 List currently connected midi output devices attached via USB, WIFI, or Bluetooth.                 
                                                                                                    
╭─ Options ────────────────────────────────────────────────────────────────────────────────────────╮
│ --json    --no-json      Convert devices to JSON. [default: no-json]                             │
│ --help                   Show this message and exit.                                             │
╰──────────────────────────────────────────────────────────────────────────────────────────────────╯


$ miditoyz stream --help
                                                                                                    
 Usage: miditoyz stream [OPTIONS]                                                                   
                                                                                                    
 Stream music from a catalog song list, a midi file, or directory full of midi files to a midi      
 device with using bank selection and program changes based on voice preferences stored in your     
 home directory on Windows as ".miditoyz\settings.json" or ".miditoyz/settings.json" on             
 MacOS/Linux. Your last song played and saved automatically each time you stream.                   
 Catalog song lists are CSV files with a mandatory header of "title,id" -- don't forget to use      
 comma to separate for CSV fields, and double-quote fields with commas in them. Create song lists   
 using the "query" command.                                                                         
 Bookmark values are based on the sequential number of the song in the playlist or directory song   
 list starting with 1. We do the right thing if you specify a bookmark number that's too big or     
 small or your play different music than last time. Don't want to play your songs in order? Try the 
 "shuffle" option. Your most important command line options are remembered between streaming        
 sessions, so subsequent streamings pick up from the last song played if you don't include them     
 (streaming exceptions: shuffle, intermission, and debug).                                          
                                                                                                    
╭─ Options ────────────────────────────────────────────────────────────────────────────────────────╮
│ --music                           TEXT     MIDI song file, directory full of music, or song list │
│                                            to stream. A song list is a CSV file with a mandatory │
│                                            header "title,id". You can specify "LAST" for last    │
│                                            song streamed.                                        │
│                                            [default: /Users/dirkleas/Desktop/pianobar.csv]       │
│ --bookmark                        INTEGER  Bookmark for last song played assuming you don't pick │
│                                            different music.                                      │
│                                            [default: 1]                                          │
│ --skip            --no-skip                Skip to next song in music list if not shuffling      │
│                                            instead of replaying bookmarked song.                 │
│                                            [default: no-skip]                                    │
│ --device                          TEXT     MIDI device to stream to (e.g. "Clavinova Port 1" for │
│                                            USB, "Network Clavinova for WIFI, etc.))              │
│                                            [default: cowchip Port 1]                             │
│ --voicing                         TEXT     Voicing to use for voice preferences.                 │
│ --shuffle         --no-shuffle             Shuffle song order. [default: no-shuffle]             │
│ --repeat          --no-repeat              Repeat your music forever. [default: no-repeat]       │
│ --intermission                    INTEGER  Add specified number of seconds intermission between  │
│                                            songs.                                                │
│                                            [default: 0]                                          │
│ --debug           --no-debug               Debug output.)) [default: no-debug]                   │
│ --help                                     Show this message and exit.                           │
╰──────────────────────────────────────────────────────────────────────────────────────────────────╯


$ miditoyz voices --help
                                                                                                    
 Usage: miditoyz voices [OPTIONS] MUSIC                                                             
                                                                                                    
 Generate a list of voices for each track in a midi song file.                                      
                                                                                                    
╭─ Arguments ──────────────────────────────────────────────────────────────────────────────────────╮
│ *    music      TEXT  MIDI song file, directory full of music, or song list to stream. A song    │
│                       list is a CSV file with a mandatory header "title,id" to generate voice    │
│                       list(s) for. You can specify "LAST" for last song streamed.                │
│                       [default: None]                                                            │
│                       [required]                                                                 │
╰──────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────────────────────────╮
│ --voices                 TEXT  Official Yamaha Clavinova "datalist" of voices. Check vendor      │
│                                documentation for other device voicing.                           │
│                                [default: /Users/dirkleas/h4x/miditoyz/datalist.pickle]           │
│ --json      --no-json          Convert MIDI song to raw JSON. [default: no-json]                 │
│ --help                         Show this message and exit.                                       │
╰──────────────────────────────────────────────────────────────────────────────────────────────────╯


$ miditoyz dump --help
                                                                                                    
 Usage: miditoyz dump [OPTIONS] MUSIC                                                               
                                                                                                    
 Dump a MIDI song file in raw text format. See also: "miditoyz raw --debug".                        
                                                                                                    
╭─ Arguments ──────────────────────────────────────────────────────────────────────────────────────╮
│ *    music      TEXT  MIDI song file, directory full of music, or song list to stream. A song    │
│                       list is a CSV file with a mandatory header "title,id" to be analyzed. You  │
│                       can specify "LAST" for last song streamed.                                 │
│                       [default: None]                                                            │
│                       [required]                                                                 │
╰──────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────────────────────────╮
│ --metadata    --no-metadata      Show only metadata. [default: no-metadata]                      │
│ --json        --no-json          Convert MIDI song to raw JSON. [default: no-json]               │
│ --help                           Show this message and exit.                                     │
╰──────────────────────────────────────────────────────────────────────────────────────────────────╯


$ miditoyz raw --help
                                                                                                    
 Usage: miditoyz raw [OPTIONS] MUSIC                                                                
                                                                                                    
 Dump a MIDI song file in alternative raw text format with optionally with hexdump-style debug      
 output. See also: "miditoyz dump --metadata".                                                      
                                                                                                    
╭─ Arguments ──────────────────────────────────────────────────────────────────────────────────────╮
│ *    music      TEXT  MIDI song file, directory full of music, or song list to stream. A song    │
│                       list is a CSV file with a mandatory header "title,id" to be analyzed. You  │
│                       can specify "LAST" for last song streamed.                                 │
│                       [default: None]                                                            │
│                       [required]                                                                 │
╰──────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────────────────────────╮
│ --debug    --no-debug      Enable extended raw debug mode. [default: no-debug]                   │
│ --help                     Show this message and exit.                                           │
╰──────────────────────────────────────────────────────────────────────────────────────────────────╯


$ miditoyz summarize --help
                                                                                                    
 Usage: miditoyz summarize [OPTIONS] MUSIC                                                          
                                                                                                    
 Summarize MIDI song metadata and voices (e.g. convenience command which runs both dump with        
 metadata and voices commands).                                                                     
                                                                                                    
╭─ Arguments ──────────────────────────────────────────────────────────────────────────────────────╮
│ *    music      TEXT  MIDI song file, directory full of music, or song list to stream. A song    │
│                       list is a CSV file with a mandatory header "title,id" to be summarized.    │
│                       You can specify "LAST" for last song streamed.                             │
│                       [default: None]                                                            │
│                       [required]                                                                 │
╰──────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────────────────────────╮
│ --help          Show this message and exit.                                                      │
╰──────────────────────────────────────────────────────────────────────────────────────────────────╯


$ miditoyz verify --help
                                                                                                    
 Usage: miditoyz verify [OPTIONS] FILE_NAME                                                         
                                                                                                    
 Verify MIDI song file can be processed with mido package or that a JSON or CSV file is the correct 
 format.                                                                                            
                                                                                                    
╭─ Arguments ──────────────────────────────────────────────────────────────────────────────────────╮
│ *    file_name      TEXT  MIDI song, JSON, or CSV file to verify for correct format.             │
│                           [default: None]                                                        │
│                           [required]                                                             │
╰──────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────────────────────────╮
│ --help          Show this message and exit.                                                      │
╰──────────────────────────────────────────────────────────────────────────────────────────────────╯


$ miditoyz catalog --help
                                                                                                    
 Usage: miditoyz catalog [OPTIONS] CATALOG_DIRECTORY                                                
                                                                                                    
 Change to a new catalog file for streaming.                                                        
                                                                                                    
╭─ Arguments ──────────────────────────────────────────────────────────────────────────────────────╮
│ *    catalog_directory      TEXT  Alternative catalog directory from one of your miditoyz song   │
│                                   collections.                                                   │
│                                   [default: None]                                                │
│                                   [required]                                                     │
╰──────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────────────────────────╮
│ --help          Show this message and exit.                                                      │
╰──────────────────────────────────────────────────────────────────────────────────────────────────╯


$ miditoyz voicing --help
                                                                                                    
 Usage: miditoyz voicing [OPTIONS] INSTRUMENT_NAME                                                  
                                                                                                    
 Change to a new instrument name for voicing streams.                                               
                                                                                                    
╭─ Arguments ──────────────────────────────────────────────────────────────────────────────────────╮
│ *    instrument_name      TEXT  Instrument name from voices. [default: None] [required]          │
╰──────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────────────────────────╮
│ --help          Show this message and exit.                                                      │
╰──────────────────────────────────────────────────────────────────────────────────────────────────╯


$ miditoyz info --help
                                                                                                    
 Usage: miditoyz info [OPTIONS]                                                                     
                                                                                                    
 Show current miditoyz settings, including user metadata tags and genres.                           
                                                                                                    
╭─ Options ────────────────────────────────────────────────────────────────────────────────────────╮
│ --json    --no-json      Convert info to JSON. [default: no-json]                                │
│ --help                   Show this message and exit.                                             │
╰──────────────────────────────────────────────────────────────────────────────────────────────────╯


$ miditoyz query --help
                                                                                                    
 Usage: miditoyz query [OPTIONS]                                                                    
                                                                                                    
 Query a song list from your catalog for streaming or managing user metadata with several options   
 to choose from depending on whether you prefer a simple or advanced capabilities. Once you see the 
 desired song list, you can save it to a .csv file with the --save option.                          
 The --connective option allows you to specify how multiple options are evaluated (e.g. OR means at 
 least one of the options match, and AND means they all must match).                                
 Options can be mixed and matched except for --sql.                                                 
                                                                                                    
╭─ Options ────────────────────────────────────────────────────────────────────────────────────────╮
│ --title                          TEXT  Query catalog song title. [default: None]                 │
│ --metadata                       TEXT  Query catalog song metadata, excluding user provided      │
│                                        metadata.                                                 │
│                                        [default: None]                                           │
│ --sources                        TEXT  Query catalog song sources. [default: None]               │
│ --voices                         TEXT  Query catalog song voicing. [default: None]               │
│ --favorite      --no-favorite          Query catalog for songs that are marked as favorites.     │
│                                        [default: no-favorite]                                    │
│ --tag                            TEXT  Query catalog with a list of one or more tags (e.g. --tag │
│                                        piano --tag karaoke).                                     │
│ --genre                          TEXT  Query catalog with a list of one or more genres (e.g.     │
│                                        --genre jazz --genre newOrleans).                         │
│ --note                           TEXT  Query catalog song note. [default: None]                  │
│ --sql                            TEXT  Query using raw SQL (experts only!). [default: None]      │
│ --save                           TEXT  Save your song list query result to a .csv file for use   │
│                                        with streaming or adding user metadata.                   │
│                                        [default: None]                                           │
│ --json          --no-json              Convert query result to JSON. [default: no-json]          │
│ --debug         --no-debug             Show SQL generated based on selected query option.        │
│                                        [default: no-debug]                                       │
│ --connective                     TEXT  Use OR or AND logic when using multiple options.          │
│                                        [default: OR]                                             │
│ --help                                 Show this message and exit.                               │
╰──────────────────────────────────────────────────────────────────────────────────────────────────╯


$ miditoyz metadata --help
                                                                                                    
 Usage: miditoyz metadata [OPTIONS] MUSIC                                                           
                                                                                                    
 Add user metadata to music to supplement the optional MIDI event metadata embedded in your song    
 files. User metadata is stored in your catalog database and is added to your music by using the    
 query command to identify the specific songs you want to specify metadata for. You can also use    
 the --backup and --restore if you wish to re-initialize your music collection and restore your     
 metadata later.                                                                                    
                                                                                                    
╭─ Arguments ──────────────────────────────────────────────────────────────────────────────────────╮
│ *    music      TEXT  MIDI song file, directory full of music, or song list to stream. A song    │
│                       list is a CSV file with a mandatory header "title,id". You can specify     │
│                       "LAST" for last song streamed.                                             │
│                       [default: None]                                                            │
│                       [required]                                                                 │
╰──────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────────────────────────╮
│ --delete      --no-delete            Delete specified option values. [default: no-delete]        │
│ --title                        TEXT  Add/update song title. [default: None]                      │
│ --favorite    --no-favorite          Add to favorites. [default: no-favorite]                    │
│ --tag                          TEXT  A list of tags, provided separately.                        │
│ --genre                        TEXT  A list of genres, provided separately.                      │
│ --note                         TEXT  Add short notes via command line or specify a plain text    │
│                                      file to load long form notes.                               │
│                                      [default: None]                                             │
│ --backup      --no-backup            Export metadata to a .csv file if you need to rerun init    │
│                                      and later restore matching metadata.                        │
│                                      [default: no-backup]                                        │
│ --restore     --no-restore           Restore metadata from a .csv file if you need to rerun init │
│                                      and later restore matching metadata.                        │
│                                      [default: no-restore]                                       │
│ --help                               Show this message and exit.                                 │
╰──────────────────────────────────────────────────────────────────────────────────────────────────╯


$ miditoyz fields --help
                                                                                                    
 Usage: miditoyz fields [OPTIONS]                                                                   
                                                                                                    
 Show the field names and types from your catalog database tables that you can use for advanced     
 queries.                                                                                           
                                                                                                    
╭─ Options ────────────────────────────────────────────────────────────────────────────────────────╮
│ --json    --no-json      Convert fields to JSON. [default: no-json]                              │
│ --help                   Show this message and exit.                                             │
╰──────────────────────────────────────────────────────────────────────────────────────────────────╯


$ miditoyz panic --help
                                                                                                    
 Usage: miditoyz panic [OPTIONS]                                                                    
                                                                                                    
 Send MIDI panic to turn off any hung notes.                                                        
                                                                                                    
╭─ Options ────────────────────────────────────────────────────────────────────────────────────────╮
│ --device        TEXT  MIDI device to panic reset (e.g. "Clavinova Port 1" for USB, "Network      │
│                       Clavinova for WIFI, etc.))                                                 │
│                       [default: cowchip Port 1]                                                  │
│ --help                Show this message and exit.                                                │
╰──────────────────────────────────────────────────────────────────────────────────────────────────╯


$ miditoyz db --help
                                                                                                    
 Usage: miditoyz db [OPTIONS]                                                                       
                                                                                                    
 Analyze music catalog database with duckdb (enter ".quit" to exit when finished).                  
                                                                                                    
╭─ Options ────────────────────────────────────────────────────────────────────────────────────────╮
│ --init    --no-init      Initialize just the catalog database, useful if you break things while  │
│                          experimenting.                                                          │
│                          [default: no-init]                                                      │
│ --help                   Show this message and exit.                                             │
╰──────────────────────────────────────────────────────────────────────────────────────────────────╯

```
