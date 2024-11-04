---
title: Convertir PDF en EPUB, LaTeX, Texte, XPS en Python
linktitle: Convertir PDF en d'autres formats
type: docs
weight: 90
url: /python-net/convert-pdf-to-other-files/
lastmod: "2022-12-23"
keywords: convertir, PDF, EPUB, LaText, Texte, XPS, Python
description: Ce sujet vous montre comment convertir un fichier PDF en d'autres formats de fichier comme EPUB, LaTeX, Texte, XPS, etc. en utilisant Python.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Convertir PDF en EPUB

{{% alert color="success" %}}
**Essayez de convertir PDF en EPUB en ligne**

Aspose.PDF pour Python vous présente une application en ligne gratuite ["PDF en EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub), où vous pouvez essayer d'examiner la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion PDF en EPUB avec une application gratuite](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

**<abbr title="Publication Électronique">EPUB</abbr>** est une norme de livre électronique libre et ouverte de l'International Digital Publishing Forum (IDPF).
 Les fichiers ont l'extension .epub.  
EPUB est conçu pour un contenu reformatable, ce qui signifie qu'un lecteur EPUB peut optimiser le texte pour un appareil d'affichage particulier. EPUB prend également en charge le contenu à mise en page fixe. Le format est destiné à être un format unique que les éditeurs et les maisons de conversion peuvent utiliser en interne, ainsi que pour la distribution et la vente. Il remplace la norme Open eBook.

Aspose.PDF pour Python prend également en charge la fonctionnalité de conversion de documents PDF au format EPUB. Aspose.PDF pour Python a une classe nommée 'EpubSaveOptions' qui peut être utilisée comme deuxième argument de la méthode [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods), pour générer un fichier EPUB.  
Veuillez essayer d'utiliser l'extrait de code suivant pour accomplir cette tâche avec Python.

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_epub.epub"
    # Ouvrir le document PDF
    document = ap.Document(input_pdf)

    # Instancier les options de sauvegarde Epub
    save_options = ap.EpubSaveOptions()

    # Spécifier la mise en page pour le contenu
    save_options.content_recognition_mode = ap.EpubSaveOptions.RecognitionMode.FLOW

    # Enregistrer le document EPUB
    document.save(output_pdf, save_options)
```

## Convertir PDF en LaTeX/TeX

**Aspose.PDF pour Python via .NET** prend en charge la conversion de PDF en LaTeX/TeX. Le format de fichier LaTeX est un format de fichier texte avec une balise spéciale utilisée dans le système de préparation de documents basé sur TeX pour une composition de haute qualité.

{{% alert color="success" %}}
**Essayez de convertir PDF en LaTeX/TeX en ligne**

Aspose.PDF pour Python vous présente l'application gratuite en ligne ["PDF to LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex), où vous pouvez essayer d'explorer la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion PDF en LaTeX/TeX avec une application gratuite](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

Pour convertir des fichiers PDF en TeX, Aspose.PDF dispose de la classe [LaTeXSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/latexsaveoptions/) qui fournit la propriété OutDirectoryPath pour enregistrer des images temporaires pendant le processus de conversion.

L'extrait de code suivant montre le processus de conversion de fichiers PDF en format TEX avec Python.

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_tex.tex"
    # Ouvrir le document PDF
    document = ap.Document(input_pdf)
    # Instancier un objet de LaTeXSaveOptions
    saveOptions = ap.LaTeXSaveOptions()
    document.save(output_pdf, saveOptions)
```

## Convertir PDF en Texte

**Aspose.PDF pour Python** prend en charge la conversion de l'ensemble du document PDF et de la page unique en un fichier texte.

### Convertir un document PDF en fichier texte

Vous pouvez convertir un document PDF en fichier TXT en utilisant la classe 'TextDevice'.

Le code suivant explique comment extraire les textes de toutes les pages.

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf =  DIR_OUTPUT + "convert_pdf_to_txt.txt"
    # Ouvrir le document PDF
    document = ap.Document(input_pdf)

    # Créer un dispositif de texte
    textDevice = ap.devices.TextDevice()

    # Convertir une page particulière et enregistrer
    textDevice.process(document.pages[1], output_pdf)
```
**Essayez de convertir Convertir PDF en Texte en ligne**

Aspose.PDF pour Python vous présente l'application gratuite en ligne ["PDF en Texte"](https://products.aspose.app/pdf/conversion/pdf-to-txt), où vous pouvez essayer d'examiner la fonctionnalité et la qualité de son fonctionnement.
{{% alert color="primary" %}}

[![Aspose.PDF Conversion PDF en Texte avec une Application Gratuite](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

## Convertir PDF en XPS

**Aspose.PDF pour Python** offre la possibilité de convertir des fichiers PDF au format <abbr title="XML Paper Specification">XPS</abbr>. Essayons d'utiliser l'extrait de code présenté pour convertir des fichiers PDF au format XPS avec Python.

{{% alert color="success" %}}
**Essayez de convertir PDF en XPS en ligne**

Aspose.PDF pour Python vous présente l'application gratuite en ligne ["PDF en XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps), où vous pouvez essayer d'examiner la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion PDF en XPS avec une Application Gratuite](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

Le type de fichier XPS est principalement associé à la spécification XML Paper Specification par Microsoft Corporation. La spécification XML Paper Specification (XPS), anciennement nommée Metro et englobant le concept marketing Next Generation Print Path (NGPP), est l'initiative de Microsoft pour intégrer la création et la visualisation de documents dans le système d'exploitation Windows.

Pour convertir des fichiers PDF en XPS, Aspose.PDF dispose de la classe [XpsSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/xpssaveoptions/) qui est utilisée comme deuxième argument de la méthode [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) pour générer le fichier XPS.

Le fragment de code suivant montre le processus de conversion d'un fichier PDF au format XPS.

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_xps.xps"
    # Ouvrir le document PDF
    document = ap.Document(input_pdf)

    # Instancier les options de sauvegarde XPS
    save_options = ap.XpsSaveOptions()

    # Enregistrer le document XPS
    document.save(output_pdf, save_options)
```

## Convertir PDF en XML

{{% alert color="success" %}}
**Essayez de convertir PDF en XML en ligne**

Aspose.PDF pour Python vous présente une application en ligne gratuite ["PDF to XML"](https://products.aspose.app/pdf/conversion/pdf-to-xml), où vous pouvez essayer d'examiner la fonctionnalité et la qualité.

[![Aspose.PDF Conversion PDF vers XML avec Application Gratuite](pdf_to_xml.png)](https://products.aspose.app/pdf/conversion/pdf-to-xml)
{{% /alert %}}

<abbr title="Extensible Markup Language">XML</abbr> est un langage de balisage et un format de fichier pour stocker, transmettre et reconstruire des données arbitraires.

Aspose.PDF pour Python prend également en charge la fonctionnalité de conversion de documents PDF en format XML. Aspose.PDF pour Python a une classe nommée 'XmlSaveOptions' qui peut être utilisée comme second argument dans la méthode [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods), pour générer un fichier XML. Veuillez essayer d'utiliser l'extrait de code suivant pour répondre à cette exigence avec Python.

```python

    import aspose.pdf as ap

    def convert_pdf_to_xml(self, infile, outfile):
        path_infile = self.dataDir + infile
        path_outfile = self.dataDir + outfile

        # Ouvrir le document PDF

        document = ap.Document(path_infile)

        # Instancier les options de sauvegarde XML
        save_options = ap.XmlSaveOptions()

        # Enregistrer le document XML
        document.save(path_outfile, save_options)
        print(infile + " converti en " + outfile)
```