# -*- coding: utf-8 -*-
import pandas as pd
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

from pptx import Presentation
from pptx.util import Pt,Inches
import os

def createSlide():
    html = urlopen("https://www.letras.mus.br/isaias-saad/ousado-amor/")
    res = BeautifulSoup(html.read(),"lxml")
    
    print((res.find_all(name='h1')[1]).text)
    print((res.find(name='h2').find(name="a").text.strip()))

    titulo = (res.find_all(name='h1')[1]).text
    subtitulo = (res.find(name='h2').find(name="a").text.strip())
    lista_paragrafos = (res.find_all(name='p'))
    print(titulo)
    print(subtitulo)
    '''
    for l in lista_paragrafos:
        print(type(l))
        l.replace("<p>","")
        l.replace("</p>","")

        print(l)
        print("-"*10)
    '''
    prs = Presentation() 
    slide = prs.slides.add_slide(prs.slide_layouts[0])
    title = slide.shapes.title
    subtitle = slide.placeholders[1]
    title.text = titulo
    subtitle.text = subtitulo
    for pa in lista_paragrafos:
        letra = prs.slides.add_slide(prs.slide_layouts[2])
        shape = letra.shapes
        left = Inches(8.2)
        top = Inches(5.7)
        shape.add_picture("base1.png", left, top)
        body_shape = shape.placeholders[1]
        tf = body_shape.text_frame.paragraphs[0]
        tf.font.size = Pt(30)
        tf.text = pa.text
    prs.save(r'slides/' + titulo + '-' + subtitulo + ".pptx")