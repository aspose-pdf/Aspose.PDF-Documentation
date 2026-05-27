---
title: Informations sur la signature
type: docs
weight: 60
url: /fr/python-net/signature-information/
description: Apprenez comment lire les noms de signature, les détails du signataire, les horodatages et les métadonnées de signature à partir de fichiers PDF signés en utilisant PdfFileSignature en Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Lire les détails de la signature des documents PDF en Python
Abstract: Cet article explique comment inspecter les métadonnées de signature dans les documents PDF signés avec Aspose.PDF for Python via .NET. Il montre comment lister les noms de signature, lire les détails du signataire, obtenir la date et l'heure de la signature, et extraire la raison et le lieu de la signature.
---

Aspose.PDF for Python via .NET fournit le [PdfFileSignature](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) façade d'inspection des signatures numériques dans les documents PDF. Après qu'un document a été signé, vous pouvez l'utiliser pour lire les noms des signatures et récupérer les métadonnées telles que le nom du signataire, les coordonnées, l'heure de signature, le motif et le lieu.

Cet exemple montre quatre tâches courantes liées aux informations de signature :

1. Lister tous les noms de signature dans un PDF signé.
1. Lire les détails du signataire pour une signature sélectionnée.
1. Obtenez la date et l'heure de la signature.
1. Lisez le motif et le lieu de la signature.

## Obtenez les noms des signatures

Utilisez cette méthode lorsqu'un PDF peut contenir une ou plusieurs signatures et que vous souhaitez inspecter les entrées de signature disponibles. L'exemple ouvre le document et imprime la liste renvoyée par `get_sign_names()`.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def get_signature_names(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        signature_names = list_signature_names(pdf_signature)
        print(f"Signature Names: {signature_names}")
    finally:
        pdf_signature.close()
```

## Obtenir les détails du signataire

Une fois que vous connaissez le nom de la signature, vous pouvez récupérer les métadonnées spécifiques au signataire. Cet exemple lit le nom du signataire et les informations de contact pour la première signature disponible dans le document.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def get_signer_details(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        signer_name = pdf_signature.get_signer_name(sign_name)
        contact_info = pdf_signature.get_contact_info(sign_name)
        print(
            f"Signer Details for '{sign_name}': "
            f"signer_name={signer_name}, contact_info={contact_info}"
        )
    finally:
        pdf_signature.close()
```

## Obtenir la date et l'heure de la signature

Utiliser `get_date_time()` pour déterminer quand une signature spécifique a été appliquée. Ceci est utile pour l'audit et pour afficher l'historique des signatures dans les flux de travail des documents.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def get_signature_date_and_time(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        signature_date = pdf_signature.get_date_time(sign_name)
        print(f"Signature Date and Time for '{sign_name}': {signature_date}")
    finally:
        pdf_signature.close()
```

## Obtenir la raison et l'emplacement de la signature

Les signatures numériques peuvent également stocker des métadonnées descriptives telles que la raison et l'emplacement de la signature. Cet exemple récupère les deux valeurs pour la signature sélectionnée et les imprime ensemble.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def get_signature_reason_and_location(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        signature_reason = pdf_signature.get_reason(sign_name)
        signature_location = pdf_signature.get_location(sign_name)
        print(
            f"Signature Reason and Location for '{sign_name}': "
            f"reason={signature_reason}, location={signature_location}"
        )
    finally:
        pdf_signature.close()
```

