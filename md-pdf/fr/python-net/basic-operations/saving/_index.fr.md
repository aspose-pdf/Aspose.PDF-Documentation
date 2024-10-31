---
title: Sauvegarder le document PDF par programmation
linktitle: Sauvegarder PDF
type: docs
weight: 30
url: /python-net/save-pdf-document/
description: Apprenez à sauvegarder un fichier PDF dans la bibliothèque Aspose.PDF pour Python via .NET. Sauvegardez le document PDF dans le système de fichiers, dans un flux, et dans les applications Web.
lastmod: "2022-12-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Sauvegarder le document PDF dans le système de fichiers

Vous pouvez sauvegarder le document PDF créé ou manipulé dans le système de fichiers en utilisant la méthode [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) de la classe [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

```python

    import aspose.pdf as ap

    document = ap.Document(input_pdf)
    # faire quelques manipulations, par exemple ajouter une nouvelle page vide
    document.pages.add()
    document.save(output_pdf)
```

## Sauvegarder le document PDF dans un flux

Vous pouvez également sauvegarder le document PDF créé ou manipulé dans un flux en utilisant les surcharges des méthodes `Save`.

```python

    import aspose.pdf as ap

    document = ap.Document(input_pdf)
    # faire quelques manipulations, par exemple ajouter une nouvelle page vide
    document.pages.add()
    document.save(io.FileIO(output_pdf, 'w'))
```


## Enregistrer au format PDF/A ou PDF/X

PDF/A est une version du Format de Document Portable (PDF) normalisée par l'ISO pour une utilisation dans l'archivage et la préservation à long terme des documents électroniques.  
PDF/A diffère du PDF en ce qu'il interdit les fonctionnalités non adaptées à l'archivage à long terme, telles que le lien de polices (par opposition à l'incorporation de polices) et le chiffrement. Les exigences ISO pour les visionneuses PDF/A incluent des directives de gestion des couleurs, la prise en charge des polices incorporées et une interface utilisateur pour la lecture des annotations incorporées.

PDF/X est un sous-ensemble de la norme ISO PDF. Le but de PDF/X est de faciliter l'échange graphique et il comporte donc une série d'exigences liées à l'impression qui ne s'appliquent pas aux fichiers PDF standards.

Dans les deux cas, la méthode [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) est utilisée pour stocker les documents, tandis que les documents doivent être préparés à l'aide de la méthode [convert](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python

    import aspose.pdf as ap

    document = ap.Document(input_pdf)
    document.pages.add()
    document.convert(output_log, ap.PdfFormat.PDF_X_3, ap.ConvertErrorAction.DELETE)
    document.save(output_pdf)
```