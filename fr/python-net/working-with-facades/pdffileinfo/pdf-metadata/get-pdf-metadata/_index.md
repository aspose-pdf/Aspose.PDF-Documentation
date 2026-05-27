---
title: Obtenir les métadonnées PDF
type: docs
weight: 20
url: /fr/python-net/get-pdf-metadata/
description: Extraire et afficher les métadonnées des documents PDF à l'aide d'Aspose.PDF for Python.
lastmod: "2026-05-22"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Récupération des métadonnées PDF à l'aide d'Aspose.PDF for Python.
Abstract: Ce guide montre comment extraire et afficher les métadonnées des documents PDF à l'aide d'Aspose.PDF for Python. Vous apprendrez à accéder aux propriétés PDF standard telles que le titre, l'auteur, les mots‑clés, les dates de création/modification, ainsi qu'aux champs de métadonnées personnalisés. De plus, le guide couvre les vérifications de la validité du PDF, du chiffrement et du statut de portefeuille.
---

Les documents PDF contiennent souvent des métadonnées précieuses qui décrivent le contenu du document, la paternité et les autorisations. Aspose.PDF fournit une API pratique pour récupérer à la fois les propriétés de métadonnées standard et personnalisées. Cet extrait de code montre comment utiliser le [PdfFileInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileinfo/) classe pour inspecter les fichiers PDF de manière programmatique, y compris des exemples détaillés en Python.

1. Chargez le fichier PDF.
1. Récupérer les métadonnées standard.
1. Vérifier le statut du PDF et la sécurité.
1. Récupérer les métadonnées personnalisées.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def get_pdf_metadata(infile):

    # Get and display PDF information
    pdf_info = pdf_facades.PdfFileInfo(infile)
    print(f"Subject: {pdf_info.subject}")
    print(f"Title: {pdf_info.title}")
    print(f"Keywords: {pdf_info.keywords}")
    print(f"Creator: {pdf_info.creator}")
    print(f"Creation Date: {pdf_info.creation_date}")
    print(f"Modification Date: {pdf_info.mod_date}")

    # Check PDF status
    print(f"Is Valid PDF: {pdf_info.is_pdf_file}")
    print(f"Is Encrypted: {pdf_info.is_encrypted}")
    print(f"Has Open Password: {pdf_info.has_open_password}")
    print(f"Has Edit Password: {pdf_info.has_edit_password}")
    print(f"Is Portfolio: {pdf_info.has_collection}")

    # Retrieve and display a specific custom attribute
    reviewer = pdf_info.get_meta_info("Reviewer")
    print(f"Reviewer: {reviewer if reviewer else 'No Reviewer metadata found.'}")
```
