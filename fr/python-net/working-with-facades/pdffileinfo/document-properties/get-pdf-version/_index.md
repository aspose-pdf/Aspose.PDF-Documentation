---
title: Obtenir la version PDF
type: docs
weight: 20
url: /fr/python-net/get-pdf-version/
description: Apprenez comment déterminer programmatique la version d'un document PDF en utilisant Aspose.PDF for Python. Ce tutoriel montre comment utiliser la classe PdfFileInfo pour vérifier la version PDF d'un fichier.
lastmod: "2026-05-22"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Récupérer la version PDF à l'aide d'Aspose.PDF for Python
Abstract: Les documents PDF possèdent des numéros de version qui indiquent les fonctionnalités et les spécifications qu'ils prennent en charge (par ex., 1.4, 1.7, 2.0). Connaître la version du PDF est important pour la compatibilité, le support des fonctionnalités et les flux de travail de traitement des documents. Dans ce guide, vous apprendrez comment récupérer la version PDF de manière programmatique en utilisant la classe PdfFileInfo dans Aspose.PDF for Python.
---

Les versions PDF définissent les fonctionnalités et capacités prises en charge dans un document, y compris les champs de formulaire, le chiffrement, les annotations et la compression. Pour les développeurs travaillant avec plusieurs PDF, vérifier la version assure la compatibilité avec les outils, bibliothèques ou flux de travail qui traitent ces fichiers.

Avec Aspose.PDF for Python, vous pouvez facilement inspecter la version PDF avec le [PdfFileInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileinfo/) classe.

1. Chargez un document PDF.
1. Récupérez sa version PDF.
1. Affichez la version dans la console.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def get_pdf_version(input_file_name):

    pdf_metadata = pdf_facades.PdfFileInfo(input_file_name)
    version = pdf_metadata.get_pdf_version()
    print(f"\nPDF Version: {version}")
```
