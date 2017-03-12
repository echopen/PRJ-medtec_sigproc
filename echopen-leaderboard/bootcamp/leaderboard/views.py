# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.files.storage import default_storage
from django.shortcuts import render

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models.fields.files import FieldFile
from django.views.generic import FormView
from django.views.generic.base import TemplateView
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from .forms import FilesForm
import string,random, subprocess
from models import Algorithm
from bootcamp.feeds.models import Feed
from bootcamp.activities.models import Activity

import numpy
from skimage import io
from skimage import filter
#from skimage import restoration
from skimage import measure
import time

from kombu import Connection
import datetime

import callme




class FakeField(object):
    storage = default_storage


fieldfile = FieldFile(None, FakeField, 'dummy.txt')


class HomePageView(TemplateView):
    template_name = 'demo/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        messages.info(self.request, 'hello http://example.com')
        return context



class PaginationView(TemplateView):
    template_name = 'demo/pagination.html'

    def get_context_data(self, **kwargs):
        context = super(PaginationView, self).get_context_data(**kwargs)
        lines = []
        for i in range(200):
            lines.append('Line %s' % (i + 1))
        paginator = Paginator(lines, 10)
        page = self.request.GET.get('page')
        try:
            show_lines = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            show_lines = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            show_lines = paginator.page(paginator.num_pages)
        context['lines'] = show_lines
        return context


class MiscView(TemplateView):
    template_name = 'demo/misc.html'


class Sign_upView(TemplateView):
    template_name = 'demo/login.html'


class LeaderboardView(FormView):
    success_url = '/form_horizontal'
    template_name = './demo/form_with_files.html'
    form_class = FilesForm

    def get_context_data(self, **kwargs):
        context = super(LeaderboardView, self).get_context_data(**kwargs)
        context['layout'] = self.request.GET.get('layout', 'vertical')        
        context['object']= self.model
        return context


    def post(self, request, *args, **kwargs):
        try:
            return HttpResponseRedirect('/leaderboard')
        except Exception as e:
            print(e)
            return HttpResponseRedirect('/leaderboard')


    def get(self, request, *args, **kwargs):
            model = Algorithm
            
            try:
                last_obj = model.objects.filter(username = request.user).order_by('-process_date').latest('process_date')
                last_run_id = last_obj.id
                print last_obj.id


            except Exception as e:
                last_run_id = None
                print(e.message)
            resp = model.objects.order_by('rank')
            paginator = Paginator(resp, 25)
            page = self.request.GET.get('page')
            try:
                resp = paginator.page(page)

            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                resp = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                resp = paginator.page(paginator.num_pages)

            return render(request, 'demo/form_with_files.html', {'last_run': last_run_id , 'form': self.form_class, 'button' :'btn-primary',  'object': resp, 'range' :paginator.page_range})


    def handle_uploaded_file(self, f):
        from metrics import run_metrics
        with open('uploaded_custom.py', 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
            destination.close()
        val_ret = {'score':0,'duration': 0}
        ret = subprocess.check_output('python uploaded_custom.py', shell=True)
        import code_exec
        from code_exec import execute_user_script
        import glob 
        denoise_list = glob.glob('./kaggle/*_*.jpg')
        total_list = glob.glob('./kaggle/*.jpg')
        raw_list= list(set(total_list) - set(denoise_list))
        run_duration = execute_user_script(raw_list)
        for i in xrange(1,40):
            tmp  = run_metrics('./kaggle/'+str(i)+'.jpg', './kaggle/denoise_'+str(i)+'.jpg')
            val_ret['score'] += tmp['score']
        val_ret['duration'] = run_duration
        return val_ret

