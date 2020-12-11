# encoding: utf-8
"""
Views relating to the grants
"""
__author__ = 'Richard Smith'
__date__ = '10 Dec 2020'
__copyright__ = 'Copyright 2018 United Kingdom Research and Innovation'
__license__ = 'BSD - see LICENSE file in top-level package directory'
__contact__ = 'richard.d.smith@stfc.ac.uk'

# Datamad2 imports
from datamad2.models import Grant, Document, DataProduct, ImportedGrant
from .base import DATAPRODUCT_TABLE_CLASS_MAP, DATAPRODUCT_FORM_CLASS_MAP
from .generic import ObjectDeleteView
import datamad2.forms as datamad_forms
from datamad2.utils import generate_document_from_template

# Django imports
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView
from django.core.exceptions import ImproperlyConfigured, ObjectDoesNotExist
from django.views.generic.edit import UpdateView
from django.urls import reverse
from django.views.generic.edit import FormView
from django.http import FileResponse


@login_required
def grant_detail(request, pk):
    """
    Grant detail page
    :param request: WSGI Request
    :param pk: Grant ID
    :return:
    """
    grant = get_object_or_404(Grant, pk=pk)
    imported_grant = grant.importedgrant

    docs = grant.document_set.filter(type='support')
    dmp_docs = grant.document_set.filter(type='dmp')

    if grant.parent_grant:
        parent_docs = grant.parent_grant.document_set.filter(type='support')
        parent_dmps = grant.parent_grant.document_set.filter(type='dmp')

    else:
        parent_docs = Document.objects.none()
        parent_dmps = Document.objects.none()

    return render(request, 'datamad2/grant_detail.html', {
        'imported_grant': imported_grant,
        'supporting_docs': docs | parent_docs,
        'dmp_docs': dmp_docs | parent_dmps,
    })


@login_required
def grant_history(request, pk):
    """
    Displays the grant history table
    :param request: WSGI Request
    :param pk: Grant ID
    :return:
    """
    grant = get_object_or_404(Grant, pk=pk)
    return render(request, 'datamad2/grant_history.html', {'grant': grant})


@login_required
def grant_history_detail(request, pk, imported_pk):
    """
    Displays the grant detail with changes highlighted
    :param request: WSGI Request
    :param pk: Grant ID
    :param imported_pk: ImportedGrant ID
    :return:
    """
    grant = get_object_or_404(Grant, pk=pk)
    imported_grant = get_object_or_404(ImportedGrant, pk=imported_pk)
    return render(request, 'datamad2/grant_detail_history.html', {'grant': grant, 'imported_grant': imported_grant})


class DataProductView(LoginRequiredMixin, TemplateView):
    """
    Lists all the data products for the specified grant
    """
    template_name = 'datamad2/dataproduct_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        grant = get_object_or_404(Grant, pk=kwargs['pk'])
        context['grant'] = grant
        context['data_products'] = {
            product: table(grant.dataproduct_set.filter(data_product_type=product))
            for product, table in DATAPRODUCT_TABLE_CLASS_MAP.items()
        }
        return context


class DataProductUpdateCreateView(LoginRequiredMixin, UpdateView):
    """
    Update or create a new data product
    """
    template_name = 'datamad2/dataproduct_form_view.html'
    model = DataProduct

    def get_initial(self):
        initial = super().get_initial()
        initial['grant_id'] = get_object_or_404(Grant, pk=self.kwargs['pk']).pk
        initial['data_product_type'] = self.kwargs['data_product_type']
        return initial

    def get_success_url(self):
        return reverse('dataproduct_view', kwargs={'pk': self.kwargs['pk']})

    def get_form_class(self):
        """Return the form class to use in this view."""
        if self.fields is not None and self.form_class:
            raise ImproperlyConfigured(
                "Specifying both 'fields' and 'form_class' is not permitted."
            )

        form_class = DATAPRODUCT_FORM_CLASS_MAP.get(self.kwargs['data_product_type'])
        return form_class

    def get_object(self, **kwargs):
        """
        This modification means this view behaves as an update or create view.
        If the object doesn't exist, it will create one.
        """
        try:
            return self.model.objects.get(pk=self.kwargs['dp_pk'])
        except (ObjectDoesNotExist, KeyError):
            return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grant'] = get_object_or_404(Grant, pk=self.kwargs['pk'])
        context['data_product_type'] = self.kwargs['data_product_type']
        return context


class DataProductDeleteView(ObjectDeleteView):
    """
    Delete a Data Product
    """
    model = DataProduct
    pk_url_kwarg = 'dp_pk'

    def get_success_url(self):
        return reverse('dataproduct_view', kwargs={'pk': self.kwargs['pk']})


class DocumentGenerationSelectView(LoginRequiredMixin, FormView):
    """
    View which displays the available templates for document generation
    Only displays the forms created by the logged in users datacentre
    """
    template_name = 'datamad2/generate_document_from_template.html'
    form_class = datamad_forms.DocumentGenerationForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['imported_grant'] = get_object_or_404(Grant, pk=self.kwargs['pk']).importedgrant
        return context

    def form_valid(self, form):
        template = form.cleaned_data['document_template']
        grant = Grant.objects.get(pk=self.kwargs['pk'])
        context = {
            'grant': grant
        }

        doc = generate_document_from_template(template, context)

        download_filename = f'{grant.grant_ref.replace("/", "_")}_{template.type.upper()}{os.path.splitext(template.template.name)[1]}'

        return FileResponse(open(doc, 'rb'), as_attachment=True, filename=download_filename)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['datacentre'] = self.request.user.data_centre
        return kwargs


class ChangeClaimFormView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Form to allow the user to reassign the primary datacentre
    """
    model = Grant
    template_name = 'datamad2/change_claim.html'
    form_class = datamad_forms.UpdateClaimForm
    permission_denied_message = "Your data centre does not match the datacentre of the grant"

    def test_func(self):
        """
        Test to make sure that the user either comes from a datacentre which
        has responsibility for the grant or the grant has not been claimed.
        Aims to prevent users from unclaiming or reassigning grants already
        assigned to another datacentre

        :return: bool
        """
        grant = get_object_or_404(Grant, pk=self.kwargs['pk'])
        user_datacentre = self.request.user.data_centre
        grant_datacentre = grant.assigned_data_centre
        return grant_datacentre is None or grant_datacentre == user_datacentre

    def get_success_url(self):
        return reverse('grant_detail', kwargs={'pk': self.kwargs['pk']})


class GrantInfoEditView(LoginRequiredMixin, UpdateView):
    """
    View which presents a form with the editable grant information
    """
    model = Grant
    form_class = datamad_forms.GrantInfoForm
    template_name = 'datamad2/grantinfo_edit.html'

    def get_success_url(self):
        return reverse('grant_detail', kwargs={'pk': self.kwargs['pk']}) + '#editable-info'
