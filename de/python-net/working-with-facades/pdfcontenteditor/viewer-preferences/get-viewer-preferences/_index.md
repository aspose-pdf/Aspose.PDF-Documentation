---
title: PDF-Viewer-Einstellungen abrufen
type: docs
weight: 20
url: /de/python-net/get-viewer-preferences/
description: Wie man PDF-Viewer-Einstellungen programmgesteuert mithilfe von Aspose.PDF for Python liest und ändert
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDF-Viewer-Einstellungen mit Aspose.PDF in Python verwalten
Abstract: Dieses Handbuch zeigt, wie man PDF-Viewer-Einstellungen programmgesteuert mit Aspose.PDF for Python liest und ändert. Viewer-Einstellungen steuern, wie ein PDF angezeigt wird, wenn es in einem PDF-Viewer geöffnet wird, beispielsweise beim Öffnen mit Gliederungen, dem Ausblenden von Symbolleisten oder der Verwendung eines Einzelseiten-Layouts.
---

Aspose.PDF stellt Werkzeuge zum Zugreifen und Aktualisieren von PDF-Viewer-Einstellungen bereit. Diese Einstellungen definieren das anfängliche Layout und das Präsentationsverhalten eines PDF-Dokuments in PDF‑Readern. Dazu gehören Optionen wie das Aktivieren der Gliederungsansicht, das Ausblenden von Menüs oder das Festlegen von Seitenlayout‑Modi. Mit PdfContentEditor können Sie vorhandene Einstellungen abrufen, bestimmte Flags prüfen und sie bei Bedarf aktualisieren.

1. ViewerPreference-Flags definieren.
1. Initialisieren [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) und PDF binden.
1. Aktuelle Viewer-Einstellungen abrufen.
1. Spezifische Flags prüfen.
1. Aktuelle Präferenzen anzeigen.

```python
import aspose.pdf.facades as pdf_facades
import sys
from enum import IntFlag
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def get_viewer_preferences(infile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Read current viewer preference flags
    viewer_preference = ViewerPreference(content_editor.get_viewer_preference())
    if viewer_preference & ViewerPreference.PAGE_MODE_USE_OUTLINES:
        print("PageModeUseOutlines is enabled")
    print(f"Current viewer preference: {viewer_preference}")
```
