---
title: Convertir PDF/A et PDF/UA en PDF en Python
linktitle: Convertir PDF/A et PDF/UA en PDF
type: docs
weight: 120
url: /fr/python-net/convert-pdf_x-to-pdf/
lastmod: "2026-05-22"
description: Apprenez comment supprimer la conformité PDF/A et PDF/UA des fichiers PDF en Python avec Aspose.PDF for Python via .NET et les enregistrer comme documents PDF standard.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Comment convertir PDF/A et PDF/UA en PDF standard en Python
Abstract: Cet article explique comment supprimer la conformité PDF/A et PDF/UA des documents PDF basés sur des normes en utilisant Aspose.PDF for Python via .NET. Il couvre les scénarios où vous pourriez avoir besoin d'un PDF standard au lieu d'un fichier d'archivage ou limité par l'accessibilité, et montre comment enregistrer le résultat après la suppression des métadonnées et des restrictions de conformité.
---

Utilisez cette page lorsque vous devez convertir un PDF basé sur des normes, tel que PDF/A ou PDF/UA, en un document PDF normal pour l'édition, le traitement ou la redistribution en aval.

Les PDF conformes aux normes sont utiles pour les flux de travail d'archivage, d'impression et d'accessibilité, mais dans certains cas vous pourriez devoir supprimer cette conformité avant d'intégrer le fichier dans d'autres systèmes ou pipelines. Aspose.PDF for Python via .NET vous permet de le faire de façon programmatique puis d'enregistrer le résultat en tant que fichier PDF standard.

## Convertir PDF/A en PDF

Cet exemple supprime les métadonnées et restrictions de conformité PDF/A d'un PDF afin que le document puisse être à nouveau enregistré en tant que fichier PDF ordinaire.

1. Chargez le document PDF en utilisant 'ap.Document'.
1. Appelez 'remove_pdfa_compliance()' pour supprimer tous les paramètres de conformité et métadonnées liés à PDF/A.
1. Enregistrez le PDF résultant vers le chemin de sortie.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDFA_to_PDF(infile, outfile):
    document = ap.Document(infile)
    document.remove_pdfa_compliance()
    document.save(outfile)
```

## Suppression de la conformité PDF/UA

Cet exemple montre comment retirer la conformité liée à PDF/UA afin que le document puisse être enregistré en tant que PDF standard pour des flux de travail ne ciblant pas l'accessibilité.

1. Chargez le document PDF en utilisant 'ap.Document()'.
1. Appelez 'document.remove_pdfa_compliance()' pour supprimer toutes les restrictions ou paramètres de conformité PDF/A.
1. Enregistrez le PDF modifié dans 'path_outfile'.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDFUA_to_PDF(infile, outfile):
    document = ap.Document(infile)
    document.remove_pdf_ua_compliance()
    document.save(outfile)
```

## Quand utiliser ce flux de travail

- Supprimez les paramètres de conformité avant d'envoyer un document dans une chaîne d'outils qui ne nécessite pas les restrictions PDF/A ou PDF/UA.
- Simplifiez le traitement en aval des documents lorsque les métadonnées d'archivage ou d'accessibilité ne sont plus nécessaires.
- Normalisez les PDF d’entrée avant de les exporter vers d’autres formats.

## Conversions associées

- [Convertir le PDF en PDF/A, PDF/E et PDF/X](/pdf/fr/python-net/convert-pdf-to-pdf_x/) si vous avez besoin du workflow inverse et souhaitez créer des PDF conformes aux normes.
- [Convertir le PDF en Word](/pdf/fr/python-net/convert-pdf-to-word/) pour une sortie de document modifiable après suppression des contraintes de conformité.
- [Convertir le PDF en HTML](/pdf/fr/python-net/convert-pdf-to-html/) pour une sortie adaptée aux navigateurs à partir de fichiers PDF standard.
