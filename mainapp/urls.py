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
]