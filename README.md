# miditoyz

a collection of command line (cli) hacks (h4x) for your midi song collection,
initially focusing the 
[Yamaha Clavinova CVP-809GP](https://usa.yamaha.com/products/musical_instruments/pianos/clavinova/cvp-809gp/index.html)

## miditoolz - command line tools for enjoying your midi song collection

sitting on a collection of a bunch of folders full of midi files purchases,  
scavanged, or inherited? here are some tools to wrangle and enjoy them

here's the current list of midi tools located in the `bin` project directory:

1. [midi](bin/midi) - display a list of currently availble midi devices to be used by other tools
to allow you to connect to your clavinova
1. [midivoices - display a list of the tracks and voices for a specified song
1. [midivoices]() - display a list of the tracks and voices for a specified song
1. [midistream](bin/midistream) - stream a directory full of midi music files or a single midi song to
your clavinova
1. [midiraw](bin/midiraw) - display the specified midi song file in plain text. midi files are usually
binary files that aren't readable by humans. `hexdump`-esque details can optionally be
displayed too
1. [midisonglists](midisonglists) - generate a `_songlist.txt` in each directory/subdirectory that 
includes song filenames and song titles. it's common that midi files have meaningless
files names (e.g. `06-01a01.mid` in my collection is the standards song **Nikki** 
burt bacharach). your os-specific file browser can be configured to sort files 
alphabetically so this file can conveniently appear first. the file begins with the
fully-qualified file name and the number of song in the directory

help is available for each of these commands by including the `--help` option (e.g. 
`midivoices --help`)

## installation/setup

tools and collection analysis tools use the popular, free scripting language. addition
bits are requied for handling midi files, working with your computer, and so forth. the tools
have been successfully tested to work on windows, macos, and linux assuming reasonably current
versions

1. install latest version of [python](https://python.org) for your operating system (os) and add it to your path
1. install latest version of [git](https://git-scm.com) for your os
1. clone this project on your computer via a terminal shell or command prompt in the directory of your choise:
```git clone https://github.com/dirkleas/clav```

    cloning the project will create a new folder named `clav` -- change directory into that folder and you'll see
a `bin` folder -- this is where the scripts are located. add this folder to your os path or create aliases for
them. on mac/linux, adding scripts to your path is sufficent for running them. on windows, you'll probably want
to use aliases to run the scripts. search online for details on creating alias entries (e.g. 
`set midistream "python c:\clav\bin\midistream`, etc.)
1. install required python packages:
```pip install -r requirements.txt```
1. scripts have built-in help for arguments and options that's accessible via the --help option (e.g. 
`midistream --help`)

--

This project is licensed under the terms of the MIT license. See [LICENSE](LICENSE) for details.
