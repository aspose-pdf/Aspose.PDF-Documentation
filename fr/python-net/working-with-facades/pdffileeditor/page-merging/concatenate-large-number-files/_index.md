---
title: Concaténer un grand nombre de fichiers PDF
type: docs
weight: 10
url: /fr/python-net/concatenate-large-number-files/
description: Fusionnez un grand nombre de fichiers PDF efficacement à l'aide d'Aspose.PDF for Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Concaténer de grands fichiers PDF en Python en utilisant la mise en mémoire tampon sur disque
Abstract: Découvrez comment fusionner un grand nombre de fichiers PDF efficacement à l'aide d'Aspose.PDF for Python. Cet exemple montre comment activer la mise en mémoire tampon sur disque pour gérer de gros PDF sans épuiser la mémoire du système, assurant une concaténation fluide de nombreux fichiers.
---

Lorsque vous travaillez avec de grandes collections de fichiers PDF, la consommation de mémoire peut devenir un goulot d'étranglement lors de la concaténation. En utilisant Aspose.PDF for Python, vous pouvez activer la mise en mémoire tampon sur disque dans la [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) classe pour fusionner de nombreux PDF efficacement. La méthode concatenate combine les fichiers d'entrée en un seul PDF tandis que le tampon sur disque empêche une forte utilisation de la mémoire. Cette approche est idéale pour le traitement de documents en masse, la génération de rapports automatisés, ou la consolidation de grandes archives PDF.

1. Créer un objet PdfFileEditor.
1. Fusionner plusieurs fichiers PDF.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


def concatenate_large_number_files(files_to_merge, output_file):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    pdf_editor.use_disk_buffer = True  # Enable disk buffering for large files
    pdf_editor.concatenate(files_to_merge, output_file)
```
