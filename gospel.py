import requests
import os
import shutil

from bs4 import BeautifulSoup
from urllib.request import urlopen
from pptx import Presentation
from pptx.util import Pt,Inches


def createSlide():
    html = urlopen("https://www.letras.mus.br/midian-lima/nao-pare/")
    res = BeautifulSoup(html.read(),"lxml")
    titulo = (res.find_all(name='h1')[1]).text
    subtitulo = (res.find(name='h2').find(name="a").text.strip())
    lista_paragrafos = (res.find("div", {"class":'cnt-letra p402_premium'}).find_all(name='p'))
  
    prs = Presentation() 
    slide = prs.slides.add_slide(prs.slide_layouts[0])
    title = slide.shapes.title
    subtitle = slide.placeholders[1]
    title.text = titulo
    subtitle.text = subtitulo
    for linha in lista_paragrafos:
        letra = prs.slides.add_slide(prs.slide_layouts[2])
        shape = letra.shapes
        left = Inches(8.2)
        top = Inches(5.7)
        shape.add_picture("base1.png", left, top)
        body_shape = shape.placeholders[1]
        tf = body_shape.text_frame.paragraphs[0]
        tf.font.size = Pt(30)
        tf.text = str(linha).replace("<br/>","\n").replace("<p>","").replace("</p>","")
    name_file = titulo + '-' + subtitulo + ".pptx"
  
    prs.save(r'slides/' + name_file)
    return name_file
    