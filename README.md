# miditoyz

This project is a command line (cli) hack for your midi song collection, initially focusing on the [Yamaha Clavinova CVP-809GP](https://usa.yamaha.com/products/musical_instruments/pianos/clavinova/cvp-809gp/index.html). The CLI tool is run from the Windows Command Prompt or the MacOS/Linux terminal/shell.

## Rationale

Are you sitting on a collection of a bunch of folders full of midi song files you've purchases, scavenged, or inherited? Here is a small set of tools to wrangle and enjoy them. Great collections are free of duplicate copies of songs stashed in multiple places with different file names -- this project can help with that. Big collections need to be cataloged and easily searched with simple ways to create song playlists which reference, but don't make more copies of your songs.

[miditoyz](miditoyz) is a single utility with useful sub-commands, the first one, `init`, is for migrating your songs into a **new, cleaned up, duplicate-free, cataloged music collection** -- your original collection is still there untouched of course. Once that's finished with the conversion of your catalog (plan for at least 3 minutes per 1000 songs), you can play or **"stream" songs from your computer to your piano with your preferred instrument voicing** via usb, MIDI DIN, or wifi via playlists. Songs outside your collections can still be played by pointing to a folder full of songs, or an individual song. You can finally **auto-play a bunch of songs one after another hands free**!!! Say goodbye to digging for a song from your piano's touch screen, pressing play, and "Next"/cueing one more ... rinse and repeat manually!!!

You can also poke around and see what midi devices you have access to, check out the voicing on your songs, even peek inside and see what's going on.

To understand what's available, you can use the built-in help by entering `miditoyz --help` to see a list of available commands, or enter `miditoyz <COMMAND> --help` (e.g. replace `<COMMAND>` with one of the commands such as `devices`, omitting the operating system prompt "$"). You can see all commands [here](help.md). The options `--install-completion` and `--show-completion` are advanced features for nerdz, so you can typically ignore them.

*Most Common Commands:*
1. `miditoyz init` - create a new, cleaned-up version of your song collection without the duplicate, renamed versions of songs sprinkled across several directories and create a catalog of your new, epic song collection. The catalog includes helpful details like the song title, where it came from in your original song collection, and all the "metadata" inside the song midi files (e.g. everything but the performance details like notes played, pedals pressed, etc.).
1. `miditoyz devices` - display a list of currently available midi devices to be used by other tools to allow you to connect to your Clavinova.
1. `miditoyz stream` - stream a song list from your song catalog, a directory full of music/midi song files or a single midi song to your midi device (e.g. Yamaha CVP Clavinova, etc) using your voice personal preferences (see **Notes** below for more voice preferences) from your song collection. For your convenience, it'll remember where it left off when you stream a set list or ask it to play a folder full of songs.
1. `miditoyz query` - query your song catalog to create a song list you can use to stream your favorite songs. The query command includes several options allowing simple text search, more searches based on song titles, metadata, or original song sources -- you can even go hard-core with a [SQL "where" clause](https://www.google.com/search?q=sql+where+clause+introduction+tutorial) syntax. Once you've got your song list, you can save it for streaming any time you'd like.

*Research/Technical Commands:*
1. `miditoyz voices` - display a list of the tracks and voices for a specified song from your song collection.
1. `miditoyz dump` - display the specified midi song file in readable plain text from your song collection. Midi files are binary files that aren't readable by humans. 
1. `miditoyz db` - access the embedded SQL song catalog database for hard-core wrangling, research, etc. -- anything goes, nothing hidden here.

> Remember, help is always available by adding the `--help` option to the end of your request (e.g. `miditoyz --help`, `miditoyz stream --help`, etc.). For your convenience, a complete help reference is available online [here](help.md) and includes help for `miditoyz` and all the commands.*

## Installation and Update

This project uses the popular, free scripting language [Python](https://www.python.org). Additional bits are required for handling midi files, working with your computer, and so forth. It's been successfully tested to work on reasonably current versions of Windows, MacOS, and Linux. Complete steps 4. and beyond via your the Windows Command Prompt or the MacOS/Linux terminal/shell by copying and pasting the steps from the grey "code" boxes below. Several steps require you to add things to your operating system (OS) path -- you can wait till the end of the list and add them all at the same time if more convenient.

### Initial Installation

Complete the following once before you can use `miditoyz`:

1. Install latest version of [python](https://www.python.org/downloads/) for your os and add it to your path. *On Windows, you can tick the last option in the installation prompt dialog to have the installer automatically add Python to your path!!!*
1. Install latest version of [git](https://git-scm.com) for your OS and add it to your path.
1. Install latest version of [duckdb](https://duckdb.org) for your OS and add it to your path.
1. `clone` this project on your computer in the directory of your choice which results in a `miditoyz` folder, navigate there, and add it to you path:
    ```
    git clone https://github.com/dirkleas/miditoyz
    cd miditoyz
    ```
1. Create default project configuration in your home directory. You may optionally alter the default voice preferences (see **Notes** section, item #1 below for more details on voice preferences):
    ```
    python -c "import os,pathlib,shutil,json; x=f'{pathlib.Path.home()}{os.sep}.miditoyz'; os.mkdir(x); [shutil.copyfile(f,f'{x}{os.sep}{f}') for f in ['settings.json','datalist.pickle','midi.j2']]; open('miditoyz.bat', 'w').write(f'@echo off{os.linesep}python {os.getcwd()}{os.sep}miditoyz %*{os.linesep}'); s=json.load(open(f'{x}{os.sep}settings.json')); s['root']=os.getcwd(); json.dump(s, open(f'{x}{os.sep}settings.json','w'));"
    ```
1. Install required Python packages:
    ```
    pip install -r requirements.txt
    ```
1. Generate a new collection from your existing song collection that removes duplicates and broken songs along with a song catalog. Depending on the size of your song catalog, this might take a while. You should consider making a backup copy of your original music collection just to be safe. Before tackling your whole collection, you can do a test run using the included "test" music collection included in this project. On my 2021 full spec Apple Macbook Pro this takes about 3 minutes per 1000 songs -- your mileage may vary ... dramatically ;-). Just follow the help instructions and appropriate examples for MacOS, Linux, or Windows:
    ```
    miditoyz init --help

    miditoyz init test/music ~/music/collection.test                 # test music MacOS or Linux
    miditoyz init test/music c:\music\collection.test                # test Windows

    miditoyz init ~/music/collection ~/music/collection.new          # MacOS or Linux
    miditoyz init c:\music\collection c:\music\collection.new        # Windows
    ```

### Update to Latest Release

1. The project is under continuous development, so to keep up to date, complete the following from wherever you initially installed the project -- don't forget to update the example collection path with your actual path name:
    ```
    cd ~/music/collection.test                                       # MacOS or Linux
    cd c:\music\collection.test                                      # Windows
    
    git pull
    pip install -r requirements.txt
    ```

## Roadmap

1. Installation tool to automate **installation/setup** section, housekeeping, [automated] testing, continued care-and-feeding, etc.
1. Add ability to specify voicing preferences based for genres/styles, individual songs, sequencer specific settings, track title heuristics, etc.
1. Add support for multiple instruments played concurrently (e.g. support independent instrument settings for settings like bookmark, device, and music) allowing multiple concurrent instances of `miditoyz`.
1. Add unique song-level metadata (e.g. genre/style, performer, songwriter, lyrics, applicable arranger style lists, custom tags, etc.), partially available from catalog `miditoyz dump` data.
1. Command line, OS-native, or web-based gui front end for tools to complement.
1. Implement a number of search and query options for choosing songs from the song catalog. Possible considerations:
    * [jq](https://jqlang.github.io/jq/) - query directly or with a wrapper tool, for example query for songs by Ronnell Bright and view numbered songs with the bit of bash/shell scripting magic if on MacOS/Linux/Windows + WSL:
    ```
    jq 'to_entries | map(select(.value.dump != null and (.value.dump[] | contains("Ronnell"))) | {"title": .value.title, "song": ("\(.key).mid")})' /tmp/songs.unique/catalog.json > /tmp/ronnell.json
    grep title /tmp/ronnell.json | cut -d'"' -f4 | nl -n ln
    ```
    * [nocodb](https://nocodb.com) - web-based spreadsheet-style option with expected search and filter options. This could be run locally or cloud with a bit of extra tooling to feed `midistream`.
    * AI/large language model (llm) interface for natural language search with support for providing song background, recommendations, etc. via text or voice (think "hey siri | alexa | siri, play some jazz standards or movie soundtracks or that song Brenda and Eddie by Billy Joel).

## Notes/Other
1. Several "datalist" files are included in more computer-friendly formats and are based on the official CVP-800 series [datalist](https://usa.yamaha.com/files/download/other_assets/7/1264707/cvp809_en_dl_c0.pdf) reference document from yamaha. You can alter/add to the default voice preferences in your home directory (i.e. `c:\users\YOUR_USERNAME` for Windows, `/Users/YOUR_USERNAME` for MacOS, and `/home/YOUR_USERNAME` for Linux) in the hidden directory `.miditoyz` in the [JSON](https://www.json.org/json-en.html)-format file `settings.json`. Inside you'll find a `voices` section where entries map song midi song voices to preferred song voices using the **MSB**, **LSB**, **PC** values from `datalist.csv`. Defaults voice preferences include mapping standard midi "Grand Piano" to the better sounding "CFX Concert Grand", "Bosendorfer Grand", etc.. You can even map voices that aren't listed in `datalist.csv` to your preferred voices. This preference mapping strategy also works for midi song files that were produced using various DAWs, other music hardware, and music composition/notation software as long as voicing is manage via standard midi control change/program change events **MSB**, **LSB**, **PC**. You'll also find other interesting settings there, including the location of your collection catalog, last music streamed, and a bookmark for the last song number. An excellent free editor for JSON files is [Visual Studio Code](https://code.visualstudio.com) -- it makes it easy by color-coding the file contents and provides hints and reminders to help you maintain the correct JSON syntax/format. Notice that voices are by default associated with the default instrument "Clavinova CVP 809". Additional instruments and associated voices can be added if you want to play multiple instruments, one at a time.
1. If your computer includes multiple versions of Python, this project uses version 3x or greater. You may need to specifically refer to Python as `python3` to reference the correct version.
1. Consider creating/activating a virtual environment for your repo clone using (e.g. `venv`, `pipenv`, `conda`, etc.) and adjusting the **Installation/Setup** per your own system administration preferences.


questions? suggestions? wanna help? reach out [here](https://github.com/dirkleas/miditoyz/issues) -- it's not just for issues and bugs!

--

This project is licensed under the terms of the MIT license. See [LICENSE](LICENSE) for details.
