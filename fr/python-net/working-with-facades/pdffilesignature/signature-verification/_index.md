---
title: Vérification de la signature
type: docs
weight: 90
url: /fr/python-net/signature-verification/
description: Apprenez comment vérifier les signatures numériques et vérifier si un PDF contient des signatures en utilisant PdfFileSignature en Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Vérifier les signatures PDF en Python
Abstract: Cet article explique comment vérifier les signatures numériques dans les documents PDF avec Aspose.PDF for Python via .NET. Il montre comment valider une signature existante et comment vérifier si un PDF contient des signatures.
---

Aspose.PDF for Python via .NET fournit le [PdfFileSignature](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) façade pour la validation de documents PDF signés. Après qu’un PDF a été signé, vous pouvez l’utiliser pour confirmer qu’une signature est valide et détecter si le document contient des entrées de signature.

Cet exemple démontre deux tâches de vérification courantes :

1. Vérifiez qu’une signature PDF existante est valide.
1. Vérifiez si un PDF contient des signatures.

## Vérifier une signature PDF

Utiliser `verify_signature()` lorsque vous devez valider une signature spécifique dans le document. L'exemple résout le premier nom de signature disponible et vérifie si cette signature est valide.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def verify_pdf_signature(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        is_valid = pdf_signature.verify_signature(sign_name)
        print(f"Signature '{sign_name}' is valid: {is_valid}")
    finally:
        pdf_signature.close()
```

## Vérifier si un PDF contient des signatures

Utiliser `contains_signature()` Lorsque vous avez simplement besoin de savoir si le PDF contient des signatures du tout. Ceci est utile comme vérification rapide avant d'exécuter une logique de vérification ou d'extraction plus détaillée.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def check_if_pdf_contains_signatures(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        contains_signatures = pdf_signature.contains_signature()
        print(f"PDF contains signatures: {contains_signatures}")
    finally:
        pdf_signature.close()
```
