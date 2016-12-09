# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.forms.formsets import BaseFormSet, formset_factory




class FilesForm(forms.Form):
    file = forms.FileField(
        label='',
        help_text='max. 42 megabytes')


