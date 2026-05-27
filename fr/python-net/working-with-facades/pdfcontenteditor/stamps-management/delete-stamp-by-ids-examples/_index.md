---
title: Supprimer le tampon par ID
type: docs
weight: 85
url: /fr/python-net/delete-stamp-by-ids-examples/
description:
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Supprimer les tampons en caoutchouc par un ID unique ou plusieurs ID dans un PDF à l'aide de PdfContentEditor
Abstract: Cet exemple montre comment supprimer les annotations de tampons en caoutchouc d'un PDF en fonction de leurs ID uniques en utilisant Aspose.PDF for Python via l'API Facades. Il couvre la suppression par ID unique ainsi que la suppression par plusieurs ID.
---

Lorsqu'on travaille avec des PDF contenant plusieurs tampons, il est souvent nécessaire de supprimer des tampons spécifiques sans affecter les autres. En utilisant la suppression basée sur l'ID, vous pouvez contrôler précisément quels tampons supprimer :

- 'delete_stamp_by_id(stamp_id, page_number)' – supprime un seul tampon par son ID sur une page spécifique
- 'delete_stamp_by_ids(page_number, stamp_ids)' – supprime plusieurs tampons par leurs ID sur une page donnée

1. Créer un [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) instance.
1. Lier le document PDF d'entrée.
1. Ajoutez deux tampons en caoutchouc avec des ID distincts.
1. Supprimez les tampons en utilisant à la fois les méthodes de suppression par ID unique et par ID multiples.
1. Enregistrer le PDF mis à jour.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def delete_stamp_by_ids_examples(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    # Create two stamps on page 1 so they can be deleted by ID
    content_editor.create_rubber_stamp(
        1,
        apd.Rectangle(120, 320, 180, 60),
        "Draft",
        "Delete by single ID",
        apd.Color.orange,
    )
    content_editor.create_rubber_stamp(
        1,
        apd.Rectangle(120, 250, 180, 60),
        "Draft",
        "Delete by multiple IDs",
        apd.Color.orange,
    )

    # Delete by single ID overload and by IDs overload
    content_editor.delete_stamp_by_id(1, 1)
    content_editor.delete_stamp_by_ids(1, [2])

    # Save updated document
    content_editor.save(outfile)
```

