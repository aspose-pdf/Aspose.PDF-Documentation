---
title: Open-Aktion entfernen
type: docs
weight: 30
url: /de/python-net/remove-open-action/
description: Dieses Beispiel lädt ein vorhandenes PDF, entfernt die Open-Aktion und speichert das bereinigte Dokument.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Entfernen der Dokument-Open-Aktion aus einem PDF mit Python
Abstract: Dieses Beispiel demonstriert, wie man eine Dokument-Open-Aktion aus einem PDF mit Aspose.PDF for Python via the Facades API entfernt. Es zeigt, wie man ein PDF bindet, die Open-Aktion löscht und das aktualisierte Dokument speichert.
---

PDF-Dokumente können Aktionen enthalten, die beim Öffnen der Datei automatisch ausgeführt werden, z. B. JavaScript‑Warnungen, Navigationsbefehle oder andere Verhaltensweisen. In einigen Szenarien müssen Sie diese Aktionen aus Sicherheits-, Compliance‑ oder Benutzererfahrungsgründen entfernen.

Mit PdfContentEditor können Sie die Dokument-Open-Aktion ganz einfach entfernen und sicherstellen, dass das PDF geöffnet wird, ohne irgendein automatisches Verhalten auszuführen.

1. Erstellen Sie das PdfContentEditor-Objekt.
1. Binden Sie das Eingabe-PDF.
1. Entfernen Sie die Dokument‑Öffnungsaktion.
1. Speichern Sie das aktualisierte Document.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def remove_open_action(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Remove open action from the document
    content_editor.remove_document_open_action()
    # Save updated document
    content_editor.save(outfile)
```
