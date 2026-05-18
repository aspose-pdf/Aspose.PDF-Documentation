---
title: PDF-Metadaten festlegen
type: docs
weight: 50
url: /de/python-net/set-pdf-metadata/
description: Metadaten in PDF-Dokumenten mit Aspose.PDF for Python via .NET ändern und speichern.
lastmod: "2026-05-18"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Aktualisieren von PDF-Metadaten mit Aspose.PDF for Python
Abstract: Dieser Leitfaden erklärt, wie man Metadaten in PDF-Dokumenten mit Aspose.PDF for Python via .NET ändert und speichert. Er zeigt, wie standardmäßige PDF‑Eigenschaften wie Titel, Betreff, Schlüsselwörter und Ersteller sowie benutzerdefinierte Metadatenfelder aktualisiert werden können. Am Ende können Sie PDF‑Metadaten programmgesteuert aktualisieren und die Änderungen speichern.
---

PDF‑Dokumente können sowohl standardmäßige Metadaten (Title, Subject, Keywords, Creator, Author) als auch benutzerdefinierte Metadaten, die als XMP‑Eigenschaften gespeichert sind, enthalten. Aspose.PDF bietet eine einfache API, um diese Eigenschaften in Python zu ändern. Dieser Leitfaden behandelt, wie diese Felder aktualisiert und die modifizierte PDF‑Datei mithilfe der [PdfFileInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileinfo/) Klasse.

1. Laden Sie die PDF-Datei.
1. Standard‑Metadaten aktualisieren.
1. Benutzerdefinierte Metadaten hinzufügen oder aktualisieren.
1. Aktualisierte Metadaten speichern.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def set_pdf_metadata(infile, outfile):

    # Get PDF information
    pdf_info = pdf_facades.PdfFileInfo(infile)

    # Set PDF metadata
    pdf_info.subject = "Aspose PDF for Python via .NET"
    pdf_info.title = "Aspose PDF for Python via .NET"
    pdf_info.keywords = "Aspose, PDF, Python, .NET"
    pdf_info.creator = "Aspose Team"

    pdf_info.set_meta_info("CustomKey", "CustomValue")

    # pdf_info.save_new_info(outfile)
    # Is obsolete, use save() method instead

    # Save updated metadata
    pdf_info.save(outfile)
```
