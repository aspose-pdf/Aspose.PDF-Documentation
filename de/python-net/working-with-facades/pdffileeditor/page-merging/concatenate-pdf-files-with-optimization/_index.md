---
title: PDF-Dateien mit Optimierung zusammenführen
type: docs
weight: 30
url: /de/python-net/concatenate-pdf-files-with-optimization/
description: Mehrere PDF-Dateien mithilfe von Aspose.PDF für Python zu einer einzigen optimierten PDF zusammenführen.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDF-Dateien mit optimiertem Ergebnis in Python zusammenführen
Abstract: Erfahren Sie, wie Sie mehrere PDF-Dateien mithilfe von Aspose.PDF für Python zu einer einzigen optimierten PDF zusammenführen. Dieses Beispiel zeigt, wie Sie die Größenoptimierung aktivieren, um die Ausgabedateigröße zu reduzieren und dabei Inhalt und Formatierung beizubehalten.
---

Beim Zusammenführen mehrerer PDFs kann die resultierende Datei groß werden, insbesondere wenn sie Bilder oder komplexe Inhalte enthält. Mit Aspose.PDF für Python können Entwickler während der Zusammenführung Optimierung aktivieren, um die Dateigröße zu reduzieren, ohne die Qualität zu verlieren. Die Eigenschaft optimize_size in der [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) Klasse stellt sicher, dass das zusammengeführte PDF kompakt und effizient ist, wodurch es sich zum Teilen, Speichern oder Archivieren eignet.

1. Erstellen Sie ein PdfFileEditor-Objekt und aktivieren Sie die Optimierung.
1. PDF-Dateien zusammenführen.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


def concatenate_pdf_files_with_optimization(files_to_merge, output_file):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    pdf_editor.optimize_size = True  # Enable optimization for smaller output file size
    pdf_editor.concatenate(files_to_merge, output_file)
```
