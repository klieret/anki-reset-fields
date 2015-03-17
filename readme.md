# Anki Addon: Reset all Fields
## Description:
Adds a button `R` to the formatting menu bar of the editor window. Once pressed 
it resets all fields (i.e. sets them to `""`). This is useful if you have a lot 
of (automatically filled) fields. The default keystroke is `Ctrl+Shift+R` but 
this can be changed by editing the source file (see below).

![scrot_cut.png](https://bitbucket.org/repo/ryKzjn/images/814931627-scrot_cut.png "Screenshot")

## Installation:
* *Method 1:* Simply put the file resetFields.py in the folder Anki/addons.  
* *Method 2:* In Anki's main window, select `Tools > Browse & Install` and insert the code from the homepage of this addon on https://ankiweb.net/shared/addons/

## Configuration
You can e.g. edit the keystroke by editing the source of this addon.

1. Open the file `resetAll.py` in the Ankis Plugin directory. On Linux this is `~/Anki/addons/`.
2. Go to the `CUSTOMIZE ME` block and do your changes.
3. Save the file.
4. Restart Anki.

## Issues, Suggestions, Feature Requests etc.
Open a ticket at [this addon's gitbucket issue page](https://bitbucket.org/ch4noyu/anki-addon-reset-all-fields/issues) (prefered method, also works without anonymously without login) or send me an [e-mail](mailto:ch4noyu@yahoo.com). German is fine, too. I am not a professional programmer, so feedback on how to improve my code is welcome, too.

## Source
The source is hostet at [this addon's bitbucket page](https://bitbucket.org/ch4noyu/anki-addon-reset-all-fields/).

## Copyright
**Copyright:** *ch4noyu* (<mailto:ch4noyu@yahoo.com>)  
**Licence:** GNU AGPL, version 3 or later

## History

* 17 March 2015: Initial version
