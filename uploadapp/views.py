from django.shortcuts import render, redirect
from .forms import FileUploadForm
from .models import UploadedFile
import cloudinary
import cloudinary.uploader
from cloudinary.utils import cloudinary_url
import os

# Cloudinary configuration
cloudinary.config( 
    cloud_name=os.environ['CLOUDINARY_CLOUD_NAME'], 
    api_key=os.environ['CLOUDINARY_API_KEY'], 
    api_secret=os.environ['CLOUDINARY_API_SECRET'],
    secure=True
)

def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                file_name = form.cleaned_data['file_name']
                public_id = form.cleaned_data['public_id'] or 'dummy'
                file = request.FILES['file']
                
                # Upload to Cloudinary
                upload_result = cloudinary.uploader.upload(
                    file,
                    public_id=public_id,
                    resource_type="auto"  # Handles both images and other files
                )
                
                # Get optimized URL
                optimize_url, _ = cloudinary_url(
                    public_id,
                    fetch_format="auto",
                    quality="auto"
                )
                
                # Save to PostgreSQL database
                uploaded_file = UploadedFile.objects.create(
                    file_name=file_name,
                    public_id=public_id,
                    cloudinary_url=optimize_url,
                    secure_url=upload_result.get('secure_url', ''),
                    file_type=file.content_type,
                    file_size=file.size
                )
                
                return render(request, 'upload.html', {
                    'form': FileUploadForm(),
                    'url': optimize_url,
                    'uploaded_file': uploaded_file
                })
            except Exception as e:
                return render(request, 'upload.html', {
                    'form': form,
                    'error': f"Upload failed: {str(e)}"
                })
    else:
        form = FileUploadForm()
    
    return render(request, 'upload.html', {'form': form})