---
title: Convertir le PDF en HTML en Python
linktitle: Convertir le PDF au format HTML
type: docs
weight: 50
url: /fr/python-net/convert-pdf-to-html/
lastmod: "2026-05-22"
description: Apprenez comment convertir un PDF en HTML en Python avec Aspose.PDF for Python via .NET, y compris la sortie multi-pages, les images externes, la gestion du SVG et le rendu HTML en couches.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Comment convertir un PDF en HTML en Python
Abstract: Cet article fournit un guide complet sur la conversion de fichiers PDF en HTML en utilisant Python, spécifiquement via la bibliothèque Aspose.PDF for Python via .NET. Il décrit les étapes nécessaires pour réaliser cette conversion de manière programmatique, en soulignant la création d’un objet `Document` à partir du PDF source et l’utilisation de `HtmlSaveOptions` pour enregistrer le document au format HTML. L’article inclut un extrait de code Python concis démontrant le processus de conversion. De plus, il présente un outil en ligne, l’application "PDF to HTML" d’Aspose.PDF, permettant aux utilisateurs d’explorer la fonctionnalité et la qualité de la conversion. L’article est structuré pour couvrir divers sujets connexes, garantissant une compréhension approfondie de l’utilisation de Python pour la conversion de PDF en HTML.
---

## Convertir le PDF en HTML

**Aspose.PDF for Python via .NET** offre de nombreuses fonctionnalités pour convertir différents formats de fichiers en documents PDF et convertir les fichiers PDF en divers formats de sortie. Cet article explique comment convertir un fichier PDF en <abbr title="HyperText Markup Language">HTML</abbr>. Vous pouvez simplement utiliser quelques lignes de code Python pour convertir un PDF en HTML. Vous pourriez avoir besoin de convertir un PDF en HTML si vous souhaitez créer un site web ou ajouter du contenu à un forum en ligne. Une façon de convertir un PDF en HTML est d'utiliser Python de manière programmatique.

{{% alert color="success" %}}
**Essayez de convertir le PDF en HTML en ligne**

