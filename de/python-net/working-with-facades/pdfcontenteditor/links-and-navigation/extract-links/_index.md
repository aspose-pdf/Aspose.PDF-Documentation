---
title: Links extrahieren
type: docs
weight: 70
url: /de/python-net/extract-links/
description: Dieses Beispiel bindet ein Eingabe-PDF, extrahiert alle Links und gibt deren Koordinaten und URIs (falls vorhanden) aus.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Links aus einem PDF mit PdfContentEditor in Python extrahieren
Abstract: Dieses Beispiel zeigt, wie man alle Links aus einem PDF-Dokument mithilfe von Aspose.PDF for Python via the Facades API extrahiert. Es zeigt, wie man Web-Links oder andere ausführbare Links, die im PDF eingebettet sind, identifiziert und abruft.
---

PDFs enthalten häufig interaktive Elemente wie Weblinks, Dokumentlinks und benutzerdefinierte Aktionen. Verwenden [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), Sie können programmgesteuert alle Linkannotationen aus einem PDF extrahieren. Dies ermöglicht es Ihnen, Links zu überprüfen oder zu verarbeiten, zum Beispiel um URLs zu validieren oder Navigationsmuster in einem Dokument zu analysieren.

1. Erstellen Sie eine PdfContentEditor-Instanz.
1. Binden Sie das Eingabe‑PDF‑Dokument.
1. Extrahieren Sie alle Links mit \u0027extract_link()\u0027.
1. Durchlaufe die extrahierten Links.
1. Prüfe, ob ein Link eine LinkAnnotation ist und ob seine Aktion eine GoToURIAction ist.
1. Gib die Rechteckkoordinaten und die URI aus.
1. Zeige eine Meldung an, wenn keine Links gefunden werden.

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
