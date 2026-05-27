---
title: Obtenir les privilèges du document
type: docs
weight: 10
url: /fr/python-net/get-document-privileges/
description: Apprenez comment vérifier programmatiquement les privilèges d’un document PDF à l’aide d’Aspose.PDF pour Python. Ce tutoriel montre comment utiliser la classe PdfFileInfo pour lire les paramètres de sécurité du document, tels que les autorisations d’impression, de copie ou de modification.
lastmod: "2026-05-22"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Récupérer les privilèges du document PDF à l’aide d’Aspose.PDF pour Python
Abstract: Les documents PDF peuvent comporter des restrictions de sécurité qui limitent des actions telles que l’impression, la copie, la modification ou le remplissage de formulaires. En accédant à ces privilèges programmatiquement, les développeurs peuvent déterminer quelles opérations sont autorisées sur un PDF. Ce guide montre comment utiliser la classe PdfFileInfo pour récupérer les privilèges du document PDF et les afficher en Python.
---

Les privilèges PDF contrôlent ce que les utilisateurs peuvent ou ne peuvent pas faire avec un document. Les autorisations courantes incluent :

- Imprimer le document
- Copie du contenu
- Modification des annotations ou du contenu
- Remplissage des champs de formulaire
- Utilisation des lecteurs d'écran
- Assemblage ou fusion de documents

Avec Aspose.PDF for Python, vous pouvez inspecter ces paramètres de manière programmatique en utilisant le [PdfFileInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileinfo/) classe. Ceci est particulièrement utile lors du travail avec plusieurs PDFs dans des flux de travail automatisés, lors de la vérification de la conformité, ou du contrôle de la gestion des documents dans les applications.

1. Charger un fichier PDF.
1. Récupérer les privilèges du document.
1. Afficher les actions autorisées pour le document.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def get_document_privileges(input_file_name):
    pdf_metadata = pdf_facades.PdfFileInfo(input_file_name)

    privileges = pdf_metadata.get_document_privilege()

    print("Document Privileges:")
    print(f"  Can Print: {privileges.allow_print}")
    print(f"  Can Degraded Print: {privileges.allow_degraded_printing}")
    print(f"  Can Copy: {privileges.allow_copy}")
    print(f"  Can Modify Contents: {privileges.allow_modify_contents}")
    print(f"  Can Modify Annotations: {privileges.allow_modify_annotations}")
    print(f"  Can Fill In: {privileges.allow_fill_in}")
    print(f"  Can Screen Readers: {privileges.allow_screen_readers}")
    print(f"  Can Assembly: {privileges.allow_assembly}")
```
