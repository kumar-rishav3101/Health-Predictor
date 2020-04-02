from django.shortcuts import render,redirect
from django.http import HttpResponse

from  . import forms
from .models import Files,Remedy
from c2c import fake_model



def first(request):
   # listt = topic.objects.all
   # print(listt)
    #myweb={"list":"listt"}
    if request.method=="POST":
        if request.POST.get("PredictCommon"):
            return redirect('/form')
       
        return redirect('/skinform')
    return render(request,'firstt.html')


def form_name_view(request):
   # form=forms.FormName()
        
   # try:
        form=forms.MyModel()
        if request.method=="POST":
            form=forms.MyModel(request.POST)
            if form.is_valid():
                
                form.save(commit=True)
                some_var = form.cleaned_data.get('Symptoms')
                days=form.cleaned_data.get('Days')
                print(days)
                print(some_var)
                for i in range(0, len(some_var)): 
                    some_var[i] = int(some_var[i])
                mydict={}
                li=[]
                for i in range(1,32):
                    if(i in some_var):
                        mydict[i]=True
                        li.append(1)
                    else:
                        mydict[i]=False
                        li.append(0)
                print(mydict) 
                print(li) 
                l=li           
                prediction=fake_model.fake_predict(l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7],l[8],l[9],l[10],l[11],l[12],l[13],l[14],l[15],l[16],l[17],l[18],l[19],l[20],l[21],l[22],l[23],l[24],l[25],l[26],l[27],l[28],l[29])
                request.session['prediction']=prediction
                if request.POST.get('SUBMIT'):
                    if days>3:
                        return redirect('/disease') 
                    else:
                        return HttpResponse("Wait for some more time")   

                 
                returnbutton= request.POST.get('Back')
                print(returnbutton)
                if returnbutton:
                   return redirect('/index')
  
                
   

        
    
        return render(request,'form.html',{'form':form})

def disease(request):
    prediction = request.session['prediction']
    print(prediction)
    if request.method=="POST":
        if request.POST.get("Back"):
            return redirect('/form')
        data=Remedy.objects.filter(Diseasename=prediction)[0]
        print(data.Diseasename)
        data_list=data. Remedies.split(r'\n')
        # print(data_list)
       
        if request.POST.get('Remedies'):
            return redirect('/remedies')
        
        
    else:
                 
        return render(request,'result.html',{'prediction':prediction})  

def remedy(request):
    prediction = request.session['prediction']
    data=Remedy.objects.filter(Diseasename=prediction)[0]
    print(data.Diseasename)
    data_list=data. Remedies.split(r'\n')
    
    if request.method=="POST":
        if(request.POST.get("Back")):
            return redirect('/disease')    
    return render(request,'remedy.html',{'data':data,'data_list':data_list})            
def fake_predict(file_type):
    import pickle
    # from keras.models import Sequential
    # from keras.layers import Convolution2D
    # from keras.layers import MaxPooling2D
    # from keras.layers import Flatten
    # from keras.layers import Dense
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import Input, Conv2D, MaxPool2D, Dense
    import tensorflow
    from keras.preprocessing import image
    from matplotlib.image import imread
    import numpy as np
    import cv2 as cv
    x=file_type
    cnn=pickle.load(open('myapp/model1.sav','rb'))
    #img=imread(x)
    img=image.load_img(x, target_size=(64, 64))
    img = image.img_to_array(img)
    img =np.expand_dims(img, axis=0)
    prediction=cnn.predict(img)
    return prediction         

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']
def create_profile(request):
    form = forms.File()
    if request.method == 'POST':
        form = forms.File(request.POST, request.FILES)
        if form.is_valid():
            user_pr = form.save(commit=False)
            user_pr.display_picture = request.FILES['display_picture']
            file_type = user_pr.display_picture.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                return render(request, 'error.html')
            res=fake_predict(user_pr.display_picture)
            out="Malign"
            if res[0]==0:
        
                out="Benign"
            x=out
            #return HttpResponse(out)  
            user_pr.save() 
            if out=="Malign":
                return render(request,'details.html',{'x':x}) 
            if out=="Benign":
                return render(request, 'details1.html', {'x': x})

              
    context = {"form": form}
    return render(request, 'create.html', context) 

