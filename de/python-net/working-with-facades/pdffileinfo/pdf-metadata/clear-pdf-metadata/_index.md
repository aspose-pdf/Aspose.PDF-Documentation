---
title: PDF-Metadaten löschen
type: docs
weight: 10
url: /de/python-net/clear-pdf-metadata/
description: Entfernen Sie alle Metadaten aus einem PDF-Dokument mithilfe von Aspose.PDF für Python via .NET.
lastmod: "2026-05-18"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDF-Metadaten löschen mit Aspose.PDF für Python
Abstract: Dieses Handbuch erklärt, wie Sie alle Metadaten aus einem PDF-Dokument mithilfe von Aspose.PDF für Python via .NET entfernen. Sie lernen, sowohl Standard‑ als auch benutzerdefinierte Metadatenfelder zu löschen und das bereinigte PDF zu speichern. Dies ist nützlich für Datenschutz, Sicherheit oder die Vorbereitung von PDFs für die öffentliche Veröffentlichung.
---

PDFs enthalten häufig Metadaten wie Titel, Autor, Schlüsselwörter, Erstellungsdaten und benutzerdefinierte Felder. In manchen Situationen möchten Sie möglicherweise alle Metadaten aus einem PDF entfernen, beispielsweise vor der Verteilung oder Archivierung. Aspose.PDF stellt die Methode clear_info() bereit, um alle Metadaten einfach zu entfernen. Nach dem Löschen können Sie das PDF mit der Methode save() speichern.

1. Laden Sie die PDF-Datei.
1. Alle Metadaten löschen.
1. Speichern Sie das bereinigte PDF.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def clear_pdf_metadata(infile, outfile):

    # Get PDF information
    pdf_info = pdf_facades.PdfFileInfo(infile)

    # Clear PDF metadata
    pdf_info.clear_info()

    # Save updated metadata
    pdf_info.save(outfile)
```
