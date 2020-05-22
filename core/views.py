from django.shortcuts import render
from PIL import Image
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse

def index(request):
	return render(request, 'index.html')

def imgtopdf(request):
	if request.method == "POST":
		img = request.FILES.get('img')
		print(type(img))
		# fs = FileSystemStorage()
		# filename = fs.save(img.name, img)
		# print(fs.url(filename))
		image1 = Image.open(img)
		im1 = image1.convert("RGB")
		print(type(im1))
		im1.save("media/image.pdf")
		print(type(im1))
		return render(request, 'imgtopdf.html',{
			"url": "convertions/image.pdf"
		})
	else:
		return render(request, 'imgtopdf.html')
