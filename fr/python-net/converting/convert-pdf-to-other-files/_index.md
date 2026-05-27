---
title: Convertir PDF en EPUB, texte, XPS et plus en Python
linktitle: Convertir le PDF en d'autres formats
type: docs
weight: 90
url: /fr/python-net/convert-pdf-to-other-files/
lastmod: "2026-05-22"
description: Apprenez comment convertir des fichiers PDF en EPUB, LaTeX, Markdown, texte, XPS et MobiXML en Python avec Aspose.PDF for Python via .NET.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Comment convertir PDF en d’autres formats avec Python
Abstract: L'article propose un guide complet sur la conversion de fichiers PDF en divers formats à l'aide d'Aspose.PDF for Python. Il couvre la conversion des PDF en formats EPUB, LaTeX/TeX, texte, XPS et XML. Chaque section commence par une invitation à essayer les applications en ligne fournies par Aspose pour convertir les PDF vers les formats respectifs, soulignant la facilité d'utilisation et la qualité de ces outils.
---

## Convertir PDF en EPUB

{{% alert color="success" %}}
**Essayez de convertir le PDF en EPUB en ligne**

Aspose.PDF for Python vous présente une application en ligne [PDF vers EPUB](https://products.aspose.app/pdf/conversion/pdf-to-epub), où vous pouvez essayer d'examiner le fonctionnement et la qualité.

[![Conversion PDF en EPUB avec l'application Aspose.PDF](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

<abbr title="Electronic Publication">EPUB</abbr> est une norme de livre numérique libre et ouverte provenant de l'International Digital Publishing Forum (IDPF). Les fichiers ont l'extension .epub.
EPUB est conçu pour du contenu réfluable, ce qui signifie qu’un lecteur EPUB peut optimiser le texte pour un dispositif d’affichage particulier. EPUB prend également en charge le contenu à mise en page fixe. Le format est destiné à être un format unique que les éditeurs et les maisons de conversion peuvent utiliser en interne, ainsi que pour la distribution et la vente. Il remplace la norme Open eBook.

Aspose.PDF for Python prend également en charge la fonctionnalité de conversion des documents PDF au format EPUB. Aspose.PDF for Python possède une classe nommée ‘EpubSaveOptions’ qui peut être utilisée comme deuxième argument de [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) méthode, pour générer un fichier EPUB.
Veuillez essayer d'utiliser le fragment de code suivant pour satisfaire cette exigence avec Python.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_EPUB(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.EpubSaveOptions()
    save_options.content_recognition_mode = ap.EpubSaveOptions.RecognitionMode.FLOW
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## Conversions associées

- [Convertir le PDF en Word](/pdf/fr/python-net/convert-pdf-to-word/) pour la sortie de documents Office modifiables.
- [Convertir le PDF en HTML](/pdf/fr/python-net/convert-pdf-to-html/) pour une sortie orientée navigateur.
- [Convertir le PDF en PDF/A, PDF/E et PDF/X](/pdf/fr/python-net/convert-pdf-to-pdf_x/) pour les flux de travail d'archivage et de conversion conformes aux normes.

## Convertir le PDF en LaTeX/TeX

**Aspose.PDF for Python via .NET** prend en charge la conversion de PDF en LaTeX/TeX.
Le format de fichier LaTeX est un format de fichier texte avec un balisage spécial et est utilisé dans le système de préparation de documents basé sur TeX pour une mise en forme de haute qualité.

{{% alert color="success" %}}
**Essayez de convertir le PDF en LaTeX/TeX en ligne**

Aspose.PDF for Python vous présente une application en ligne ["PDF en LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex), où vous pouvez essayer d'examiner le fonctionnement et la qualité.

[![Aspose.PDF Conversion PDF vers LaTeX/TeX avec App](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

Pour convertir des fichiers PDF en TeX, Aspose.PDF possède la classe [LaTeXSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/latexsaveoptions/) qui fournit la propriété OutDirectoryPath pour enregistrer les images temporaires pendant le processus de conversion.

Le fragment de code suivant montre le processus de conversion des fichiers PDF au format TEX avec Python.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_TeX(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.LaTeXSaveOptions()
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## Convertir le PDF en texte

**Aspose.PDF for Python** prend en charge la conversion d'un document PDF complet et d'une page unique en fichier texte. Vous pouvez convertir un document PDF en fichier TXT en utilisant la classe 'TextDevice'. Le fragment de code suivant explique comment extraire le texte de toutes les pages.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_TXT(infile, outfile):
    document = ap.Document(infile)
    device = ap.devices.TextDevice()
    device.process(document.pages[1], outfile)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Essayez de convertir PDF en texte en ligne**

Aspose.PDF for Python vous présente une application en ligne ["PDF en texte"](https://products.aspose.app/pdf/conversion/pdf-to-txt), où vous pouvez essayer d'examiner le fonctionnement et la qualité.

[![Aspose.PDF Conversion PDF en texte avec l'App](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

## Convertir le PDF en XPS

**Aspose.PDF for Python** offre la possibilité de convertir des fichiers PDF au format XPS. Essayons d'utiliser le fragment de code présenté pour convertir des fichiers PDF au format XPS avec Python.

{{% alert color="success" %}}
**Essayez de convertir le PDF en XPS en ligne**

Aspose.PDF for Python vous présente une application en ligne ["PDF en XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps), où vous pouvez essayer d'examiner le fonctionnement et la qualité.

[![Conversion Aspose.PDF PDF vers XPS avec App](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

Le type de fichier XPS est principalement associé à la spécification XML Paper Specification de Microsoft Corporation. La spécification XML Paper Specification (XPS), anciennement nom de code Metro et englobant le concept marketing Next Generation Print Path (NGPP), est l'initiative de Microsoft visant à intégrer la création et la visualisation de documents dans le système d'exploitation Windows.

Pour convertir des fichiers PDF en XPS, Aspose.PDF dispose de la classe [XpsSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/xpssaveoptions/) qui est utilisé comme deuxième argument du [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) méthode pour générer le fichier XPS.

Le fragment de code suivant montre le processus de conversion d'un fichier PDF en format XPS.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_XPS(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.XpsSaveOptions()
    save_options.use_new_imaging_engine = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## Convertir le PDF en MD

Aspose.PDF possède la classe ‘MarkdownSaveOptions()’, qui convertit un document PDF au format Markdown (MD) tout en préservant les images et les ressources.

1. Chargez le PDF source en utilisant 'ap.Document'.
1. Créez une instance de 'MarkdownSaveOptions'.
1. Définissez 'resources_directory_name' sur 'images' – les images extraites seront stockées dans ce dossier.
1. Enregistrez le document Markdown converti en utilisant les options configurées.
1. Imprimer un message de confirmation après la conversion.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_MD(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.MarkdownSaveOptions()
    save_options.resources_directory_name = "images"
    save_options.use_image_html_tag = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

Un fichier Markdown avec du texte et des images liées stockées dans le dossier d'images spécifié.

## Convertir le PDF en MobiXML

Cette méthode convertit un document PDF au format MOBI (MobiXML), qui est couramment utilisé pour les livres électroniques sur les appareils Kindle.

1. Chargez le document PDF source en utilisant 'ap.Document'.
1. Enregistrez le document au format 'ap.SaveFormat.MOBI_XML'.
1. Imprimez un message de confirmation une fois la conversion terminée.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_MobiXML(infile, outfile):
    document = ap.Document(infile)
    document.save(outfile, ap.SaveFormat.MOBI_XML)

    print(infile + " converted into " + outfile)
```
