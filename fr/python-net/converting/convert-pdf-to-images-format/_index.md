---
title: Convertir le PDF en formats d'image en Python
linktitle: Convertir le PDF en images
type: docs
weight: 70
url: /fr/python-net/convert-pdf-to-images-format/
lastmod: "2026-05-22"
description: Apprenez comment rendre les pages PDF en fichiers TIFF, BMP, EMF, JPEG, PNG, GIF et SVG avec Python et Aspose.PDF for Python via .NET.
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Convertissez les pages PDF en fichiers TIFF, PNG, JPEG, GIF, BMP, EMF et SVG en Python.
Abstract: Cet article explique comment convertir des fichiers PDF en formats d'image courants avec Aspose.PDF for Python via .NET. Il couvre l'exportation TIFF à l'échelle du document avec `TiffDevice`, la génération d'images raster page par page avec les sous‑classes de `ImageDevice` telles que `BmpDevice`, `JpegDevice`, `PngDevice`, `GifDevice` et `EmfDevice`, ainsi que l'exportation vectorielle en SVG avec `SvgSaveOptions`. Chaque section comprend les étapes principales et des exemples Python nécessaires pour enregistrer le contenu PDF sous forme de sortie image.
---

## Python Convertir le PDF en image

**Aspose.PDF for Python via .NET** prend en charge plusieurs méthodes pour convertir le contenu PDF en images. En pratique, la plupart des flux de travail utilisent l'une des deux options :

- l'approche Device pour le rendu des pages PDF en formats d'images raster
- l'approche SaveOptions pour l'exportation du contenu PDF vers SVG

Cet article montre comment convertir des fichiers PDF en TIFF, BMP, EMF, JPEG, PNG, GIF et SVG.

La bibliothèque comprend plusieurs classes de rendu. `DocumentDevice` est conçu pour la conversion de l'ensemble du document, tandis que `ImageDevice` cible des pages individuelles.

## Convertir le PDF en utilisant la classe DocumentDevice

Utiliser `DocumentDevice` lorsque vous souhaitez rendre le PDF complet en un seul fichier TIFF multipage.

