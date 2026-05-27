---
title: Diviser les fichiers PDF en Python
linktitle: Diviser les fichiers PDF
type: docs
weight: 60
url: /fr/python-net/split-pdf/
description: Apprenez comment diviser les pages PDF en fichiers PDF distincts en Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Division des pages PDF à l'aide de Python
Abstract: L'article discute du processus de division des pages PDF en fichiers individuels à l'aide de Python, en soulignant l'utilité de cette fonctionnalité pour la gestion de gros documents PDF. Il fait référence à l'Aspose.PDF Splitter, un outil en ligne conçu pour démontrer la fonctionnalité de division de PDF. L'article fournit une méthode détaillée pour réaliser cela dans les applications Python, impliquant l'itération à travers les pages d'un document\u0027s via le \u0060Document\u0060 objet\u0027s \u0060PageCollection\u0060. Pour chaque page, un nouveau \u0060Document\u0060 objet est créé, la page est ajoutée à celui-ci, et le nouveau fichier PDF est enregistré en utilisant la méthode \u0060save()\u0060. Un extrait de code Python accompagnant illustre ce processus, montrant les étapes nécessaires pour diviser un document PDF en fichiers séparés en itérant à travers ses pages et en enregistrant chacune comme un PDF individuel.
---

Diviser les pages PDF peut être une fonctionnalité utile pour ceux qui souhaitent diviser un gros fichier en pages séparées ou en groupes de pages.

Utilisez ce flux de travail lorsque vous devez découper de gros PDF en fichiers d’une page ou en ensembles de documents plus petits pour la distribution, la révision ou le traitement en aval.

## Exemple en direct

[Aspose.PDF Splitter](https://products.aspose.app/pdf/splitter) est une application web en ligne gratuite qui vous permet d'examiner le fonctionnement de la fonctionnalité de découpage de présentation.

[![Aspose Split PDF](splitter.png)](https://products.aspose.app/pdf/splitter)

Ce sujet montre comment découper les pages PDF en fichiers PDF individuels dans vos applications Python. Pour découper les pages PDF en fichiers PDF d’une seule page en utilisant Python, les étapes suivantes peuvent être suivies :

1. Parcourez les pages du document PDF à travers le [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) objet [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) collection
1. Pour chaque itération, créez un nouvel objet Document et ajoutez l'élément individuel [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) objet dans le document vide
1. Enregistrez le nouveau PDF en utilisant [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) méthode

## Diviser un PDF en plusieurs fichiers ou PDF séparés en Python

Le fragment de code Python suivant vous montre comment diviser les pages d'un PDF en fichiers PDF individuels.

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

## Sujets liés au Document

- [Travailler avec des documents PDF en Python](/pdf/fr/python-net/working-with-documents/)
- [Fusionner des fichiers PDF en Python](/pdf/fr/python-net/merge-pdf-documents/)
- [Optimiser des fichiers PDF en Python](/pdf/fr/python-net/optimize-pdf/)
- [Manipuler des documents PDF en Python](/pdf/fr/python-net/manipulate-pdf-document/)

