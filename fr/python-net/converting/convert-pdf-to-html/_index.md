---
title: Convertir PDF en HTML en Python
linktitle: Convertir PDF au format HTML
type: docs
weight: 50
url: fr/python-net/convert-pdf-to-html/
lastmod: "2021-11-01"
description: Ce sujet vous montre comment convertir un fichier PDF au format HTML avec la bibliothèque Aspose.PDF pour Python .NET.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Vue d'ensemble

Cet article explique comment **convertir un PDF en HTML en utilisant Python**. Il couvre ces sujets.

_Format_: **HTML**
- [Python PDF en HTML](#python-pdf-to-html)
- [Python Convertir PDF en HTML](#python-pdf-to-html)
- [Python Comment convertir un fichier PDF en HTML](#python-pdf-to-html)

## Convertir PDF en HTML

**Aspose.PDF pour Python via .NET** offre de nombreuses fonctionnalités pour convertir divers formats de fichiers en documents PDF et convertir des fichiers PDF en divers formats de sortie.
 Cet article explique comment convertir un fichier PDF en <abbr title="HyperText Markup Language">HTML</abbr>. Vous pouvez utiliser juste quelques lignes de code Python pour convertir un PDF en HTML. Vous pourriez avoir besoin de convertir un PDF en HTML si vous souhaitez créer un site web ou ajouter du contenu à un forum en ligne. Une façon de convertir un PDF en HTML est d'utiliser Python de manière programmatique.

{{% alert color="success" %}}
**Essayez de convertir un PDF en HTML en ligne**

Aspose.PDF pour Python vous propose une application en ligne gratuite ["PDF to HTML"](https://products.aspose.app/pdf/conversion/pdf-to-html), où vous pouvez essayer d'explorer la fonctionnalité et la qualité qu'elle offre.

[![Aspose.PDF Conversion PDF en HTML avec une application gratuite](pdf_to_html.png)](https://products.aspose.app/pdf/conversion/pdf-to-html)
{{% /alert %}}

<a name="csharp-pdf-to-html"><strong>Étapes : Convertir un PDF en HTML en Python</strong></a>

1. Créez une instance de l'objet [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) avec le document PDF source.
2. Enregistrez-le sur [HtmlSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlsaveoptions/) en appelant la méthode [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_html.html"
    # Ouvrir le document PDF
    document = ap.Document(input_pdf)

    # enregistrer le document au format HTML
    save_options = ap.HtmlSaveOptions()
    document.save(output_pdf, save_options)
```

## Voir Aussi

Cet article couvre également ces sujets. Les codes sont les mêmes que ci-dessus.

_Format_: **HTML**
- [Python PDF en Code HTML](#python-pdf-to-html)
- [Python PDF en API HTML](#python-pdf-to-html)
- [Python PDF en HTML Programmatiquement](#python-pdf-to-html)
- [Python PDF en Bibliothèque HTML](#python-pdf-to-html)
- [Python Enregistrer PDF comme HTML](#python-pdf-to-html)
- [Python Générer HTML à partir de PDF](#python-pdf-to-html)
- [Python Créer HTML à partir de PDF](#python-pdf-to-html)

- [Python Convertisseur PDF en HTML](#python-pdf-to-html)