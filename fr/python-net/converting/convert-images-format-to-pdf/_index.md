---
title: Convertir les formats d'image en PDF avec Python
linktitle: Convertir des images en PDF
type: docs
weight: 60
url: /fr/python-net/convert-images-format-to-pdf/
lastmod: "2026-05-22"
description: Apprenez à convertir BMP, CGM, DICOM, PNG, TIFF, EMF, SVG et d'autres formats d'image en PDF avec Python grâce à Aspose.PDF for Python via .NET.
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Comment convertir des images en PDF avec Python
Abstract: Cet article fournit un guide complet sur la conversion de divers formats d'image en PDF à l'aide de Python, en exploitant spécifiquement la bibliothèque Aspose.PDF pour Python via .NET. L'article couvre une gamme de formats d'image incluant BMP, CGM, DICOM, EMF, GIF, PNG, SVG et TIFF. Chaque section détaille les étapes nécessaires pour réaliser la conversion, en fournissant des extraits de code pour illustrer le processus. Par exemple, convertir un BMP en PDF implique la création d'un nouveau document PDF, la définition du placement de l'image, l'insertion de l'image et l'enregistrement du document. De même, pour des formats tels que CGM, DICOM et d'autres, des options de chargement spécifiques et des étapes de traitement sont décrites. L'article met également en avant les avantages d'utiliser Aspose.PDF pour de telles tâches, comme son support de différentes méthodes d'encodage et la capacité de traiter à la fois des images à une seule trame et des images à plusieurs trames.
---

## Conversions associées

