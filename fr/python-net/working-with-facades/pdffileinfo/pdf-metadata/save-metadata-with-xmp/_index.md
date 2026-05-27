---
title: Enregistrer les métadonnées avec XMP
type: docs
weight: 30
url: /fr/python-net/save-metadata-with-xmp/
description: Enregistrer les métadonnées PDF en utilisant XMP avec Aspose.PDF for Python via .NET
lastmod: "2026-05-22"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Enregistrement des métadonnées PDF avec XMP en utilisant Aspose.PDF for Python
Abstract: Ce guide montre comment enregistrer les métadonnées PDF en utilisant XMP (Extensible Metadata Platform) avec Aspose.PDF for Python via .NET. XMP garantit que les métadonnées standard et personnalisées sont incorporées dans un format XML standardisé à l'intérieur du PDF, améliorant la compatibilité entre les applications et les flux de travail.
---

Les métadonnées PDF peuvent être stockées de plusieurs façons, et XMP est la méthode moderne et standardisée pour incorporer des métadonnées à l'intérieur d'un fichier PDF. En utilisant Aspose.PDF, vous pouvez mettre à jour les champs standard tels que Titre, Sujet, Mots‑clés et Créateur, puis les enregistrer au format XMP afin d'assurer une compatibilité plus large et une pérennité. Cette méthode est recommandée par rapport aux méthodes de stockage de métadonnées héritées.

1. Chargez le fichier PDF.
1. Définir les champs de métadonnées standard.
1. Enregistrer les métadonnées au format XMP.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def save_info_with_xmp(infile, outfile):

    # Get PDF information
    pdf_info = pdf_facades.PdfFileInfo(infile)

    # Set PDF metadata
    pdf_info.subject = "Aspose PDF for Python via .NET"
    pdf_info.title = "Aspose PDF for Python via .NET"
    pdf_info.keywords = "Aspose, PDF, Python, .NET"
    pdf_info.creator = "Aspose Team"

    # Save updated metadata
    pdf_info.save_new_info_with_xmp(outfile)
```
