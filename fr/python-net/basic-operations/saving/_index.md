---
title: Enregistrer un document PDF de manière programmatique
linktitle: Enregistrer PDF
type: docs
weight: 30
url: /fr/python-net/save-pdf-document/
description: Apprenez comment enregistrer un fichier PDF en Python avec la bibliothèque Aspose.PDF pour Python via .NET. Enregistrez un document PDF sur le système de fichiers, vers un flux et dans les applications Web.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Enregistrement de documents PDF en utilisant la bibliothèque Aspose.PDF en Python
Abstract: L'article fournit des conseils sur l'enregistrement de documents PDF à l'aide de la bibliothèque Aspose.PDF en Python. Il présente trois méthodes principales pour enregistrer les PDF sur le système de fichiers, vers un flux, et dans des formats spécifiques comme PDF/A ou PDF/X. La méthode `save()` de la classe `Document` est centrale pour ces opérations. Pour enregistrer un PDF sur le système de fichiers, un document peut être créé ou manipulé, par exemple en ajoutant une nouvelle page, puis enregistré directement à un chemin. Pour enregistrer vers un flux, les surcharges de la méthode `Save` permettent d'écrire un document dans un objet flux. De plus, l'article explique comment enregistrer des documents aux formats PDF/A ou PDF/X, qui sont respectivement des normes d'archivage à long terme et d'échange graphique. Ce processus nécessite de préparer le document avec la méthode `convert` avant de l'enregistrer. Les extraits de code Python fournis illustrent chaque approche, montrant l'application pratique de ces méthodes.
---

## Enregistrer un document PDF sur le système de fichiers

Vous pouvez enregistrer le document PDF créé ou manipulé sur le système de fichiers en utilisant la méthode [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) de la classe [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

```python

    import aspose.pdf as ap

    document = ap.Document(input_pdf)
    # make some manipation, i.g add new empty page
    document.pages.add()
    document.save(output_pdf)
```

## Enregistrer un document PDF dans un flux

Vous pouvez également enregistrer le document PDF créé ou manipulé dans un flux en utilisant les surcharges des méthodes `Save`.

```python

    import aspose.pdf as ap

    document = ap.Document(input_pdf)
    # make some manipation, i.g add new empty page
    document.pages.add()
    document.save(io.FileIO(output_pdf, 'w'))
```

## Enregistrer le format PDF/A ou PDF/X

PDF/A est une version normalisée ISO du format de document portable (PDF) destinée à l'archivage et à la préservation à long terme de documents électroniques.
PDF/A diffère du PDF en ce qu'il interdit les fonctionnalités peu adaptées à l'archivage à long terme, telles que le lien de polices (par opposition à l'incorporation de polices) et le chiffrement. Les exigences ISO pour les lecteurs PDF/A incluent des directives de gestion des couleurs, la prise en charge des polices incorporées et une interface utilisateur permettant de lire les annotations incorporées.

PDF/X est un sous-ensemble de la norme ISO PDF. Le but de PDF/X est de faciliter l'échange graphique, et il comporte donc une série d'exigences liées à l'impression qui ne s'appliquent pas aux fichiers PDF standard.

Dans les deux cas, la méthode [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) est utilisée pour enregistrer les documents, tandis que les documents doivent être préparés à l'aide de la méthode [convert](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python

    import aspose.pdf as ap

    document = ap.Document(input_pdf)
    document.pages.add()
    document.convert(output_log, ap.PdfFormat.PDF_X_3, ap.ConvertErrorAction.DELETE)
    document.save(output_pdf)
```

