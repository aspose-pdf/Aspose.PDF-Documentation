---
title: Convertir PDF en Différents Formats d'Image en Python
linktitle: Convertir PDF en Images
type: docs
weight: 70
url: /python-cpp/convert-pdf-to-images-format/
lastmod: "2023-06-23"
description: Ce sujet vous montre comment utiliser Aspose.PDF pour Python pour convertir un PDF en différents formats d'images tels que TIFF, BMP, EMF, JPEG, PNG, GIF, SVG avec quelques lignes de code.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## Vue d'ensemble

Cet article explique comment convertir un PDF en différents formats d'image en utilisant Python. Il couvre les sujets suivants.

## Python Convertir PDF en Image

### Python Convertir PDF en PNG

1. Importez le module AsposePdfPython, qui fournit un wrapper Python pour la bibliothèque Aspose.PDF.
1. Ouvrez un document PDF en utilisant la fonction `document_open`, qui prend le nom du fichier comme argument et retourne un objet Document.
1. Obtenez les pages du document en utilisant la fonction `document_get_pages`, qui prend un objet Document comme argument et retourne un objet PageCollection.

1. Obtenez la page souhaitée du document à l'aide de la fonction `page_collection_get_page`, qui prend un objet PageCollection et un index comme arguments et retourne un objet Page.
1. Créez un objet PngDevice en utilisant la fonction `png_device_create`, qui ne prend aucun argument. Cet objet peut convertir les pages PDF en images PNG avec des paramètres par défaut.
1. Enregistrez la page souhaitée du document en tant qu'image PNG en utilisant la fonction `png_device_save_page_to_file`, qui prend un objet PngDevice, un objet Page et un nom de fichier comme arguments.
1. Fermez les poignées des objets PngDevice et Document en utilisant la fonction close_handle, qui prend un objet comme argument et libère ses ressources.

```python

from AsposePdfPython import *

doc = document_open("blank_pdf_document.pdf")
pages = document_get_pages(doc)
page = page_collection_get_page(pages,1)

pngDevice = png_device_create()
png_device_save_page_to_file(pngDevice,page,"test.png")

```

### Python Convertir PDF en JPEG

1. Ouvrez un document PDF en utilisant la fonction `document_open`, qui prend le nom du fichier comme argument et retourne un objet Document.
1. Obtenez les pages du document en utilisant la fonction `document_get_pages`, qui prend un objet Document comme argument et retourne un objet PageCollection.
1. Obtenez la page souhaitée du document en utilisant la fonction `page_collection_get_page`, qui prend un objet PageCollection et un index comme arguments et retourne un objet Page.
1. Créez un objet Resolution en utilisant la fonction `resolution_create`, qui prend la valeur de résolution en points par pouce (DPI) comme argument.
1. Créez un objet JpegDevice en utilisant la fonction `jpeg_device_create_from_width_height_resolution`, qui prend les valeurs de largeur, hauteur et résolution comme arguments. Cet objet peut convertir des pages PDF en images JPEG avec les paramètres spécifiés.

1. Enregistrez la page souhaitée du document en tant qu'image JPEG en utilisant la fonction `jpeg_device_save_page_to_file`, qui prend un objet JpegDevice, un objet Page et un nom de fichier comme arguments.
1. Fermez les poignées des objets JpegDevice et Document en utilisant la fonction `close_handle`, qui prend un objet comme argument et libère ses ressources.

```python

    from AsposePdfPython import *

    doc = document_open("blank_pdf_document.pdf")
    pages = document_get_pages(doc)
    page = page_collection_get_page(pages,1)

    res = resolution_create(300)
    jpegDevice = jpeg_device_create_from_width_height_resolution(1239,1754,res)
    jpeg_device_save_page_to_file(jpegDevice,page,"test.jpeg")
```