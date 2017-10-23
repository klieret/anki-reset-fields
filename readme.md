# Anki Addon: Reset all Fields

**[Overview over my other Anki add-ons](http://www.lieret.net/opensource/#anki)**

## Description

**Note: Meanwhile, there are other add-ons with similar functionality available, e.g. [this one](https://ankiweb.net/shared/info/136533494). Therefore, I am currently not maintaining this project anymore.**

Adds a button ```R``` to the formatting menu bar of the editor window. Once pressed 
it resets all fields (i.e. sets them to ```""```). This is useful if you have a lot 
of (automatically filled) fields. The default keystroke is ```Ctrl+Shift+R``` but 
this can be changed by editing the source file (see below).

![scrot_cut.png](https://raw.githubusercontent.com/klieret/readme-files/master/anki-reset-fields/scrot_cut.png)

## Installation

Simply put the file ```reset_all_fields.py``` and the folder ```reset_all_fields``` in the folder ```Anki/addons```.

## Configuration
You can e.g. edit the keystroke by editing the source of this addon.

1. Open the file ```reset_all_fields/reset_all_fields.py``` in the Ankis Plugin directory. On Linux this is e.. ```~/Documents/Anki/addons/```.
2. Go to the ```CUSTOMIZE ME``` block and do your changes.
3. Save the file.
4. Restart Anki.

## License

The contents of this repository are licensed under the [*AGPL3* license](https://choosealicense.com/licenses/agpl-3.0/) (to be compatible with the license of Anki and its addons as detailed [here](https://ankiweb.net/account/terms)).

## History

* 23 Okt 2017: Moved to github.
* 16 May 2015: Fix: Still works after chaning card models
* 17 March 2015: Initial version
