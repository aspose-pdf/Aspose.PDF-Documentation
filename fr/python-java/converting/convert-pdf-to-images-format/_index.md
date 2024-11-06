---
title: Convertir un PDF en Différents Formats d'Image en Python
linktitle: Convertir un PDF en Images
type: docs
weight: 70
url: fr/python-java/convert-pdf-to-images-format/
lastmod: "2023-04-06"
description: Ce sujet vous montre comment utiliser Aspose.PDF pour Python afin de convertir un PDF en divers formats d'images, par exemple TIFF, BMP, EMF, JPEG, PNG, GIF, SVG avec quelques lignes de code.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## Vue d'ensemble

Cet article explique comment convertir un PDF en différents formats d'image en utilisant Python. Il couvre les sujets suivants.

_Format d'Image_: **TIFF**
- [Python PDF en TIFF](#python-pdf-to-tiff)
- [Python Convertir PDF en TIFF](#python-pdf-to-tiff)
- [Python Convertir des Pages Particulières ou Uniques de PDF en TIFF](#python-pdf-to-tiff-pages)


_Format d'Image_: **BMP**
- [Python PDF en BMP](#python-pdf-to-bmp)
- [Python Convertir PDF en BMP](#python-pdf-to-bmp)
- [Convertisseur PDF en BMP Python](#python-pdf-to-bmp)

_Format d'Image_: **EMF**
- [Python PDF en EMF](#python-pdf-to-emf)

- [Python Convertir PDF en EMF](#python-pdf-to-emf)
- [Python PDF to EMF Converter](#python-pdf-to-emf)

_Format d'image_: **JPG**
- [Python PDF en JPG](#python-pdf-to-jpg)
- [Python Convertir PDF en JPG](#python-pdf-to-jpg)
- [Python PDF en Convertisseur JPG](#python-pdf-to-jpg)

_Format d'image_: **PNG**
- [Python PDF en PNG](#python-pdf-to-png)
- [Python Convertir PDF en PNG](#python-pdf-to-png)
- [Python PDF en Convertisseur PNG](#python-pdf-to-png)

_Format d'image_: **GIF**
- [Python PDF en GIF](#python-pdf-to-gif)
- [Python Convertir PDF en GIF](#python-pdf-to-gif)
- [Python PDF en Convertisseur GIF](#python-pdf-to-gif)

_Format d'image_: **SVG**
- [Python PDF en SVG](#python-pdf-to-svg)
- [Python Convertir PDF en SVG](#python-pdf-to-svg)
- [Python PDF en Convertisseur SVG](#python-pdf-to-svg)

## Python Convertir PDF en Image

**Aspose.PDF pour Python** utilise plusieurs approches pour convertir PDF en image.
 Généralement parlant, nous utilisons deux approches : la conversion en utilisant l'approche Device et la conversion en utilisant SaveOption. Cette section vous montrera comment convertir des documents PDF en formats d'image tels que BMP, JPEG, GIF, PNG, EMF, TIFF, et SVG en utilisant l'une de ces approches.

Il y a plusieurs classes dans la bibliothèque qui vous permettent d'utiliser un dispositif virtuel pour transformer des images. DocumentDevice est orienté pour la conversion de l'ensemble du document, mais ImageDevice - pour une page particulière.

## Convertir un PDF en utilisant la classe DocumentDevice

**Aspose.PDF pour Python** rend possible la conversion des pages PDF en images TIFF.

La classe [TiffDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/tiffdevice/) (basée sur DocumentDevice) vous permet de convertir des pages PDF en images TIFF. Cette classe fournit une méthode nommée [`Process`](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/tiffdevice/#methods) qui vous permet de convertir toutes les pages d'un fichier PDF en une seule image TIFF.

{{% alert color="success" %}}

**Essayez de convertir un PDF en TIFF en ligne**
Aspose.PDF for Python via .NET vous présente l'application gratuite en ligne ["PDF to TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff), où vous pouvez essayer d'explorer la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF conversion PDF to TIFF with Free App](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

### Convertir les pages PDF en une image TIFF

Aspose.PDF for Python explique comment convertir toutes les pages d'un fichier PDF en une seule image TIFF :

<a name="csharp-pdf-to-tiff"><strong>Étapes : Convertir PDF en TIFF en Python</strong></a>

1. Créez un objet de la classe [Document](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/).
2. Créez des objets [TiffSettings](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/tiffsettings/) et [TiffDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/tiffdevice/)

3. Appelez la méthode [TiffDevice.Process()](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/tiffdevice/#methods) pour convertir le document PDF en TIFF.  
4. Pour définir les propriétés du fichier de sortie, utilisez la classe [TiffSettings](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/tiffsettings/).

Le code suivant montre comment convertir toutes les pages PDF en une seule image TIFF.

```python
from asposepdf import Api, Device

# initier la licence
documentName = "testdata/license/Aspose.PDF.PythonviaJava.lic"
licenseObject = Api.License()
licenseObject.setLicense(documentName)

# Ouvrir le document PDF
DIR_INPUT = "testdata/"
DIR_OUTPUT = "testout/"
input_pdf = DIR_INPUT + "source.pdf"
output_image = DIR_OUTPUT + "image.tiff"
# Ouvrir le document PDF
document = Api.Document(input_pdf)
# Créer un objet Resolution
resolution = Device.Resolution(300)

# Créer un objet TiffSettings
tiffSettings = Device.TiffSettings()
tiffSettings._CompressionType = Device.CompressionType.LZW
tiffSettings._ColorDepth = Device.ColorDepth.Default
tiffSettings._Skip_blank_pages = False

# Créer un périphérique TIFF
tiffDevice = Device.TiffDevice(resolution, tiffSettings)

# Convertir une page particulière et enregistrer l'image dans le flux
tiffDevice.process(document, output_image)
```


## Convertir un PDF en utilisant la classe ImageDevice

`ImageDevice` est l'ancêtre de `BmpDevice`, `JpegDevice`, `GifDevice`, `PngDevice` et `EmfDevice`.

- La classe [BmpDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/bmpdevice/) vous permet de convertir des pages PDF en images <abbr title="Bitmap Image File">BMP</abbr>.
- La classe [EmfDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/emfdevice/) vous permet de convertir des pages PDF en images <abbr title="Enhanced Meta File">EMF</abbr>.
- La classe [JpegDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/jpegdevice/) vous permet de convertir des pages PDF en images JPEG.
- La classe [PngDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/pngdevice/) vous permet de convertir des pages PDF en images <abbr title="Portable Network Graphics">PNG</abbr>.

- La classe [GifDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/gifdevice/) vous permet de convertir des pages PDF en images <abbr title="Graphics Interchange Format">GIF</abbr>.

Prenons un regard sur comment convertir une page PDF en image.

La classe [BmpDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/) fournit une méthode nommée [Process](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/#methods) qui vous permet de convertir une page particulière du fichier PDF au format d'image BMP. Les autres classes ont la même méthode. Donc, si nous avons besoin de convertir une page PDF en image, nous devons simplement instancier la classe requise.

Les étapes suivantes et le fragment de code en Python montrent cette possibilité

 - [Convertir PDF en BMP en Python](#python-pdf-to-image)
 - [Convertir PDF en EMF en Python](#python-pdf-to-image)
 - [Convertir PDF en JPG en Python](#python-pdf-to-image)
 - [Convertir PDF en PNG en Python](#python-pdf-to-image)
 - [Convertir PDF en GIF en Python](#python-pdf-to-image)

<a name="csharp-pdf-to-image"><strong>Étapes : PDF vers Image (BMP, EMF, JPG, PNG, GIF) en Python</strong></a>

1. Chargez le fichier PDF en utilisant la classe [Document](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/).
2. Créez une instance de sous-classe de [ImageDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/imagedevice/) c'est-à-dire.
   * [BmpDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/bmpdevice/) (pour convertir PDF en BMP)
   * [EmfDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/emfdevice/) (pour convertir PDF en Emf)
   * [JpegDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/jpegdevice/) (pour convertir PDF en JPG)
   * [PngDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/pngdevice/) (pour convertir PDF en PNG)
   * [GifDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/gifdevice/) (pour convertir PDF en GIF)
3. Appelez la méthode [ImageDevice.Process()](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/imagedevice/#methods) pour effectuer la conversion PDF en image.

### Convertir PDF en BMP

```python
from asposepdf import Api, Device

DIR_INPUT = "testdata/"
DIR_OUTPUT = "testout/"

input_pdf = DIR_INPUT + "source.pdf"
output_pdf = DIR_OUTPUT + "image"
# Ouvrir le document PDF
document = Api.Document(input_pdf)

# Créer un objet Résolution
resolution = Device.Resolution(300)
device = Device.BmpDevice(resolution)

for i in range(0, document.getPages.size):
    # Créer un nom de fichier pour l'enregistrement
    imageFileName = output_pdf + "_page_" + str(i + 1) + "_out.bmp"
    # Convertir une page particulière et enregistrer l'image dans le fichier
    device.process(document.getPages.getPage(i + 1), outputFileName=imageFileName)
```


### Convertir PDF en EMF

```python

from asposepdf import Api, Device

DIR_INPUT = "../../testdata/"
DIR_OUTPUT = "../../testout/"

input_pdf = DIR_INPUT + "source.pdf"
output_pdf = DIR_OUTPUT + "image"
# Ouvrir le document PDF
document = Api.Document(input_pdf)

# Créer un objet Résolution
resolution = Device.Resolution(300)
device = Device.EmfDevice(resolution)

for i in range(0, document.getPages.size):
    # Créer un nom de fichier pour enregistrer
    imageFileName = output_pdf + "_page_" + str(i + 1) + "_out.emf"
    # Convertir une page particulière et enregistrer l'image dans le fichier
    device.process(document.getPages.getPage(i + 1), outputFileName=imageFileName)
```  

### Convertir PDF en JPEG

```python

from asposepdf import Api, Device

DIR_INPUT = "../../testdata/"
DIR_OUTPUT = "../../testout/"

input_pdf = DIR_INPUT + "source.pdf"
output_pdf = DIR_OUTPUT + "image"
# Ouvrir le document PDF
document = Api.Document(input_pdf)

# Créer un objet Résolution
resolution = Device.Resolution(300)
device = Device.JpegDevice(resolution)

for i in range(0, document.getPages.size):
    # Créer un nom de fichier pour enregistrer
    imageFileName = output_pdf + "_page_" + str(i + 1) + "_out.jpeg"
    # Convertir une page particulière et enregistrer l'image dans le fichier
    device.process(document.getPages.getPage(i + 1), outputFileName=imageFileName)
``` 


### Convertir PDF en PNG

```python

from asposepdf import Api, Device

DIR_INPUT = "../../testdata/"
DIR_OUTPUT = "../../testout/"

input_pdf = DIR_INPUT + "source.pdf"
output_pdf = DIR_OUTPUT + "image"
# Ouvrir le document PDF
document = Api.Document(input_pdf)

# Créer un objet Resolution
resolution = Device.Resolution(300)
device = Device.PngDevice(resolution)

for i in range(0, document.getPages.size):
    # Créer un nom de fichier pour enregistrer
    imageFileName = output_pdf + "_page_" + str(i + 1) + "_out.png"
    # Convertir une page particulière et enregistrer l'image dans le fichier
    device.process(document.getPages.getPage(i + 1), outputFileName=imageFileName)
```

### Convertir PDF en GIF

```python

from asposepdf import Api, Device

DIR_INPUT = "../../testdata/"
DIR_OUTPUT = "../../testout/"

input_pdf = DIR_INPUT + "source.pdf"
output_pdf = DIR_OUTPUT + "image"
# Ouvrir le document PDF
document = Api.Document(input_pdf)

# Créer un objet Resolution
resolution = Device.Resolution(300)
device = Device.GifDevice(resolution)

for i in range(0, document.getPages.size):
    # Créer un nom de fichier pour enregistrer
    imageFileName = output_pdf + "_page_" + str(i + 1) + "_out.gif"
    # Convertir une page particulière et enregistrer l'image dans le fichier
    device.process(document.getPages.getPage(i + 1), outputFileName=imageFileName)
```


{{% alert color="success" %}}
**Essayez de convertir PDF en PNG en ligne**

À titre d'exemple de la façon dont nos applications gratuites fonctionnent, veuillez vérifier la fonctionnalité suivante.

Aspose.PDF pour Python vous présente une application en ligne gratuite ["PDF en PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png), où vous pouvez essayer d'examiner la fonctionnalité et la qualité de son fonctionnement.

[![Comment convertir un PDF en PNG en utilisant l'application gratuite](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## Convertir PDF en utilisant la classe SaveOptions

Cette partie de l'article vous montre comment convertir un PDF en <abbr title="Scalable Vector Graphics">SVG</abbr> en utilisant Python et la classe SaveOptions.

{{% alert color="success" %}}
**Essayez de convertir PDF en SVG en ligne**

Aspose.PDF pour Python via .NET vous présente une application en ligne gratuite ["PDF en SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg), où vous pouvez essayer d'examiner la fonctionnalité et la qualité de son fonctionnement.

[![Conversion Aspose.PDF PDF en SVG avec l'application gratuite](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

**Scalable Vector Graphics (SVG)** est une famille de spécifications d'un format de fichier basé sur XML pour les graphiques vectoriels bidimensionnels, à la fois statiques et dynamiques (interactifs ou animés). La spécification SVG est une norme ouverte qui est en cours de développement par le World Wide Web Consortium (W3C) depuis 1999.

Les images SVG et leurs comportements sont définis dans des fichiers texte XML. Cela signifie qu'ils peuvent être recherchés, indexés, scriptés et, si nécessaire, compressés. En tant que fichiers XML, les images SVG peuvent être créées et éditées avec n'importe quel éditeur de texte, mais il est souvent plus pratique de les créer avec des programmes de dessin comme Inkscape.

Aspose.PDF pour Python prend en charge la fonctionnalité de conversion d'image SVG au format PDF et offre également la possibilité de convertir des fichiers PDF au format SVG.
 Pour répondre à cette exigence, la classe [SvgSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/svgsaveoptions/) a été introduite dans l'espace de noms Aspose.PDF. Instanciez un objet de SvgSaveOptions et passez-le en tant que deuxième argument à la méthode [Document.Save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

Le code suivant montre les étapes pour convertir un fichier PDF en format SVG avec Python.

<a name="csharp-pdf-to-svg"><strong>Étapes : Convertir un PDF en SVG en Python</strong></a>

1. Créez un objet de la classe [Document](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/).
2. Créez un objet [SvgSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/svgsaveoptions/) avec les paramètres nécessaires.
3. Appelez la méthode [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods) et passez-lui l'objet [SvgSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/svgsaveoptions/) pour convertir le document PDF en SVG.

### Convertir PDF en SVG

```python

from asposepdf import Api

documentName = "testdata/input.pdf"
doc = Api.Document(documentName, None)
documentOutName = "testout/out.svg"
doc.save(documentOutName, Api.SaveFormat.Svg)
```