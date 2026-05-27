---
title: Ajouter une action de document
type: docs
weight: 20
url: /fr/python-net/add-document-action/
description: Cet exemple ajoute une alerte JavaScript qui apparaît lorsque le PDF est ouvert. Le script est attaché à l'événement d'ouverture du document et s'exécute automatiquement dans les visionneuses PDF prises en charge.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ajouter une action JavaScript d'ouverture de document à un PDF avec Python
Abstract: Cet exemple montre comment ajouter une action JavaScript au niveau du document qui se déclenche lorsqu'un PDF est ouvert. En utilisant Aspose.PDF for Python via the Facades API, l'exemple montre comment lier un document, attribuer une action d'événement d'ouverture, et enregistrer le PDF mis à jour.
---

Les actions au niveau du document vous permettent de définir des comportements qui s'exécutent automatiquement lorsqu'un certain événement se produit, comme l'ouverture d'un PDF. Avec [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), vous pouvez attacher du code JavaScript à ces événements. Cela peut être utilisé pour des notifications, une logique de validation ou des flux de travail interactifs.

1. Créer l'objet PdfContentEditor.
1. Lier le PDF d'entrée.
1. Ajouter une action de niveau document.
1. Enregistrer le Document mis à jour.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_document_action(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add JavaScript action for document open event
    content_editor.add_document_additional_action(
        content_editor.DOCUMENT_OPEN,
        "app.alert('Document opened with PdfContentEditor action');",
    )
    # Save updated document
    content_editor.save(outfile)
```
