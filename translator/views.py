from django.shortcuts import render
from .import translate

# Create your views here.
def translator(request):
    if request.method=='POST':
        original_text=request.POST['my_textarea']
        output= translate.translate(original_text)
        print(output)
        return render(request,'translator.html',{'output_text': output,'original_text':original_text})
    else:
        return render(request,'translator.html')