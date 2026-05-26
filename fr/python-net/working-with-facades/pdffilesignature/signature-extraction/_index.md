---
title: Extraction de signature
type: docs
weight: 50
url: /fr/python-net/signature-extraction/
description: Apprenez comment extraire une image de signature et le certificat de signature d'un PDF signé à l'aide de PdfFileSignature en Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extraire l'image de signature et le certificat d'un PDF en Python
Abstract: Cet article explique comment extraire les données liées à la signature des documents PDF signés avec Aspose.PDF for Python via .NET. Il montre comment lire la première signature disponible, exporter son image et enregistrer le flux du certificat associé dans un fichier de sortie.
---

Aspose.PDF for Python via .NET fournit le [PdfFileSignature](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) façade pour inspecter et extraire des données à partir de documents PDF signés. Après qu'un PDF a été signé, vous pouvez l'utiliser pour exporter les ressources de signature telles que l'image visuelle de la signature et le certificat associé à la signature.

Cet exemple illustre deux tâches d'extraction courantes:

1. Extraire l'image visuelle associée à une signature.
1. Extraire le certificat de signature d'un PDF signé.

## Extraire une image de signature

Utilisez cette méthode lorsque le PDF contient une signature visible et que vous souhaitez exporter ses données d'image. L'exemple ouvre le document signé, récupère le premier nom de signature disponible, extrait le flux d'image et l'écrit dans un fichier.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def extract_signature_image(infile, outfile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        signature_image = pdf_signature.extract_image(sign_name)
        write_stream_data(signature_image, outfile)
    finally:
        pdf_signature.close()
```

## Extraire un certificat de signature

Utiliser `extract_certificate()` lorsque vous avez besoin des données du certificat jointes à une signature. Ceci est utile pour l'inspection, les flux de travail de validation ou le stockage du certificat du signataire séparément du document PDF.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def extract_signature_certificate(infile, outfile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        signature_certificate = pdf_signature.extract_certificate(sign_name)
        write_stream_data(signature_certificate, outfile)
    finally:
        pdf_signature.close()
```

