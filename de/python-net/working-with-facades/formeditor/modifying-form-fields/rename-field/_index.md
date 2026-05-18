---
title: Feld umbenennen
type: docs
weight: 70
url: /de/python-net/rename-field/
description: Ein vorhandenes Formularfeld in einem PDF-Dokument mit Aspose.PDF for Python umbenennen.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ein PDF-Formularfeld mit Python umbenennen
Abstract: Dieses Beispiel zeigt, wie man ein vorhandenes Formularfeld in einem PDF-Dokument mit Aspose.PDF for Python umbenennt. Der Code öffnet ein Eingabe‑PDF, ändert den Namen eines angegebenen Formularfeldes mithilfe der FormEditor‑Klasse und speichert das aktualisierte Dokument.
---

PDF‑Formulare basieren häufig auf Feldnamen für Skripting, Automatisierung und Datenverarbeitung. Mit Aspose.PDF for Python können Entwickler vorhandene Felder umbenennen, ohne sie neu zu erstellen oder das Formularlayout zu ändern.

Der [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) Die Klasse stellt die Methode ‘rename_field’ bereit, mit der Entwickler den Namen eines vorhandenen Feldes ändern können, während Position, Wert und Aussehen erhalten bleiben.

1. Laden Sie das vorhandene PDF-Formular.
1. Erstellen Sie eine FormEditor-Instanz.
1. Binden Sie das PDF-Dokument an den Editor.
1. Benennen Sie das Ziel‑Feld um.
1. Speichere das aktualisierte PDF.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def rename_field(infile, outfile):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Bind document to FormEditor
    form_editor.bind_pdf(infile)
    # Rename field in document
    form_editor.rename_field("City", "Town")
    # Save updated document
    form_editor.save(outfile)
```

