---
title: Movie-Annotation hinzufügen
type: docs
weight: 10
url: /de/python-net/add-movie-annotation/
description: Dieses Beispiel bindet ein Eingabe-PDF, fügt eine Movie-Annotation auf Seite 1 hinzu und speichert das aktualisierte PDF.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Movie-Annotation zu einem PDF mit PdfContentEditor in Python hinzufügen
Abstract: Dieses Beispiel zeigt, wie man einen Film (Video) in ein PDF-Dokument einbettet, indem man Aspose.PDF for Python via the Facades API verwendet. Es zeigt, wie man eine anklickbare Annotation hinzufügt, die ein Video direkt im PDF abspielt.
---

Movie-Annotationen in PDFs ermöglichen das Einbetten von Multimedia-Inhalten, wie Videos, in Ihre Dokumente. Verwenden [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), können Sie ein Rechteck auf einer Seite definieren, in dem das Video angezeigt wird. Beim Klicken kann das Video direkt aus dem PDF abgespielt werden, wodurch Ihre Dokumente interaktiver und ansprechender werden.

1. Erstellen Sie eine PdfContentEditor-Instanz.
1. Binden Sie das Eingabe‑PDF‑Dokument.
1. Definieren Sie ein Rechteck für die Filmannotation.
1. Spezifizieren Sie die Videodatei zum Einbetten.
1. Weisen Sie die Seitenzahl für die Annotation zu.
1. Speichern Sie das aktualisierte PDF-Dokument.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_movie_annotation(infile, movie_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add movie annotation to page 1
    content_editor.create_movie(apd.Rectangle(80, 500, 220, 120), movie_file, 1)
    # Save updated document
    content_editor.save(outfile)
```
