# Leaderboard

Leaderboard is based on Bootcamp which is an open source **Enterprise social network** built with [Python][0] using the [Django Web Framework][1].

## Infrastructre
With our leaderboard infra you'll submit your source code, to win the challenge !!                   
Front-server : django infrastructure, which can by started by >> python manage.py runserver 0.0.0.0:8000.
Back-server : will process your code against datas and images depend with our challenge >> python echopen-leaderboard/processor-node/server_echopen.py.
Sign_in and submit this code on the IDE for example :  echopen-leaderboard/processor-node/uploaded_custom.py.


These 2 side discuss with rabbitmq, which have to be installed first on your local machine.

## Bootcamp 

The project has three basic apps:

* Feed (A Twitter-like microblog)
* Articles (A collaborative blog)
* Question & Answers (A Stack Overflow-like platform)

### Feed App

The Feed app has infinite scrolling, activity notifications, live updates for likes and comments, and comment tracking.


### Articles App

The Articles app is a basic blog, with articles pagination, tag filtering and draft management.


### Question & Answers App

The Q&A app works just like Stack Overflow. You can mark a question as favorite, vote up or vote down answers, accept an answer and so on.


### Technology Stack

- Python 2.7
- Django 1.9.4
- Twitter Bootstrap 3
- jQuery 2


### Installation Guide

Take a look at our wiki page for a detailed [installation guide][3].


### Demo

Try Bootcamp now at [http://trybootcamp.vitorfs.com][2].

[0]: https://www.python.org/
[1]: https://www.djangoproject.com/
[2]: http://trybootcamp.vitorfs.com/
[3]: https://github.com/vitorfs/bootcamp/wiki/Installing-and-Running-Bootcamp


## HackIDE


hackIDE is an online code editor, compiler and interpreter based on Django, powered by HackerEarth API! Go, hack it!

####Visit - [hackIDE | Online Code Editor, Compiler & Interpreter](http://hackide.herokuapp.com)


## Screenshot- 
![Screenshot for HackIDE](/hackIDE/static/hackIDE/img/screenshot.png?raw=true "Screenshot for HackIDE")

## How to run the server locally

```
$ python manage.py collectstatic
$ HACKIDE_DEBUG=true python manage.py runserver
```

Note that the IDE may not show up without a valid api token from HackerEarth. To specify the HackerEarth api token, supply it with ```HE_CLIENT_SECRET``` as a command line argument.

```
$ python manage.py collectstatic
$ HE_CLIENT_SECRET=your_token_here python manage.py runserver
```

## TODO
 - [x] Add "Download code as a zipped file" option
 - [x] Implement "Save code on cloud" feature
 - [x] Implement profiling system allowing users to make their profiles and saving codes in their profiles

