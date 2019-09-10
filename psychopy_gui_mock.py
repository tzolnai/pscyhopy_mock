#    Copyright (C) <2019>  <Tamás Zolnai>    <zolnaitamas2000@gmail.com>

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

#!\\usr\\bin\\env python
# -*- coding: utf-8 -*-

from psychopy import gui

class Field:
    def __init__(self):
        label = None
        initial = None
        color = None
        choices = None
        tip = None
        enabled = None


class PsychoPyGuiMock:
    def __init__(self):
        self.list_of_texts = []
        self.list_of_fields = []
        self.list_of_values = []
        self.return_value = True

        self.act_dlg_field_number = 0

        gui.Dlg.__init__ = self.init
        gui.Dlg.addText = self.addText
        gui.Dlg.addField = self.addField
        gui.Dlg.show = self.show

    def init(self, title='PsychoPy Dialog', pos=None, size=None, style=None, labelButtonOK=' OK ', labelButtonCancel=' Cancel ', screen=-1):
        self.act_dlg_field_number = 0

    def getListOfTexts(self):
        return self.list_of_texts

    def getListOfFields(self):
        return self.list_of_fields

    def setReturnValue(self, return_value):
        self.return_value = return_value

    def addText(self, text, color='', isFieldLabel=False):
        self.list_of_texts.append(text)

    def addField(self, label='', initial='', color='', choices=None, tip='', enabled=True):
        field = Field()
        field.label = label
        field.initial = initial
        field.color = color
        field.choices = choices
        field.tip = tip
        field.enabled = enabled
        self.list_of_fields.append(field)
        self.act_dlg_field_number += 1

    def addFieldValues(self, list_of_values):
        self.list_of_values = list_of_values

    def show(self):
        gui.Dlg.OK = self.return_value
        data = []

        if self.act_dlg_field_number == 0:
            return data

        for field in self.list_of_fields[-self.act_dlg_field_number:]:
            if len(self.list_of_values):
                data.append(self.list_of_values[0])
                self.list_of_values = self.list_of_values[1:]
            else:
                if len(field.initial) > 0:
                    data.append(field.initial)
                elif field.choices is not None:
                    data.append(field.choices[0])
                else:
                    data.append('')
        return data