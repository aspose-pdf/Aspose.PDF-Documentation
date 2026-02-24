---
title: Ajouter des tampons de page au PDF avec Python
linktitle: Ajout de tampons de page
type: docs
weight: 30
url: /fr/python-net/page-stamps-in-the-pdf-file/
description: Aspose.PDF for Python via .NET vous permet d’ajouter un tampon de page à votre fichier PDF.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comment ajouter des tampons de page à un PDF avec Python
Abstract: Cet article explique comment ajouter un tampon de page à un document PDF à l’aide d’Aspose.PDF pour Python. Un tampon de page vous permet de superposer ou de placer en dessous du contenu — tel que des logos, des filigranes ou des annotations — sur une page spécifique d’un PDF. L’exemple montre comment ouvrir un PDF existant, créer un objet PdfPageStamp à partir d’une autre page PDF, le configurer comme tampon d’arrière-plan, puis l’appliquer à une page particulière. Le PDF tamponné est ensuite enregistré comme un nouveau document. Cette technique est utile pour le branding, le filigranage ou la mise en évidence de contenus au niveau de la page dans des flux de travail PDF automatisés.
---

Aspose.PDF for Python via .NET montre comment appliquer un tampon de page (filigrane ou superposition) à une page spécifique d’un PDF [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/). Le tampon de page peut être une page PDF existante utilisée comme couche d’arrière‑plan ou de premier plan (voir [`PdfPageStamp`](https://reference.aspose.com/pdf/python-net/aspose.pdf.pdfpagestamp/)). Cela est utile pour ajouter des logos, des filigranes ou d’autres contenus de page récurrents.

1. Ouvrez le document PDF à l’aide de `ap.Document()` (voir [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)).
1. Créez un objet `PdfPageStamp` en utilisant la page PDF ou le fichier à utiliser comme tampon (voir [`PdfPageStamp`](https://reference.aspose.com/pdf/python-net/aspose.pdf.pdfpagestamp/)).
1. Définissez les propriétés du tampon, par ex., `background = True` pour le placer derrière le contenu.
1. Ajoutez le tampon à une page spécifique en utilisant `document.pages[page_number].add_stamp(page_stamp)` (voir [`Page.add_stamp()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) et [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/)).
1. Enregistrez le PDF modifié dans le fichier de sortie spécifié en utilisant [`Document.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_page_stamp(input_file_name, page_stamp_name, output_file_name):
    # Open PDF document
    document = ap.Document(input_file_name)

    page_stamp = ap.PdfPageStamp(page_stamp_name, 1)
    page_stamp.background = True

    # Add stamp to particular page
    document.pages[1].add_stamp(page_stamp)

    document.save(output_file_name)
```

