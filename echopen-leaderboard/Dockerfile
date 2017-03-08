#Download base image leaderboard
FROM python:2.7


ADD ./requirements.txt /requirements.txt
ADD ./manage.py /manage.py
ADD ./bootcamp/settings.py /settings.py
ADD ./uploaded_custom.py /uploaded_custom.py
ADD ./bootcamp/urls.py /urls.py
ADD ./bootcamp/wsgi.py /wsgi.py
ADD ./bootcamp/demo.db /demo.db
ADD ./Procfile /Procfile
ADD ./bootcamp/decorators.py /decorators.py

ADD ./bootcamp /bootcamp
#ADD ./processor_node /processor

RUN pip install cython
RUN pip install numpy
RUN pip install scikit-image
RUN pip install -r requirements.txt
RUN pip install kombu
RUN pip install Unipath
RUN pip install callme
RUN pip install mongoengine
RUN pip install requests
RUN python django-admin runserver &
EXPOSE 8888

