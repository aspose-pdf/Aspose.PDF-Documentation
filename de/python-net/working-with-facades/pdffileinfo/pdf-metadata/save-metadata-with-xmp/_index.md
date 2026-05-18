---
title: Metadaten mit XMP speichern
type: docs
weight: 30
url: /de/python-net/save-metadata-with-xmp/
description: PDF-Metadaten mit XMP speichern mit Aspose.PDF for Python via .NET
lastmod: "2026-05-18"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDF-Metadaten mit XMP speichern mit Aspose.PDF for Python
Abstract: Dieses Handbuch zeigt, wie PDF-Metadaten mithilfe von XMP (Extensible Metadata Platform) mit Aspose.PDF for Python via .NET gespeichert werden können. XMP stellt sicher, dass sowohl Standard‑ als auch benutzerdefinierte Metadaten in einem standardisierten XML‑Format im PDF eingebettet werden, was die Kompatibilität zwischen Anwendungen und Arbeitsabläufen verbessert.
---

PDF-Metadaten können auf verschiedene Weise gespeichert werden, und XMP ist die moderne, standardisierte Methode, Metadaten in einer PDF‑Datei einzubetten. Mit Aspose.PDF können Sie Standardfelder wie Title, Subject, Keywords und Creator aktualisieren und anschließend im XMP‑Format speichern, um eine breitere Kompatibilität und Zukunftssicherheit zu gewährleisten. Diese Methode wird gegenüber traditionellen Metadaten‑Speichermethoden empfohlen.

1. Laden Sie die PDF-Datei.
1. Standard‑Metadatenfelder festlegen.
1. Metadaten im XMP-Format speichern.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def save_info_with_xmp(infile, outfile):

    # Get PDF information
    pdf_info = pdf_facades.PdfFileInfo(infile)

    # Set PDF metadata
    pdf_info.subject = "Aspose PDF for Python via .NET"
    pdf_info.title = "Aspose PDF for Python via .NET"
    pdf_info.keywords = "Aspose, PDF, Python, .NET"
    pdf_info.creator = "Aspose Team"

    # Save updated metadata
    pdf_info.save_new_info_with_xmp(outfile)
```
