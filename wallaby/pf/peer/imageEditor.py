# Copyright (c) by it's authors. 
# Some rights reserved. See LICENSE, AUTHORS.

from editor import Editor

class ImageEditor(Editor):
    def __init__(self, *args, **ka):
        Editor.__init__(self, *args)

    def _fieldChanged(self):
        name = value = None
        if self._valueCallback:
            value, name, usePathAsAttachmentName = self._valueCallback()

        if (self._document and not usePathAsAttachmentName):
            self._document.set(self._path, name)

        if name and not usePathAsAttachmentName:
            self._document.setAttachment(name, value)
        elif usePathAsAttachmentName:
            self._document.setAttachment(self._path, value)

        self._throwFieldChanged(self._path)