- [Convertir le PDF en formats d\'image](/pdf/fr/python-net/convert-pdf-to-images-format/) lorsque vous avez besoin du flux de travail inverse.
- [Convertir le HTML en PDF](/pdf/fr/python-net/convert-html-to-pdf/) pour le contenu Web et les sources MHTML.
- [Convertir d'autres formats de fichier en PDF](/pdf/fr/python-net/convert-other-files-to-pdf/) pour EPUB, XPS, texte et d'autres entrées non-image.

## Conversions d'images Python en PDF

**Aspose.PDF for Python via .NET** permet de convertir différents formats d'images en fichiers PDF. Notre bibliothèque démontre des extraits de code pour convertir les formats d'image les plus populaires, tels que - BMP, CGM, DICOM, EMF, JPG, PNG, SVG et TIFF.

## Convertir BMP en PDF

Convertir des fichiers BMP en document PDF en utilisant la bibliothèque **Aspose.PDF for Python via .NET**.

<abbr title="Bitmap Image File">BMP</abbr> les images sont des fichiers ayant une extension. BMP représente des fichiers d'image bitmap qui sont utilisés pour stocker des images numériques bitmap. Ces images sont indépendantes de l'adaptateur graphique et sont également appelées format de fichier bitmap indépendant du dispositif (DIB).

Vous pouvez convertir des fichiers BMP en PDF avec l'API Aspose.PDF for Python via .NET. Par conséquent, vous pouvez suivre les étapes suivantes pour convertir des images BMP :

Étapes pour convertir BMP en PDF en Python :

1. Créer un document PDF vide.
1. Créez la page dont vous avez besoin, par exemple, nous avons créé le format A4, mais vous pouvez spécifier votre propre format.
1. Place l'image (from infile) à l'intérieur de la page en utilisant le rectangle défini.
1. Enregistrez le document au format PDF.

Ainsi, le fragment de code suivant suit ces étapes et montre comment convertir BMP en PDF en utilisant Python :

```python
import aspose.pdf as ap
from os import path
import sys

def convert_BMP_to_PDF(infile, outfile):
    document = ap.Document()
    page = document.pages.add()
    rectangle = ap.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(infile, rectangle)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Essayez de convertir BMP en PDF en ligne**

Aspose vous présente une application en ligne ["BMP en PDF"](https://products.aspose.app/pdf/conversion/bmp-to-pdf/), où vous pouvez essayer d'examiner le fonctionnement et la qualité.

[![Aspose.PDF Conversion BMP en PDF avec l'application](bmp_to_pdf.png)](https://products.aspose.app/pdf/conversion/bmp-to-pdf/)
{{% /alert %}}

## Convertir CGM en PDF

Convertir un CGM (Computer Graphics Metafile) en PDF (ou un autre format pris en charge) en utilisant Aspose.PDF for Python via .NET.

<abbr title="Computer Graphics Metafile">CGM</abbr> est une extension de fichier pour un format Metafile de Graphiques Informatiques couramment utilisé dans les applications de CAO (conception assistée par ordinateur) et de graphiques de présentation. CGM est un format de graphisme vectoriel qui prend en charge trois méthodes d'encodage différentes : binaire (optimal pour la vitesse de lecture du programme), basé sur les caractères (produit la plus petite taille de fichier et permet des transferts de données plus rapides) ou encodage en texte clair (permet aux utilisateurs de lire et modifier le fichier avec un éditeur de texte).

Vérifiez le extrait de code suivant pour convertir les fichiers CGM au format PDF.

Étapes pour convertir CGM en PDF en Python :

1. Définir les chemins de fichiers
1. Définir les options de chargement pour le CGM.
1. Convertir CGM en PDF
1. Message de conversion d'impression

```python
import aspose.pdf as ap
from os import path
import sys

def convert_CGM_to_PDF(infile, outfile):
    options = ap.CgmLoadOptions()
    document = ap.Document(infile, options)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

## Convertir DICOM en PDF

<abbr title="Digital Imaging and Communications in Medicine">DICOM</abbr> format est la norme de l'industrie médicale pour la création, le stockage, la transmission et la visualisation d'images médicales numériques et de documents des patients examinés.

**Aspose.PDF pour Python** vous permet de convertir les images DICOM et SVG, mais pour des raisons techniques, pour ajouter des images vous devez spécifier le type de fichier à ajouter au PDF.

L'extrait de code suivant montre comment convertir des fichiers DICOM au format PDF avec Aspose.PDF. Vous devez charger l'image DICOM, placer l'image sur une page d'un fichier PDF et enregistrer la sortie au format PDF. Nous utilisons la bibliothèque supplémentaire pydicom pour définir les dimensions de cette image. Si vous souhaitez positionner l'image sur la page, vous pouvez ignorer cet extrait de code.

1. Chargez le fichier DICOM.
1. Extraire les dimensions de l'image.
1. Imprimer la taille de l'image.
1. Créer un nouveau document PDF.
1. Préparer l'image DICOM pour le PDF.
1. Définir la taille de la page PDF et les marges.
1. Ajoutez l'image à la page.
1. Enregistrez le PDF.
1. Message de conversion d'impression.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_DICOM_to_PDF(infile, outfile):
    # Load the DICOM file
    import pydicom

    dicom_file = pydicom.dcmread(infile)

    # Get the dimensions of the image
    rows = dicom_file.Rows
    columns = dicom_file.Columns

    # Print the dimensions
    print(f"DICOM image size: {rows} x {columns} pixels")

    # Initialize new Document
    document = ap.Document()
    page = document.pages.add()
    image = ap.Image()
    image.file_type = ap.ImageFileType.DICOM
    image.file = infile

    # Set page dimensions
    page.page_info.height = rows
    page.page_info.width = columns
    page.page_info.margin.bottom = 0
    page.page_info.margin.top = 0
    page.page_info.margin.right = 0
    page.page_info.margin.left = 0
    page.paragraphs.add(image)

    document.save(outfile)
    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Essayez de convertir DICOM en PDF en ligne**

Aspose vous présente une application en ligne ["DICOM en PDF"](https://products.aspose.app/pdf/conversion/dicom-to-pdf/), où vous pouvez essayer d'examiner le fonctionnement et la qualité.

[![Conversion DICOM en PDF à l'aide de l'application Aspose.PDF](dicom_to_pdf.png)](https://products.aspose.app/pdf/conversion/dicom-to-pdf/)
{{% /alert %}}

## Convertir EMF en PDF

<abbr title="Enhanced metafile format">EMF</abbr> stocke des images graphiques de manière indépendante du dispositif. Les métafichiers EMF sont composés d'enregistrements de longueur variable, organisés chronologiquement, pouvant rendre l'image stockée après analyse sur n'importe quel dispositif de sortie.

Le fragment de code suivant montre comment convertir un EMF en PDF avec Python :

```python

import aspose.pdf as ap
from os import path
import sys

def convert_EMF_to_PDF(infile, outfile):
    document = ap.Document()
    page = document.pages.add()
    rectangle = ap.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    # add image to new pdf page
    page.add_image(infile, rectangle)

    # Save the file into PDF format
    document.save(outfile)
    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Essayez de convertir EMF en PDF en ligne**

Aspose vous présente une application en ligne ["EMF en PDF"](https://products.aspose.app/pdf/conversion/emf-to-pdf/), où vous pouvez essayer d'examiner le fonctionnement et la qualité.

[![Conversion EMF en PDF avec Aspose.PDF en utilisant l'application](emf_to_pdf.png)](https://products.aspose.app/pdf/conversion/emf-to-pdf/)
{{% /alert %}}

## Convertir GIF en PDF

Convertir des fichiers GIF en document PDF à l'aide de la bibliothèque **Aspose.PDF for Python via .NET**.

<abbr title="Graphics Interchange Format">GIF</abbr> est capable de stocker des données compressées sans perte de qualité dans un format ne dépassant pas 256 couleurs. Le format GIF indépendant du matériel a été développé en 1987 (GIF87a) par CompuServe pour la transmission d’images bitmap sur les réseaux.

Ainsi, le fragment de code suivant suit ces étapes et montre comment convertir BMP en PDF en utilisant Python :

```python

import aspose.pdf as ap
from os import path
import sys

def convert_GIF_to_PDF(infile, outfile):
    document = ap.Document()
    page = document.pages.add()
    rectangle = ap.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(infile, rectangle)

    document.save(outfile)
    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Essayez de convertir un GIF en PDF en ligne**

Aspose vous présente une application en ligne [GIF vers PDF](https://products.aspose.app/pdf/conversion/gif-to-pdf/), où vous pouvez essayer d'examiner le fonctionnement et la qualité.

[![Aspose.PDF Conversion GIF en PDF à l'aide de l'application](bmp_to_pdf.png)](https://products.aspose.app/pdf/conversion/gif-to-pdf/)
{{% /alert %}}

## Convertir PNG en PDF

**Aspose.PDF for Python via .NET** supporte la fonction de conversion d'images PNG en format PDF. Vérifiez le snippet de code suivant pour réaliser votre tâche.

<abbr title="Portable Network Graphics">PNG</abbr> fait référence à un type de format de fichier d'image raster qui utilise une compression sans perte, ce qui le rend populaire auprès de ses utilisateurs.

Vous pouvez convertir une image PNG en PDF en suivant les étapes ci-dessous :

1. Créer un nouveau document PDF.
1. Définir le placement d'image.
1. Enregistrez le PDF.
1. Message de conversion d'impression.

De plus, l'extrait de code ci‑dessous montre comment convertir PNG en PDF avec Python :

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PNG_to_PDF(infile, outfile):
    document = ap.Document()
    page = document.pages.add()
    rectangle = ap.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(infile, rectangle)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Essayez de convertir PNG en PDF en ligne**

Aspose vous présente une application en ligne ["PNG en PDF"](https://products.aspose.app/pdf/conversion/png-to-pdf/), où vous pouvez essayer d'examiner le fonctionnement et la qualité.

[![Aspose.PDF Conversion PNG en PDF à l'aide de l'application](png_to_pdf.png)](https://products.aspose.app/pdf/conversion/png-to-pdf/)
{{% /alert %}}

## Convertir SVG en PDF

**Aspose.PDF for Python via .NET** explique comment convertir des images SVG au format PDF et comment obtenir les dimensions du fichier SVG source.

Scalable Vector Graphics (SVG) est une famille de spécifications d’un format de fichier basé sur XML pour les graphiques vectoriels bidimensionnels, à la fois statiques et dynamiques (interactifs ou animés). La spécification SVG est une norme ouverte qui est en cours de développement par le World Wide Web Consortium (W3C) depuis 1999.

<abbr title="Scalable Vector Graphics">SVG</abbr> les images et leurs comportements sont définis dans des fichiers texte XML. Cela signifie qu'elles peuvent être recherchées, indexées, scriptées, et si nécessaire, compressées. En tant que fichiers XML, les images SVG peuvent être créées et modifiées avec n'importe quel éditeur de texte, mais il est souvent plus pratique de les créer avec des programmes de dessin tels qu'Inkscape.

{{% alert color="success" %}}
**Essayez de convertir le format SVG en PDF en ligne**

Aspose.PDF for Python via .NET vous présente une application en ligne ["SVG en PDF"](https://products.aspose.app/pdf/conversion/svg-to-pdf), où vous pouvez essayer d'examiner le fonctionnement et la qualité.

[![Aspose.PDF Conversion SVG vers PDF avec App](svg_to_pdf.png)](https://products.aspose.app/pdf/conversion/svg-to-pdf)
{{% /alert %}}

L'extrait de code suivant montre le processus de conversion d'un fichier SVG en format PDF avec Aspose.PDF for Python.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_SVG_to_PDF(infile, outfile):
    load_options = ap.SvgLoadOptions()
    document = ap.Document(infile, load_options)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

## Convertir TIFF en PDF

**Aspose.PDF** format de fichier pris en charge, qu'il s'agisse d'une image TIFF à une seule trame ou à plusieurs trames. Cela signifie que vous pouvez convertir l'image TIFF en PDF.

TIFF ou TIF, Tagged Image File Format, représente des images raster destinées à être utilisées sur une variété d'appareils conformes à cette norme de format de fichier. Une image TIFF peut contenir plusieurs cadres avec différentes images. Le format de fichier Aspose.PDF est également pris en charge, qu'il s'agisse d'une image TIFF à cadre unique ou à plusieurs cadres.

Vous pouvez convertir le TIFF en PDF de la même manière que les autres formats de fichiers raster graphiques :

```python
import aspose.pdf as ap
from os import path
import sys

def convert_TIFF_to_PDF(infile, outfile):
    document = ap.Document()
    page = document.pages.add()
    rectangle = ap.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(infile, rectangle)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

## Convertir CDR en PDF

L'extrait de code suivant montre comment charger un fichier CorelDRAW (CDR) et l'enregistrer en PDF en utilisant 'CdrLoadOptions' dans Aspose.PDF for Python via .NET.

1. Créez 'CdrLoadOptions()' pour configurer la façon dont le fichier CDR doit être chargé.
1. Initialisez un objet Document avec le fichier CDR et les options de chargement.
1. Enregistrez le document au format PDF.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_CDR_to_PDF(infile, outfile):
    load_options = ap.CdrLoadOptions()
    document = ap.Document(infile, load_options)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

## Convertir JPEG en PDF

Cet exemple montre comment convertir un fichier JPEG en PDF en utilisant Aspose.PDF for Python via .NET.

1. Créer un nouveau document PDF.
1. Ajouter une nouvelle page.
1. Définissez le rectangle de placement (taille A4 : 595×842 points).
1. Insérez l'image dans la page.
1. Enregistrez le PDF.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_JPEG_to_PDF(infile, outfile):
    document = ap.Document()
    page = document.pages.add()
    rectangle = ap.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(infile, rectangle)

    document.save(outfile)
    print(infile + " converted into " + outfile)
```
