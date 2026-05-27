---
title: Essayer de concaténer des fichiers PDF
type: docs
weight: 70
url: /fr/python-net/try-concatenate-pdf-files/
description: Concaténez plusieurs fichiers PDF en utilisant Aspose.PDF for Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Fusionner des fichiers PDF en toute sécurité en Python avec la gestion des erreurs
Abstract: Apprenez comment concaténer en toute sécurité plusieurs fichiers PDF en utilisant Aspose.PDF for Python. La méthode try_concatenate tente de fusionner les PDF sans lever d'exceptions, permettant aux développeurs de gérer les échecs de manière élégante.
---

La fusion de fichiers PDF peut parfois échouer en raison de fichiers corrompus, de formats incompatibles ou d'autres problèmes. En utilisant Aspose.PDF for Python, vous pouvez utiliser la méthode try_concatenate de la [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) classe pour tenter en toute sécurité la concaténation. Au lieu de lever une exception, la méthode renvoie False si l'opération échoue, permettant une gestion contrôlée des erreurs dans les flux de travail automatisés. 

1. Créer un objet PdfFileEditor.
1. Tentative de concaténation de fichiers PDF.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


def try_concatenate_pdf_files(files_to_merge, output_file):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    if not pdf_editor.try_concatenate(files_to_merge, output_file):
        print("Concatenation failed for the provided files.")
```
