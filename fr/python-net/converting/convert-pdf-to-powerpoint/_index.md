---
title: Convertir PDF en PowerPoint avec Python
linktitle: Convertir PDF en PowerPoint
type: docs
weight: 30
url: /fr/python-net/convert-pdf-to-powerpoint/
description: Apprenez comment convertir des fichiers PDF en PowerPoint avec Python en utilisant Aspose.PDF for Python via .NET, incluant des diapositives PPTX éditables et une sortie de diapositives basée sur des images.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comment convertir PDF en PowerPoint avec Python
Abstract: Cet article fournit un guide complet sur la conversion de fichiers PDF en présentations PowerPoint en utilisant Python, en se concentrant spécifiquement sur le format PPTX. Il présente l'utilisation d'Aspose.PDF for Python via .NET, qui facilite le processus de conversion en permettant aux pages PDF d'être transformées en diapositives individuelles dans un fichier PPTX. L'article décrit les étapes nécessaires à la conversion, y compris la création d'instances des classes Document et PptxSaveOptions et l'utilisation de la méthode Save. De plus, il met en avant une fonctionnalité permettant de convertir des PDF en PPTX avec des diapositives sous forme d'images en définissant une propriété spécifique dans PptxSaveOptions. Des extraits de code sont fournis pour illustrer le processus de conversion. L'article fait également référence à une application en ligne pour tester la fonctionnalité de conversion PDF vers PPTX, offrant aux utilisateurs une expérience pratique. En outre, il répertorie divers sujets et fonctionnalités liés disponibles dans ce contexte, soulignant la polyvalence et l'approche programmatique pour gérer les conversions de PDF vers PowerPoint en utilisant Python.
---

## Conversion PDF Python vers PowerPoint et PPTX

**Aspose.PDF for Python via .NET** vous permet de suivre la progression de la conversion PDF en PPTX.

Nous disposons d’une API nommée Aspose.Slides qui offre la fonctionnalité de créer ainsi que de manipuler des présentations PPT/PPTX. Cette API fournit également la fonctionnalité de conversion. <abbr title="Microsoft PowerPoint 2007 XML Presentation">PPTX</abbr> fichiers au format PDF. Au cours de cette conversion, les pages individuelles du fichier PDF sont converties en diapositives distinctes dans le fichier PPTX.

Lors de la conversion PDF en PPTX, le texte est rendu sous forme de texte que vous pouvez sélectionner/mettre à jour. Veuillez noter que, afin de convertir des fichiers PDF au format PPTX, Aspose.PDF fournit une classe nommée [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/). Un objet de la classe PptxSaveOptions est passé en tant que deuxième argument à la [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods)Le fragment de code suivant montre le processus de conversion des fichiers PDF au format PPTX.

Cette conversion est particulièrement utile lorsque vous souhaitez réutiliser des rapports PDF, des présentations ou des documents de travail sous forme de fichiers de présentation modifiables.

## Conversion simple de PDF en PowerPoint en utilisant Python et Aspose.PDF for Python via .NET

Afin de convertir un PDF en PPTX, Aspose.PDF for Python via .NET recommande d'utiliser les étapes de code suivantes.

Étapes : Convertir le PDF en PowerPoint en Python

1. Créer une instance de [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) classe.
1. Créer une instance de [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/) classe.
1. Appeler le [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) méthode.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PPTX(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.PptxSaveOptions()
    document.save(outfile, save_options)
```

## Convertir le PDF en PPTX avec les diapositives sous forme d'images

{{% alert color="success" %}}
**Essayez de convertir PDF en PowerPoint en ligne**

Aspose.PDF vous présente une application en ligne ["PDF en PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx), où vous pouvez essayer d'examiner le fonctionnement et la qualité.


[![Conversion Aspose.PDF PDF vers PPTX avec l'application](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

Dans le cas où vous devez convertir un PDF interrogeable en PPTX sous forme d'images plutôt que de texte sélectionnable, Aspose.PDF fournit cette fonctionnalité via [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/) classe. Pour ce faire, définissez la propriété [slides_as_images](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/#properties) de [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/) classe à 'true' comme indiqué dans l'exemple de code suivant.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PPTX_slides_as_images(infile, outfile):

    document = ap.Document(infile)
    save_options = ap.PptxSaveOptions()
    save_options.slides_as_images = True

    document.save(outfile, save_options)
```

## Convertir PDF en PPTX avec une résolution d'image personnalisée

Cette méthode convertit un document PDF en fichier PowerPoint (PPTX) tout en définissant une résolution d'image personnalisée (300 DPI) pour une qualité améliorée.

1. Chargez le PDF dans un objet 'ap.Document'.
1. Créez une instance de 'PptxSaveOptions'.
1. Définissez la propriété 'image_resolution' à 300 DPI pour un rendu de haute qualité.
1. Enregistrez le PDF en tant que fichier PPTX en utilisant les options de sauvegarde définies.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PPTX_image_resolution(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.PptxSaveOptions()
    save_options.image_resolution = 300

    document.save(outfile, save_options)
```

## Conversions associées

- [Convertir le PDF en Word](/pdf/fr/python-net/convert-pdf-to-word/) pour une sortie de document modifiable au lieu de diapositives.
- [Convertir le PDF en Excel](/pdf/fr/python-net/convert-pdf-to-excel/) lorsque le PDF source contient des données commerciales contenant de nombreuses tables.
- [Convertir le PDF en HTML](/pdf/fr/python-net/convert-pdf-to-html/) pour des flux de travail de publication prêts pour le navigateur.