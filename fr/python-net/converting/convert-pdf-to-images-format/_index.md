---
title: Convertir PDF en différents formats d'image en Python
linktitle: Convertir PDF en images
type: docs
weight: 70
url: /fr/python-net/convert-pdf-to-images-format/
lastmod: "2025-09-27"
description: Découvrez comment convertir les pages PDF en images telles que PNG, JPEG ou TIFF en utilisant Aspose.PDF en Python via .NET.
sitemap: 
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Comment convertir PDF en formats d'image en Python
Abstract: Cet article fournit un guide complet sur la conversion de fichiers PDF en divers formats d'image à l'aide de Python, en exploitant spécifiquement la bibliothèque Aspose.PDF pour Python. Le document décrit les méthodes de conversion des PDF vers des formats d'image incluant TIFF, BMP, EMF, JPG, PNG, GIF et SVG. Deux approches principales de conversion sont présentées – l'utilisation de l'approche Device et de SaveOption. L'approche Device consiste à utiliser des classes telles que `DocumentDevice` et `ImageDevice` pour la conversion du document entier ou d'une page spécifique. Des étapes détaillées et des exemples de code Python sont fournis pour convertir les pages PDF en différents formats tels que le TIFF à l'aide de `TiffDevice`, et le BMP, EMF, JPEG, PNG et GIF en utilisant les classes de dispositif respectives (`BmpDevice`, `EmfDevice`, `JpegDevice`, `PngDevice`, `GifDevice`). Pour la conversion SVG, la classe `SvgSaveOptions` est présentée. L'article met également en avant des outils en ligne pour essayer ces conversions.
---

## Convertir PDF en image avec Python

**Aspose.PDF for Python** utilise plusieurs approches pour convertir PDF en image. En général, nous employons deux approches : la conversion à l'aide de l'approche Device et la conversion à l'aide de SaveOption. Cette section vous montrera comment convertir des documents PDF en formats d'image tels que BMP, JPEG, GIF, PNG, EMF, TIFF et SVG en utilisant l'une de ces approches.

Il existe plusieurs classes dans la bibliothèque qui vous permettent d'utiliser un dispositif virtuel pour transformer des images. DocumentDevice est destiné à la conversion du document entier, tandis qu'ImageDevice - pour une page particulière.

## Convertir PDF en utilisant la classe DocumentDevice

**Aspose.PDF for Python** permet de convertir des pages PDF en images TIFF.

