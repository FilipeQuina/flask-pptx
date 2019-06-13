# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from pptx import Presentation
from pptx.util import Pt,Inches
import os
import unittest
import time
import re

options = Options()
options.add_argument("--headless")
    
#def createSlide():
driver = webdriver.Firefox(options=options, executable_path=os.getcwd()+"/vendor/geckodriver/geckodriver.exe")

verificationErrors = []
accept_next_alert = True

print("VAI")
lista_musicas = ['https://www.letras.mus.br/anderson-freire/1789576/']
for lista in lista_musicas:
    driver.get(lista)
    titulo = driver.find_element_by_css_selector('.cnt-head_title > h1:nth-child(1)').text
    subtitulo = driver.find_element_by_css_selector('.cnt-head_title > h2:nth-child(2) > a:nth-child(1)').text
    lista_paragrafos = driver.find_element_by_css_selector('.cnt-letra').find_elements_by_tag_name('p')
    #paragrafos = []
    #for p in lista_paragrafos:
    #    paragrafos.append(p.text)
    #    print(p.text)
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
driver.quit()
   
if __name__ == "__main__":
    unittest.main()
