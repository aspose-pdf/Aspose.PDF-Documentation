---
title: Gestion des droits d\'utilisation
type: docs
weight: 100
url: /fr/python-net/usage-rights-management/
description: Apprenez comment détecter et supprimer les droits d\'utilisation des documents PDF à l\'aide de PdfFileSignature en Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Supprimer les droits d\'utilisation PDF en Python
Abstract: Cet article explique comment inspecter et supprimer les droits d\'utilisation des documents PDF avec Aspose.PDF for Python via .NET. Il montre comment vérifier si un PDF contient des droits d\'utilisation et comment enregistrer une nouvelle version du document après la suppression de ces droits.
---

Aspose.PDF for Python via .NET fournit le [PdfFileSignature](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) façade pour travailler avec des PDF signés et les paramètres de droits d\'utilisation associés. Dans certains flux de travail, il peut être nécessaire d\'inspecter si un document contient des droits d\'utilisation et de les supprimer avant d\'enregistrer une version mise à jour du fichier.

Cet exemple illustre une tâche courante de gestion des droits d\'utilisation :

1. Vérifiez si un PDF contient des droits d'utilisation.
1. Supprimez les droits d'utilisation du document.
1. Enregistrez le fichier PDF mis à jour.

## Vérifiez si le PDF contient des droits d'utilisation

Avant de supprimer les droits d'utilisation, l'exemple vérifie l'état actuel du document en appelant `contains_usage_rights()`. Cela vous permet de confirmer si les droits d'utilisation sont présents avant d'apporter des modifications.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def check_usage_rights(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        had_usage_rights = pdf_signature.contains_usage_rights()
        print(f"PDF contains usage rights: {had_usage_rights}")
    finally:
        pdf_signature.close()
```

## Supprimer les droits d'utilisation du PDF

Utiliser `remove_usage_rights()` lorsque le document ne doit plus conserver ses paramètres de droits d’utilisation existants. L’exemple vérifie l’état initial, supprime les droits et enregistre le PDF mis à jour dans un nouveau fichier.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def remove_usage_rights(infile, outfile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        had_usage_rights = pdf_signature.contains_usage_rights()
        print(f"PDF contains usage rights before removal: {had_usage_rights}")
        pdf_signature.remove_usage_rights()
        pdf_signature.save(outfile)
    finally:
        pdf_signature.close()
```
