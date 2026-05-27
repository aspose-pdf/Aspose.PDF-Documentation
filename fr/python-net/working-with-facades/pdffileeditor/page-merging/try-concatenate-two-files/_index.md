---
title: Essayer de concaténer deux fichiers PDF
type: docs
weight: 90
url: /fr/python-net/try-concatenate-two-files/
description: Concaténez deux fichiers PDF à l'aide d'Aspose.PDF for Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Fusionner deux fichiers PDF en toute sécurité en Python sans exceptions
Abstract: Apprenez comment concaténer en toute sécurité deux fichiers PDF à l'aide d'Aspose.PDF for Python. La méthode try_concatenate fusionne les fichiers sans lever d'exceptions, permettant une gestion d'erreurs souple en cas d'échec de l'opération.
---

Fusionner deux fichiers PDF peut parfois échouer en raison de corruption de fichiers, de formats incompatibles ou d'autres problèmes. En utilisant Aspose.PDF for Python, la méthode try_concatenate de la classe PdfFileEditor vous permet d'essayer de fusionner deux PDF en toute sécurité. Si l'opération échoue, elle renvoie False au lieu de lever une exception, vous donnant un contrôle total sur la gestion des erreurs dans les flux de travail automatisés ou le traitement par lots.

1. Créer un objet PdfFileEditor.
1. Tenter de fusionner deux fichiers PDF.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


def try_concatenate_two_files(files_to_merge, output_file):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    if not pdf_editor.try_concatenate(
        files_to_merge[0], files_to_merge[1], output_file
    ):
        print("Concatenation failed for the provided files.")
```
