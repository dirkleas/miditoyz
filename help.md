
# miditoyz
here's a full list of all the `miditoyz` command help genrated by 
calling `miditoyz --help` and `miditoyz <command> --help` for each 
command:

```
$ miditoyz --help
Usage: miditoyz [OPTIONS] COMMAND [ARGS]...

Options:
  --install-completion [bash|zsh|fish|powershell|pwsh]
                                  Install completion for the specified shell.
  --show-completion [bash|zsh|fish|powershell|pwsh]
                                  Show completion for the specified shell, to
                                  copy it or customize the installation.
  --help                          Show this message and exit.

Commands:
  catalog  Memorize a new catalog file for future streaming.
  devices  List available midi devices.
  dump     Dump a MIDI song file in raw text format.
  init     Generate a new music collection from a source directory in...
  raw      Dump a MIDI song file in raw text format, optionally with...
  stream   Stream music from a catalog song list, a midi file, or...
  voices   Generate a list of voices for each track in a midi song file.

$ miditoyz init --help
Usage: miditoyz init [OPTIONS] SOURCE_DIRECTORY DESTINATION_DIRECTORY

  Generate a new music collection from a source directory in destination
  directory without duplicate songs.

Arguments:
  SOURCE_DIRECTORY       Directory full of MIDI songs to clean up.  [required]
  DESTINATION_DIRECTORY  Directory for cleaned up MIDI song collection with
                         duplicates removed and catalog generated.  [required]

Options:
  --help  Show this message and exit.

$ miditoyz devices --help
Usage: miditoyz devices [OPTIONS]

  List available midi devices.

Options:
  --help  Show this message and exit.

$ miditoyz stream --help
Usage: miditoyz stream [OPTIONS]

  Stream music from a catalog song list, a midi file, or directory full of
  midi files to a midi device with using bank selection and program changes
  based on voice preferences stored in "~/.miditoyz/settings.json" and saved
  automatically each time you stream. Catalog song lists are JSON files with
  the format: [{"title": "Autumn Leaves", "song": "hash.mid"}, ...] and can be
  created from your collections "catalog.json". Bookmark values are based on
  the sequential number of the song in the playlist or directory song list
  starting with 1. We do the right thing if you specify a bookmark number
  that's too big or small or your play different music than last time. Your
  command line options are remembered between streaming sessions, so
  subsequent streamings pick up from the last song played.

Options:
  --music TEXT        MIDI song file, directory full of music, or catalog list
                      to stream. A catalog list is a JSON file containing list
                      of song titles and "hashes" with the format: [{"title":
                      "Autumn Leaves", "song": "hash.mid"}, ...].  [default:
                      /Users/dirkleas/h4x/clav.toys/PIANOFORCE MUSIC
                      FILES/Standards]
  --bookmark INTEGER  Bookmark for last song played assuming you don't pick
                      different music.  [default: 14]
  --device TEXT       MIDI device to stream to (e.g. "Clavinova Port 1" for
                      USB, "Network Clavinova for WIFI, etc.))  [default:
                      Clavinova Port 1]
  --help              Show this message and exit.

$ miditoyz voices --help
Usage: miditoyz voices [OPTIONS] MIDI_FILE

  Generate a list of voices for each track in a midi song file.

Arguments:
  MIDI_FILE  MIDI file for voice list  [required]

Options:
  --voices TEXT           Official Yamaha Clavinova "datalist" of voices.
                          Check vendor documentation for other device voicing.
                          [default: /Users/dirkleas/.miditoyz/datalist.pickle]
  --detail / --no-detail  Include voice MSB, LSB, PC voice values for
                          searching datalist csv or pdf for voice names.
                          [default: no-detail]
  --help                  Show this message and exit.

$ miditoyz dump --help
Usage: miditoyz dump [OPTIONS] SONG

  Dump a MIDI song file in raw text format. See also: "miditoyz raw --debug".

Arguments:
  SONG  The path to the MIDI song file to be analyzed.  [required]

Options:
  --metadata / --no-metadata  Show only metadata.  [default: no-metadata]
  --help                      Show this message and exit.

$ miditoyz raw --help
Usage: miditoyz raw [OPTIONS] MIDI_FILE

  Dump a MIDI song file in raw text format, optionally with hexdump-style
  debug output. See also: "miditoyz dump --metadata".

Arguments:
  MIDI_FILE  MIDI file to dump in extended raw debug format.  [required]

Options:
  --debug / --no-debug  Enable extended raw debug mode.  [default: no-debug]
  --help                Show this message and exit.

$ miditoyz catalog --help
Usage: miditoyz catalog [OPTIONS] CATALOG_FILE

  Memorize a new catalog file for future streaming.

Arguments:
  CATALOG_FILE  Catalog file from your miditoyz song collection.  [required]

Options:
  --help  Show this message and exit.
```

--

This project is licensed under the terms of the MIT license. See LICENSE for details.
