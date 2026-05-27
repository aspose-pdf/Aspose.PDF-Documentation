---
title: Extraire les liens
type: docs
weight: 70
url: /fr/python-net/extract-links/
description: Cet exemple charge un PDF d'entrée, extrait tous les liens et affiche leurs coordonnées ainsi que leurs URI (si disponibles).
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extraire les liens d'un PDF en utilisant PdfContentEditor en Python
Abstract: Cet exemple montre comment extraire tous les liens d'un document PDF en utilisant Aspose.PDF for Python via the Facades API. Il montre comment identifier et récupérer les liens web ou d'autres liens exploitables intégrés dans le PDF.
---

Les PDF contiennent souvent des éléments interactifs tels que des liens web, des liens de document et des actions personnalisées. En utilisant [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), vous pouvez extraire programmétiquement toutes les annotations de lien d'un PDF. Cela vous permet d'inspecter ou de traiter les liens, par exemple pour valider les URL ou analyser les schémas de navigation dans un document.

1. Créer une instance de PdfContentEditor.
1. Lier le document PDF d'entrée.
1. Extraire tous les liens en utilisant 'extract_link()'.
1. Itérer à travers les liens extraits.
1. Vérifier si un lien est une LinkAnnotation et si son action est une GoToURIAction.
1. Afficher les coordonnées du rectangle et l'URI.
1. Afficher un message si aucun lien n'est trouvé.

```python
import aspose.pdf.facades as pdf_facades
from aspose.pycore import cast, is_assignable
import aspose.pydrawing as apd
import aspose.pdf as ap

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def extract_links(infile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Extract links from the document
    links = content_editor.extract_link()

    count = 0
    for link in links:
        count += 1
        print(f"Link {count}: {link.rect}")
        if is_assignable(link, ap.annotations.LinkAnnotation):
            annotation = cast(ap.annotations.LinkAnnotation, link)
            if is_assignable(annotation.action, ap.annotations.GoToURIAction):
                action = cast(ap.annotations.GoToURIAction, annotation.action)
                print(f"  URI: {action.uri}")

    if count == 0:
        print("No links found")
```