Le [TiffDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/) la classe est basée sur `DocumentDevice` et fournit le [processus](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/#methods) méthode pour convertir toutes les pages d'un fichier PDF en une sortie TIFF unique.

{{% alert color="success" %}}
**Essayez de convertir le PDF en TIFF en ligne**

Aspose.PDF for Python via .NET vous présente une application en ligne ["PDF en TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff), où vous pouvez essayer d'examiner le fonctionnement et la qualité.

[![Conversion Aspose.PDF de PDF en TIFF avec l'application](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

### Convertir les pages PDF en une image TIFF

Aspose.PDF for Python via .NET peut rendre chaque page d'un fichier PDF en une image TIFF.

Étapes : Convertir le PDF en TIFF en Python

1. Chargez le PDF source avec le [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) classe.
1. Créer [TiffSettings](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffsettings/) et [TiffDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/) objets.
1. Configurez les options TIFF telles que la compression, la profondeur de couleur et la gestion des pages blanches.
1. Appeler le [process](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/#methods) méthode pour écrire le fichier TIFF.

Le fragment de code suivant montre comment convertir toutes les pages PDF en une seule image TIFF.

```python
import aspose.pdf as ap
from io import FileIO
from os import path
import sys

def convert_PDF_to_TIFF(infile, outfile):
    document = ap.Document(infile)

    resolution = ap.devices.Resolution(300)
    tiffSettings = ap.devices.TiffSettings()
    tiffSettings.compression = ap.devices.CompressionType.LZW
    tiffSettings.depth = ap.devices.ColorDepth.DEFAULT
    tiffSettings.skip_blank_pages = False

    tiffDevice = ap.devices.TiffDevice(resolution, tiffSettings)
    tiffDevice.process(document, f"{outfile}.tiff")

    print(infile + " converted into " + outfile)
```

## Convertir le PDF en utilisant la classe ImageDevice

Utiliser `ImageDevice` Lorsque vous avez besoin d’une sortie page par page au format d’image raster.

`ImageDevice` est la classe de base pour `BmpDevice`, `JpegDevice`, `GifDevice`, `PngDevice`, et `EmfDevice`.

- Le [BmpDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/) class vous permet de convertir les pages PDF en images BMP.
- Le [EmfDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/emfdevice/) La classe vous permet de convertir des pages PDF en images EMF.
- Le [JpegDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/jpegdevice/) La classe vous permet de convertir les pages PDF en images JPEG.
- Le [PngDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/pngdevice/) La classe vous permet de convertir des pages PDF en images PNG.
- Le [GifDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/gifdevice/) La classe vous permet de convertir des pages PDF en images GIF.

Le flux de travail est le même pour chaque format : charger le document, créer le dispositif approprié, puis traiter la page requise.

[BmpDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/) expose le [process](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/#methods) méthode pour rendre une page spécifique en BMP. Les autres classes d'appareil image suivent le même modèle, vous pouvez donc changer de format en modifiant la classe d'appareil.

Les liens et exemples de code suivants montrent comment rendre les pages PDF aux formats d'image courants :

- [Convertir PDF en BMP en Python](#convert-pdf-to-bmp)
- [Convertir PDF en EMF en Python](#convert-pdf-to-emf)
- [Convertir PDF en JPEG avec Python](#convert-pdf-to-jpeg)
- [Convertir un PDF en PNG en Python](#convert-pdf-to-png)
- [Convertir le PDF en GIF en Python](#convert-pdf-to-gif)

Étapes : PDF en image (BMP, EMF, JPG, PNG, GIF) en Python

1. Chargez le fichier PDF avec le [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) classe.
1. Créer une instance de ce qui est requis [ImageDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/imagedevice/) sous-classe:
    - [BmpDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/) (pour convertir le PDF en BMP)
    - [EmfDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/emfdevice/) (pour convertir PDF en EMF)
    - [JpegDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/jpegdevice/) (pour convertir le PDF en JPG)
    - [PngDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/pngdevice/) (pour convertir le PDF en PNG)
    - [GifDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/gifdevice/) (pour convertir PDF en GIF)
1. Parcourez les pages que vous voulez exporter.
1. Appeler le [ImageDevice.process()](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/imagedevice/#methods) méthode pour enregistrer chaque page en tant qu'image.

### Convertir PDF en BMP

```python
import aspose.pdf as ap
from io import FileIO
from os import path
import sys

def convert_PDF_to_BMP(infile, outfile):
    document = ap.Document(infile)
    resolution = ap.devices.Resolution(300)
    device = ap.devices.BmpDevice(resolution)
    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(outfile + str(page_count) + "_out.bmp", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

    print(infile + " converted into " + outfile)
```

### Convertir PDF en EMF

```python
import aspose.pdf as ap
from io import FileIO
from os import path
import sys

def convert_PDF_to_EMF(infile, outfile):
    document = ap.Document(infile)
    resolution = ap.devices.Resolution(300)
    device = ap.devices.EmfDevice(resolution)
    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(outfile + str(page_count) + "_out.emf", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

    print(infile + " converted into " + outfile)
```  

### Convertir le PDF en JPEG

```python
import aspose.pdf as ap
from io import FileIO
from os import path
import sys

def convert_PDF_to_JPEG(infile, outfile):
    document = ap.Document(infile)
    resolution = ap.devices.Resolution(300)
    device = ap.devices.JpegDevice(resolution)
    page_count = 1

    while page_count <= len(document.pages):
        image_stream = FileIO(outfile + str(page_count) + "_out.jpeg", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

    print(infile + " converted into " + outfile)
```

### Convertir le PDF en PNG

```python
import aspose.pdf as ap
from io import FileIO
from os import path
import sys

def convert_PDF_to_PNG(infile, outfile):
    document = ap.Document(infile)
    resolution = ap.devices.Resolution(300)

    device = ap.devices.PngDevice(resolution)
    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(outfile + str(page_count) + "_out.png", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1
```

### Convertir le PDF en PNG avec la police par défaut

```python
import aspose.pdf as ap
from io import FileIO
from os import path
import sys

def convert_PDF_to_PNG_with_default_font(infile, outfile):
    document = ap.Document(infile)
    resolution = ap.devices.Resolution(300)

    rendering_options = ap.RenderingOptions()
    rendering_options.default_font_name = "Arial"

    device = ap.devices.PngDevice(resolution)
    device.rendering_options = rendering_options

    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(outfile + str(page_count) + "_out.png", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1
```

### Convertir PDF en GIF

```python
import aspose.pdf as ap
from io import FileIO
from os import path
import sys

def convert_PDF_to_GIF(infile, outfile):
    document = ap.Document(infile)
    resolution = ap.devices.Resolution(300)
    device = ap.devices.GifDevice(resolution)
    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(outfile + str(page_count) + "_out.gif", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Essayez de convertir PDF en PNG en ligne**

À titre d'exemple de la façon dont nos applications fonctionnent, veuillez consulter la fonctionnalité suivante.

Aspose.PDF for Python vous présente une application en ligne ["PDF en PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png), où vous pouvez essayer d'examiner le fonctionnement et la qualité.

[![Comment convertir PDF en PNG à l'aide de l'App](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## Convertir le PDF en utilisant la classe SaveOptions

Utiliser `SaveOptions` Lorsque vous voulez exporter le contenu PDF en SVG.

{{% alert color="success" %}}
**Essayez de convertir PDF en SVG en ligne**

Aspose.PDF for Python via .NET vous présente une application en ligne ["PDF en SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg), où vous pouvez essayer d'examiner le fonctionnement et la qualité.

[![Aspose.PDF Conversion PDF en SVG avec App](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

**Scalable Vector Graphics (SVG)** est un format basé sur XML pour les graphiques vectoriels bidimensionnels. Comme SVG reste vectoriel, il est utile lorsque vous avez besoin d’une sortie évolutive pour le web, l’interface utilisateur ou les flux de conception.

Les fichiers SVG sont basés sur du texte, recherchables et faciles à post-traiter dans d’autres outils.

Aspose.PDF for Python via .NET peut à la fois convertir SVG en PDF et exporter des pages PDF en SVG. Pour la conversion PDF vers SVG, créez un [SvgSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/svgsaveoptions/) objet et le passer à [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) méthode.

Les étapes suivantes montrent comment convertir un fichier PDF en SVG avec Python.

Étapes : Convertir le PDF en SVG en Python

1. Chargez le PDF source à l'aide de [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) classe.
1. Créer un [SvgSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/svgsaveoptions/) objet et configurez les options requises.
1. Appeler le [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) méthode avec le `SvgSaveOptions` instance pour écrire la sortie SVG.

### Convertir le PDF en SVG

```python
import aspose.pdf as ap
from io import FileIO
from os import path
import sys

def convert_PDF_to_SVG(infile, outfile):
    document = ap.Document(infile)

    save_options = ap.SvgSaveOptions()
    save_options.compress_output_to_zip_archive = False
    save_options.treat_target_file_name_as_directory = True

    document.save(f"{outfile}.svg", save_options)
```

## Conversions associées

- [Convertir les formats d'image en PDF](/pdf/fr/python-net/convert-images-format-to-pdf/) lorsque vous devez recréer des PDF à partir de JPG, PNG, TIFF, SVG ou d'autres sources d'images.
- [Convertir le PDF en HTML](/pdf/fr/python-net/convert-pdf-to-html/) pour une sortie adaptée aux navigateurs au lieu d'images matricielles.
- [Convertir le PDF en d'autres formats](/pdf/fr/python-net/convert-pdf-to-other-files/) pour les flux de travail d'exportation EPUB, Markdown, texte et XPS.
