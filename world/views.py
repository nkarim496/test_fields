from django.shortcuts import render
from .forms import UploadForm
from .load import save_to_db
import os
import shutil
from zipfile import ZipFile


# Create your views here.
def index(request):
    form = UploadForm()
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            zipfile = ZipFile(file)
            tmp_folder = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'tmp'))
            zipfile.extractall(tmp_folder)
            for filename in os.listdir(tmp_folder):
                if filename.endswith('.shp'):
                    print(filename)
                    shp_path = os.path.join(tmp_folder, filename)
                    save_to_db(shp_path)
            shutil.rmtree(tmp_folder)
    return render(request, 'index.html', {'form': form})
