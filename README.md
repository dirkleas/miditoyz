# miditoyz

a collection of command line (cli) hacks (h4x) for your midi song collection, initially focusing the [Yamaha Clavinova CVP-809GP](https://usa.yamaha.com/products/musical_instruments/pianos/clavinova/cvp-809gp/index.html)

why? are you sitting on a collection of a bunch of folders full of midi files purchases, scavanged, or inherited? here are some tools to wrangle and enjoy them

these goodies are located in the `bin` project directory:

1. [midi](bin/midi) - display a list of currently available midi devices to be used by other tools to allow you to connect to your clavinova
1. [midivoices]() - display a list of the tracks and voices for a specified song
1. [midistream](bin/midistream) - stream a directory full of midi music files or a single midi song to your clavinova using your voice preferences (see **notes** below for more voice preferences)
1. [midiraw](bin/midiraw) - display the specified midi song file in plain text. midi files are binary files that aren't readable by humans. `hexdump`-esque details can optionally be displayed too
1. [midisonglists](midisonglists) - generate a `_songlist.txt` in each directory/subdirectory that includes song filenames and song titles. it's common that midi files have meaningless filenames (i.e. `06-01a01.mid` in my collection is the standards song **nikki** burt bacharach). your os-specific file browser can be configured to sort files alphabetically so this file can conveniently appear first. the file begins with the fully-qualified file name and the number of song in the directory

help is available for each of these commands by including the `--help` option (i.e. `midi --help`, `midivoices --help`, etc.)

## installation/setup

this project uses the popular, free scripting language [python](https://www.python.org). addition bits are required for handling midi files, working with your computer, and so forth. the tools have been successfully tested to work on windows, macos, and linux assuming reasonably current versions. steps 3. and beyond via your os command prompt/terminal shell:

1. install latest version of [python](https://www.python.org/downloads/) for your operating system (os) and add it to your path
1. install latest version of [git](https://git-scm.com) for your os and add it to your path
1. clone this project on your computer via a terminal shell or command prompt in the directory of your choice. cloning the project will create a new folder named `miditoyz` -- change directory into that folder and you'll see a `bin` folder containing the scripts. add this folder to your os path or create aliases for them (i.e. windows `set midistream "python c:\clav\bin\midistream`, etc.):
    ```
    git clone https://github.com/dirkleas/clav
    ```
1. create default project configuration in your home directory, altering voice preferences if you wish:
    ```
    python -c "import os, pathlib, shutil; x = f'{pathlib.Path.home()}/.miditoyz'; os.mkdir(x); shutil.copyfile('settings.json', f'{x}/settingsjson'); shutil.copyfile('datalist.pickle', f'{x}/datalist.pickle')"
    ```
1. install required python packages:
    ```
    pip install -r requirements.txt
    ```
1. generate the song lists for your collection assuming the entire collection lives in a single directory with lots of other nested directories inside it by specifying your top-level/root directory as described in the help -- be patient, this can take a while depending on the size of your collection:
    ```
    midisonglists --help
    ```

## roadmap

1. add ability to specify voicing preferences based for genres/styles, individual songs, sequencer specific settings, track title heuristics, etc.
1. add housekeeping function to remove song duplicates, whether duplicate song directories, renamed songs, etc.
1. add unique song-level metadata (e.g. genre/style, performer, songwriter, lyrics, applicable arranger style lists, custom tags, etc.)
1. os-native or web-based gui front end for tools (later would require local micro-server)

## notes/other
1. several "datalist" files are included in more computer-friendly formats and are based on the official cvp-800 series [datalist](https://usa.yamaha.com/files/download/other_assets/7/1264707/cvp809_en_dl_c0.pdf) reference document from yamaha. you can alter default voice preferences in `.miditoyz/settings.json` in the `voices` section where entries map song voices to preferred song voices using the **MSB**, **LSB**, **PC** values from `datalist.csv`. defaults voice preferences include mapping standard midi "Grand Piano" to the better sounding "CSP Grand Piano", etc.
1. if your computer includes multiple versions of python, this project uses version 3x or greater. you may need to refer to python as `python3` to specifically reference the correct version
1. consider creating/activating a virtual environment for your repo clone using (e.g. `venv`, `pipenv`, `conda`, etc.) and altering the **installation/setup** accordingly
1. consider creating a unified songlist by concatenating all the individual `_songlist.txt` files and stripping out the initial directory/blank line

--

This project is licensed under the terms of the MIT license. See [LICENSE](LICENSE) for details.