Aspose.PDF for Python vous présente une application en ligne ["PDF vers HTML"](https://products.aspose.app/pdf/conversion/pdf-to-html), où vous pouvez essayer d'examiner le fonctionnement et la qualité.

[![Aspose.PDF Conversion PDF en HTML avec l'application](pdf_to_html.png)](https://products.aspose.app/pdf/conversion/pdf-to-html)
{{% /alert %}}

Étapes : Convertir le PDF en HTML en Python

1. Créer une instance de [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) objet avec le document PDF source.
1. Enregistrer dans [HtmlSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlsaveoptions/) en appelant [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) méthode.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_HTML(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.HtmlSaveOptions()
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## Conversions associées

- [Convertir le HTML en PDF](/pdf/fr/python-net/convert-html-to-pdf/) lorsque vous avez besoin du flux de travail inverse du web vers le document.
- [Convertir le PDF en Word](/pdf/fr/python-net/convert-pdf-to-word/) si la sortie de document modifiable est plus utile que le HTML.
- [Convertir le PDF en formats d\'image](/pdf/fr/python-net/convert-pdf-to-images-format/) pour les scénarios d'exportation raster.

### Convertir le PDF en HTML en enregistrant les images dans le dossier spécifié

Cette fonction convertit un fichier PDF au format HTML en utilisant Aspose.PDF for Python via .NET. Toutes les images extraites sont stockées dans un dossier spécifié au lieu d'être intégrées dans le fichier HTML.

1. Configurer les options d'enregistrement HTML.
1. Enregistrer au format HTML avec des images externes.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_HTML_storing_images(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.HtmlSaveOptions()
    images_path = path.join(path.dirname(infile), "images")
    save_options.special_folder_for_all_images = images_path
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

### Convertir le PDF en HTML multi‑pages

Cette fonction convertit un fichier PDF en HTML multipage, chaque page PDF étant exportée comme un fichier HTML séparé. Cela rend la sortie plus facile à parcourir et réduit le temps de chargement pour les gros PDFs.

1. Chargez le PDF source en utilisant 'ap.Document'.
1. Créez 'HtmlSaveOptions' et définissez `split_into_pages`.
1. Enregistrez le document au format HTML avec les pages séparées en fichiers distincts.
1. Imprimez un message de confirmation.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_HTML_multi_page(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.HtmlSaveOptions()
    save_options.split_into_pages = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

### Convertir le PDF en HTML tout en enregistrant les images SVG dans le dossier spécifié

Cette fonction convertit un PDF en format HTML tout en enregistrant toutes les images sous forme de fichiers SVG dans un dossier spécifié, au lieu de les intégrer directement dans le HTML.

1. Chargez le PDF source en utilisant 'ap.Document'.
1. Créer 'HtmlSaveOptions' et définir `special_folder_for_svg_images` sur le dossier cible.
1. Enregistrez le document au format HTML avec des images SVG externes.
1. Imprimez un message de confirmation.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_HTML_storing_svg(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.HtmlSaveOptions()
    images_path = path.join(path.dirname(infile), "svg_images")
    save_options.special_folder_for_svg_images = images_path
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

### Convertir un PDF en HTML et enregistrer des images SVG compressées

Ce fragment convertit un PDF au format HTML, en enregistrant toutes les images en tant que fichiers SVG dans un dossier spécifié et en les compressant pour réduire la taille du fichier.

1. Chargez le document PDF en utilisant 'ap.Document'.
1. Créer 'HtmlSaveOptions' et :
   - Définissez 'special_folder_for_svg_images' pour stocker les images SVG de façon externe.
   - Activez 'compress_svg_graphics_if_any' pour compresser les images SVG.
1. Enregistrez le document au format HTML avec des images SVG externes compressées.
1. Imprimez un message de confirmation.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_HTML_compress_svg(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.HtmlSaveOptions()
    images_path = path.join(path.dirname(infile), "svg_images")
    save_options.special_folder_for_svg_images = images_path
    save_options.compress_svg_graphics_if_any = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

### Convertir le PDF en HTML avec contrôle des images raster intégrées

Ce snippet convertit un PDF au format HTML, en intégrant les images raster comme arrière-plans de page PNG. Cette approche préserve la qualité de l'image et la mise en page dans le HTML.

1. Chargez le document PDF en utilisant 'ap.Document'.
1. Créez 'HtmlSaveOptions' et 'set raster_images_saving_mode' à 'AS_EMBEDDED_PARTS_OF_PNG_PAGE_BACKGROUND'.
1. Enregistrez le document au format HTML avec des images raster intégrées.
1. Imprimez un message de confirmation.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_HTML_PNG_background(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.HtmlSaveOptions()
    save_options.raster_images_saving_mode = ap.HtmlSaveOptions.RasterImagesSavingModes.AS_EMBEDDED_PARTS_OF_PNG_PAGE_BACKGROUND
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

### Convertir le PDF en page HTML contenant uniquement le corps

Cette fonction convertit un PDF au format HTML, générant du contenu « body‑only » sans balises « html » ou « head » supplémentaires, et divise la sortie en pages distinctes.

1. Chargez le document PDF en utilisant 'ap.Document'.
1. Créer 'HtmlSaveOptions' et configurer :
   - 'html_markup_generation_mode = WRITE_ONLY_BODY_CONTENT' pour ne générer que le contenu du 'body'.
   - 'split_into_pages' pour créer des fichiers HTML séparés pour chaque page PDF.
1. Enregistrez le document au format HTML avec les options spécifiées.
1. Imprimez un message de confirmation.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_HTML_body_content(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.HtmlSaveOptions()
    save_options.html_markup_generation_mode = (
        ap.HtmlSaveOptions.HtmlMarkupGenerationModes.WRITE_ONLY_BODY_CONTENT
    )
    save_options.split_into_pages = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

### Convertir le PDF en HTML avec rendu de texte transparent

Cette fonction convertit un PDF au format HTML, en rendant tout le texte transparent, y compris les textes ombrés, ce qui préserve la fidélité visuelle tout en permettant une mise en forme flexible dans le HTML de sortie.

1. Chargez le document PDF en utilisant 'ap.Document'.
1. Créer 'HtmlSaveOptions' et configurer :
    - 'save_transparent_texts' pour rendre le texte normal transparent.
    - 'save_shadowed_texts_as_transparent_texts' pour rendre le texte ombré transparent.
1. Enregistrez le document au format HTML avec un rendu de texte transparent.
1. Imprimez un message de confirmation.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_HTML_transparent_text_rendering(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.HtmlSaveOptions()
    save_options.save_transparent_texts = True
    save_options.save_shadowed_texts_as_transparent_texts = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

### Convertir le PDF en HTML avec le rendu des calques du document

Cette fonction convertit un PDF au format HTML, en préservant les calques du document en convertissant le contenu balisé en calques séparés dans le HTML de sortie. Cela permet aux éléments en couches (tels que les annotations, les arrière-plans et les superpositions) d'être rendus avec précision.

1. Chargez le document PDF en utilisant 'ap.Document'.
1. Créez 'HtmlSaveOptions' et activez 'convert_marked_content_to_layers' pour préserver les calques.
1. Enregistrez le document au format HTML avec un contenu en couches.
1. Imprimez un message de confirmation.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_HTML_document_layers_rendering(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.HtmlSaveOptions()
    save_options.convert_marked_content_to_layers = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

