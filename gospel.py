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
import slides
from pptx import Presentation
from pptx.util import Pt,Inches
import os
import unittest
import time
import re

options = Options()
#options.add_argument("--headless")

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(options=options, executable_path = r"/usr/local/bin/geckodriver")
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled_test_case(self):
        driver = self.driver
        lista_musicas = [
        'https://www.letras.mus.br/anderson-freire/1789576/',
        'https://www.letras.mus.br/thaiane-seghetto/meu-amado/',
        'https://www.letras.mus.br/anderson-freire/a-gloria-tua/',
        'https://www.letras.mus.br/ministerio-pedras-vivas/pai-nosso/',
        'https://www.letras.mus.br/ministerio-cristo-vivo/1950960/'
        ]
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


        print(titulo)
        print(subtitulo)
        print(lista_paragrafos)




            

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        #self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
