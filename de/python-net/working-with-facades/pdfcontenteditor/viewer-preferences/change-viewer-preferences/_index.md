---
title: PDF-Viewer-Einstellungen ändern
type: docs
weight: 10
url: /de/python-net/change-viewer-preferences/
description: Dieses Modul demonstriert, wie man die Viewer-Einstellungen eines PDF-Dokuments mithilfe von Aspose.PDF for Python anpasst.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDF-Viewer-Erlebnis mit Python anpassen
Abstract: Steuern Sie, wie Ihr PDF-Dokument beim Öffnen erscheint, indem Sie die Viewer-Einstellungen programmatisch ändern. Diese Funktion ermöglicht es Ihnen, die Benutzeroberfläche und das Layout anzupassen und somit ein konsistentes Anzeigeerlebnis zu gewährleisten.
---

PDF-Dateien verfügen über integrierte Viewer-Einstellungen, die Aspekte wie Seitenlayout, Symbolleisten‑Sichtbarkeit und Fensterverhalten steuern. Mit diesem Skript können Sie:

- Untersuchen Sie die aktuellen Viewer-Einstellungen eines PDFs.
- Layout-Optionen ändern (z. B. einseitig, einspaltig, zweispaltig).
- UI-Elemente wie Symbolleiste, Menüleiste oder Titelanzeige umschalten.
- Das PDF mit den aktualisierten Einstellungen speichern für ein kontrolliertes Anzeigeerlebnis.

1. ViewerPreference-Flags definieren.
1. Aktuelle Viewer-Einstellungen abrufen.
1. Einstellungen ändern.
1. Aktualisierte Einstellungen anwenden.
1. Speichern Sie das PDF.

```python
import aspose.pdf.facades as pdf_facades
import sys
from enum import IntFlag
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Define ViewerPreference flags
class ViewerPreference(IntFlag):
    HIDE_TOOLBAR = 1
    HIDE_MENUBAR = 2
    HIDE_WINDOW_UI = 4
    FIT_WINDOW = 8
    CENTER_WINDOW = 16
    DISPLAY_DOC_TITLE = 32
    NON_FULL_SCREEN_PAGE_MODE_USE_NONE = 64
    NON_FULL_SCREEN_PAGE_MODE_USE_OUTLINES = 128
    NON_FULL_SCREEN_PAGE_MODE_USE_THUMBS = 256
    NON_FULL_SCREEN_PAGE_MODE_USE_OC = 512
    DIRECTION_L2R = 1024
    DISPLAY_DOC_TITLE_IN_TITLE_BAR = 2048
    PAGE_LAYOUT_SINGLE_PAGE = 4096
    PAGE_LAYOUT_ONE_COLUMN = 8192
    PAGE_LAYOUT_TWO_COLUMN_LEFT = 16384
    PAGE_LAYOUT_TWO_COLUMN_RIGHT = 32768
    PAGE_LAYOUT_TWO_PAGE_LEFT = 65536
    PAGE_LAYOUT_TWO_PAGE_RIGHT = 131072


def change_viewer_preferences(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    # Get current viewer preference and toggle single-page layout
    current_preference = ViewerPreference(content_editor.get_viewer_preference())
    updated_preference = current_preference | ViewerPreference.PAGE_LAYOUT_SINGLE_PAGE
    content_editor.change_viewer_preference(int(updated_preference))

    # Save updated document
    content_editor.save(outfile)
```
