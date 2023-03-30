import glob
from string import Template

tmp_gallery = Template('''
---
title: gallery
---
$images

''')

def makeGallery():
    path = 'docs/images/'
    types = ('*.jpg', '*.jpeg', '*.png', '*.gif')
    files_images = []
    for files in types: files_images.extend(glob.glob(path+files))
    md_images = []
    for image in files_images:
        md = '![]('+image.replace('docs/','')+')\n'
        md_images.append(md)
    string = tmp_gallery.safe_substitute(images=''.join(md_images))
    f = open("docs/gallery.md", "w")
    f.write(string)
    f.close()
    print(string)
    return 'yes'

def on_pre_build(config):
    makeGallery()
    return config



