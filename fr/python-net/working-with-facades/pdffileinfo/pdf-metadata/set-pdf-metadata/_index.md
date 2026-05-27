---
title: Définir les métadonnées PDF
type: docs
weight: 50
url: /fr/python-net/set-pdf-metadata/
description: Modifier et enregistrer les métadonnées dans les documents PDF en utilisant Aspose.PDF for Python via .NET.
lastmod: "2026-05-22"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Mise à jour des métadonnées PDF à l'aide d'Aspose.PDF for Python
Abstract: Ce guide explique comment modifier et enregistrer les métadonnées dans les documents PDF en utilisant Aspose.PDF for Python via .NET. Il démontre comment mettre à jour les propriétés PDF standard telles que le titre, le sujet, les mots‑clés et le créateur, ainsi que les champs de métadonnées personnalisés. À la fin, vous serez capable de mettre à jour les métadonnées PDF de manière programmatique et d’enregistrer les modifications.
---

Les documents PDF peuvent contenir à la fois des métadonnées standard (Title, Subject, Keywords, Creator, Author) et des métadonnées personnalisées stockées sous forme de propriétés XMP. Aspose.PDF fournit une API simple pour modifier ces propriétés en Python. Ce guide explique comment mettre à jour ces champs et enregistrer le fichier PDF modifié en utilisant le [PdfFileInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileinfo/) classe.

1. Chargez le fichier PDF.
1. Mettre à jour les métadonnées standard.
1. Ajouter ou mettre à jour les métadonnées personnalisées.
1. Enregistrer les métadonnées mises à jour.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def set_pdf_metadata(infile, outfile):

    # Get PDF information
    pdf_info = pdf_facades.PdfFileInfo(infile)

    # Set PDF metadata
    pdf_info.subject = "Aspose PDF for Python via .NET"
    pdf_info.title = "Aspose PDF for Python via .NET"
    pdf_info.keywords = "Aspose, PDF, Python, .NET"
    pdf_info.creator = "Aspose Team"

    pdf_info.set_meta_info("CustomKey", "CustomValue")

    # pdf_info.save_new_info(outfile)
    # Is obsolete, use save() method instead

    # Save updated metadata
    pdf_info.save(outfile)
```
