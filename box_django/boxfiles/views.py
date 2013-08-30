from django.shortcuts import render_to_response
from django.http import Http404

from datetime import datetime

from boxfiles.models import SimpleFile

def home(request):
  user = request.user
  public_files = SimpleFile.objects.filter(is_public=True).order_by('-mtime')
  private_files = SimpleFile.objects.filter(is_public=False).order_by('-mtime')
  num_files = len(public_files) + len(private_files)
  return render_to_response('base_boxfiles.html', {
    'now': datetime.now().isoformat(),
    'public_files': public_files,
    'private_files': private_files,
    'num_files': num_files,
  })

def fileview(request, file_id):
  try:
    file = SimpleFile.objects.get(id=file_id, owner=request.user)
  except SimpleFile.DoesNotExist:
    raise Http404()
  return render_to_response('fileview.html', {
    'file': file,
    'now': datetime.now().isoformat(),
  })
