---
title: Convertir un PDF en Différents Formats d'Image en Python
linktitle: Convertir PDF en Images
type: docs
weight: 70
url: fr/python-net/convert-pdf-to-images-format/
lastmod: "2022-12-23"
description: Ce sujet montre comment utiliser Aspose.PDF pour Python pour convertir un PDF en divers formats d'images, par exemple TIFF, BMP, EMF, JPEG, PNG, GIF, SVG avec quelques lignes de code.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## Vue d'ensemble

Cet article explique comment convertir un PDF en différents formats d'image en utilisant Python. Il couvre les sujets suivants.

_Format d'image_: **TIFF**
- [Python PDF en TIFF](#python-pdf-to-tiff)
- [Python Convertir PDF en TIFF](#python-pdf-to-tiff)
- [Python Convertir des Pages Uniques ou Particulières de PDF en TIFF](#python-pdf-to-tiff-pages)

_Format d'image_: **BMP**
- [Python PDF en BMP](#python-pdf-to-bmp)
- [Python Convertir PDF en BMP](#python-pdf-to-bmp)
- [Convertisseur Python PDF en BMP](#python-pdf-to-bmp)

_Format d'image_: **EMF**
- [Python PDF en EMF](#python-pdf-to-emf)
- [Python Convertir PDF en EMF](#python-pdf-to-emf)
- [Python PDF to EMF Converter](#python-pdf-to-emf)

_Format d'image_: **JPG**
- [Python PDF vers JPG](#python-pdf-to-jpg)
- [Python Convertir PDF en JPG](#python-pdf-to-jpg)
- [Python Convertisseur PDF en JPG](#python-pdf-to-jpg)

_Format d'image_: **PNG**
- [Python PDF vers PNG](#python-pdf-to-png)
- [Python Convertir PDF en PNG](#python-pdf-to-png)
- [Python Convertisseur PDF en PNG](#python-pdf-to-png)

_Format d'image_: **GIF**
- [Python PDF vers GIF](#python-pdf-to-gif)
- [Python Convertir PDF en GIF](#python-pdf-to-gif)
- [Python Convertisseur PDF en GIF](#python-pdf-to-gif)

_Format d'image_: **SVG**
- [Python PDF vers SVG](#python-pdf-to-svg)
- [Python Convertir PDF en SVG](#python-pdf-to-svg)
- [Python Convertisseur PDF en SVG](#python-pdf-to-svg)

## Python Convertir PDF en Image

**Aspose.PDF pour Python** utilise plusieurs approches pour convertir PDF en image.
 Généralement parlant, nous utilisons deux approches : la conversion en utilisant l'approche Device et la conversion en utilisant SaveOption. Cette section vous montrera comment convertir des documents PDF en formats d'image tels que BMP, JPEG, GIF, PNG, EMF, TIFF et SVG en utilisant l'une de ces approches.

Il existe plusieurs classes dans la bibliothèque qui vous permettent d'utiliser un dispositif virtuel pour transformer des images. DocumentDevice est orienté pour la conversion de l'ensemble du document, mais ImageDevice - pour une page particulière.

## Convertir un PDF en utilisant la classe DocumentDevice

**Aspose.PDF pour Python** rend possible la conversion de Pages PDF en images TIFF.

La classe [TiffDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/) (basée sur DocumentDevice) vous permet de convertir des pages PDF en images TIFF. Cette classe fournit une méthode nommée [process](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/#methods) qui vous permet de convertir toutes les pages d'un fichier PDF en une seule image TIFF.

{{% alert color="success" %}}

**Essayez de convertir un PDF en TIFF en ligne**
Aspose.PDF pour Python via .NET vous présente l'application gratuite en ligne ["PDF to TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff), où vous pouvez essayer d'explorer la fonctionnalité et la qualité de son fonctionnement.

[![Conversion Aspose.PDF PDF en TIFF avec l'application gratuite](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

### Convertir les pages PDF en une image TIFF

Aspose.PDF pour Python explique comment convertir toutes les pages d'un fichier PDF en une seule image TIFF :

<a name="csharp-pdf-to-tiff"><strong>Étapes : Convertir PDF en TIFF en Python</strong></a>

1. Créez un objet de la classe [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
2. Créez des objets [TiffSettings](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffsettings/) et [TiffDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/).

3. Appelez la méthode [process](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/#methods) pour convertir le document PDF en TIFF.
4. Pour définir les propriétés du fichier de sortie, utilisez la classe [TiffSettings](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffsettings/).

Le snippet de code suivant montre comment convertir toutes les pages PDF en une seule image TIFF.

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_tiff.tiff"
    # Ouvrir le document PDF
    document = ap.Document(input_pdf)

    # Créer un objet Resolution
    resolution = ap.devices.Resolution(300)

    # Créer un objet TiffSettings
    tiffSettings = ap.devices.TiffSettings()
    tiffSettings.compression = ap.devices.CompressionType.LZW
    tiffSettings.depth = ap.devices.ColorDepth.DEFAULT
    tiffSettings.skip_blank_pages = False

    # Créer un dispositif TIFF
    tiffDevice = ap.devices.TiffDevice(resolution, tiffSettings)

    # Convertir une page particulière et enregistrer l'image dans le flux
    tiffDevice.process(document, output_pdf)
```


## Convertir un PDF en utilisant la classe ImageDevice

`ImageDevice` est l'ancêtre de `BmpDevice`, `JpegDevice`, `GifDevice`, `PngDevice` et `EmfDevice`.

- La classe [BmpDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/) vous permet de convertir des pages PDF en images <abbr title="Bitmap Image File">BMP</abbr>.
- La classe [EmfDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/emfdevice/) vous permet de convertir des pages PDF en images <abbr title="Enhanced Meta File">EMF</abbr>.
- La classe [JpegDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/jpegdevice/) vous permet de convertir des pages PDF en images JPEG.
- La classe [PngDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/pngdevice/) vous permet de convertir des pages PDF en images <abbr title="Portable Network Graphics">PNG</abbr>.

- La classe [GifDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/gifdevice/) vous permet de convertir des pages PDF en images <abbr title="Graphics Interchange Format">GIF</abbr>.

Prenons un moment pour examiner comment convertir une page PDF en image.

La classe [BmpDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/) fournit une méthode nommée [process](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/#methods) qui vous permet de convertir une page particulière du fichier PDF au format image BMP. Les autres classes ont la même méthode. Ainsi, si nous avons besoin de convertir une page PDF en image, il suffit d'instancier la classe requise.

<a name="csharp-pdf-to-bmp"></a>
<a name="csharp-pdf-to-emf"></a>
<a name="csharp-pdf-to-jpg"></a>
<a name="csharp-pdf-to-png"></a>
<a name="csharp-pdf-to-gif"></a>
    
Les étapes suivantes et l'extrait de code en Python montrent cette possibilité
 
 - [Convertir un PDF en BMP en Python](#python-pdf-to-image)
 - [Convertir un PDF en EMF en Python](#python-pdf-to-image)
 - [Convertir un PDF en JPG en Python](#python-pdf-to-image)
 - [Convertir un PDF en PNG en Python](#python-pdf-to-image)
 - [Convertir un PDF en GIF en Python](#python-pdf-to-image)


<a name="csharp-pdf-to-image"><strong>Étapes : PDF en Image (BMP, EMF, JPG, PNG, GIF) en Python</strong></a>

1. Chargez le fichier PDF en utilisant la classe [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
2. Créez une instance de la sous-classe de [ImageDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/imagedevice/) c'est-à-dire
   * [BmpDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/) (pour convertir PDF en BMP)
   * [EmfDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/emfdevice/) (pour convertir PDF en Emf)
   * [JpegDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/jpegdevice/) (pour convertir PDF en JPG)
   * [PngDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/pngdevice/) (pour convertir PDF en PNG)
   * [GifDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/gifdevice/) (pour convertir PDF en GIF)
3. Appelez la méthode [ImageDevice.Process()](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/imagedevice/#methods) pour effectuer la conversion de PDF en Image.

### Convertir PDF en BMP

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "many_pages.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_bmp"
    # Ouvrir le document PDF
    document = ap.Document(input_pdf)

    # Créer un objet Résolution
    resolution = ap.devices.Resolution(300)
    device = ap.devices.BmpDevice(resolution)

    for i in range(0, len(document.pages)):
        # Créer un fichier pour enregistrer
        imageStream = io.FileIO(
            output_pdf + "_page_" + str(i + 1) + "_out.bmp", 'x'
        )
        # Convertir une page particulière et enregistrer l'image dans le flux
        device.process(document.pages[i + 1], imageStream)
        imageStream.close()
```


### Convertir PDF en EMF

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_emf"
    # Ouvrir le document PDF
    document = ap.Document(input_pdf)

    # Créer un objet Résolution
    resolution = ap.devices.Resolution(300)
    device = ap.devices.EmfDevice(resolution)

    for i in range(0, len(document.pages)):
        # Créer un fichier pour enregistrer
        imageStream = io.FileIO(
            output_pdf + "_page_" + str(i + 1) + "_out.emf", 'x'
        )
        # Convertir une page particulière et enregistrer l'image dans le flux
        device.process(document.pages[i + 1], imageStream)
        imageStream.close()
```  

### Convertir PDF en JPEG

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "many_pages.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_jpeg"
    # Ouvrir le document PDF
    document = ap.Document(input_pdf)

    # Créer un objet Résolution
    resolution = ap.devices.Resolution(300)
    device = ap.devices.JpegDevice(resolution)

    for i in range(0, len(document.pages)):
        # Créer un fichier pour enregistrer
        imageStream = io.FileIO(
            output_pdf + "_page_" + str(i + 1) + "_out.jpeg", "x"
        )
        # Convertir une page particulière et enregistrer l'image dans le flux
        device.process(document.pages[i + 1], imageStream)
        imageStream.close()  
``` 


### Convertir PDF en PNG

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_png"
    # Ouvrir le document PDF
    document = ap.Document(input_pdf)

    # Créer un objet Resolution
    resolution = ap.devices.Resolution(300)
    device = ap.devices.PngDevice(resolution)

    for i in range(0, len(document.pages)):
        # Créer un fichier pour enregistrer
        imageStream = io.FileIO(
            output_pdf + "_page_" + str(i + 1) + "_out.png", 'x'
        )
        # Convertir une page particulière et enregistrer l'image dans le flux
        device.process(document.pages[i + 1], imageStream)
        imageStream.close()
``` 

### Convertir PDF en GIF

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "many_pages.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_gif"
    # Ouvrir le document PDF
    document = ap.Document(input_pdf)

    # Créer un objet Resolution
    resolution = ap.devices.Resolution(300)

    device = ap.devices.GifDevice(resolution)

    for i in range(0, len(document.pages)):
        # Créer un fichier pour enregistrer
        imageStream = io.FileIO(
            output_pdf + "_page_" + str(i + 1) + "_out.gif", 'x'
        )
        # Convertir une page particulière et enregistrer l'image dans le flux
        device.process(document.pages[i + 1], imageStream)
        # Fermer le flux
        imageStream.close()  
``` 


{{% alert color="success" %}}
**Essayez de convertir PDF en PNG en ligne**

À titre d'exemple de fonctionnement de nos applications gratuites, veuillez vérifier la fonctionnalité suivante.

Aspose.PDF pour Python vous présente l'application gratuite en ligne ["PDF to PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png), où vous pouvez essayer d'explorer la fonctionnalité et la qualité de son fonctionnement.

[![Comment convertir PDF en PNG en utilisant l'application gratuite](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## Convertir PDF en utilisant la classe SaveOptions

Cette partie de l'article vous montre comment convertir un PDF en <abbr title="Scalable Vector Graphics">SVG</abbr> en utilisant Python et la classe SaveOptions.

{{% alert color="success" %}}
**Essayez de convertir PDF en SVG en ligne**

Aspose.PDF pour Python via .NET vous présente l'application gratuite en ligne ["PDF to SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg), où vous pouvez essayer d'explorer la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion PDF en SVG avec l'application gratuite](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

**Scalable Vector Graphics (SVG)** est une famille de spécifications d'un format de fichier basé sur XML pour les graphiques vectoriels bidimensionnels, à la fois statiques et dynamiques (interactifs ou animés). La spécification SVG est une norme ouverte qui est en développement par le World Wide Web Consortium (W3C) depuis 1999.

Les images SVG et leurs comportements sont définis dans des fichiers texte XML. Cela signifie qu'ils peuvent être recherchés, indexés, scriptés et, si nécessaire, compressés. En tant que fichiers XML, les images SVG peuvent être créées et éditées avec n'importe quel éditeur de texte, mais il est souvent plus pratique de les créer avec des programmes de dessin tels qu'Inkscape.

Aspose.PDF pour Python prend en charge la fonctionnalité de conversion d'image SVG en format PDF et offre également la capacité de convertir des fichiers PDF en format SVG.
 Pour accomplir cette exigence, la classe [SvgSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/svgsaveoptions/) a été introduite dans l'espace de noms Aspose.PDF. Instanciez un objet SvgSaveOptions et passez-le comme deuxième argument à la méthode [Document.Save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

Le fragment de code suivant montre les étapes pour convertir un fichier PDF en format SVG avec Python.

<a name="csharp-pdf-to-svg"><strong>Étapes : Convertir un PDF en SVG en Python</strong></a>

1. Créez un objet de la classe [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
2. Créez un objet [SvgSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/svgsaveoptions/) avec les paramètres nécessaires.
3. Appelez la méthode [Document.Save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) et passez l'objet [SvgSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/svgsaveoptions/) pour convertir le document PDF en SVG.

### Convertir PDF en SVG

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_svg.svg"
    # Ouvrir le document PDF
    document = ap.Document(input_pdf)

    # Instancier un objet de SvgSaveOptions
    saveOptions = ap.SvgSaveOptions()

    # Ne pas compresser l'image SVG dans une archive Zip
    saveOptions.compress_output_to_zip_archive = False
    saveOptions.treat_target_file_name_as_directory = True

    # Enregistrer la sortie dans des fichiers SVG
    document.save(output_pdf, saveOptions)
```