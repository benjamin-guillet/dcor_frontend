# HiPerCic Project / St. Olaf College / Computer Science Dept.
###################################################################################
# apps/dcor/urls.py
# Holds url patterns for the app site.  Links urls requested by users to various view functions
###################################################################################
from django.conf.urls.defaults import *

urlpatterns = patterns(
    # The path to this specific app's view functions
    'hipercic.apps.dcor.views', # remember to insert your app's name!
    (r'^$', 'home'),  # calls the home view!
	(r'^jobs/$', 'job_submit'),
	(r'^jobs/submit','job_submit'),
	(r'^jobs/pending','job_pending'),
)