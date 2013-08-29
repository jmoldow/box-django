from django.shortcuts import render_to_response

from datetime import datetime

def home(request):
  return render_to_response('base_boxfiles.html', {'now': datetime.now().isoformat()})
