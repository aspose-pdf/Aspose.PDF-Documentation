---
title: Enregistrer un document PDF par programmation
linktitle: Enregistrer le PDF
type: docs
weight: 30
url: /fr/python-net/save-pdf-document/
description: Apprenez comment enregistrer un fichier PDF avec la bibliothèque Python Aspose.PDF for Python via .NET. Enregistrez le document PDF sur le système de fichiers, dans un flux, et dans les applications Web.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Enregistrement de documents PDF à l'aide de la bibliothèque Aspose.PDF en Python
Abstract: L'article fournit des conseils sur la sauvegarde de documents PDF à l'aide de la bibliothèque Aspose.PDF en Python. Il présente trois méthodes principales pour enregistrer les PDF – sur le système de fichiers, dans un flux, et dans des formats spécifiques tels que PDF/A ou PDF/X. La méthode `save()` de la classe `Document` est centrale pour ces opérations. Pour enregistrer un PDF sur le système de fichiers, un document peut être créé ou manipulé, par exemple en ajoutant une nouvelle page, puis enregistré directement à un chemin. Pour enregistrer dans un flux, les surcharges de la méthode `Save` permettent d'écrire un document dans un objet flux. De plus, l'article explique comment enregistrer les documents aux formats PDF/A ou PDF/X, qui sont des normes respectivement pour l'archivage à long terme et l'échange graphique. Ce processus nécessite de préparer le document avec la méthode `convert` avant de l'enregistrer. Les extraits de code Python fournis démontrent chaque approche, illustrant l'application pratique de ces méthodes.
---

## Enregistrer le document PDF sur le système de fichiers

Vous pouvez enregistrer le document PDF créé ou manipulé sur le système de fichiers en utilisant [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) méthode de [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) classe.

```python
import aspose.pdf as ap

def save_document_to_file(infile, outfile):
    document = ap.Document(infile)
    # make some manipulation, e.g. add new empty page
    document.pages.add()
    document.save(outfile)
```

## Enregistrer le document PDF dans un flux

Vous pouvez également enregistrer le PDF créé ou manipulé dans un flux en utilisant les surcharges de `Save` méthodes.

```python
import aspose.pdf as ap
import io

def save_document_to_stream(infile, outfile):
    document = ap.Document(infile)
    # make some manipulation, e.g. add new empty page
    document.pages.add()
    with io.FileIO(outfile, 'w') as stream:
        document.save(stream)
```

## Enregistrer le format PDF/A ou PDF/X

Vous pouvez facilement enregistrer un document dans une version spécifique du PDF, comme PDF/A ou PDF/X. Dans ce cas, nous devons appeler la méthode convert avant d'enregistrer le document.

PDF/A est une version normalisée ISO du Portable Document Format (PDF) destinée à l'archivage et à la conservation à long terme des documents électroniques.
PDF/A diffère du PDF en ce qu'il interdit les fonctionnalités non adaptées à l'archivage à long terme, telles que le liaison de police (par opposition à l'intégration de police) et le chiffrement. Les exigences ISO pour les visionneuses PDF/A comprennent les directives de gestion des couleurs, la prise en charge des polices intégrées et une interface utilisateur pour la lecture des annotations incorporées.

PDF/X est un sous-ensemble de la norme ISO PDF. Le but de PDF/X est de faciliter l'échange graphique, et il comporte donc une série d'exigences liées à l'impression qui ne s'appliquent pas aux fichiers PDF standard.

Dans les deux cas, le [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) méthode est utilisée pour stocker les documents, tandis que les documents doivent être préparés en utilisant le [convert](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) méthode.

```python
import aspose.pdf as ap
import io


def save_document_as_standard(infile, outfile, logfile):
    document = ap.Document(infile)
    document.pages.add()
    document.convert(logfile, ap.PdfFormat.PDF_X_3, ap.ConvertErrorAction.DELETE)
    document.save(outfile)
```
