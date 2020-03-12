from django.shortcuts import render,redirect
from .form import Expenseform,Budform
from .models import Depense,Budget
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models import HoverTool, LassoSelectTool, WheelZoomTool, PointDrawTool, ColumnDataSource
from bokeh.palettes import Category20c, Spectral6
from bokeh.transform import cumsum
from numpy import pi
import pandas as pd
from bokeh.resources import CDN
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm,User


# Create your views here.


 

def compte(request):
    if request.method == 'POST':
      formEx = Expenseform(request.POST)
      formb = Budform(request.POST)
      if formEx.is_valid() and formb.is_valid():
          formEx.save()
          formb.save()
    formEx = Expenseform()
    formb = Budform()
    dtex = Depense.objects.all()
    bud = Budget.objects.all()[1].budgets
     
    return render(request,"compte.html",{"form":formEx,"formb":formb,"exp":dtex,"bud":bud})

    



 
def evolution(request):
   
    habillement = 0
    manager = 0
    nutrition = 0
    transport = 0
    oeuvre_de_charite = 0
    investissements = 0
    credi = 0
    autre = 0
    counts = []
    
    
    items = ["Habillement", "Menager", "Nutritions","Transport","Crédits","O.Charité","Investissement","Autres"]
    dep = Depense.objects.values()
    
    for i in dep:
        if  "HA" in i.values() :
            habillement += 1
        elif ("ME" in i.values()):
            manager += 1
        elif ("NU" in i.values()):
            nutrition += 1   
        elif ("TR" in i.values()):
            transport += 1
        elif ("CR" in i.values()):
            credi += 1
        elif ("OC" in i.values()):
            oeuvre_de_charite += 1
        elif ("INV" in i.values()):
            investissements += 1
        elif ("O" in i.values()):
            autre += 1
    counts.extend([habillement,manager,nutrition,transport,credi,oeuvre_de_charite,investissements,autre])
   
    plot = figure(x_range=items, plot_height=600, plot_width=1100, title="Depenses")
    plot.title.text_font_size = '20pt'
    
    plot.xaxis.major_label_text_font_size = "14pt" 
    plot.vbar(items, top=counts, width=0.8, color= "grey", legend="Depense Kind")
    plot.legend.label_text_font_size = '14pt'

    script, div = components(plot)

    return render(request, 'evolutions.html' , {'script': script, 'div':div})

 