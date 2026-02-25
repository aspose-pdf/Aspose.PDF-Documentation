---
title: Diviser un PDF programmément en Python
linktitle: Diviser des fichiers PDF
type: docs
weight: 60
url: /fr/python-net/split-pdf-document/
description: Ce sujet montre comment diviser les pages d’un PDF en fichiers PDF individuels dans vos applications Python.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Division des pages PDF à l’aide de Python
Abstract: L’article discute du processus de division des pages PDF en fichiers individuels à l’aide de Python, soulignant l’utilité d’une telle fonctionnalité pour gérer de grands documents PDF. Il fait référence à l’Aspose.PDF Splitter, un outil en ligne conçu pour démontrer la fonctionnalité de division de PDF. L’article fournit une méthode détaillée pour réaliser cela dans les applications Python, impliquant l’itération à travers les pages d’un document PDF via la collection `PageCollection` de l’objet `Document`. Pour chaque page, un nouvel objet `Document` est créé, la page y est ajoutée, et le nouveau fichier PDF est enregistré à l’aide de la méthode `save()`. Un extrait de code Python accompagne le tout, illustrant ce processus, montrant les étapes nécessaires pour diviser un document PDF en fichiers séparés en parcourant ses pages et en enregistrant chacune en tant que PDF individuel.
---

Diviser les pages PDF peut être une fonctionnalité utile pour ceux qui souhaitent scinder un gros fichier en pages séparées ou en groupes de pages.

## Exemple en direct

[Aspose.PDF Splitter](https://products.aspose.app/pdf/splitter) est une application web gratuite en ligne qui vous permet d'examiner comment fonctionne la fonctionnalité de division de PDF.

[![Aspose Split PDF](splitter.png)](https://products.aspose.app/pdf/splitter)

Ce sujet montre comment diviser les pages PDF en fichiers PDF individuels dans vos applications Python. Pour diviser les pages PDF en fichiers PDF d’une seule page à l’aide de Python, les étapes suivantes peuvent être suivies :

1. Parcourez les pages du document PDF via la collection [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) de l’objet [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)
1. Pour chaque itération, créez un nouvel objet Document et ajoutez l’objet [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) individuel dans le document vide
1. Enregistrez le nouveau PDF à l’aide de la méthode [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods)

## Diviser le PDF en plusieurs fichiers ou PDF séparés en Python

Le fragment de code Python suivant vous montre comment diviser les pages PDF en fichiers PDF individuels.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    page_count = 1

    # Loop through all the pages
    for pdfPage in document.pages:
        new_document = ap.Document()
        new_document.pages.add(pdfPage)
        new_document.save(output_path + "_page_" + str(page_count) + ".pdf")
        page_count = page_count + 1
```


