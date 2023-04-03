# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 13:29:48 2023

@author: Nakano_Lab
"""

from PIL import Image

im = Image.open("1.png")
im.save("1_test.png", quality=95)