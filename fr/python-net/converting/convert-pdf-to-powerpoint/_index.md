---
title: Convertir PDF en PowerPoint avec Python
linktitle: Convertir PDF en PowerPoint
type: docs
weight: 30
url: /fr/python-net/convert-pdf-to-powerpoint/
description: Apprenez comment convertir un PDF en PowerPoint avec Python, y compris PDF en PPTX, diapositives sous forme d'images et résolution d'image personnalisée avec Aspose.PDF.
lastmod: "2026-04-14"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Convertir PDF en diapositives PowerPoint PPTX en Python
Abstract: Cet article montre comment convertir des fichiers PDF en présentations PowerPoint avec Aspose.PDF for Python via .NET. Il couvre la conversion PDF vers PPTX, la conversion des diapositives en images et la définition de la résolution d'image pour la sortie de la présentation.
---

## Convertir PDF en PowerPoint avec Python

**Aspose.PDF for Python via .NET** vous permet de convertir des fichiers PDF en présentations PowerPoint PPTX à partir du code Python.

Utilisez ce flux de travail lorsque vous devez réutiliser des rapports PDF, des présentations, des brochures ou des documents à distribuer sous forme de fichiers PowerPoint. Lors de la conversion, les pages PDF individuelles sont converties en diapositives séparées dans le fichier PPTX.

Lors de la conversion PDF vers PPTX, le texte peut être rendu sous forme de texte sélectionnable que vous pouvez mettre à jour dans PowerPoint. Pour convertir des fichiers PDF au format PPTX, Aspose.PDF fournit le [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/) classe. Passez un `PptxSaveOptions` objet comme deuxième argument du [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) méthode.

## Convertir PDF en PPTX en Python

Pour convertir PDF en PPTX, utilisez les étapes de code suivantes.

Étapes : Convertir PDF en PowerPoint en Python

1. Créez une instance de [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) classe.
1. Créez une instance de [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/) classe.
1. Appelez le [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) méthode.

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
**Essayez de convertir le PDF en PowerPoint en ligne**

Aspose.PDF fournit une version en ligne ["PDF en PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx) application où vous pouvez tester la qualité de la conversion.


[![Conversion Aspose.PDF PDF en PPTX avec App](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

Au cas où vous auriez besoin de convertir un PDF consultable en PPTX sous forme d'images au lieu de texte sélectionnable, Aspose.PDF fournit une telle fonctionnalité via [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/) classe. Pour ce faire, définissez la propriété [slides_as_images](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/#properties) de [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/) classe à 'true' comme indiqué dans l'exemple de code suivant.

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

## Convertir le PDF en PPTX avec une résolution d'image personnalisée

Cette méthode convertit un document PDF en fichier PowerPoint (PPTX) tout en définissant une résolution d'image personnalisée (300 DPI) pour une meilleure qualité.

1. Chargez le PDF dans un objet 'ap.Document'.
1. Créez une instance 'PptxSaveOptions'.
1. Définissez la propriété 'image_resolution' à 300 DPI pour un rendu de haute qualité.
1. Enregistrez le PDF en tant que fichier PPTX en utilisant les options d’enregistrement définies.

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

- [Convertir le PDF en Word](/pdf/fr/python-net/convert-pdf-to-word/) pour une sortie de document éditable au lieu de diapositives.
- [Convertir le PDF en Excel](/pdf/fr/python-net/convert-pdf-to-excel/) lorsque le PDF source contient des données d’entreprise fortement tabulaires.
- [Convertir le PDF en HTML](/pdf/fr/python-net/convert-pdf-to-html/) pour les flux de travail de publication prêts pour le navigateur.
