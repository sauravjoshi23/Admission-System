from django.conf.urls import url
from .views import *

urlpatterns =[
	url(r'^$', index, name='index'),
	url(r'^Computer_Engineering$', display_Computer, name='display_Computer'),
	url(r'^IT_Engineering$', display_IT, name='display_IT'),
	url(r'^Mechanical_Engineering$', display_Mechanical, name='display_Mechanical'),
	url(r'^Electronics_Engineering$', display_Electronics, name='display_Electronics'),

	url(r'^add_Computer$', add_Computer, name="add_Computer"),
    url(r'^add_IT$', add_IT, name="add_IT"),
    url(r'^add_Mechanical$', add_Mechanical, name="add_Mechanical"),
    url(r'^add_Electronics$', add_Electronics, name="add_Electronics"),

    url(r'^edit_Computer/(?P<pk>\d+)$', edit_Computer, name="edit_Computer"),
    url(r'^edit_IT/(?P<pk>\d+)$', edit_IT, name="edit_IT"),
    url(r'^edit_Mechanical/(?P<pk>\d+)$', edit_Mechanical, name="edit_Mechanical"),
    url(r'^edit_Electronics/(?P<pk>\d+)$', edit_Electronics, name="edit_Electronics"),

    url(r'^delete_Computer/(?P<pk>\d+)$', delete_Computer, name="delete_Computer"),
    url(r'^delete_IT/(?P<pk>\d+)$', delete_IT, name="delete_IT"),
    url(r'^delete_Mechanical/(?P<pk>\d+)$', delete_Mechanical, name="delete_Mechanical"),
    url(r'^delete_Electronics/(?P<pk>\d+)$', delete_Electronics, name="delete_Electronics"),
]