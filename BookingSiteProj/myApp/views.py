# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def index(request):
	return render(request, 'firstPage/formSubmit.html')
def secondPage(request):
	return render(request, 'firstPage/secondPage.html')
