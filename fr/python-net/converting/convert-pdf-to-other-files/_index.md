---
title: Convertir PDF en EPUB, LaTeX, texte, XPS avec Python
linktitle: Convertir PDF en d'autres formats
type: docs
weight: 90
url: /fr/python-net/convert-pdf-to-other-files/
lastmod: "2025-09-27"
description: Ce sujet vous montre comment convertir un fichier PDF en d’autres formats tels que EPUB, LaTeX, texte, XPS, etc., en utilisant Python.
sitemap: 
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Comment convertir PDF en d'autres formats avec Python
Abstract: L'article fournit un guide complet sur la conversion de fichiers PDF en divers formats à l'aide d'Aspose.PDF pour Python. Il couvre la conversion des PDF en formats EPUB, LaTeX/TeX, texte, XPS et XML. Chaque section commence par une invitation à essayer les applications en ligne gratuites proposées par Aspose pour convertir les PDF vers les formats correspondants, soulignant la facilité d'utilisation et la qualité de ces outils.
---

## Convertir PDF en EPUB

{{% alert color="success" %}}
**Essayez de convertir PDF en EPUB en ligne**

Aspose.PDF pour Python vous propose une application gratuite en ligne ["PDF en EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub), où vous pouvez tester la fonctionnalité et la qualité de son fonctionnement.

[![Conversion Aspose.PDF PDF en EPUB avec application gratuite](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

<abbr title="Electronic Publication">EPUB</abbr> est une norme de livre électronique libre et ouverte du International Digital Publishing Forum (IDPF). Les fichiers ont l'extension .epub.
EPUB est conçue pour du contenu réajustable, ce qui signifie qu'un lecteur EPUB peut optimiser le texte pour un dispositif d'affichage particulier. EPUB prend également en charge le contenu à mise en page fixe. Le format est destiné à être un format unique que les éditeurs et les sociétés de conversion peuvent utiliser en interne, ainsi que pour la distribution et la vente. Il remplace la norme Open eBook.

Aspose.PDF pour Python prend également en charge la conversion de documents PDF au format EPUB. Aspose.PDF pour Python possède une classe nommée 'EpubSaveOptions' qui peut être utilisée comme deuxième argument de la méthode [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) pour générer un fichier EPUB.
Veuillez essayer d'utiliser le fragment de code suivant pour répondre à cette exigence avec Python.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    save_options = ap.EpubSaveOptions()
    save_options.content_recognition_mode = (
        ap.EpubSaveOptions.RecognitionMode.FLOW
    )
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

## Convertir PDF en LaTeX/TeX

**Aspose.PDF pour Python via .NET** prend en charge la conversion de PDF en LaTeX/TeX.
Le format de fichier LaTeX est un format de fichier texte avec une balise spéciale et est utilisé dans le système de préparation de documents basé sur TeX pour une composition de haute qualité.

{{% alert color="success" %}}
**Essayez de convertir PDF en LaTeX/TeX en ligne**

Aspose.PDF pour Python vous propose une application gratuite en ligne ["PDF en LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex), où vous pouvez tester la fonctionnalité et la qualité de son fonctionnement.

[![Conversion Aspose.PDF PDF en LaTeX/TeX avec application gratuite](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

Pour convertir des fichiers PDF en TeX, Aspose.PDF possède la classe [LaTeXSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/latexsaveoptions/) qui fournit la propriété OutDirectoryPath pour enregistrer les images temporaires pendant le processus de conversion.

Le fragment de code suivant montre le processus de conversion de fichiers PDF au format TEX avec Python.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    save_options = ap.LaTeXSaveOptions()

    document.save(path_outfile, save_options)
    print(infile + " converted into " + outfile)
```

## Convertir PDF en texte

**Aspose.PDF pour Python** prend en charge la conversion d'un document PDF complet ou d'une page unique en fichier texte. Vous pouvez convertir un document PDF en fichier TXT en utilisant la classe 'TextDevice'. Le fragment de code suivant explique comment extraire le texte de toutes les pages.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    device = ap.devices.TextDevice()
    device.process(document.pages[1], path_outfile)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Essayez de convertir PDF en texte en ligne**

Aspose.PDF pour Python vous propose une application gratuite en ligne ["PDF en texte"](https://products.aspose.app/pdf/conversion/pdf-to-txt), où vous pouvez tester la fonctionnalité et la qualité de son fonctionnement.

[![Conversion Aspose.PDF PDF en texte avec application gratuite](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

## Convertir PDF en XPS

**Aspose.PDF pour Python** offre la possibilité de convertir des fichiers PDF au format XPS. Essayons d'utiliser le fragment de code présenté pour convertir des fichiers PDF au format XPS avec Python.

{{% alert color="success" %}}
**Essayez de convertir PDF en XPS en ligne**

Aspose.PDF pour Python vous propose une application gratuite en ligne ["PDF en XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps), où vous pouvez tester la fonctionnalité et la qualité de son fonctionnement.

[![Conversion Aspose.PDF PDF en XPS avec application gratuite](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

Le type de fichier XPS est principalement associé à la spécification XML Paper Specification de Microsoft Corporation. La spécification XML Paper Specification (XPS), anciennement nommée code nom Metro et englobant le concept marketing Next Generation Print Path (NGPP), est l'initiative de Microsoft d'intégrer la création et la visualisation de documents dans le système d'exploitation Windows.

Pour convertir des fichiers PDF en XPS, Aspose.PDF possède la classe [XpsSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/xpssaveoptions/) qui est utilisée comme deuxième argument de la méthode [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) pour générer le fichier XPS.

Le fragment de code suivant montre le processus de conversion d'un fichier PDF au format XPS.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    save_options = ap.XpsSaveOptions()
    save_options.use_new_imaging_engine = True
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

## Convertir le PDF en MD

Aspose.PDF possède la classe 'MarkdownSaveOptions()', qui convertit un document PDF en format Markdown (MD) tout en préservant les images et les ressources.

1. Chargez le PDF source en utilisant 'ap.Document'.
1. Créez une instance de 'MarkdownSaveOptions'.
1. Définissez 'resources_directory_name' sur 'images' – les images extraites seront stockées dans ce dossier.
1. Enregistrez le document Markdown converti en utilisant les options configurées.
1. Affichez un message de confirmation après la conversion.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    save_options = ap.MarkdownSaveOptions()
    # save_options.extract_vector_graphics = True
    save_options.resources_directory_name = "images"
    save_options.use_image_html_tag = True
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

Un fichier Markdown avec du texte et des images liées stockées dans le dossier d'images spécifié.

## Convertir le PDF en MobiXML

Cette méthode convertit un document PDF au format MOBI (MobiXML), couramment utilisé pour les livres électroniques sur les appareils Kindle.

1. Chargez le document PDF source en utilisant 'ap.Document'.
1. Enregistrez le document avec le format 'ap.SaveFormat.MOBI_XML'.
1. Affichez un message de confirmation une fois la conversion terminée.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    document.save(path_outfile, ap.SaveFormat.MOBI_XML)

    print(infile + " converted into " + outfile)
```
