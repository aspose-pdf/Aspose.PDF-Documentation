---
title: Gérer le tampon par ID
type: docs
weight: 95
url: /fr/python-net/manage-stamp-by-id/
description: Comment manipuler les annotations de tampons en caoutchouc dans un PDF par leurs ID uniques en utilisant Aspose.PDF pour Python
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Gérer les tampons en caoutchouc par ID dans un PDF en utilisant PdfContentEditor en Python
Abstract: Cet exemple montre comment manipuler les annotations de tampons en caoutchouc dans un PDF par leurs ID uniques en utilisant Aspose.PDF pour Python via l'API Facades. Vous pouvez masquer ou afficher des tampons spécifiques sur certaines pages sans affecter les autres tampons.
---

Dans les PDF contenant plusieurs tampons en caoutchouc, il peut être utile de contrôler les tampons individuels en fonction de leur ID. Les méthodes 'hide_stamp_by_id()' et 'show_stamp_by_id()' permettent un contrôle sélectif de la visibilité. Cet exemple montre comment :

- Ajouter plusieurs tampons avec des ID uniques
- Masquer un tampon sur une page spécifique
- Afficher un tampon sur une autre page

En utilisant des opérations basées sur l’ID, vous évitez de suivre les tampons par position de page ou d’autres attributs.

1. Créer un [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) instance.
1. Lier le document PDF d'entrée.
1. Ajouter des tampons en caoutchouc avec des ID spécifiques.
1. Masquer et afficher les tampons en fonction de leurs ID et des numéros de page.
1. Enregistrer le document PDF mis à jour.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def manage_stamp_by_id(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    content_editor.create_rubber_stamp(
        1,
        apd.Rectangle(200, 380, 180, 60),
        "Draft",
        "Draft stamp for ID-based operations",
        apd.Color.orange,
    )

    content_editor.create_rubber_stamp(
        2,
        apd.Rectangle(200, 480, 180, 60),
        "Draft",
        "Draft stamp for ID-based operations",
        apd.Color.orange,
    )

    # Apply ID-based stamp operations
    content_editor.hide_stamp_by_id(1, 1)
    content_editor.show_stamp_by_id(1, 2)

    # Save updated document
    content_editor.save(outfile)
```
