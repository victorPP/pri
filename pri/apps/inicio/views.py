from django.shortcuts import render_to_response
from django.template import RequestContext

from  django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect



def index_view(request):
		return render_to_response('inicio/index.html',context_instance=RequestContext(request))
		

