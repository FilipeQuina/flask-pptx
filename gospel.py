import requests
import os
import shutil

from bs4 import BeautifulSoup
from urllib.request import urlopen
from pptx import Presentation
from pptx.util import Pt,Inches

prs = Presentation() 
slide = prs.slides.add_slide(prs.slide_layouts[0])
left = Inches(8.2)
top = Inches(5.7)

def createSlide(url):
    html = urlopen(url)
    res = BeautifulSoup(html.read(),"lxml")
    titulo = (res.find_all(name='h1')[1]).text
    subtitulo = (res.find(name='h2').find(name="a").text.strip())
    letraCompleta = (res.find("div", {"class":'cnt-letra p402_premium'}).find_all(name='p'))
  
    title = slide.shapes.title
    subtitle = slide.placeholders[1]
    title.text = titulo
    subtitle.text = subtitulo

    generate_slide(makeText(letraCompleta))
       
    name_file = titulo + '-' + subtitulo + ".pptx" 
    prs.save(r'slides/' + name_file)
    return name_file

def generate_slide(paragrafos):
    for linhas in paragrafos:
        letra = prs.slides.add_slide(prs.slide_layouts[2])
        shape = letra.shapes
        left = Inches(8.2)
        top = Inches(5.7)
        shape.add_picture("base1.png", left, top)
        body_shape = shape.placeholders[1]
        tf = body_shape.text_frame.paragraphs[0]
        tf.font.size = Pt(40)
        for linha in linhas:
            tf.text += "\n"
            tf.text += str(linha)

def makeText(letraCompleta):
    textClear = []
    for paragrafos in letraCompleta:
        l = str(paragrafos).replace("<p>","").replace("</p>","").split("<br/>")
        for i in range (len(l)):
            if len(l)>=5:
                halfText = int(len(l)/2)
                lineStart = l[i:halfText]
                lineEnd = l[halfText:int(len(l))]
                textClear.append(lineStart)
                textClear.append(lineEnd)
                break
            else:
                textClear.append(l)
                break
    return textClear