---
title: Gestion des signatures
type: docs
weight: 80
url: /fr/python-net/signature-management/
description: Apprenez à supprimer les signatures numériques des documents PDF et, si vous le souhaitez, à nettoyer les champs de signature à l’aide de PdfFileSignature en Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Supprimer les signatures PDF et nettoyer les champs de signature en Python
Abstract: Cet article explique comment gérer les signatures numériques existantes dans les documents PDF avec Aspose.PDF for Python via .NET. Il montre comment supprimer une signature d’un PDF et comment supprimer une signature ainsi que son champ de signature associé.
---

Aspose.PDF for Python via .NET fournit le [PdfFileSignature](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) facade pour travailler avec les signatures numériques existantes dans les documents PDF. En plus de lire et de valider les signatures, vous pouvez également les supprimer lorsqu’un flux de travail nécessite la mise à jour du contenu signé ou l’effacement du champ de signature.

Cet exemple illustre deux tâches courantes de gestion des signatures :

1. Supprimer une signature d'un document PDF.
1. Supprimer une signature et nettoyer le champ de signature associé.

## Supprimer une signature d'un PDF

Utiliser `remove_signature()` Lorsque vous souhaitez supprimer la signature sélectionnée du document tout en conservant la structure du champ de signature sous-jacente. L'exemple ouvre le PDF signé, résout le nom de la signature, la supprime et enregistre le fichier de sortie mis à jour.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def remove_signature_from_pdf(infile, outfile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        pdf_signature.remove_signature(sign_name)
        pdf_signature.save(outfile)
    finally:
        pdf_signature.close()
```

## Supprimer une signature et nettoyer le champ

Utilisez la surcharge avec le supplémentaire `True` indiquez lorsque vous souhaitez supprimer la signature et également nettoyer le champ de signature associé. Cela est utile lorsque le champ ne doit pas rester dans le document après la suppression de la signature.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def remove_signature_with_field_cleanup(infile, outfile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        pdf_signature.remove_signature(sign_name, True)
        pdf_signature.save(outfile)
    finally:
        pdf_signature.close()
```
