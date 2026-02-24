---
title: Convertir PDF en HTML avec Python
linktitle: Convertir PDF au format HTML
type: docs
weight: 50
url: /fr/python-net/convert-pdf-to-html/
lastmod: "2025-09-27"
description: Ce sujet vous montre comment convertir un fichier PDF au format HTML avec la bibliothèque Aspose.PDF pour Python via .NET.
sitemap: 
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Comment convertir PDF en HTML avec Python
Abstract: Cet article fournit un guide complet sur la conversion de fichiers PDF en HTML en utilisant Python, spécifiquement via la bibliothèque Aspose.PDF pour Python via .NET. Il décrit les étapes nécessaires pour réaliser cette conversion de manière programmatique, en soulignant la création d'un objet `Document` à partir du PDF source et l'utilisation de `HtmlSaveOptions` pour enregistrer le document au format HTML. L'article inclut un extrait de code Python concis démontrant le processus de conversion. De plus, il présente un outil en ligne, l'application "PDF to HTML" d'Aspose.PDF, permettant aux utilisateurs d'explorer la fonctionnalité et la qualité de la conversion. L'article est structuré pour couvrir divers sujets liés, garantissant une compréhension approfondie de l'utilisation de Python pour la conversion PDF en HTML.
---

## Convertir PDF en HTML

**Aspose.PDF for Python via .NET** offre de nombreuses fonctionnalités pour convertir divers formats de fichiers en documents PDF et convertir les fichiers PDF en divers formats de sortie. Cet article explique comment convertir un fichier PDF en <abbr title="HyperText Markup Language">HTML</abbr>. Vous pouvez utiliser seulement quelques lignes de code Python pour convertir un PDF en HTML. Vous pourriez avoir besoin de convertir un PDF en HTML si vous souhaitez créer un site web ou ajouter du contenu à un forum en ligne. Une façon de convertir un PDF en HTML est d'utiliser Python de manière programmatique.

{{% alert color="success" %}}
**Essayez de convertir PDF en HTML en ligne**

