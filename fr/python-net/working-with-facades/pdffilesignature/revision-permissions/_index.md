---
title: Révision et autorisations
type: docs
weight: 40
url: /fr/python-net/revision-permissions/
description: Apprenez à inspecter les révisions de signature, les révisions de document et les autorisations de certification dans les fichiers PDF en utilisant PdfFileSignature en Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Lire les données de révision de signature PDF et les autorisations d'accès en Python
Abstract: Cet article explique comment inspecter les informations de révision et d'autorisation dans les fichiers PDF signés ou certifiés avec Aspose.PDF for Python via .NET. Il montre comment obtenir le numéro de révision d'une signature, compter le nombre total de révisions du document et lire les autorisations d'accès d'un PDF certifié.
---

Aspose.PDF for Python via .NET fournit le [PdfFileSignature](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) façade pour travailler avec des documents PDF signés et certifiés. En plus d’ajouter des signatures, vous pouvez également inspecter les métadonnées de signature afin de comprendre combien de révisions un document contient et quels changements sont autorisés après la certification.

Cet exemple démontre trois tâches d’inspection courantes :

1. Obtenez le numéro de révision d’une signature existante.
1. Obtenez le nombre total de révisions dans un document signé.
1. Lire les autorisations d'accès d'un PDF certifié.

## Obtenir le numéro de révision d'une signature

Utilisez cette approche lorsqu'un PDF contient déjà une ou plusieurs signatures et que vous devez identifier la révision associée à une signature spécifique. L'exemple résout le premier nom de signature disponible, puis appelle `get_revision()`.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def get_signature_revision(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        signature_revision = pdf_signature.get_revision(sign_name)
        print(f"Signature Revision for '{sign_name}': {signature_revision}")
    finally:
        pdf_signature.close()
```

## Obtenir le nombre total de révisions du document

Utiliser `get_total_revision()` lorsque vous avez besoin de savoir combien de révisions sont stockées dans le PDF signé. Cela est utile pour vérifier si le document a subi plusieurs mises à jour après l'application de la signature d'origine.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def get_total_document_revisions(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        total_revisions = pdf_signature.get_total_revision()
        print(f"Total Document Revisions: {total_revisions}")
    finally:
        pdf_signature.close()
```

## Obtenir les autorisations d'accès d'un PDF certifié

Les documents certifiés peuvent définir quels changements sont autorisés après la certification. Utilisez `get_access_permissions()` pour inspecter ce niveau d'autorisation et déterminer si le document autorise aucune modification, le remplissage de formulaires ou d'autres modifications contrôlées.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def get_access_permissions(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        access_permissions = pdf_signature.get_access_permissions()
        print(f"Access Permissions: {access_permissions}")
    finally:
        pdf_signature.close()
```

