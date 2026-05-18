---
title: Feld verschieben
type: docs
weight: 50
url: /de/python-net/move-field/
description: Verschieben Sie ein vorhandenes Formularfeld an eine andere Position in einem PDF-Dokument.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Verschieben Sie ein PDF-Formularfeld zu einer neuen Position mit Python
Abstract: Dieses Beispiel zeigt, wie man ein vorhandenes Formularfeld mit Aspose.PDF for Python an eine andere Position in einem PDF-Dokument verschiebt. Der Code öffnet ein bestehendes PDF, verlegt das angegebene Formularfeld zu neuen Koordinaten und speichert das aktualisierte Dokument.
---

PDF-Formulare erfordern häufig nach der Erstellung Layout-Anpassungen. Mit Aspose.PDF for Python können Entwickler vorhandene Formularfelder an eine neue Position verschieben, ohne sie neu zu erstellen.

Dieses Beispiel zeigt, wie das Feld "Country" neu positioniert wird, indem neue Koordinaten für die Platzierung innerhalb der Seite angegeben werden. Das [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) Die Klasse stellt die Methode move_field bereit, um Felder innerhalb einer PDF‑Seite zu verschieben.

1. Öffnen Sie das vorhandene PDF‑Formular.
1. Erstellen Sie ein FormEditor-Objekt.
1. Binden Sie das PDF-Dokument an den FormEditor.
1. Verschieben Sie das Feld 'Country' an eine neue Position unter Verwendung von Koordinaten.
1. Speichern Sie das geänderte Dokument.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def move_field(infile, outfile):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Bind document to FormEditor
    form_editor.bind_pdf(infile)
    # Move field to new page
    form_editor.move_field("Country", 200, 600, 280, 620)
    # Save updated document
    form_editor.save(outfile)
```
