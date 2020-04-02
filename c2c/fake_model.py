import csv
def fake_predict(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,aa,ab,ac,ad):
    import pickle
    x=[[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,aa,ab,ac,ad]]
    randomforest=pickle.load(open('c2c/model.sav','rb'))
    prediction=randomforest.predict(x)
    if prediction==9:
        prediction='Rabies'
    elif prediction==2:
        prediction='Chicken Pox'
    elif prediction==5:
        prediction="Conjuctivitis"    
    elif prediction==0:
        prediction="Anaemia"
    elif prediction==1:
        prediction="Asthma"    
    elif prediction==4:
        prediction="Common Cold" 
    elif prediction==11:
        prediction="Diarrohea"       
    elif prediction==6:
        prediction="FLU" 
    elif prediction==12:
        prediction="Hepatatis A" 
    elif prediction==13:
        prediction="Malaria" 
    elif prediction==8:
        prediction="Measales" 
    elif prediction==10:
        prediction="TB" 
    elif prediction==14:
        prediction="Typhoid" 
    elif prediction==7:
        prediction="Influenza" 
    else :
        prediction="Cholera" 
                                              
    return prediction
