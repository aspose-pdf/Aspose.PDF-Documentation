---
title: Convertir PDF en EPUB, LaTeX, Texte, XPS en Python
linktitle: Convertir PDF en d'autres formats
type: docs
weight: 90
url: /fr/python-java/convert-pdf-to-other-files/
lastmod: "2023-04-06"
keywords: convertir, PDF, EPUB, LaText, Texte, XPS, Python
description: Ce sujet vous montre comment convertir un fichier PDF en d'autres formats de fichiers comme EPUB, LaTeX, Texte, XPS, etc. en utilisant Python.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Convertir PDF en EPUB

{{% alert color="success" %}}
**Essayez de convertir PDF en EPUB en ligne**

Aspose.PDF pour Python vous présente une application gratuite en ligne ["PDF to EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub), où vous pouvez essayer d'explorer la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion PDF en EPUB avec une application gratuite](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

**<abbr title="Publication Électronique">EPUB</abbr>** est une norme de livre électronique libre et ouverte de l'International Digital Publishing Forum (IDPF).
 Les fichiers ont l'extension .epub.  
EPUB est conçu pour un contenu reformatable, ce qui signifie qu'un lecteur EPUB peut optimiser le texte pour un appareil d'affichage particulier. EPUB prend également en charge le contenu à mise en page fixe. Le format est destiné à être un format unique que les éditeurs et les maisons de conversion peuvent utiliser en interne, ainsi que pour la distribution et la vente. Il remplace la norme Open eBook.

Aspose.PDF pour Python prend également en charge la fonctionnalité de conversion des documents PDF au format EPUB. Aspose.PDF pour Python a une classe nommée 'EpubSaveOptions' qui peut être utilisée comme le deuxième argument de la méthode [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods), pour générer un fichier EPUB. Veuillez essayer d'utiliser l'extrait de code suivant pour accomplir cette tâche avec Python.

```python

from asposepdf import Api

# initier la licence
documentName = "testdata/license/Aspose.PDF.PythonviaJava.lic"
licenseObject = Api.License()
licenseObject.setLicense(documentName)

# Convertir en Epub
documentName = "testdata/Hello.pdf"
doc = Api.Document(documentName, None)
documentOutName = "testout/out.epub"
doc.save(documentOutName, Api.SaveFormat.Epub)
```

## Convertir PDF en LaTeX/TeX

**Aspose.PDF pour Python via Java** prend en charge la conversion de PDF en LaTeX/TeX. Le format de fichier LaTeX est un format de fichier texte avec un balisage spécial utilisé dans le système de préparation de documents basé sur TeX pour une composition de haute qualité.

{{% alert color="success" %}}
**Essayez de convertir un PDF en LaTeX/TeX en ligne**

Aspose.PDF pour Python vous présente l'application en ligne gratuite ["PDF to LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex), où vous pouvez essayer d'explorer la fonctionnalité et la qualité de son fonctionnement.

[![Conversion Aspose.PDF PDF en LaTeX/TeX avec une application gratuite](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

Pour convertir des fichiers PDF en TeX, Aspose.PDF dispose de la classe [LaTeXSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/latexsaveoptions/) qui fournit la propriété OutDirectoryPath pour enregistrer les images temporaires pendant le processus de conversion.

Le code suivant montre le processus de conversion de fichiers PDF au format TEX avec Python.

```python
from asposepdf import Api

documentName = "testdata/Hello.pdf"
doc = Api.Document(documentName, None)
documentOutName = "testout/out.tex"
doc.save(documentOutName, Api.SaveFormat.TeX)
```

## Convertir PDF en Texte

**Aspose.PDF pour Python** prend en charge la conversion d'un document PDF entier et d'une seule page en un fichier texte.

### Convertir un document PDF en fichier texte

Vous pouvez convertir un document PDF en fichier TXT en utilisant la classe 'TextDevice'.

L'extrait de code suivant explique comment extraire les textes de toutes les pages.

```python

from asposepdf import Api, Device

DIR_INPUT = "testdata/"
DIR_OUTPUT = "testout/"

input_pdf = DIR_INPUT + "source.pdf"
output_pdf = DIR_OUTPUT + "convert_pdf_to_text"
# Ouvrir le document PDF
document = Api.Document(input_pdf)

device = Device.TextDevice()

for i in range(0, document.getPages.size):
    imageFileName = output_pdf + "_page_" + str(i + 1) + "_out.txt"
    # Convertir une page particulière et enregistrer sous forme de fichier texte
    device.process(document.getPages.getPage(i + 1), imageFileName)
```


{{% alert color="success" %}}
**Essayez de convertir Convertir PDF en texte en ligne**

Aspose.PDF pour Python vous présente une application en ligne gratuite ["PDF à Texte"](https://products.aspose.app/pdf/conversion/pdf-to-txt), où vous pouvez essayer d'examiner la fonctionnalité et la qualité avec lesquelles elle fonctionne.

[![Aspose.PDF Conversion PDF en Texte avec Application Gratuite](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

## Convertir PDF en XPS

**Aspose.PDF pour Python** offre la possibilité de convertir des fichiers PDF au format <abbr title="Spécification Papier XML">XPS</abbr>. Essayons d'utiliser l'exemple de code présenté pour convertir des fichiers PDF au format XPS avec Python.

{{% alert color="success" %}}
**Essayez de convertir PDF en XPS en ligne**

Aspose.PDF pour Python vous présente une application en ligne gratuite ["PDF à XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps), où vous pouvez essayer d'examiner la fonctionnalité et la qualité avec lesquelles elle fonctionne.

[![Aspose.PDF Conversion PDF en XPS avec Application Gratuite](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

Le type de fichier XPS est principalement associé à la spécification XML Paper par Microsoft Corporation. La spécification XML Paper (XPS), anciennement nommée Metro et englobant le concept marketing Next Generation Print Path (NGPP), est l'initiative de Microsoft pour intégrer la création et la visualisation de documents dans le système d'exploitation Windows.

Pour convertir des fichiers PDF en XPS, Aspose.PDF dispose de la classe [XpsSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/xpssaveoptions/) qui est utilisée comme second argument de la méthode [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods) pour générer le fichier XPS.

Le snippet de code suivant montre le processus de conversion d'un fichier PDF en format XPS.

```python

from asposepdf import Api

documentName = "../../testdata/Hello.pdf"
doc = Api.Document(documentName, None)
documentOutName = "../../testout/out.xps"
doc.save(documentOutName, Api.SaveFormat.Xps)

```