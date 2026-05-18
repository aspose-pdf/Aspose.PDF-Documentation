---
title: Seiteninformationen abrufen
type: docs
weight: 10
url: /de/python-net/get-page-info/
description: Erfahren Sie, wie Sie programmgesteuert Seiteninformationen in einer PDF mit Aspose.PDF for Python abrufen können. Dieser Leitfaden zeigt, wie Sie die Seitenbreite, -höhe, Drehung und Versätze für eine bestimmte Seite in einem PDF‑Dokument ermitteln.
lastmod: "2026-05-18"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDF‑Seiteninformationen mit Aspose.PDF for Python abrufen
Abstract: Die Funktion extrahiert die Breite, Höhe, Drehung sowie die horizontalen (X) und vertikalen (Y) Versätze einer PDF‑Seite. Diese Eigenschaften werden in Punkten zurückgegeben und spiegeln die physische Größe der Seite sowie die Positionierung des Inhalts innerhalb der PDF wider. Die Funktion gibt die abgerufenen Werte aus, sodass Entwickler das Layout und die Orientierung der Seite für weitere PDF‑Manipulationen verstehen können.
---

Die ‘get_page_information’-Hilfsfunktion hilft Entwicklern, die Struktur und das Layout von PDF‑Seiten zu verstehen. Jede PDF‑Seite kann unterschiedliche Abmessungen, Drehungen und interne Versätze haben, die die Platzierung von Inhalten oder Automatisierungsaufgaben beeinflussen können.

Sie ermöglicht das Abrufen wichtiger Metadaten und Layout‑Informationen für eine bestimmte Seite in einer PDF‑Datei. Die Aspose.PDF Facades‑API liefert Details wie Seitenbreite, -höhe, Drehung und X/Y‑Versätze. Diese Informationen sind für Aufgaben wie Seitenlayout‑Analyse, Anmerkungsplatzierung oder automatisierte PDF‑Verarbeitung unverzichtbar.

1. Ein PDF-Fassade-Objekt erstellen.
1. Seitenabmessungen und Layout abrufen.
1. Die abgerufenen Werte ausgeben oder speichern.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def get_page_information(infile):

    # Get and display PDF information
    pdf_info = pdf_facades.PdfFileInfo(infile)
    page_width = pdf_info.get_page_width(1)
    page_height = pdf_info.get_page_height(1)
    page_rotation = pdf_info.get_page_rotation(1)
    page_x_offset = pdf_info.get_page_x_offset(1)
    page_y_offset = pdf_info.get_page_y_offset(1)

    print(f"Page Width: {page_width}")
    print(f"Page Height: {page_height}")
    print(f"Page Rotation: {page_rotation}")
```
