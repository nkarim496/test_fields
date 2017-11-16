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
            # создает временную папку для shapefile
            tmp_folder = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'tmp'))
            zipfile.extractall(tmp_folder)
            # ищет файл с расширением .shp
            for filename in os.listdir(tmp_folder):
                if filename.endswith('.shp'):
                    # абсолютный путь к .shp файлу
                    shp_path = os.path.join(tmp_folder, filename)
                    save_to_db(shp_path)

                    # todo рендерим shapefile в mapnik    
                    
            # после того как shapefile импортирован в БД и карта отрендерена удаляем временные файлы
            shutil.rmtree(tmp_folder)
    return render(request, 'index.html', {'form': form})
