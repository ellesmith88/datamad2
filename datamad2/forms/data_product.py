# encoding: utf-8
"""

"""
__author__ = 'Richard Smith'
__date__ = '25 Sep 2020'
__copyright__ = 'Copyright 2018 United Kingdom Research and Innovation'
__license__ = 'BSD - see LICENSE file in top-level package directory'
__contact__ = 'richard.d.smith@stfc.ac.uk'

from django import forms
from django.forms import formset_factory
from datamad2.models import DataProduct


class DigitalDataProductForm(forms.ModelForm):
    class Meta:
        model = DataProduct
        fields = [
            'description',
            'contact',
            'data_volume',
            'delivery_date',
            'embargo_date',
            'doi',
            'preservation_plan',
            'additional_comments'
        ]


class ModelSourceDataProductForm(forms.ModelForm):
    class Meta:
        model = DataProduct
        fields = [
            'name',
            'contact',
            'description',
            'sample_destination',
            'additional_comments'
        ]


class PysicalDataProductForm(forms.ModelForm):
    class Meta:
        model = DataProduct
        fields = [
            'name',
            'contact',
            'data_format',
            'issues',
            'delivery_date',
            'additional_comments'
        ]


class HardcopyDataProductForm(forms.ModelForm):
    class Meta:
        model = DataProduct
        fields = [
            'name',
            'contact',
            'data_format',
            'issues',
            'delivery_date',
            'additional_comments'
        ]


class ThirdPartyDataProductForm(forms.ModelForm):
    class Meta:
        model = DataProduct
        fields = [
            'name',
            'contact',
            'data_location',
            'description',
            'data_volume',
            'responsibility',
            'issues',
            'additional_comments'
        ]


DigitalDataProductFormset = formset_factory(DigitalDataProductForm, extra=0, can_delete=True)
ModelSourceDataProductFormset = formset_factory(ModelSourceDataProductForm, extra=0, can_delete=True)
PysicalDataProductFormset = formset_factory(PysicalDataProductForm, extra=0, can_delete=True)
HardcopyDataProductFormset = formset_factory(HardcopyDataProductForm, extra=0, can_delete=True)
ThirdPartyDataProductFormset = formset_factory(ThirdPartyDataProductForm, extra=0, can_delete=True)