Aspose.PDF for Python vous propose une application en ligne gratuite ["PDF to HTML"](https://products.aspose.app/pdf/conversion/pdf-to-html), où vous pouvez essayer d'examiner la fonctionnalité et la qualité de son fonctionnement.

[![Conversion Aspose.PDF PDF en HTML avec l'application gratuite](pdf_to_html.png)](https://products.aspose.app/pdf/conversion/pdf-to-html)
{{% /alert %}}

Étapes : Convertir PDF en HTML avec Python

1. Créez une instance de l'objet [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) avec le document PDF source.
1. Enregistrez-le avec [HtmlSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlsaveoptions/) en appelant la méthode [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    document = apdf.Document(path_infile)
    save_options = apdf.HtmlSaveOptions()
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

### Convertir PDF en HTML en enregistrant les images dans le dossier spécifié

Cette fonction convertit un fichier PDF au format HTML en utilisant Aspose.PDF pour Python via .NET. Toutes les images extraites sont stockées dans un dossier spécifié au lieu d'être intégrées dans le fichier HTML.

1. Configurez les options d'enregistrement HTML.
1. Enregistrez en HTML avec des images externes.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    document = apdf.Document(path_infile)
    save_options = apdf.HtmlSaveOptions()
    save_options.special_folder_for_all_images = self.data_dir
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

### Convertir PDF en HTML multi-pages

Cette fonction convertit un fichier PDF en HTML multi-pages, où chaque page du PDF est exportée en tant que fichier HTML distinct. Cela rend la sortie plus facile à parcourir et réduit le temps de chargement pour les gros PDF.

1. Chargez le PDF source en utilisant 'ap.Document'.
1. Créez 'HtmlSaveOptions' et utilisez 'set split_into_pages'.
1. Enregistrez le document en HTML avec les pages séparées en fichiers distincts.
1. Affichez un message de confirmation.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    document = apdf.Document(path_infile)
    save_options = apdf.HtmlSaveOptions()
    save_options.split_into_pages = True
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

### Convertir PDF en HTML en enregistrant les images SVG dans le dossier spécifié

Cette fonction convertit un PDF au format HTML tout en stockant toutes les images sous forme de fichiers SVG dans un dossier spécifié, au lieu de les intégrer directement dans le HTML.

1. Chargez le PDF source en utilisant 'ap.Document'.
1. Créez 'HtmlSaveOptions' et utilisez 'set special_folder_for_svg_images' pour le dossier cible.
1. Enregistrez le document en HTML avec des images SVG externes.
1. Affichez un message de confirmation.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    document = apdf.Document(path_infile)
    save_options = apdf.HtmlSaveOptions()
    save_options.special_folder_for_svg_images = self.data_dir
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

### Convertir PDF en HTML et enregistrer les images SVG compressées

Cet extrait convertit un PDF au format HTML, stockant toutes les images sous forme de fichiers SVG dans un dossier spécifié et les compressant pour réduire la taille du fichier.

1. Chargez le document PDF en utilisant 'ap.Document'.
1. Créez 'HtmlSaveOptions' et :
- Définissez 'special_folder_for_svg_images' pour stocker les images SVG à l'extérieur.
- Activez 'compress_svg_graphics_if_any' pour compresser les images SVG.
1. Enregistrez le document en HTML avec des images SVG externes compressées.
1. Affichez un message de confirmation.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    document = apdf.Document(path_infile)
    save_options = apdf.HtmlSaveOptions()
    save_options.special_folder_for_svg_images = self.data_dir
    save_options.compress_svg_graphics_if_any = True
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

### Convertir PDF en HTML avec contrôle des images raster intégrées

Cet extrait convertit un PDF au format HTML, intégrant les images raster comme arrière-plans de page PNG. Cette approche préserve la qualité des images et la mise en page dans le HTML.

1. Chargez le document PDF en utilisant 'ap.Document'.
1. Créez 'HtmlSaveOptions' et définissez 'raster_images_saving_mode' sur 'AS_EMBEDDED_PARTS_OF_PNG_PAGE_BACKGROUND'.
1. Enregistrez le document au format HTML avec des images raster intégrées.
1. Affichez un message de confirmation.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    document = apdf.Document(path_infile)
    save_options = apdf.HtmlSaveOptions()
    save_options.raster_images_saving_mode = apdf.HtmlSaveOptions.RasterImagesSavingModes.AS_EMBEDDED_PARTS_OF_PNG_PAGE_BACKGROUND
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

### Convertir un PDF en page HTML contenant uniquement le corps

Cette fonction convertit un PDF au format HTML, en générant du contenu « body-only » sans balises supplémentaires 'html' ou 'head', et divise la sortie en pages séparées.

1. Chargez le document PDF en utilisant 'ap.Document'.
1. Créez 'HtmlSaveOptions' et configurez :
- 'html_markup_generation_mode = WRITE_ONLY_BODY_CONTENT' pour ne générer que le contenu du 'body'.
- 'split_into_pages' pour créer des fichiers HTML distincts pour chaque page du PDF.
1. Enregistrez le document au format HTML avec les options spécifiées.
1. Affichez un message de confirmation.

```python

from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    document = apdf.Document(path_infile)
    save_options = apdf.HtmlSaveOptions()
    save_options.html_markup_generation_mode = apdf.HtmlSaveOptions.HtmlMarkupGenerationModes.WRITE_ONLY_BODY_CONTENT
    save_options.split_into_pages = True
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

### Convertir un PDF en HTML avec rendu de texte transparent

Cette fonction convertit un PDF au format HTML, en rendant tout le texte transparent, y compris les textes ombrés, ce qui préserve la fidélité visuelle tout en permettant une mise en forme flexible dans le HTML de sortie.

1. Chargez le document PDF en utilisant 'ap.Document'.
1. Créez 'HtmlSaveOptions' et configurez :
- 'save_transparent_texts' pour rendre le texte normal transparent.
- 'save_shadowed_texts_as_transparent_texts' pour rendre le texte ombré transparent.
1. Enregistrez le document au format HTML avec le rendu de texte transparent.
1. Affichez un message de confirmation.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    document = apdf.Document(path_infile)
    save_options = apdf.HtmlSaveOptions()
    save_options.save_transparent_texts = True
    save_options.save_shadowed_texts_as_transparent_texts = True
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

### Convertir un PDF en HTML avec rendu des calques du document

Cette fonction convertit un PDF au format HTML, en préservant les calques du document en convertissant le contenu marqué en calques séparés dans le HTML de sortie. Cela permet aux éléments en couches (comme les annotations, arrière-plans et superpositions) d'être rendus avec précision.

1. Chargez le document PDF en utilisant 'ap.Document'.
1. Créez 'HtmlSaveOptions' et activez 'convert_marked_content_to_layers' pour préserver les calques.
1. Enregistrez le document au format HTML avec un contenu en calques.
1. Affichez un message de confirmation.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    document = apdf.Document(path_infile)
    save_options = apdf.HtmlSaveOptions()
    save_options.convert_marked_content_to_layers  = True
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```


