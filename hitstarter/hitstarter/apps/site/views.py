from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.http import Http404
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render_to_response, Http404, HttpResponse
from django.template import loader, RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST 
from django.views.decorators.http import require_http_methods
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.base import TemplateView
from django.db import connection, transaction

from hitstarter.apps.site.models import Project
import hitstarter.apps.site.models as projects

def home(request):

    featured_projects = projects.get_featured_projects()

    return render_to_response('index.html', {
        'projects': featured_projects
        },
        context_instance=RequestContext(request))

def project(request, project_id):

    project = projects.get_project_by_id(project_id)

    return render_to_response('project.html', {
            'project': project,
        },
        context_instance=RequestContext(request))
