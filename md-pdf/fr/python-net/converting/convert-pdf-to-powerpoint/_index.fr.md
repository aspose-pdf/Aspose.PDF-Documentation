---
title: Convertir PDF en PowerPoint en Python
linktitle: Convertir PDF en PowerPoint
type: docs
weight: 30
url: /python-net/convert-pdf-to-powerpoint/
description: Aspose.PDF vous permet de convertir des PDF au format PPT (PowerPoint) en utilisant Python. Il est possible de convertir un PDF en PPTX avec des diapositives sous forme d'images.
lastmod: "2022-12-23"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## Vue d'ensemble

Est-il possible de convertir un fichier PDF en PowerPoint ? Oui, vous pouvez ! Et c'est facile !
Cet article explique comment **convertir un PDF en PowerPoint en utilisant Python**. Il couvre ces sujets.

_Format_: **PPTX**
- [Python PDF en PPTX](#python-pdf-to-pptx)
- [Python Convertir PDF en PPTX](#python-pdf-to-pptx)
- [Python Comment convertir un fichier PDF en PPTX](#python-pdf-to-pptx)

_Format_: **PowerPoint**
- [Python PDF en PowerPoint](#python-pdf-to-powerpoint)
- [Python Convertir PDF en PowerPoint](#python-pdf-to-powerpoint)
- [Python Comment convertir un fichier PDF en PowerPoint](#python-pdf-to-powerpoint)


## Conversion de PDF en PowerPoint et PPTX en Python

**Aspose.PDF for Python via .NET** vous permet de suivre la progression de la conversion de PDF en PPTX.

Nous avons une API nommée Aspose.Slides qui offre la fonctionnalité de créer ainsi que de manipuler des présentations PPT/PPTX. Cette API offre également la fonctionnalité de convertir des fichiers PPT/PPTX au format PDF. Lors de cette conversion, les pages individuelles du fichier PDF sont converties en diapositives séparées dans le fichier PPTX.

Lors de la conversion de PDF en <abbr title="Microsoft PowerPoint 2007 XML Presentation">PPTX</abbr>, le texte est rendu en tant que texte où vous pouvez le sélectionner/le mettre à jour. Veuillez noter que pour convertir des fichiers PDF au format PPTX, Aspose.PDF fournit une classe nommée [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/). Un objet de la classe PptxSaveOptions est passé comme deuxième argument à la méthode [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods). Le code suivant montre le processus de conversion des fichiers PDF en format PPTX.

## Conversion simple de PDF en PowerPoint en utilisant Python et Aspose.PDF pour Python

Afin de convertir un PDF en PPTX, Aspose.PDF pour Python conseille d'utiliser les étapes de code suivantes.

<a name="csharp-pdf-to-powerpoint"><strong>Étapes : Convertir un PDF en PowerPoint en Python</strong></a> | <a name="csharp-pdf-to-pptx"><strong>Étapes : Convertir un PDF en PPTX en Python</strong></a>

1. Créez une instance de la classe [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)
2. Créez une instance de la classe [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/)
3. Utilisez la méthode **Save** de l'objet **Document** pour enregistrer le PDF en tant que PPTX

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_pptx.pptx"
    # Ouvrir le document PDF
    document = ap.Document(input_pdf)
    # Instancier l'instance de PptxSaveOptions
    save_option = ap.PptxSaveOptions()
    # Enregistrer le fichier au format MS PowerPoint
    document.save(output_pdf, save_option)
```

## Convertir un PDF en PPTX avec des diapositives sous forme d'images


{{% alert color="success" %}}
**Essayez de convertir un PDF en PowerPoint en ligne**

Aspose.PDF pour Python vous présente l'application en ligne gratuite ["PDF to PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx), où vous pouvez essayer d'examiner la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion PDF en PPTX avec l'application gratuite](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

Dans le cas où vous auriez besoin de convertir un PDF consultable en PPTX sous forme d'images au lieu de texte sélectionnable, Aspose.PDF propose une telle fonctionnalité via la classe [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/). Pour y parvenir, définissez la propriété [slides_as_images](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/#properties) de la classe [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/) à 'true' comme indiqué dans l'exemple de code suivant.

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf =  DIR_OUTPUT + "convert_pdf_to_pptx_with_slides_as_images.pptx"
    # Ouvrir le document PDF
    document = ap.Document(input_pdf)
    # Instancier l'instance PptxSaveOptions
    save_option = ap.PptxSaveOptions()
    save_option.slides_as_images = True
    # Enregistrer le fichier au format MS PowerPoint
    document.save(output_pdf, save_option)
```


## Voir Aussi

Cet article couvre également ces sujets. Les codes sont les mêmes qu'au-dessus.

_Format_: **PowerPoint**
- [Python PDF vers Code PowerPoint](#python-pdf-to-powerpoint)
- [Python PDF vers API PowerPoint](#python-pdf-to-powerpoint)
- [Python PDF vers PowerPoint Programmatiquement](#python-pdf-to-powerpoint)
- [Python PDF vers Bibliothèque PowerPoint](#python-pdf-to-powerpoint)
- [Python Enregistrer PDF comme PowerPoint](#python-pdf-to-powerpoint)
- [Python Générer PowerPoint depuis PDF](#python-pdf-to-powerpoint)
- [Python Créer PowerPoint depuis PDF](#python-pdf-to-powerpoint)
- [Python Convertisseur PDF vers PowerPoint](#python-pdf-to-powerpoint)

_Format_: **PPTX**
- [Python PDF vers Code PPTX](#python-pdf-to-pptx)
- [Python PDF vers API PPTX](#python-pdf-to-pptx)
- [Python PDF vers PPTX Programmatiquement](#python-pdf-to-pptx)
- [Python PDF vers Bibliothèque PPTX](#python-pdf-to-pptx)
- [Python Enregistrer PDF comme PPTX](#python-pdf-to-pptx)
- [Python Générer PPTX depuis PDF](#python-pdf-to-pptx)
- [Python Créer PPTX depuis PDF](#python-pdf-to-pptx)
- [Python Convertisseur PDF vers PPTX](#python-pdf-to-pptx)