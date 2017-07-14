# coding: utf-8

from django.conf.urls import url
from django.views import static
from django.contrib import admin

import views
import images
import card
from music import Music
from book import Book
from movie import Movie
from word import Word

urlpatterns = [
    url(r'^$', views.index),
    url(r'^time/?$', views.current_time),
    url(r'^todos/?$', views.TodoView.as_view(), name='todo_list'),
    url(r'^cards/?$', views.CardView.as_view(), name='card_list'),
    url(r'^cards/preview/$', views.CardPreviewView.as_view(), name='card_list'),
    url(r'^cards/published/?$', views.CardPublishedView.as_view(), name='card_list'),
    url(r'^cards/deleted/?$', views.CardDeletedView.as_view(), name='card_list'),
    url(r'^users/?$', views.UserView.as_view(), name='user_list'),
    url(r'^imageNew/?$', views.imageNew),
    url(r'^static/(?P<path>.*)$', static.serve, {'document_root': 'static'}),
    url(r'^card/generate/(?P<id>\w+)$', card.generate),
    url(r'^card/review/(?P<id>\w+)$', card.review),
    url(r'^card/publish/(?P<id>\w+)$', card.publish),
    url(r'^card/recall/(?P<id>\w+)$', card.recall),
    url(r'^card/reject/(?P<id>\w+)$', card.reject),
    #url(r'^card/list?$', card.list),
    url(r'^card/preview/(?P<id>\w+).png$', card.preview),
    url(r'^card/download/(?P<id>\w+).png$', card.download),
    url(r'^image/text?$', images.image_text),
    url(r'^os/?$', views.os_info),
    url(r'^music/preview/(?P<param>[\w\W]+)$', Music.preview),
    url(r'^book/preview/(?P<param>[\w\W]+)$', Book.preview),
    url(r'^movie/preview/(?P<param>[\w\W]+)$', Movie.preview),
    url(r'^word/preview/(?P<param>[\w\W]+)$', Word.preview),
    url(r'^image/wxacode?$', images.wxacode),
    url(r'^image/template?$', images.template),
    url(r'^image/template2?$', images.template2),
    url(r'^image/template3?$', images.template3),
    url(r'^image/template4?$', images.template4),
    url(r'^image/template6?$', images.template6),
    url(r'^image/book?$', images.book),
    url(r'^image/template5/(?P<font>\w+)$', images.template5),
    url(r'^image/filters/blur?$',images.filter_blur),
    url(r'^image/filters/contour?$', images.filter_contour),
    url(r'^image/filters/detail?$', images.filter_detail),
    url(r'^image/filters/edge_enhance?$', images.filter_edge_enhance),
    url(r'^image/filters/edge_enhance_more?$', images.filter_edge_enhance_more),
    url(r'^image/filters/emboss?$', images.filter_emboss),
    url(r'^image/filters/find_edges?$', images.filter_find_edges),
    url(r'^image/filters/smooth?$', images.filter_smooth),
    url(r'^image/filters/smooth_more?$', images.filter_smooth_more),
    url(r'^image/filters/sharpen?$', images.filter_sharpen),
    url(r'^image/filters/gaussian_blur?$', images.filter_gaussian_blur),
    url(r'^image/filters/unsharp_mask?$', images.filter_unsharp_mask)

]
