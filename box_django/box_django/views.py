from django.shortcuts import render_to_response

from datetime import datetime

def home(request):
  return render_to_response('index.html', {'now': datetime.now().isoformat()})
