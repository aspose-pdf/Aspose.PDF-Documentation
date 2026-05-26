---
title: Effacer les métadonnées PDF
type: docs
weight: 10
url: /fr/python-net/clear-pdf-metadata/
description: Supprimez toutes les métadonnées d'un document PDF à l'aide d'Aspose.PDF for Python via .NET.
lastmod: "2026-05-22"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Effacement des métadonnées PDF avec Aspose.PDF for Python
Abstract: Ce guide explique comment supprimer toutes les métadonnées d'un document PDF à l'aide d'Aspose.PDF for Python via .NET. Vous apprendrez à effacer les champs de métadonnées standards et personnalisés et à enregistrer le PDF assaini. Cela est utile pour la confidentialité, la sécurité ou la préparation de PDFs pour une diffusion publique.
---

Les PDF contiennent souvent des métadonnées telles que le titre, l'auteur, les mots‑clés, les dates de création et les champs personnalisés. Dans certains cas, vous pouvez souhaiter supprimer toutes les métadonnées d'un PDF, par exemple avant la distribution ou l'archivage. Aspose.PDF fournit la méthode clear_info() pour supprimer facilement toutes les métadonnées. Après la suppression, vous pouvez enregistrer le PDF à l'aide de la méthode save().

1. Chargez le fichier PDF.
1. Effacer toutes les métadonnées.
1. Enregistrer le PDF nettoyé.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def clear_pdf_metadata(infile, outfile):

    # Get PDF information
    pdf_info = pdf_facades.PdfFileInfo(infile)

    # Clear PDF metadata
    pdf_info.clear_info()

    # Save updated metadata
    pdf_info.save(outfile)
```
