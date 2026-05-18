---
title: PDF-Version abrufen
type: docs
weight: 20
url: /de/python-net/get-pdf-version/
description: Erfahren Sie, wie Sie programmgesteuert die Version eines PDF-Dokuments mit Aspose.PDF für Python ermitteln können. Dieses Tutorial demonstriert, wie Sie die PdfFileInfo-Klasse verwenden, um die PDF-Version einer Datei zu prüfen.
lastmod: "2026-05-18"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDF-Version mit Aspose.PDF für Python abrufen
Abstract: PDF-Dokumente haben Versionsnummern, die die unterstützten Funktionen und Spezifikationen angeben (z. B. 1.4, 1.7, 2.0). Die Kenntnis der PDF-Version ist wichtig für Kompatibilität, Funktionsunterstützung und Dokumentenverarbeitungs-Workflows. In diesem Leitfaden lernen Sie, wie Sie die PDF-Version programmgesteuert mithilfe der PdfFileInfo-Klasse in Aspose.PDF für Python abrufen.
---

PDF-Versionen definieren die in einem Dokument unterstützten Funktionen und Fähigkeiten, einschließlich Formularfelder, Verschlüsselung, Anmerkungen und Kompression. Für Entwickler, die mit mehreren PDFs arbeiten, stellt das Überprüfen der Version die Kompatibilität mit Werkzeugen, Bibliotheken oder Workflows sicher, die diese Dateien verarbeiten.

Mit Aspose.PDF für Python können Sie die PDF-Version einfach prüfen mit dem [PdfFileInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileinfo/) Klasse.

1. Laden Sie ein PDF-Dokument.
1. Rufen Sie die PDF-Version ab.
1. Zeigen Sie die Version in der Konsole an.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def get_pdf_version(input_file_name):

    pdf_metadata = pdf_facades.PdfFileInfo(input_file_name)
    version = pdf_metadata.get_pdf_version()
    print(f"\nPDF Version: {version}")
```
