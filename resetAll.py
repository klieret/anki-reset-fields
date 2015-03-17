#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
DESCRIPTION:
Adds a button 'R' to the formatting menu bar of the editor window. Once pressed 
it resets all fields (i.e. sets them to ""). This is useful if you have a lot 
of (automatically filled) fields. The default keystroke is Ctrl+Shift+R but 
this can be changed by editing the source file.

INSTALLATION
Method 1: Simply put the file resetFields.py in the folder Anki/addons.
Method 2: In Anki's main window, select Tools>Browse & Install and insert the 
Code from the Anki's addon page.

ISSUES
Open a ticket at https://bitbucket.org/ch4noyu (prefered method) or send me an 
e-mail (<ch4noyu@yahoo.com>).

SUGGESTIONS 
Send me an e-mail (German/English)! I am not a professional programmer, so 
feedback on how to improve my code is welcome, too.

SOURCE 
Source hostet at https://bitbucket.org/ch4noyu 

COPYRIGHT
Copyright: ch4noyu <ch4noyu@yahoo.com>
Licence: GNU AGPL, version 3 or later
"""

# -----------------------------------------------------------
# Go to the "CUSTOMIZE ME" block to adapt keystrokes etc.
# Changes will only take effect after saving this file and
# restarting anki!
# ----------------------------------------------------------- 

from anki.hooks import addHook     # hooks
from aqt import mw                 # main window

class resetFields(object):
    """ Adds a button that resets all fields in the editor."""
    
    def __init__(self):
        """ Do nothing """
        pass
    
    def setupMenu(self,editor):
        """ Adds the button to the editor menu. """
        self.editor=editor
        # CUSTOMIZE ME
        # ---------------------
        # You can easily change the following parameters:
        #     text: Button text
        #     tip: Toolip
        #     key: Keystroke to activate.
        # the default values are:
        # editor._addButton("reset", self.reset, text="R", tip="Reset all fields (Ctrl+Shift+R)",  key="Ctrl+Shift+R")
        editor._addButton("reset", self.reset, text="R", tip="Reset all fields (Ctrl+Shift+R)",  key="Ctrl+Shift+R")
        # ---------------------
        
    def reset(self):
        """ Resets all fields. """
        # reset all fields
        note=self.editor.note # note that is currently edited
        model=note.model()
        fieldNames=mw.col.models.fieldNames(model)
        for field in fieldNames:
            note[field]=''
        # save:
        note.flush()
        # display:
        self.editor.setNote(note)

# initialize class        
resetFieldsInstance=resetFields()

# All functions that are added to the hook "setupEditorButtons" 
# will be run after anki is finished setting up the formatting 
# editor buttons. 
# See http://ankisrs.net/docs/addons.html#hooks for more information.
addHook("setupEditorButtons",resetFieldsInstance.setupMenu)
