---
title: Ajouter des tampons de page à PDF en Python
linktitle: Ajout de tampons de page
type: docs
weight: 30
url: /fr/python-net/page-stamps-in-the-pdf-file/
description: Apprenez à ajouter des tampons de page PDF en tant que superpositions ou arrière-plans en Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comment ajouter des tampons de page à PDF en utilisant Python
Abstract: Cet article explique comment ajouter un tampon de page à un document PDF à l'aide d'Aspose.PDF pour Python. Un tampon de page vous permet de superposer ou de placer en arrière‑plan du contenu — tel que des logos, filigranes ou annotations — sur une page spécifique d'un PDF. L'exemple montre comment ouvrir un PDF existant, créer un objet PdfPageStamp à partir d'une autre page PDF, le configurer comme tampon d'arrière‑plan, et l'appliquer à une page particulière. Le PDF tamponné est ensuite enregistré en tant que nouveau document. Cette technique est utile pour le branding, le filigrane ou la mise en évidence de contenu au niveau de la page dans des workflows PDF automatisés.
---

Aspose.PDF for Python via .NET montre comment appliquer un tampon de page (filigrane ou superposition) à une page spécifique dans un PDF [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/). Le tampon de page peut être une page PDF existante utilisée comme couche d'arrière-plan ou de premier plan (voir [`PdfPageStamp`](https://reference.aspose.com/pdf/python-net/aspose.pdf.pdfpagestamp/)). Ceci est utile pour ajouter des logos, des filigranes ou d'autres contenus de page répétitifs.

1. Ouvrez le document PDF en utilisant `ap.Document()` (voir [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)).
1. Créer un `PdfPageStamp` objet utilisant la page PDF ou le fichier à utiliser comme tampon (voir [`PdfPageStamp`](https://reference.aspose.com/pdf/python-net/aspose.pdf.pdfpagestamp/)).
1. Définissez les propriétés du tampon, par ex., `background = True` le placer derrière le contenu.
1. Ajouter le tampon à une page spécifique en utilisant `document.pages[page_number].add_stamp(page_stamp)` (voir [`Page.add_stamp()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) et [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/)).
1. Enregistrez le PDF modifié dans le fichier de sortie spécifié en utilisant [`Document.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python
import sys
import aspose.pdf as ap
from os import path

def add_page_stamp(input_file_name, page_stamp_name, output_file_name):
    # Open PDF document
    document = ap.Document(input_file_name)

    page_stamp = ap.PdfPageStamp(page_stamp_name, 1)
    page_stamp.background = True

    # Add stamp to particular page
    document.pages[1].add_stamp(page_stamp)

    document.save(output_file_name)
```

## Sujets liés à l'estampage

- [Tamponner les pages PDF en Python](/pdf/fr/python-net/stamping/)
- [Ajouter des numéros de page à un PDF en Python](/pdf/fr/python-net/add-page-number/)
- [Ajouter des tampons d'image à un PDF en Python](/pdf/fr/python-net/image-stamps-in-pdf-page/)
- [Ajouter des tampons de texte à un PDF en Python](/pdf/fr/python-net/text-stamps-in-the-pdf-file/)