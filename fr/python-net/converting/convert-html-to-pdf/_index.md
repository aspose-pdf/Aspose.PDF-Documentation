---
title: Convertir HTML en PDF en Python
linktitle: Convertir un fichier HTML en PDF
type: docs
weight: 40
url: /fr/python-net/convert-html-to-pdf/
lastmod: "2022-12-22"
description: Ce sujet vous montre comment convertir HTML en PDF et MHTML en PDF en utilisant Aspose.PDF. pour Python.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Aperçu

Aspose.PDF pour Python via .NET est une solution professionnelle qui vous permet de créer des fichiers PDF à partir de pages web et de code HTML brut dans vos applications.

Cet article explique comment **convertir HTML en PDF en utilisant Python**. Il couvre les sujets suivants.

_Format_: **HTML**
- [Python HTML en PDF](#python-html-to-pdf)
- [Python Convertir HTML en PDF](#python-html-to-pdf)
- [Python Comment convertir HTML en PDF](#python-html-to-pdf)

## Conversion de HTML en PDF avec Python

**Aspose.PDF pour Python** est une API de manipulation PDF qui vous permet de convertir n'importe quel document HTML existant en PDF sans effort. Le processus de conversion de HTML en PDF peut être personnalisé de manière flexible.

## Convertir HTML en PDF

L'exemple de code Python suivant montre comment convertir un document HTML en PDF.

1. Créez une instance de la classe [HtmlLoadOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlloadoptions/).
2. Initialisez l'objet [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
3. Enregistrez le document PDF de sortie en appelant la méthode **Document.Save()**.

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "little_html.html"
    output_pdf = DIR_OUTPUT + "convert_html_to_pdf.pdf"
    options = ap.HtmlLoadOptions()
    document = ap.Document(input_pdf, options)
    document.save(output_pdf)
```

{{% alert color="success" %}}
**Essayez de convertir HTML en PDF en ligne**

Aspose vous présente une application gratuite en ligne ["HTML to PDF"](https://products.aspose.app/html/en/conversion/html-to-pdf), où vous pouvez essayer d'explorer la fonctionnalité et la qualité avec lesquelles elle fonctionne.

[![Aspose.PDF Conversion HTML en PDF en utilisant l'application gratuite](html.png)](https://products.aspose.app/html/en/conversion/html-to-pdf)
{{% /alert %}}