# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.conf.urls import url

from .views import HomePageView,  LeaderboardView, MiscView, Sign_upView


urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^misc$', MiscView.as_view(), name='misc'),
    url(r'^leaderboard$', LeaderboardView.as_view(), name='leaderboard'),
    url(r'^login$', Sign_upView.as_view(), name='login'),

]
