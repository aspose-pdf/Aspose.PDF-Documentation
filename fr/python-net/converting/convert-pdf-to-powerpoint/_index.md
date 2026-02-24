---
title: Convertir PDF en PowerPoint avec Python
linktitle: Convertir PDF en PowerPoint
type: docs
weight: 30
url: /fr/python-net/convert-pdf-to-powerpoint/
description: Apprenez à convertir facilement des PDF en présentations PowerPoint à l'aide d'Aspose.PDF pour Python via .NET. Guide étape par étape pour une transformation fluide de PDF en PPTX.
lastmod: "2025-09-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comment convertir PDF en PowerPoint avec Python
Abstract: Cet article fournit un guide complet sur la conversion de fichiers PDF en présentations PowerPoint à l'aide de Python, en se concentrant spécifiquement sur le format PPTX. Il présente l'utilisation d'Aspose.PDF pour Python via .NET, qui facilite le processus de conversion en permettant de transformer les pages PDF en diapositives individuelles dans un fichier PPTX. L'article décrit les étapes nécessaires à la conversion, y compris la création d'instances des classes Document et PptxSaveOptions ainsi que l'utilisation de la méthode Save. De plus, il met en évidence une fonctionnalité permettant de convertir les PDF en PPTX avec des diapositives sous forme d'images en définissant une propriété spécifique dans PptxSaveOptions. Des extraits de code sont fournis pour illustrer le processus de conversion. L'article fait également référence à une application en ligne pour tester la fonctionnalité de conversion PDF vers PPTX, offrant aux utilisateurs une expérience pratique. En outre, il répertorie divers sujets et fonctionnalités liés disponibles dans ce contexte, soulignant la polyvalence et l'approche programmatique pour gérer les conversions de PDF en PowerPoint avec Python.
---

## Conversion de PDF en PowerPoint et PPTX avec Python

**Aspose.PDF pour Python via .NET** vous permet de suivre la progression de la conversion PDF en PPTX.

Nous disposons d'une API nommée Aspose.Slides qui offre la fonctionnalité de créer ainsi que de manipuler des présentations PPT/PPTX. Cette API fournit également la fonctionnalité de convertir les fichiers <abbr title="Microsoft PowerPoint 2007 XML Presentation">PPTX</abbr> au format PDF. Au cours de cette conversion, les pages individuelles du fichier PDF sont converties en diapositives séparées dans le fichier PPTX.

Lors de la conversion PDF en PPTX, le texte est rendu comme du texte où vous pouvez le sélectionner/mettre à jour. Veuillez noter que, afin de convertir des fichiers PDF au format PPTX, Aspose.PDF fournit une classe nommée [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/). Un objet de la classe PptxSaveOptions est passé en second argument à la méthode [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods). Le fragment de code suivant montre le processus de conversion des fichiers PDF en format PPTX.

## Conversion simple de PDF en PowerPoint avec Python et Aspose.PDF pour Python via .NET

Pour convertir un PDF en PPTX, Aspose.PDF pour Python recommande d'utiliser les étapes de code suivantes.

Étapes : Convertir PDF en PowerPoint avec Python

1. Créez une instance de la classe [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Créez une instance de la classe [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/).
1. Appelez la méthode [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    save_options = apdf.PptxSaveOptions()
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

## Convertir PDF en PPTX avec des diapositives sous forme d'images

{{% alert color="success" %}}
**Essayez de convertir PDF en PowerPoint en ligne**

Aspose.PDF vous propose une application en ligne gratuite ["PDF to PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx), où vous pouvez essayer d'examiner les fonctionnalités et la qualité de son fonctionnement.


[![Conversion Aspose.PDF de PDF en PPTX avec application gratuite](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

En cas de besoin de convertir un PDF recherchable en PPTX sous forme d'images plutôt que de texte sélectionnable, Aspose.PDF propose cette fonctionnalité via la classe [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/). Pour ce faire, définissez la propriété [slides_as_images](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/#properties) de la classe [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/) à 'true' comme indiqué dans l'exemple de code suivant.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    save_options = apdf.PptxSaveOptions()
    save_options.slides_as_images = True

    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

## Convertir PDF en PPTX avec résolution d'image personnalisée

Cette méthode convertit un document PDF en fichier PowerPoint (PPTX) tout en définissant une résolution d'image personnalisée (300 DPI) pour une meilleure qualité.

1. Chargez le PDF dans un objet 'ap.Document'.
1. Créez une instance 'PptxSaveOptions'.
1. Définissez la propriété 'image_resolution' à 300 DPI pour un rendu de haute qualité.
1. Enregistrez le PDF en tant que fichier PPTX en utilisant les options d'enregistrement définies.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    save_options = apdf.PptxSaveOptions()
    save_options.image_resolution = 300

    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

