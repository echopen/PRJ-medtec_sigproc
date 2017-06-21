#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: sahildua2305
# @Date:   2016-01-06 00:11:27
# @Last Modified by:   Sahil Dua
# @Last Modified time: 2016-08-11 00:06:17

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
import string,random, subprocess
from bootcamp.leaderboard.models import Algorithm
from bootcamp.feeds.models import Feed
from bootcamp.activities.models import Activity
from django.http import HttpResponseRedirect, HttpResponse

import string,random, subprocess
from bootcamp.leaderboard.models import Algorithm
from bootcamp.feeds.models import Feed
from bootcamp.activities.models import Activity

from kombu import Connection
import datetime
import callme


from django.shortcuts import render
from django.http import JsonResponse, HttpResponseForbidden
from models import codes

import requests, json, os 
import uuid

# access config variable
#DEBUG = (os.environ.get('HACKIDE_DEBUG') != None)
# DEBUG = (os.environ.get('HACKIDE_DEBUG') or "").lower() == "true"
#CLIENT_SECRET = os.environ['HE_CLIENT_SECRET'] if not DEBUG else ""

permitted_languages = ["C", "CPP", "CSHARP", "CLOJURE", "CSS", "HASKELL", "JAVA", "JAVASCRIPT", "OBJECTIVEC", "PERL", "PHP", "PYTHON", "R", "RUBY", "RUST", "SCALA"]

CLIENT_SECRET = '8eba4fb5086f2a7e838388a5812c0c2faa77d612'

"""
Check if source given with the request is empty
"""
def source_empty_check(source): 	
   if source == "":
    response = {
      "message" : "Source can't be empty!",
    }
    return JsonResponse(response, safe=False)


"""
Check if lang given with the request is valid one or not
"""
def lang_valid_check(lang):
  if lang not in permitted_languages:
    response = {
      "message" : "Invalid language - not supported!",
    }
    return JsonResponse(response, safe=False)


"""
Handle case when at least one of the keys (lang or source) is absent
"""
def missing_argument_error():
  response = {
    "message" : "ArgumentMissingError: insufficient arguments for compilation!",
  }
  return JsonResponse(response, safe=False)



"""
View catering to /ide/ URL,
simply renders the index.html template
"""
def index(request):
  # render the index.html
  return render(request, 'hackIDE/index.html', {'source_code':'''def install_packages():"\n    import pip\n    pip.main(['install', 'my_package'])\n\n\ndef run(rawSignal,image_shape):\n    #your exec code here"'''})


"""
View catering to /ide/ URL,
simply renders the index.html template
"""
def hackide(request, code_id=None):
  # render the index.html
  query = Algorithm.objects.filter(id=code_id)
  for obj in query:
      print(obj.source_code)

  return render(request, 'hackIDE/index.html', {'source_code': obj.source_code})


"""
Method catering to AJAX call at /ide/run/ endpoint,
makes call at HackerEarth's /run/ endpoint and returns the run result as a JsonResponse object
"""


class runCode(FormView):
  success_url = '/form_horizontal'
  template_name = './demo/form_with_files.html'

  def get_context_data(self, **kwargs):
        context = super(runCode, self).get_context_data(**kwargs)        
        return context
  
  
  def get(self, request, *args, **kwargs): 
          render(request, 'hackIDE/index.html', {'source_code':'toto'})
    
  
	  
  def post(self, request):
	  if request.is_ajax():
		    source = request.POST['source']
		    # Handle Empty Source Case
		    source_empty_check(source)
		    print source
		    lang = request.POST['lang']
		    # Handle Invalid Language Case
		    lang_valid_check(lang)
                    proxy = callme.Proxy(server_id='fooserver',amqp_host='salamander.rmq.cloudamqp.com', amqp_vhost='spwlpmyp', amqp_user='spwlpmyp', amqp_password='_O3u6xA_26r_lGSBpfJY_fJn4Eu_9Sl3')
                    
                    resp = proxy.enveloppe_extract(source)


                    model = Algorithm
                    #source = source    + '\n' + resp['error_msg']
                    run_rank = model.objects.filter(score__lte=int(resp['score'])).order_by('rank')
                    if len(run_rank) > 0:
                        rankobj = run_rank.last()
                        rank = rankobj.rank + 1

                    else:
                        rank = 1
                     
                    run_rank_low = model.objects.filter(score__gt=int(resp['score']))
                    if len(run_rank_low) > 0 :
                        for i in run_rank_low:
                            i.rank += 1
                            i.save()

                    else:
                        pass
                    
                                  
                    b = Algorithm(username=request.user.username, user=request.user, rank = rank, score=resp['score'], time= resp['duration'], source_code=source, cpu=18)
                    b.save()
                    job_post = u'{0} has sent a job score: {1} rank: {2} :'.format(request.user.username,resp['score'], rank)
                    cop_resp = resp
                    resp = model.objects.all().order_by('rank')
                    values = resp.values('id')
                    
                    for ind, item  in enumerate(values) :
                        if (item['id']) == b.id:
                            paging =  divmod(ind, 5)[0]


                    print(cop_resp)
                    if cop_resp['error_msg'] == 'None':
                        r={'compile_status':'OK', 'run_status_status':'OK'}
                    else:
                        r = {'compile_status': 'OK', 'run_status_status': 'ERROR', 'run_status_error':cop_resp['error_msg']}



                    feed = Feed(user=request.user, post=job_post, job_link='/leaderboard?q=foo&flop=flip&page='+str(paging+1))
                    feed.save()
                    like = Activity(activity_type=Activity.RUN_PROCESSED, feed=feed.pk, user=request.user)
                    like.save()

                    user = request.user
                    user.profile.notify_liked_bis(feed)

                    import json
                    #r['compile_status'] = 'OK'
                    #r['run_status']['status'] = 'AC'
                    #r['run_status']['time_used'] = '12'
                    #r['run_status']['memory_used'] = '12'
                    #r['run_status']['output_html'] = "dededed"
                    #r['run_status']['stderr'] =  "toto"

                    #r   = json.dumps(r)
                    #return HttpResponse(r, content_type="application/json")
                    return JsonResponse(r, safe=False)
		    #return HttpResponse(render(request, 'hackIDE/index.html'))

	  else:
		print('error')  
		return HttpResponseForbidden()


