---
title: Convertir HTML en PDF en Python
linktitle: Convertir le fichier HTML en PDF
type: docs
weight: 40
url: /fr/python-net/convert-html-to-pdf/
lastmod: "2025-09-27"
description: Apprenez à convertir le contenu HTML en document PDF à l'aide d'Aspose.PDF pour Python via .NET
sitemap: 
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Comment convertir HTML en PDF en utilisant Aspose.PDF pour Python
Abstract: Aspose.PDF pour Python via .NET offre une solution robuste pour créer des fichiers PDF à partir de pages Web et de code HTML brut au sein des applications. Cet article propose un guide sur la conversion de HTML en PDF en utilisant Python, en détaillant l'utilisation d'Aspose.PDF pour Python, une API de manipulation de PDF qui permet une conversion fluide des documents HTML au format PDF. Le processus de conversion peut être personnalisé selon les besoins. L'article comprend un exemple de code Python démontrant le processus de conversion, qui implique la création d'une instance de la classe HtmlLoadOptions, l'initialisation d'un objet Document et l'enregistrement du document PDF de sortie à l'aide de la méthode Document.Save(). De plus, Aspose propose un outil en ligne pour convertir HTML en PDF, permettant aux utilisateurs d'explorer la fonctionnalité et la qualité du processus de conversion.
---

## Conversion HTML en PDF avec Python

**Aspose.PDF pour Python** est une API de manipulation PDF qui vous permet de convertir tout document HTML existant en PDF sans problème. Le processus de conversion de HTML en PDF peut être personnalisable de manière flexible.

## Convertir HTML en PDF

L'exemple de code Python suivant montre comment convertir un document HTML en PDF.

1. Créez une instance de la classe [HtmlLoadOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlloadoptions/).
1. Initialisez l'objet [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Enregistrez le document PDF de sortie en appelant la méthode **document.save()**.

```python

    from os import path
    import aspose.pdf as ap
    import requests
    import io

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.HtmlLoadOptions()
    load_options.page_layout_option = ap.HtmlPageLayoutOption.SCALE_TO_PAGE_WIDTH
    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Essayez de convertir HTML en PDF en ligne**

Aspose vous présente une application en ligne gratuite ["HTML to PDF"](https://products.aspose.app/html/en/conversion/html-to-pdf), où vous pouvez essayer d'examiner la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion HTML en PDF avec l'application gratuite](html.png)](https://products.aspose.app/html/en/conversion/html-to-pdf)
{{% /alert %}}

## Convertir HTML en PDF en utilisant le type média

Cet exemple montre comment convertir un fichier HTML en PDF en utilisant Aspose.PDF pour Python via .NET avec des options de rendu spécifiques.

1. Créez une instance de la classe [HtmlLoadOptions()](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlloadoptions/). Le 'html_media_type' applique les règles CSS destinées à l'affichage à l'écran. La propriété 'html_media_type' peut avoir plusieurs valeurs. Vous pouvez la définir sur HtmlMediaType.SCREEN ou HtmlMediaType.PRINT.
1. Chargez le HTML dans un ap.Document en utilisant les options de chargement.
1. Enregistrez le document au format PDF.

```python

    from os import path
    import aspose.pdf as ap
    import requests
    import io

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.HtmlLoadOptions()
    load_options.html_media_type = ap.HtmlMediaType.SCREEN
    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

## Convertir HTML en PDF avec règle CSS de priorité de page

Certains documents peuvent contenir des paramètres de mise en page qui utilisent [the Page rule](https://developer.mozilla.org/en-US/docs/Web/CSS/@page), ce qui peut créer des ambiguïtés lors de la génération du layout. Vous pouvez contrôler la priorité à l'aide de la propriété 'is_priority_css_page_rule'. Si cette propriété est définie sur 'True', la règle CSS est appliquée en premier.

1. Créez une instance de la classe [HtmlLoadOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlloadoptions/).
1. Définissez 'is_priority_css_page_rule = False' pour désactiver la priorité des règles CSS @page, permettant à d'autres styles de prévaloir.
1. Chargez le HTML dans un ap.Document avec les options configurées.
1. Enregistrez le document au format PDF.

```python

    from os import path
    import aspose.pdf as ap
    import requests
    import io

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.HtmlLoadOptions()
    # load_options.is_priority_css_page_rule = False
    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

## Convertir HTML en PDF avec des polices intégrées

Cet exemple montre comment convertir un fichier HTML en PDF tout en intégrant les polices. Si vous avez besoin d'un document PDF avec des polices intégrées, vous devez définir 'is_embed_fonts' sur True.

1. Créez 'HtmlLoadOptions()' pour configurer la conversion HTML vers PDF.
1. Définissez 'is_embed_fonts = True' pour garantir que toutes les polices utilisées dans le HTML sont intégrées directement dans le PDF, préservant la fidélité visuelle.
1. Chargez le HTML dans un ap.Document avec ces options.
1. Enregistrez le document au format PDF.

```python

    from os import path
    import aspose.pdf as ap
    import requests
    import io

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.HtmlLoadOptions()
    load_options.is_embed_fonts = True
    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

## Rendre le contenu sur une seule page lors de la conversion HTML en PDF

Cet exemple démontre comment convertir un fichier HTML en un PDF d'une seule page en utilisant Aspose.PDF pour Python.
Vous pouvez afficher tout le contenu sur une page unique en utilisant la propriété 'is_render_to_single_page'.

1. Créez une instance de 'HtmlLoadOptions()' pour configurer le processus de conversion.
1. Activez 'is_render_to_single_page' pour rendre tout le contenu HTML sur une seule page PDF continue.
1. Chargez le document avec les options configurées dans un 'ap.Document'.
1. Enregistrez le résultat sous forme de fichier PDF.

```python
    from os import path
    import aspose.pdf as ap
    import requests
    import io

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    options = ap.HtmlLoadOptions()
    options.is_render_to_single_page = True

    doc = ap.Document(path_infile, options)
    doc.save(path_outfile)
```

## Convertir MHTML en PDF

Cet exemple montre comment convertir un fichier MHT (MHTML) en document PDF en utilisant Aspose.PDF pour Python avec des dimensions de page spécifiques.

1. Créez une instance de ap.MhtLoadOptions() pour configurer le traitement du fichier MHT.
1. Définissez divers paramètres, tels que la taille de la page.
1. Initialisez le document avec le fichier d'entrée et les options de chargement configurées.
1. Enregistrez le document résultant au format PDF.

```python

    from os import path
    import aspose.pdf as ap
    import requests
    import io

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    load_options = ap.MhtLoadOptions()
    load_options.page_info.width = 842
    load_options.page_info.height= 1191
    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```
