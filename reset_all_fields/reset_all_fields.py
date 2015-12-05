#!/usr/bin/env python
# -*- coding: utf-8 -*-

from aqt import mw, dialogs      # main window

class ResetFields(object):
    """ Adds a button that resets all fields in the editor."""

    def __init__(self):
        """ Do nothing """
        self.editor = None

    def setup_menu(self,editor):
        """ Adds the button to the editor menu. """
        self.editor = editor
        # CUSTOMIZE ME
        # ---------------------
        # You can easily change the following parameters:
        #   text: Button text
        #   tip: Toolip
        #   key: Keystroke to activate.
        # the default values are:
        # editor._addButton("reset", self.reset, text="R", tip="Reset all fields (Ctrl+Shift+R)", key="Ctrl+Shift+R")
        editor._addButton("reset", self.reset, text="R", tip="Reset all fields (Ctrl+Shift+R)", key="Ctrl+Shift+R")
        # ---------------------

    def reset(self):
        """ Resets all fields. """
        # reset all fields
        note = self.editor.note # note that is currently edited
        if not note:
            # this shouldn't happen
            return
        model = note.model()
        field_names = mw.col.models.fieldNames(model)
        for field in field_names:
            note[field] = ''
        # save:
        note.flush()
        # display:
        self.editor.setNote(note)

    def model_changed(self):
        """ Gets called if model changed. """
        # this is needed for some reason, else editor.note
        # is None for some reason and the above won't work.
        addCardsDialog = dialogs._dialogs["AddCards"][1]
        if addCardsDialog:
            self.editor = addCardsDialog.editor