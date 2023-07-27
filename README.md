# miditoyz

command line (cli) hacks (h4x) for your midi song collection, initially focusing on the [Yamaha Clavinova CVP-809GP](https://usa.yamaha.com/products/musical_instruments/pianos/clavinova/cvp-809gp/index.html)

why? are you sitting on a collection of a bunch of folders full of midi song files you've purchases, scavenged, or inherited? here are some tools to wrangle and enjoy them. great collections are free of duplicate copies of songs stashed in multiple places with different file names -- this project can help with that. big collections need to be cataloged and easily searched with simple ways to create song playlists which reference, but don't make more copies of your songs -- again, this project has your back!

[miditoyz](miditoyz) is a single utility with useful sub-commands, the first on `init` is for migrating your songs into a **new, cleaned up, duplicate-free, cataloged music collection** -- your original collection is still there untouched of course. once that's finished with the conversion of your catalog (plan for at least 3 minutes per 1000 songs), you can play or **"stream" songs from your computer to your piano with your preferred instrument voicing** via usb, MIDI DIN, or wifi via playlists. songs outside your collections can still be played by pointing to a folder full of songs, or an individual song. you can finally **auto-play a bunch of songs one after another hands free**!!! say goodbye to digging for a song from your piano's touch screen, pressing play, and "Next"/cueing one more ... rinse and repeat manually!!!

you can also poke round and see what midi devices you have access to, check out the voicing on your songs, even peek inside and see what's going on.

to understand what's available, you can use the built-in help by entering `miditoyz --help` to see a list of available commands, or enter `miditoyz <COMMAND> --help` as follows (e.g. replace `<COMMAND>` with one of the commands such as `devices`, omitting the operating system prompt "$"). "--install-completion" and "--show-completion" are advanced options for nerdz, you can ignore them. here are a couple of `--help` examples, but you can see all commands [here](help.md).

*most common commands:*
1. `miditoyz init` - create a new, cleaned-up version of your song collection without the duplicate, renamed versions of songs sprinkled across several directories and create a catalog of your new, epic song collection. the catalog incudes helpful details like the song title, where it came from in your original song collection, and all the "metadata" inside the song midi files (e.g. everything but the performance details like notes played, pedals pressed, etc.)
1. `miditoyz devices` - display a list of currently available midi devices to be used by other tools to allow you to connect to your clavinova
1. `miditoyz stream` - stream a song list from your song catalog, a directory full of music/midi song files or a single midi song to your midi device (e.g. yamaha cvp clavinova, etc) using your voice personal preferences (see **notes** below for more voice preferences) from your song collection. for your convenience, it'll remember where it left off when you stream a setlist or ask it to play a folder full of songs

*research/technical commands:*
1. `miditoyz voices` - display a list of the tracks and voices for a specified song from your song collection
1. `miditoyz dump` - display the specified midi song file in readable plain text from your song collection. midi files are binary files that aren't readable by humans. 
1. `miditoyz raw` - display the specified midi song file in nerdier plain text from your song collection. hexdump-style details can optionally be displayed too

remember, help is always available by adding the `--help` option (i.e. `miditoyz --help`, `miditoyz voices --help`, etc.). the current help generated from all commands is available online [here](help.md)

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
    python -c "import os, pathlib, shutil; x = f'{pathlib.Path.home()}/.miditoyz'; os.mkdir(x); shutil.copyfile('settings.json', f'{x}/settings.json'); shutil.copyfile('datalist.pickle', f'{x}/datalist.pickle')"
    ```
1. install required python packages:
    ```
    pip install -r requirements.txt
    ```
1. generate a new collection from your existing song collection that removes duplicates and broken songs along with a song catalog. depending on the size of your song catalog, this might take a while. it might be worth copying a subset of your collection to a temporary directory and playing around with that first before tackling your entire monster collection. on my 2021 fancy apple macbook pro this takes about 3 minutes per 1000 songs -- your mileage may vary ... dramatically ;-). just follow the help instructions and appropriate examples for mac, linux, or windows:
    ```
    miditoyz init --help

    miditoyz init ~/music/collection ~/music/collection.new          # mac or linux
    miditoyz init c:\music\collection c:\music\collection.new        # windows
    ```

## roadmap

1. research `fcntl` not available on windows
1. installation tool to automate **installation/setup** section, housekeeping, [automated] testing, continued care-and-feeding, etc.
1. consider python "complier" (i.e. [PyInstaller](https://pyinstaller.org/en/stable/), [cx_Freeze](https://cx-freeze.readthedocs.io/en/stable/), [Nuitka](https://nuitka.net), etc.)
1. add ability to specify voicing preferences based for genres/styles, individual songs, sequencer specific settings, track title heuristics, etc.
1. add unique song-level metadata (e.g. genre/style, performer, songwriter, lyrics, applicable arranger style lists, custom tags, etc.), partially available from catalog `miditoyz dump` data
1. command line, os-native, or web-based gui front end for tools to complement
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
