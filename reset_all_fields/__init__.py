#!/usr/bin/env python
# -*- coding: utf-8 -*-

from anki.hooks import addHook   # hooks
from reset_all_fields import ResetFields

# initialize class      
resetFieldsInstance = ResetFields()

# All functions that are added to the hook "setupEditorButtons" 
# will be run after anki is finished setting up the formatting 
# editor buttons. 
# See http://ankisrs.net/docs/addons.html#hooks for more information.
addHook("setupEditorButtons", resetFieldsInstance.setup_menu)

# similar thing: model_changed gets called if the current model changes.
addHook("currentModelChanged", resetFieldsInstance.model_changed)