---
title: Vérifications d'intégrité de la signature
type: docs
weight: 70
url: /fr/python-net/signature-integrity-checks/
description: Apprenez comment vérifier si une signature PDF couvre l'intégralité du document et valider l'intégrité du document signé en utilisant PdfFileSignature en Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Valider la couverture et l'intégrité de la signature PDF en Python
Abstract: Cet article explique comment inspecter l'intégrité des signatures numériques dans les documents PDF signés avec Aspose.PDF for Python via .NET. Il montre comment vérifier si une signature couvre l'intégralité du document et comment valider l'intégrité du contenu signé.
---

Aspose.PDF for Python via .NET fournit le [PdfFileSignature](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) façade de validation des documents PDF signés. Après qu'un fichier a été signé, vous pouvez l'utiliser pour vérifier si la signature s'applique au document complet et si le contenu signé est toujours valide.

Cet exemple montre deux vérifications d'intégrité courantes :

1. Vérifiez si une signature couvre l'ensemble du document.
1. Validez l'intégrité du contenu PDF signé.

## Vérifiez si une signature couvre l'ensemble du document

Utiliser `covers_whole_document()` lorsque vous devez vérifier que la signature s'applique à l'intégralité du PDF et non seulement à une partie de son contenu. L'exemple lit le premier nom de signature disponible et vérifie sa portée.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def check_signature_coverage(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        covers_document = pdf_signature.covers_whole_document(sign_name)
        print(f"Signature '{sign_name}' covers the whole document: {covers_document}")
    finally:
        pdf_signature.close()
```

## Valider l'intégrité du document

Utiliser `verify_signed()` pour confirmer que le contenu du document signé n'a pas été altéré après l'application de la signature. Cette méthode aide à vérifier si le document reste valable pour la signature sélectionnée.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def validate_document_integrity(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        is_valid = pdf_signature.verify_signed(sign_name)
        print(f"Document integrity for '{sign_name}' is valid: {is_valid}")
    finally:
        pdf_signature.close()
```

