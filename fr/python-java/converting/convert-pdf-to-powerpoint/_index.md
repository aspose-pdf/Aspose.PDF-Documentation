---
title: Convertir PDF en PowerPoint en Python
linktitle: Convertir PDF en PowerPoint
type: docs
weight: 30
url: fr/python-java/convert-pdf-to-powerpoint/
description: Aspose.PDF vous permet de convertir PDF en format PPT (PowerPoint) en utilisant Python. Il y a une possibilité de convertir PDF en PPTX avec des diapositives comme images.
lastmod: "2023-04-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## Vue d'ensemble

Est-il possible de convertir un fichier PDF en PowerPoint ? Oui, vous pouvez ! Et c'est facile !
Cet article explique comment **convertir PDF en PowerPoint en utilisant Python**. Il couvre ces sujets.

_Format_: **PPTX**
- [Python PDF en PPTX](#python-pdf-en-pptx)
- [Python Convertir PDF en PPTX](#python-pdf-en-pptx)
- [Python Comment convertir un fichier PDF en PPTX](#python-pdf-en-pptx)

_Format_: **PowerPoint**
- [Python PDF en PowerPoint](#python-pdf-en-powerpoint)
- [Python Convertir PDF en PowerPoint](#python-pdf-en-powerpoint)
- [Python Comment convertir un fichier PDF en PowerPoint](#python-pdf-en-powerpoint)


## Conversion de PDF en PowerPoint et PPTX avec Python

**Aspose.PDF pour Python via Java** vous permet de suivre l'évolution de la conversion de PDF en PPTX.

Nous avons une API nommée Aspose.Slides qui offre la fonctionnalité de créer ainsi que de manipuler des présentations PPT/PPTX. Cette API fournit également la fonctionnalité de convertir des fichiers PPT/PPTX au format PDF. Au cours de cette conversion, les pages individuelles du fichier PDF sont converties en diapositives séparées dans le fichier PPTX.

Lors de la conversion de PDF en <abbr title="Microsoft PowerPoint 2007 XML Presentation">PPTX</abbr>, le texte est rendu sous forme de texte où vous pouvez le sélectionner/le mettre à jour. Veuillez noter que pour convertir des fichiers PDF au format PPTX, Aspose.PDF fournit une classe nommée [`PptxSaveOptions`](https://reference.aspose.com/pdf/java/aspose.pdf/pptxsaveoptions). Un objet de la classe PptxSaveOptions est passé en tant que second argument à la [`méthode Document.Save(..)`](https://reference.aspose.com/pdf/java/aspose.pdf/document/methods/save). Le fragment de code suivant montre le processus de conversion des fichiers PDF au format PPTX.

## Conversion simple de PDF en PowerPoint en utilisant Python et Aspose.PDF pour Python

Afin de convertir un PDF en PPTX, Aspose.PDF pour Python conseille d'utiliser les étapes de code suivantes.

<a name="csharp-pdf-to-powerpoint"><strong>Étapes : Convertir PDF en PowerPoint en Python</strong></a> | <a name="csharp-pdf-to-pptx"><strong>Étapes : Convertir PDF en PPTX en Python</strong></a>

1. Créez une instance de la classe [Document](https://reference.aspose.com/pdf/java/aspose.pdf/document)
2. Créez une instance de la classe [PptxSaveOptions](https://reference.aspose.com/pdf/java/aspose.pdf/pptxsaveoptions)
3. Utilisez la méthode **Save** de l'objet **Document** pour enregistrer le PDF en tant que PPTX

```python

DIR_INPUT = "testdata/"
DIR_OUTPUT = "testout/"

input_pdf = DIR_INPUT + "Hello.pdf"
output_pdf = DIR_OUTPUT + "convert_pdf_to_pptx_with_options.pptx"
# Ouvrir le document PDF
document = Api.Document(input_pdf)

save_options = Api.PptxSaveOptions()
save_options._ImageResolution = 300
save_options._SeparateImages = True
save_options._OptimizeTextBoxes = True

# Enregistrez le fichier au format de document MS Word
document.save(output_pdf, save_options)
```


## Convertir un PDF en PPTX avec des diapositives comme images

{{% alert color="success" %}}
**Essayez de convertir un PDF en PowerPoint en ligne**

Aspose.PDF pour Python vous présente une application en ligne gratuite ["PDF to PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx), où vous pouvez essayer d'examiner la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion PDF en PPTX avec une application gratuite](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

Dans le cas où vous devez convertir un PDF consultable en PPTX sous forme d'images au lieu de texte sélectionnable, Aspose.PDF fournit une telle fonctionnalité via la classe [Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/pptxsaveoptions/). Pour y parvenir, définissez la propriété [SlidesAsImages](https://reference.aspose.com/pdf/python-java/aspose.pdf/pptxsaveoptions/#properties) de la classe [PptxSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/pptxsaveoptions/) à 'true' comme montré dans l'exemple de code suivant.

```python

DIR_INPUT = "testdata/"
DIR_OUTPUT = "testout/"

input_pdf = DIR_INPUT + "Hello.pdf"
output_pdf = DIR_OUTPUT + "convert_pdf_to_pptx_with_options.pptx"
# Ouvrir le document PDF
document = Api.Document(input_pdf)

save_options = Api.PptxSaveOptions()
save_options._ImageResolution = 300
save_options._SlidesAsImages = True

# Enregistrer le fichier au format document MS Word
document.save(output_pdf, save_options)
```


## Voir Aussi

Cet article couvre également ces sujets. Les codes sont les mêmes qu'au-dessus.

_Format_: **PowerPoint**
- [Code Python PDF vers PowerPoint](#python-pdf-to-powerpoint)
- [API Python PDF vers PowerPoint](#python-pdf-to-powerpoint)
- [Programmer en Python PDF vers PowerPoint](#python-pdf-to-powerpoint)
- [Bibliothèque Python PDF vers PowerPoint](#python-pdf-to-powerpoint)
- [Enregistrer PDF en PowerPoint avec Python](#python-pdf-to-powerpoint)
- [Générer PowerPoint à partir de PDF avec Python](#python-pdf-to-powerpoint)
- [Créer PowerPoint à partir de PDF avec Python](#python-pdf-to-powerpoint)
- [Convertisseur Python PDF vers PowerPoint](#python-pdf-to-powerpoint)

_Format_: **PPTX**
- [Code Python PDF vers PPTX](#python-pdf-to-pptx)
- [API Python PDF vers PPTX](#python-pdf-to-pptx)
- [Programmer en Python PDF vers PPTX](#python-pdf-to-pptx)
- [Bibliothèque Python PDF vers PPTX](#python-pdf-to-pptx)
- [Enregistrer PDF en PPTX avec Python](#python-pdf-to-pptx)
- [Générer PPTX à partir de PDF avec Python](#python-pdf-to-pptx)
- [Créer PPTX à partir de PDF avec Python](#python-pdf-to-pptx)

- [Convertisseur Python PDF vers PPTX](#python-pdf-to-pptx)