La classe [TiffDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/) (basée sur DocumentDevice) vous permet de convertir des pages PDF en images TIFF. Cette classe fournit une méthode nommée [process](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/#methods) qui permet de convertir toutes les pages d'un fichier PDF en une seule image TIFF.

{{% alert color="success" %}}
**Essayez de convertir PDF en TIFF en ligne**

Aspose.PDF for Python via .NET vous propose une application en ligne gratuite ["PDF en TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff), où vous pouvez essayer d'examiner la fonctionnalité et la qualité du résultat.

[![Conversion Aspose.PDF PDF en TIFF avec application gratuite](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

### Convertir les pages PDF en une seule image TIFF

Aspose.PDF for Python explique comment convertir toutes les pages d'un fichier PDF en une seule image TIFF :

Étapes : Convertir PDF en TIFF avec Python

1. Créez un objet de la classe [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Créez les objets [TiffSettings](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffsettings/) et [TiffDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/).
1. Appelez la méthode [process](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/#methods) pour convertir le document PDF en TIFF.
1. Pour définir les propriétés du fichier de sortie, utilisez la classe [TiffSettings](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffsettings/).

Le fragment de code suivant montre comment convertir toutes les pages PDF en une seule image TIFF.

```python

    from os import path
    import aspose.pdf as apdf
    from io import FileIO

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)

    resolution = apdf.devices.Resolution(300)
    tiffSettings = apdf.devices.TiffSettings()
    tiffSettings.compression = apdf.devices.CompressionType.LZW
    tiffSettings.depth = apdf.devices.ColorDepth.DEFAULT
    tiffSettings.skip_blank_pages = False

    tiffDevice = apdf.devices.TiffDevice(resolution, tiffSettings)
    tiffDevice.process(document, path_outfile)

    print(infile + " converted into " + outfile)
```

## Convertir PDF en utilisant la classe ImageDevice

`ImageDevice` est le parent de `BmpDevice`, `JpegDevice`, `GifDevice`, `PngDevice` et `EmfDevice`.

- La classe [BmpDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/) vous permet de convertir des pages PDF en images <abbr title="Bitmap Image File">BMP</abbr>.
- La classe [EmfDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/emfdevice/) vous permet de convertir des pages PDF en images <abbr title="Enhanced Meta File">EMF</abbr>.
- La classe [JpegDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/jpegdevice/) vous permet de convertir des pages PDF en images JPEG.
- La classe [PngDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/pngdevice/) vous permet de convertir des pages PDF en images <abbr title="Portable Network Graphics">PNG</abbr>.
- La classe [GifDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/gifdevice/) vous permet de convertir des pages PDF en images <abbr title="Graphics Interchange Format">GIF</abbr>.

Examinons comment convertir une page PDF en image.

La classe [BmpDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/) propose une méthode nommée [process](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/#methods) qui permet de convertir une page particulière du fichier PDF au format d'image BMP. Les autres classes possèdent la même méthode. Ainsi, si nous devons convertir une page PDF en image, il suffit d'instancier la classe requise.

Les étapes suivantes et le fragment de code en Python illustrent cette possibilité :

- [Convertir PDF en BMP avec Python](#python-pdf-to-image)
- [Convertir PDF en EMF avec Python](#python-pdf-to-image)
- [Convertir PDF en JPG avec Python](#python-pdf-to-image)
- [Convertir PDF en PNG avec Python](#python-pdf-to-image)
- [Convertir PDF en GIF avec Python](#python-pdf-to-image)

Étapes : PDF en image (BMP, EMF, JPG, PNG, GIF) avec Python

1. Chargez le fichier PDF en utilisant la classe [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Créez une instance d'une sous-classe de [ImageDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/imagedevice/) c’est‑à‑dire.
* [BmpDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/) (pour convertir PDF en BMP)
* [EmfDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/emfdevice/) (pour convertir PDF en Emf)
* [JpegDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/jpegdevice/) (pour convertir PDF en JPG)
* [PngDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/pngdevice/) (pour convertir PDF en PNG)
* [GifDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/gifdevice/) (pour convertir PDF en GIF)
1. Appelez la méthode [ImageDevice.process()](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/imagedevice/#methods) pour effectuer la conversion PDF en image.

### Convertir le PDF en BMP

```python

    from os import path
    import aspose.pdf as apdf
    from io import FileIO

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    resolution = apdf.devices.Resolution(300)
    device = apdf.devices.BmpDevice(resolution)
    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(path_outfile + str(page_count) + "_out.bmp", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

    print(infile + " converted into " + outfile)
```

### Convertir le PDF en EMF

```python

    from os import path
    import aspose.pdf as apdf
    from io import FileIO

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    resolution = apdf.devices.Resolution(300)
    device = apdf.devices.EmfDevice(resolution)
    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(path_outfile + str(page_count) + "_out.emf", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

    print(infile + " converted into " + outfile)
```  

### Convertir le PDF en JPEG

```python

    from os import path
    import aspose.pdf as apdf
    from io import FileIO

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    resolution = apdf.devices.Resolution(300)
    device = apdf.devices.JpegDevice(resolution)
    page_count = 1

    while page_count <= len(document.pages):
        image_stream = FileIO(path_outfile + str(page_count) + "_out.jpeg", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

    print(infile + " converted into " + outfile)
```


### Convertir le PDF en PNG

```python

    from os import path
    import aspose.pdf as apdf
    from io import FileIO

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    resolution = apdf.devices.Resolution(300)

    device = apdf.devices.PngDevice(resolution)
    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(path_outfile + str(page_count) + "_out.png", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

    print(infile + " converted into " + outfile)
```

### Convertir le PDF en PNG avec la police par défaut

```python

    from os import path
    import aspose.pdf as ap
    from io import FileIO


    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    resolution = ap.devices.Resolution(300)

    rendering_options = ap.RenderingOptions()
    rendering_options.default_font_name = "Arial"

    device = ap.devices.PngDevice(resolution)
    device.rendering_options = rendering_options

    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(path_outfile + str(page_count) + "_out.png", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

    print(infile + " converted into " + outfile)
```

### Convertir le PDF en GIF

```python

    from os import path
    import aspose.pdf as apdf
    from io import FileIO

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    resolution = apdf.devices.Resolution(300)
    device = apdf.devices.GifDevice(resolution)
    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(path_outfile + str(page_count) + "_out.gif", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Essayez de convertir le PDF en PNG en ligne**

À titre d'exemple du fonctionnement de nos applications gratuites, veuillez consulter la fonctionnalité suivante.

Aspose.PDF for Python vous présente l'application gratuite en ligne [\"PDF to PNG\"](https://products.aspose.app/pdf/conversion/pdf-to-png), où vous pouvez essayer d'examiner les fonctionnalités et la qualité de son fonctionnement.

[![Comment convertir un PDF en PNG avec l'application gratuite](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## Convertir le PDF en utilisant la classe SaveOptions

Cette partie de l'article vous montre comment convertir le PDF en <abbr title="Scalable Vector Graphics">SVG</abbr> en utilisant Python et la classe SaveOptions.

{{% alert color="success" %}}
**Essayez de convertir le PDF en SVG en ligne**

Aspose.PDF for Python via .NET vous présente l'application gratuite en ligne [\"PDF to SVG\"](https://products.aspose.app/pdf/conversion/pdf-to-svg), où vous pouvez essayer d'examiner les fonctionnalités et la qualité de son fonctionnement.

[![Conversion Aspose.PDF PDF en SVG avec l'application gratuite](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

**Scalable Vector Graphics (SVG)** est une famille de spécifications d'un format de fichier XML destiné aux graphiques vectoriels bidimensionnels, à la fois statiques et dynamiques (interactifs ou animés). La spécification SVG est une norme ouverte qui est développée par le World Wide Web Consortium (W3C) depuis 1999.

Les images SVG et leurs comportements sont définis dans des fichiers texte XML. Cela signifie qu'elles peuvent être recherchées, indexées, scriptées et, si nécessaire, compressées. En tant que fichiers XML, les images SVG peuvent être créées et modifiées avec n'importe quel éditeur de texte, mais il est souvent plus pratique de les créer avec des programmes de dessin tels qu'Inkscape.

Aspose.PDF for Python prend en charge la fonctionnalité de conversion d'image SVG au format PDF et offre également la capacité de convertir des fichiers PDF au format SVG. Pour répondre à cette exigence, la classe [SvgSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/svgsaveoptions/) a été introduite dans l'espace de noms Aspose.PDF. Instanciez un objet SvgSaveOptions et transmettez‑le en tant que deuxième argument à la méthode [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

Le fragment de code suivant montre les étapes de conversion d'un fichier PDF au format SVG avec Python.

Étapes : Convertir le PDF en SVG avec Python

1. Créez un objet de la classe [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Créez l'objet [SvgSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/svgsaveoptions/) avec les paramètres nécessaires.
1. Appelez la méthode [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) et transmettez‑lui l'objet [SvgSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/svgsaveoptions/) pour convertir le document PDF en SVG.

### Convertir le PDF en SVG

```python

    from os import path
    import aspose.pdf as apdf
    from io import FileIO

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)

    save_options = apdf.SvgSaveOptions()
    save_options.compress_output_to_zip_archive = False
    save_options.treat_target_file_name_as_directory = True

    document.save(path_outfile, save_options)
    print(infile + " converted into " + outfile)
```

