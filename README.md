# miditoyz

a command line (cli) hack (h4x) for your midi song collection, initially focusing on the [Yamaha Clavinova CVP-809GP](https://usa.yamaha.com/products/musical_instruments/pianos/clavinova/cvp-809gp/index.html)

why? are you sitting on a collection of a bunch of folders full of midi song files you've purchases, scavenged, or inherited? here are some tools to wrangle and enjoy them. great collections are free of duplicate copies of songs stashed in multiple places with different file names -- this project can help with that. big collections need to be cataloged and easily searched with simple ways to create song playlists which reference, but don't make more copies of your songs -- again, this project has your back!

[miditoyz](miditoyz) is a single utility with useful sub-commands, the first of which is for converting your songs into a new, cleaned up, and cataloged collection -- your original collection is still there untouched of course. once that's finished with the conversion of your catalog (plan for at least 3 minutes per 1000 songs), you can play or "stream" songs from your computer to your piano via usb, MIDI DIN, or wifi via playlists. songs outside your collections can still be played by pointing to a folder full of songs, or an individual song. you can finally auto-play a bunch of songs one after another. say goodbye to digging for a song from your piano's touch screen, pressing play, and cueing one more, then rinse and repeat manually...

you can also poke round and see what midi devices you have access to, check out the voicing on your songs, even peek inside and see what's going on.

to understand what's available, you can use the built-in help -- simply enter `miditoyz --help` to see a list of all the commands, and then see the details for a particular command by entering `miditoyz stream --help`.
```
(clav) ➜  miditoyz git:(main) miditoyz --help

 Usage: miditoyz [OPTIONS] COMMAND [ARGS]...

╭─ Options ────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --install-completion          Install completion for the current shell.                                              │
│ --show-completion             Show completion for the current shell, to copy it or customize the installation.       │
│ --help                        Show this message and exit.                                                            │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ───────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ devices  list available midi devices                                                                                 │
│ dump     Dump a MIDI file in raw text format. if you need hashdump-esque details, use "midiraw --debug" instead      │
│ init     generate a new music collection from a source directory in destination directory without duplicate songs    │
│ raw      Dump a MIDI file in raw text format, optionally with hexdump output.                                        │
│ stream   Stream music as a catalog song list, a midi file, or directory full of midi files to a midi device with     │
│          using bank selection and program changes based on voice preferences stored in "~/.miditoyz/settings.json"   │
│          and created automatically the first time you stream. Catalog song lists are JSON files with the format:     │
│          [{"title": "Autumn Leaves", "song": "hash.mid"}, ...] created from your collections "catalog.json" list.    │
│          Command line options are remembered between streaming sessions, so subsequent streamings pick up from the   │
│          last song played. Bookmark values are based on line numbers from the directory's "_songlist.txt" file,      │
│          which starts with a title and blank line, so the first song is line 3 (e.g. "--bookmark 3"). Bookmark       │
│          values are reset to 3 if the music is a song rather than a directory, is either too low/high, or if the     │
│          music is different than the last time you streamed.                                                         │
│ voices   Generate a list of voices for each track in a midi file                                                     │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

(clav) ➜  miditoyz git:(main) miditoyz stream --help

 Usage: miditoyz stream [OPTIONS] NAME

 stream playlist, folders, or individual songs to a device

╭─ Arguments ──────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ *    name      TEXT  [default: None] [required]                                                                      │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --help          Show this message and exit.                                                                          │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

(clav) ➜  miditoyz git:(main)
```
here's the currently available commands:

*most common commands:*
1. `miditoys init` - create a new, cleaned-up version of your song collection without the duplicate, renamed versions of songs sprinkled across several directories and create a catalog of your new, epic song collection. the catalog incudes helpful details like the song title, where it came from in your original song collection, and all the "metadata" inside the song midi files (e.g. everything but the performance details like notes played, pedals pressed, etc.)
1. `miditoyz devices` - display a list of currently available midi devices to be used by other tools to allow you to connect to your clavinova
1. `miditoyz stream` - stream a song list from your song catalog, a directory full of music/midi song files or a single midi song to your midi device (e.g. yamaha cvp clavinova, etc) using your voice personal preferences (see **notes** below for more voice preferences) from your song collection. for your convenience, it'll remember where it left off when you stream a setlist or ask it to play a folder full of songs

*research/technical commands:*
1. `miditoyz voices` - display a list of the tracks and voices for a specified song from your song collection
1. `miditoyz mididump` - display the specified midi song file in readable plain text from your song collection. midi files are binary files that aren't readable by humans. 
1. `miditoyz raw` - display the specified midi song file in nerdier plain text from your song collection. `hexdump`-esque details can optionally be displayed too

help is available for each of these commands by including the `--help` option (i.e. `midi --help`, `midivoices --help`, etc.)

## installation/setup

this project uses the popular, free scripting language [python](https://www.python.org). addition bits are required for handling midi files, working with your computer, and so forth. the tools have been successfully tested to work on windows, macos, and linux assuming reasonably current versions. steps 3. and beyond via your os command prompt/terminal shell:

1. install latest version of [python](https://www.python.org/downloads/) for your operating system (os) and add it to your path
1. install latest version of [git](https://git-scm.com) for your os and add it to your path
1. "clone" this project on your computer via a terminal shell or command prompt in the directory of your choice. cloning the project will create a new folder named `miditoyz` -- change directory into that folder and you'll see the `miditoyz` script. add this folder to your os path or create aliases for them (i.e. windows `set miditoyz "python c:\miditoyz\miditoyz`, etc.):
    ```
    git clone https://github.com/dirkleas/miditoyz
    cd miditoyz
    ```
1. create default project configuration in your home directory, altering voice preferences if you wish:
    ```
    python -c "import os, pathlib, shutil; x = f'{pathlib.Path.home()}/.miditoyz'; os.mkdir(x); shutil.copyfile('settings.json', f'{x}/settingsjson'); shutil.copyfile('datalist.pickle', f'{x}/datalist.pickle')"
    ```
1. install required python packages:
    ```
    pip install -r requirements.txt
    ```
1. generate a new collection from your existing song collection that removes duplicates and broken songs along with a song catalog. depending on the size of your song catalog, this might take a while. it might be worth copying a subset of your collection to a temporary directory and playing around with that first before tackling your entire monster collection. on my 2021 fancy apple macbook pro this takes about 3 minutes per 1000 songs -- your mileage may vary ... dramatically ;-). just follow the help instructions and appropriate examples for mac, linux, or windows:
    ```
    miditoyz init --help

    miditoyz ~/music/collection ~/music/collection.new          # mac or linux
    miditoyz c:\music\collection c:\music\collection.new        # windows
    ```

## roadmap

1. installation tool, housekeeping, testing [automation], care-and-feeding, etc.
1. add ability to specify voicing preferences based for genres/styles, individual songs, sequencer specific settings, track title heuristics, etc.
1. add unique song-level metadata (e.g. genre/style, performer, songwriter, lyrics, applicable arranger style lists, custom tags, etc.), partially available from catalog `miditoyz dump` data
1. command line, os-native, or web-based gui front end for tools (later would require local micro-server)
1. implement a number of search and query options for choosing songs from the song catalog. possible considerations:
    * [jq](https://jqlang.github.io/jq/) - query directly or with a wrapper tool, for example query for songs by Ronnell Bright and view numbered songs with the bit of bash magic if on mac/linux/windows10+wsl:
    ```
    jq 'to_entries | map(select(.value.dump != null and (.value.dump[] | contains("Ronnell"))) | {"title": .value.title, "song": ("\(.key).mid")})' /tmp/songs.unique/catalog.json > /tmp/ronnell.json
    grep title /tmp/ronnell.json | cut -d'"' -f4 | nl -n ln
    ```
    * [nocodb](https://nocodb.com) - web-based spreadsheet-style option with expected search and filter options. could be run locally or cloud with a bit of extra tooling to feed `midistream`
    * ai/large language model (llm) interface for natural language search with support for providing song background, recommendations, etc. via text or voice (think "hey siri | alexa | siri, play some jazz standards or movie soundtracks or that song brenda and eddie by billy joel)

## notes/other
1. several "datalist" files are included in more computer-friendly formats and are based on the official cvp-800 series [datalist](https://usa.yamaha.com/files/download/other_assets/7/1264707/cvp809_en_dl_c0.pdf) reference document from yamaha. you can alter default voice preferences in `.miditoyz/settings.json` in the `voices` section where entries map song voices to preferred song voices using the **MSB**, **LSB**, **PC** values from `datalist.csv`. defaults voice preferences include mapping standard midi "Grand Piano" to the better sounding "CSP Grand Piano", etc.
1. if your computer includes multiple versions of python, this project uses version 3x or greater. you may need to refer to python as `python3` to specifically reference the correct version
1. consider creating/activating a virtual environment for your repo clone using (e.g. `venv`, `pipenv`, `conda`, etc.) and altering the **installation/setup** accordingly



questions? suggestions? wanna help? reach out [here](https://github.com/dirkleas/miditoyz/issues) -- it's not just for issues and bugs!

--

This project is licensed under the terms of the MIT license. See [LICENSE](LICENSE) for details.
